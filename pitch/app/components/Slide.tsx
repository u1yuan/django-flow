import type { ReactNode } from "react";
import type { Theme } from "../content";

export function Slide({
  theme,
  label,
  children,
}: {
  theme: Theme;
  label: string;
  children: ReactNode;
}) {
  return (
    <section className="slide" data-theme={theme} aria-label={label}>
      <div className="slide-content">{children}</div>
    </section>
  );
}
