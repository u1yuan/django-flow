# QA concept extraction

Sources and access levels are in `source-trace.md`. Paper A locators are section numbers, because the HTML view has no page numbers. Paper B locators are printed journal pages. Quotes are 25 words or fewer. Paper B quotes were rechecked in this session against a `pdftotext` extract of the author reprint (temp only). The page 58 body after the standfirst was read.

Paper A is a research plan. Its concepts describe gaps it identifies and methods it intends to use. None of them is a validated finding.

## Paper A: Effendy et al. (2025)

| ID | Concept | Location | Short quote |
| --- | --- | --- | --- |
| A-1 | The paper declares itself a plan, and its methods are written in the future tense | Title; §4.2 para 1 | "This research will be conducted in three stages to address the research questions." |
| A-2 | Gap: insufficient reporting standards for model performance, which comparison between models needs | Abstract; §5 last para | "insufficient reporting standards for model performance required for model comparison" |
| A-3 | Gap: no standards for fault reporting or for appropriate metrics | §3 para 1 (citing Alamin [18]) | "lack of standards in fault reporting & appropriate metrics" |
| A-4 | Gap: QA tasks are not defined clearly for each workflow stage | Abstract; §3 para 1 | "do not explain clearly how the QA process is carried out at each stage, especially at the model-building stage" |
| A-5 | QA tasks are to be made concrete as guidelines or checklists | §3 RQ2; §5 para 2 | "This QA process will then be formulated in greater detail, such as guidelines or checklists." |
| A-6 | Planned model-performance report format | §5 para 2 | "including guidelines, checklists, and model performance reports format" |
| A-7 | Research variables defined for each research question (independent and dependent) | §4.1 | "research variables are defined for each of the RQs" |
| A-8 | Validation methods: Likert survey with ANOVA and correlation analysis, expert validation, and experiments with teams | §4.2 paras 1–3; Abstract | "The formulated QA model is then presented to experts for validation and feedback." |
| A-9 | Comparison of a typical framework with the proposed one | §4.2 para 3 | "In the first experiment, the teams will use the typical QA framework." |
| A-10 | Planned bias controls: at least two teams, and a time gap between the experiments | §4.2 para 3 | "There will be a sufficient time gap between the experiments to reduce bias." |
| A-11 | Planned outcome: whether the fault report format helps stakeholders compare models | §4.2 para 3, item (4) | "whether the fault report format can aid stakeholders in comparing different ML models" |
| A-12 | Model-building factors that may vary, such as algorithm selection and hyperparameters | §5 para 1 | "data quality, algorithm selection methods, hyperparameter settings, parameter optimization, evaluation tools" |
| A-13 | Practice gap: developers focus on accuracy and functional testing | §1 para 4 | "developers generally focus more on ML model accuracy and end-product functionality testing" |

## Paper B: Remmel et al. (2014)

