import type { Criterion } from "../content";

export function FeasibilityBars({ items }: { items: Criterion[] }) {
  return (
    <ol className="bars" aria-label="Feasibility scores out of 5">
      {items.map((item) => (
        <li key={item.label} className={item.score <= 2 ? "is-low" : undefined}>
          <span className="bars-label">{item.label}</span>
          <span className="bars-score">
            {item.score}
            <span>/5</span>
          </span>
          <span className="bars-track" aria-hidden="true">
            <span style={{ width: `${(item.score / 5) * 100}%` }} />
          </span>
        </li>
      ))}
    </ol>
  );
}
