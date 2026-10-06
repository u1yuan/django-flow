"use client";

import gsap from "gsap";
import { useCallback, useEffect, useLayoutEffect, useRef, useState } from "react";
import { slides } from "../content";
import { EditorialSlide } from "./EditorialSlide";
import { TitleSlide } from "./TitleSlide";

const STAGE_W = 1440;
const STAGE_H = 810;
const CHROME = 72;

function deckEase(progress: number): number {
  const x1 = 0.32;
  const y1 = 0.72;
  const x2 = 0;
  const y2 = 1;
  const cx = 3 * x1;
  const bx = 3 * (x2 - x1) - cx;
  const ax = 1 - cx - bx;
  const cy = 3 * y1;
  const by = 3 * (y2 - y1) - cy;
  const ay = 1 - cy - by;
  const sampleX = (t: number) => ((ax * t + bx) * t + cx) * t;
  const sampleY = (t: number) => ((ay * t + by) * t + cy) * t;
  const sampleDX = (t: number) => (3 * ax * t + 2 * bx) * t + cx;

  if (progress <= 0) return 0;
  if (progress >= 1) return 1;
  let t = progress;
  for (let i = 0; i < 6; i += 1) {
    const dx = sampleX(t) - progress;
    const slope = sampleDX(t);
    if (Math.abs(dx) < 1e-5 || Math.abs(slope) < 1e-6) break;
    t -= dx / slope;
  }
  return sampleY(Math.min(1, Math.max(0, t)));
}

function indexFromHash(): number {
  if (typeof window === "undefined") return 0;
  const match = window.location.hash.match(/^#\/(\d+)$/);
  if (!match) return 0;
  const next = Number(match[1]) - 1;
  if (next < 0 || next >= slides.length) return 0;
  return next;
}

function Arrow({ direction }: { direction: "left" | "right" }) {
  return (
    <svg width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true">
      {direction === "left" ? (
        <path d="M9 2.5 L4.5 7 L9 11.5" stroke="currentColor" strokeWidth="1.25" strokeLinecap="round" strokeLinejoin="round" />
      ) : (
        <path d="M5 2.5 L9.5 7 L5 11.5" stroke="currentColor" strokeWidth="1.25" strokeLinecap="round" strokeLinejoin="round" />
      )}
    </svg>
  );
}

export function Deck() {
  const [index, setIndex] = useState(0);
  const [ready, setReady] = useState(false);
  const [scale, setScale] = useState(1);
  const stageRef = useRef<HTMLDivElement>(null);

  const go = useCallback((delta: number) => {
    setIndex((current) => {
      const next = current + delta;
      if (next < 0 || next >= slides.length) return current;
      return next;
    });
  }, []);

  useEffect(() => {
    setIndex(indexFromHash());
    setReady(true);
    const onHash = () => setIndex(indexFromHash());
    window.addEventListener("hashchange", onHash);
    return () => window.removeEventListener("hashchange", onHash);
  }, []);

  useEffect(() => {
    if (!ready) return;
    const next = `#/${index + 1}`;
    if (window.location.hash !== next) {
      history.replaceState(null, "", next);
    }
  }, [index, ready]);

  useEffect(() => {
    const fit = () => {
      const next = Math.min(
        window.innerWidth / STAGE_W,
        (window.innerHeight - CHROME) / STAGE_H,
      );
      setScale(next);
    };
    fit();
    window.addEventListener("resize", fit);
    return () => window.removeEventListener("resize", fit);
  }, []);

  useEffect(() => {
    const onKey = (event: KeyboardEvent) => {
      const key = event.key;
      if (key === "ArrowRight" || key === "PageDown" || key === " ") {
        event.preventDefault();
        go(1);
      } else if (key === "ArrowLeft" || key === "PageUp") {
        event.preventDefault();
        go(-1);
      } else if (key === "Home") {
        event.preventDefault();
        setIndex(0);
      } else if (key === "End") {
        event.preventDefault();
        setIndex(slides.length - 1);
      }
    };
    window.addEventListener("keydown", onKey);
    return () => window.removeEventListener("keydown", onKey);
  }, [go]);

  useLayoutEffect(() => {
    const node = stageRef.current?.querySelector<HTMLElement>(".slide-content");
    if (!node) return;
    const reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (reduce) {
      gsap.set(node, { opacity: 1, scale: 1 });
      return;
    }
    const tween = gsap.fromTo(
      node,
      { opacity: 0, scale: 0.96 },
      { opacity: 1, scale: 1, duration: 0.85, ease: deckEase, overwrite: true },
    );
    return () => {
      tween.kill();
    };
  }, [index, ready]);

  const slide = slides[index];

  return (
    <main className="deck">
      <div className="grain" aria-hidden="true" />

      <div
        className="stage-slot"
        style={{ width: STAGE_W * scale, height: STAGE_H * scale }}
      >
        <div
          className="stage"
          style={{ transform: `scale(${scale})` }}
          key={slide.id}
          ref={stageRef}
        >
          {slide.kind === "title" ? (
            <TitleSlide slide={slide} />
          ) : (
            <EditorialSlide kind={slide.kind} />
          )}
        </div>
      </div>

      <nav className="nav-pill" aria-label="Slides">
        <button
          type="button"
          className="nav-btn"
          onClick={() => go(-1)}
          disabled={index === 0}
        >
          <span>Previous</span>
          <span className="nav-icon">
            <Arrow direction="left" />
          </span>
        </button>
        <p className="nav-pos">
          <span>{index + 1}</span>
          <span aria-hidden="true">/</span>
          <span>{slides.length}</span>
        </p>
        <button
          type="button"
          className="nav-btn"
          onClick={() => go(1)}
          disabled={index === slides.length - 1}
        >
          <span>Next</span>
          <span className="nav-icon">
            <Arrow direction="right" />
          </span>
        </button>
      </nav>
    </main>
  );
}