| ID | Concept | Location | Short quote |
| --- | --- | --- | --- |
| B-1 | The study evaluates feasibility and acceptance of two QA process parts | p. 58 standfirst; p. 60 "Case Study Design" | "analyzes the feasibility and acceptance by developers of two parts of the quality assurance process" |
| B-2 | Separate goals for feasibility and acceptance, analyzed from the developer's viewpoint | p. 60 "Research Questions" | "Goal 1: Assess the feasibility of variability modeling." … "Goal 3: Assess the acceptance of variability modeling." |
| B-3 | Effort is its own question: do the advantages outweigh the effort? | p. 60 "Feasibility"; p. 62 Table 1 (E_RQ_VM, E_RQ_DC) | "if the Dune developers think that the advantages of these methods outbalance the effort required" |
| B-4 | Each research question is coded and linked to a hypothesis and a data source; the design follows the goal question metric approach | p. 60; p. 62 Table 1 and legend | "F = feasibility, E = effort, A = acceptance" |
| B-5 | Acceptance is measured with the technology acceptance model (usefulness, ease of use, intention to use) | pp. 60–61 "Acceptance" | "perceived usefulness and ease of use are of primary relevance for acceptance behavior." |
| B-6 | Desk-checking: the developer reads their own code before check-in | p. 59 "Review" | "consciously read one's own code before checking it in (also called desk-checking)" |
| B-7 | Desk-checking is deliberately **not** a structured inspection | p. 60 para 3 | "We don't pursue a structured inspection or review process, as the goal is to keep the quality assurance process practical and simple." |
| B-8 | Desk-checking checklist | p. 63 sidebar "Proposed Desk-Checking Checklist" | "Before checking in, please read through the source code one more time" |
| B-9 | Subjective checklist items need minimum requirements | p. 64 "Disadvantages of Desk-Checking"; p. 65 "Goal 2" | "Most of the items in the checklist are subjective." / "Minimum requirements must be defined for each issue" |
| B-10 | Variability modeling: variation points and their variants | p. 59 "Case Study Background" | "Software characteristics that can vary are called variation points and a variation point's possible values are called variants." |
| B-11 | Each valid combination of variants is a test case (coverage of configurations) | p. 63 "Advantages of Variability Modeling" | "every valid combination of variants is a test case" |
| B-12 | The chosen viewpoint and level of detail change what the model covers | p. 63 "Capturing the Variability…"; p. 64 para 1 | "the viewpoint has a major influence on the created variability model." |
| B-13 | Participants and context are described | p. 60 "Case Study Design" | "The case study was executed with a group of six Dune developers." |
| B-14 | Data sources and aggregation rules: counting similar answers, Likert median, tie rule | p. 61 "Research Methods" | "For the closed questionnaire questions, we used a Likert scale and aggregated the answers with a median." |
| B-15 | Desk-checking was not tried out directly | p. 61 "Research Methods" | "The developers didn't try out desk-checking directly because it wasn't possible to simulate a realistic application of desk-checking." |
| B-16 | Anti-priming controls: the moderator stayed neutral, and open questions came before closed ones | p. 65 "Construct Validity" | "The moderator didn't mention any advantages or disadvantages of the methods." |
| B-17 | Triangulation, chain of evidence, external observer, and member checking | p. 65 "Construct Validity" | "To achieve a methodological triangulation, we combined different types of data collection methods: observation, questionnaire, and discussion." |
| B-18 | Reliability: every step documented, peer-reviewed, and the design externally reviewed | p. 66 "Reliability" | "A second researcher peer reviewed each step." |
| B-19 | Threats to validity reported, including a confound from the method's own tooling | p. 65 "Construct Validity" | "Some problems with this specific variability modeling language might have negatively influenced the results" |
| B-20 | Generalization is qualified | pp. 65–66 "External Validity" | "Further examination is necessary to confirm this." |
| B-21 | Instruments were checked before use | p. 65 "Construct Validity" | "Several researchers checked the questions in the questionnaire for understandability." |

## Candidate seeds: confirmed or discarded

| Seed | Decision | Basis |
| --- | --- | --- |
| A: completeness of performance reporting (metrics, baselines, comparability) | **Confirmed, split in two.** Metrics and comparability: A-2, A-3, A-6, A-11. Baseline: A-9 is a design element of A's planned experiment, not a reporting standard, so it becomes its own criterion (C03) | Abstract; §3; §4.2; §5 |
| A: clarity of the quality tasks at each phase | **Confirmed** | A-4, A-5 |
| A: whether the paper reports a plan or evidence | **Confirmed as adapted.** A labels itself a plan (A-1) but never discusses "plan versus evidence" as a QA concept. The criterion generalizes A's self-labelling | Title; §4.2 |
| A: validation method (expert review, pilot) | **Confirmed.** The abstract says "pilot project scheme". §4.2 describes this as two experiments with at least two teams. Bias controls (A-10) became their own criterion (C06) | A-8, A-10 |
| B: feasibility and acceptance as separate questions | **Confirmed and extended to include effort,** which B treats as its own question (E codes) | B-2, B-3, B-4 |
| B: desk-checking as a structured review pass | **Partly discarded.** B says explicitly that desk-checking is *not* a structured inspection (B-7). The kept part is a checklist-guided self-review before release (B-6, B-8). It is used in two ways: as an adapted criterion about authors' self-review (C15), and as the reviewer's own pre-scoring pass (`desk-check-checklist.md`) | pp. 59, 60, 63 |
| B: variability coverage | **Confirmed as adapted.** B uses variability modeling to derive system tests for a software framework. Applying it to "which configurations a paper's results hold for" is an extension. A-12 adds the ML settings dimension | B-10, B-11, B-12; A-12 |
| B: honest reporting of the method's own limits | **Confirmed** | B-19, B-20 |

## Concepts added beyond the seeds

- **Traceability from research question to data** (C07): A-7 and B-4.
- **Acceptance measured with defined constructs** (C09): B-5.
- **Participant and context description** (C10): B-13.
- **Analysis and aggregation procedure** (C11): A-8 and B-14.
- **Validity safeguards** (C12): B-16, B-17, and B-18. B-16 also informs C06.

## Design principle taken from Paper B

B-9 says subjective checklist items need minimum requirements. In this rubric, each score anchor therefore states an observable minimum condition, not a quality adjective. Using the concept this way is an adaptation.
