import {
  agenda,
  comparison,
  consultantQuestions,
  consultation,
  members,
  recommendation,
} from "../content";
import { MemberCard } from "./MemberCard";
import { Slide } from "./Slide";
import { Subject } from "./Subject";

function Intro() {
  return (
    <Slide theme="editorial" label="Introduction">
      <div className="intro">
        <div className="intro-main">
          <p className="kicker">
            {consultation.occasion} · {consultation.date}
          </p>
          <h1 className="intro-title">Preliminary Title Consultation</h1>
          <p className="intro-for">
            {consultation.group} with {consultation.audience}
          </p>
          <p className="intro-source">{consultation.source}.</p>
        </div>
        <div className="accordion">
          {agenda.map((item) => (
            <article key={item.name} className="accordion-slice bezel" data-theme={item.theme} tabIndex={0}>
              <div className="bezel-core accordion-core">
                <div className="accordion-reveal">
                  <Subject theme={item.theme} fit="xMidYMid slice" />
                </div>
                <div className="accordion-meta">
                  <strong>{item.name}</strong>
                  <span>{item.domain}</span>
                  <em>{item.score}</em>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </Slide>
  );
}

function Members() {
  return (
    <Slide theme="editorial" label="Members">
      <div className="members">
        <header>
          <p className="kicker">{consultation.group}</p>
          <h1 className="members-title">Who is in the room.</h1>
        </header>
        <ul className="member-list">
          {members.map((member) => (
            <MemberCard key={member.name} member={member} />
          ))}
        </ul>
      </div>
    </Slide>
  );
}

function Closing() {
  const [lead, ...rest] = comparison;

  return (
    <Slide theme="editorial" label="Recommendation">
      <div className="closing">
        <header className="closing-head">
          <p className="kicker">
            Comparison · {consultation.source}
          </p>
          <h1 className="closing-title">{recommendation.lead}</h1>
        </header>

        <div className="compare">
          {lead ? (
            <article className="bezel compare-lead" data-theme={lead.theme}>
              <div className="bezel-core compare-lead-core">
                <div className="compare-title">
                  <div>
                    <p className="compare-name">{lead.name}</p>
                    <p className="compare-line">{lead.line}</p>
                  </div>
                  <p className="compare-score">
                    {lead.score}
                    <span>/40</span>
                  </p>
                </div>
                <div className="compare-subject">
                  <Subject theme={lead.theme} fit="xMidYMid slice" />
                </div>
                <CompareFacts item={lead} />
              </div>
            </article>
          ) : null}
          {rest.map((item) => (
            <article key={item.name} className="bezel compare-side" data-theme={item.theme}>
              <div className="bezel-core compare-side-core">
                <div className="compare-title">
                  <p className="compare-name">{item.name}</p>
                  <p className="compare-line">{item.line}</p>
                  <p className="compare-score">
                    {item.score}
                    <span>/40</span>
                  </p>
                </div>
                <div className="compare-subject">
                  <Subject theme={item.theme} fit="xMidYMid meet" />
                </div>
                <CompareFacts item={item} />
              </div>
            </article>
          ))}
        </div>

        <div className="closing-bottom">
          <p className="recommend-body">{recommendation.body}</p>
          <ol className="next-steps">
            {recommendation.steps.map((step) => (
              <li key={step}>{step}</li>
            ))}
          </ol>
        </div>

        <section className="ask" aria-label="Questions for the consultant">
          <p className="kicker">Questions for Doc Garcia</p>
          <ol>
            {consultantQuestions.map((question) => (
              <li key={question}>{question}</li>
            ))}
          </ol>
        </section>
      </div>
    </Slide>
  );
}

function CompareFacts({
  item,
}: {
  item: (typeof comparison)[number];
}) {
  return (
    <dl>
      <div>
        <dt>Rank</dt>
        <dd>{item.rank} of 3</dd>
      </div>
      <div>
        <dt>Data</dt>
        <dd>{item.data}</dd>
      </div>
      <div>
        <dt>Time</dt>
        <dd>{item.time}</dd>
      </div>
    </dl>
  );
}

export function EditorialSlide({ kind }: { kind: "intro" | "members" | "closing" }) {
  if (kind === "intro") return <Intro />;
  if (kind === "members") return <Members />;
  return <Closing />;
}
