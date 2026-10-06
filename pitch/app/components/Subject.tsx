type SubjectTheme = "hydro" | "env" | "logi";

function NetCup({ x, y }: { x: number; y: number }) {
  const top = y + 10;
  return (
    <g>
      <path
        d={`M${x - 13} ${top + 5} C ${x - 9} ${top + 16}, ${x + 9} ${top + 16}, ${x + 13} ${top + 5} L ${x + 10} ${top + 22} H ${x - 10} Z`}
        fill="currentColor"
        opacity="0.14"
        stroke="currentColor"
        strokeWidth="1.4"
      />
      <ellipse cx={x} cy={top + 5} rx="13" ry="4.2" stroke="currentColor" strokeWidth="1.4" />
      <path
        d={`M${x} ${top + 3} C ${x - 7} ${top - 8}, ${x - 11} ${top - 18}, ${x - 3} ${top - 22} M${x} ${top + 3} C ${x + 8} ${top - 7}, ${x + 13} ${top - 16}, ${x + 4} ${top - 20}`}
        stroke="currentColor"
        strokeWidth="1.45"
        strokeLinecap="round"
      />
    </g>
  );
}

function Channel({ y }: { y: number }) {
  return (
    <g>
      <rect x="220" y={y} width="376" height="42" rx="8" stroke="currentColor" strokeWidth="2.2" />
      <path
        d={`M232 ${y + 28} H584`}
        stroke="currentColor"
        strokeWidth="5"
        strokeLinecap="round"
        opacity="0.18"
      />
      <NetCup x={300} y={y} />
      <NetCup x={410} y={y} />
      <NetCup x={520} y={y} />
    </g>
  );
}

function Hydro({ fit }: { fit: string }) {
  return (
    <svg className="subject-svg" viewBox="0 0 640 440" fill="none" preserveAspectRatio={fit} aria-hidden="true">
      <rect x="36" y="278" width="112" height="122" rx="10" stroke="currentColor" strokeWidth="2.2" />
      <path d="M48 338 H136 V386 H48 Z" fill="currentColor" opacity="0.16" />
      <path d="M48 338 H136" stroke="currentColor" strokeWidth="1.2" opacity="0.65" />
      <path d="M90 198 V360" stroke="currentColor" strokeWidth="2.2" strokeLinecap="round" />
      <circle cx="90" cy="190" r="8" stroke="currentColor" strokeWidth="2.2" />
      <path d="M82 354 H98" stroke="currentColor" strokeWidth="1.7" strokeLinecap="round" />
      <path d="M84 360 H96" stroke="currentColor" strokeWidth="1.2" strokeLinecap="round" opacity="0.7" />
      <circle cx="148" cy="278" r="16" stroke="currentColor" strokeWidth="2.2" />
      <circle cx="148" cy="278" r="4.5" fill="currentColor" />
      <path d="M148 262 V64 H548" stroke="currentColor" strokeWidth="2.2" strokeLinejoin="round" />
      <path d="M292 64 V112 M402 64 V198 M522 64 V284" stroke="currentColor" strokeWidth="2.2" />
      <Channel y={112} />
      <Channel y={198} />
      <Channel y={284} />
    </svg>
  );
}

