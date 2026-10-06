import { domainFromKicker, type TitleContent } from "../content";
import { FeasibilityBars } from "./FeasibilityBars";
import { Slide } from "./Slide";
import { StatChip } from "./StatChip";
import { Subject } from "./Subject";

export function TitleSlide({ slide }: { slide: TitleContent }) {
  const study = slide.chips.find((chip) => chip.label === "Study score");
  const rank = slide.chips.find((chip) => chip.label === "Rank");
  const scoreParts = (study?.value ?? "").split("/");

  return (
    <Slide theme={slide.theme} label={slide.short}>
      <header className="title-head">
        <p className="kicker">{domainFromKicker(slide.kicker)}</p>
        <div className="title-nameplate">
          <h1 className="title-display">{slide.short}</h1>
          <div className="title-rank">
            <p className="title-rank-value">
              {scoreParts[0]?.trim()}
              <span>/{scoreParts[1]?.trim()}</span>
            </p>
            {rank ? <p className="title-rank-label">{rank.value}</p> : null}
          </div>
        </div>
        <p className="title-full">{slide.title}</p>
      </header>

      <div className="title-bento">
        <div className="bezel bento-copy">
          <div className="bezel-core bento-copy-core">
            <p className="overview">{slide.overview}</p>
            <section className="bento-block" aria-label="Objectives">
              <h2>Objectives</h2>
              <ol>
                {slide.objectives.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ol>
            </section>

            <section className="bento-block" aria-label="Dataset feasibility">
              <div className="block-head">
                <h2>Dataset</h2>
                <p>{slide.datasetScore}</p>
              </div>
              <ul>
                {slide.dataset.map((item) => (
                  <li key={item}>{item}</li>
                ))}
              </ul>
            </section>

            <section className="bento-block" aria-label="Algorithm feasibility">
              <div className="block-head">
                <h2>Algorithm</h2>
                <p>{slide.algorithmScore}</p>
              </div>
              <p className="block-copy">{slide.algorithmStudy}</p>
              <p className="block-copy block-now">{slide.algorithmNow}</p>
            </section>
          </div>
        </div>

        <div className="bezel subject-plate">
          <div className="bezel-core subject-frame">
            <Subject theme={slide.theme} />
          </div>
        </div>
      </div>

      <FeasibilityBars items={slide.criteria} />

      <footer className="title-foot">
        <div className="chip-row">
          {slide.chips.map((chip) => (
            <StatChip key={chip.label} {...chip} />
          ))}
        </div>
        <p className="footnote">{slide.footnote}</p>
      </footer>
    </Slide>
  );
}
