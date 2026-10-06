import type { Chip } from "../content";

export function StatChip({ label, value }: Chip) {
  return (
    <div className="chip">
      <div className="chip-core">
        <span className="chip-label">{label}</span>
        <span className="chip-value">{value}</span>
      </div>
    </div>
  );
}