function Trees({ fit }: { fit: string }) {
  return (
    <svg className="subject-svg" viewBox="0 0 640 440" preserveAspectRatio={fit} aria-hidden="true">
      <path
        d="M24 356 C 150 334, 250 386, 370 348 C 480 314, 548 332, 616 304 V 428 H 24 Z"
        fill="currentColor"
        opacity="0.1"
      />
      <path
        d="M24 356 C 150 334, 250 386, 370 348 C 480 314, 548 332, 616 304"
        fill="none"
        stroke="currentColor"
        strokeWidth="1.7"
      />
      <path d="M198 350 C 188 270, 180 214, 190 156 H 218 C 226 214, 220 274, 214 350 Z" fill="currentColor" />
      <path
        d="M204 176 C 132 164, 96 112, 118 64 C 134 28, 188 16, 214 52 C 232 24, 294 38, 300 86 C 334 62, 372 104, 350 154 C 376 188, 328 214, 274 206 C 258 232, 218 220, 204 176 Z"
        fill="currentColor"
      />
      <path d="M438 338 C 430 286, 424 242, 432 198 H 462 C 468 244, 464 288, 456 338 Z" fill="currentColor" />
      <path
        d="M448 206 C 368 198, 336 150, 362 102 C 380 68, 444 60, 470 100 C 494 64, 566 78, 568 130 C 608 110, 646 162, 606 202 C 628 234, 560 256, 500 236 C 478 260, 438 244, 448 206 Z"
        fill="currentColor"
        opacity="0.78"
      />
    </svg>
  );
}

function Tomato({ cx, cy, r }: { cx: number; cy: number; r: number }) {
  const s = r / 52;
  return (
    <g>
      <circle cx={cx} cy={cy} r={r} fill="currentColor" />
      <path
        d={`M${cx} ${cy - r + 2} V ${cy - r - r * 0.16}`}
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
      />
      <g transform={`translate(${cx} ${cy - r}) scale(${s})`}>
        <path d="M0 4 C -10 -8, -34 -18, -18 2 C -12 6, -4 6, 0 4 Z" fill="currentColor" opacity="0.55" />
        <path d="M0 4 C 10 -8, 34 -18, 18 2 C 12 6, 4 6, 0 4 Z" fill="currentColor" opacity="0.55" />
        <path d="M0 4 C -4 -20, 4 -20, 0 4 Z" fill="currentColor" opacity="0.7" />
        <path d="M0 6 C -16 2, -22 16, -6 10 Z" fill="currentColor" opacity="0.4" />
        <path d="M0 6 C 16 2, 22 16, 6 10 Z" fill="currentColor" opacity="0.4" />
      </g>
    </g>
  );
}

function Tomatoes({ fit }: { fit: string }) {
  return (
    <svg className="subject-svg" viewBox="0 0 640 440" fill="none" preserveAspectRatio={fit} aria-hidden="true">
      <path
        d="M300 24 C 318 78, 250 108, 286 164 C 322 214, 246 246, 292 300"
        stroke="currentColor"
        strokeWidth="1.7"
        strokeLinecap="round"
      />
      <path
        d="M286 164 C 348 142, 392 166, 366 206 C 332 194, 300 194, 286 164 Z"
        fill="currentColor"
        opacity="0.88"
      />
      <path
        d="M286 164 C 228 132, 188 164, 214 202 C 242 184, 270 186, 286 164 Z"
        fill="currentColor"
        opacity="0.7"
      />
      <Tomato cx={168} cy={268} r={54} />
      <Tomato cx={318} cy={300} r={68} />
      <Tomato cx={478} cy={252} r={46} />
      <path d="M64 318 H 584 L 548 404 H 100 Z" stroke="currentColor" strokeWidth="1.7" strokeLinejoin="round" />
      <path d="M92 318 H 556" stroke="currentColor" strokeWidth="9" strokeLinecap="round" opacity="0.18" />
      <path
        d="M156 336 V 390 M 260 332 V 394 M 364 332 V 394 M 468 336 V 390"
        stroke="currentColor"
        strokeWidth="1.25"
        opacity="0.5"
      />
    </svg>
  );
}

export function Subject({
  theme,
  fit = "xMidYMid meet",
}: {
  theme: SubjectTheme;
  fit?: string;
}) {
  return (
    <div className="subject" data-theme={theme}>
      {theme === "hydro" ? <Hydro fit={fit} /> : null}
      {theme === "env" ? <Trees fit={fit} /> : null}
      {theme === "logi" ? <Tomatoes fit={fit} /> : null}
    </div>
  );
}
