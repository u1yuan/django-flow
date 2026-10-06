/**
 * All pitch copy lives here.
 * Member second lines: set `personal` to a short phrase to show it.
 * Leave `personal` as "" and only the name is shown.
 */

export type Theme = "editorial" | "hydro" | "env" | "logi";

export type Criterion = {
  label: string;
  score: number;
};

export type Chip = {
  label: string;
  value: string;
};

export type Member = {
  name: string;
  personal: string;
};

export type TitleContent = {
  id: string;
  kind: "title";
  theme: Exclude<Theme, "editorial">;
  kicker: string;
  short: string;
  title: string;
  overview: string;
  objectives: string[];
  datasetScore: string;
  dataset: string[];
  algorithmScore: string;
  algorithmStudy: string;
  algorithmNow: string;
  criteria: Criterion[];
  chips: Chip[];
  footnote: string;
};

export type EditorialContent = {
  id: string;
  kind: "intro" | "members" | "closing";
  theme: "editorial";
};

export type SlideContent = TitleContent | EditorialContent;

export const consultation = {
  group: "Group Django",
  audience: "Doc Manuel B. Garcia",
  occasion: "First title consultation",
  date: "1 October 2026",
  source: "Feasibility study, submitted 17 September 2026",
};

export function domainFromKicker(kicker: string): string {
  const piece = kicker.split("·").pop();
  return (piece ?? kicker).trim();
}

export const members: Member[] = [
  { name: "Reese Lauren C. Chan", personal: "" },
  { name: "Fathi Mahad Ebrahim", personal: "" },
  { name: "Denienz A. Pacate", personal: "" },
  { name: "Juan Angelo Roy B. Whitty", personal: "" },
];

const hydroCriteria: Criterion[] = [
  { label: "Tech", score: 5 },
  { label: "Data", score: 2 },
  { label: "Model", score: 5 },
  { label: "Ops", score: 4 },
  { label: "Cost", score: 5 },
  { label: "Time", score: 3 },
  { label: "Ethics", score: 5 },
  { label: "Risk", score: 3 },
];

const envCriteria: Criterion[] = [
  { label: "Tech", score: 4 },
  { label: "Data", score: 3 },
  { label: "Model", score: 5 },
  { label: "Ops", score: 3 },
  { label: "Cost", score: 3 },
  { label: "Time", score: 4 },
  { label: "Ethics", score: 5 },
  { label: "Risk", score: 4 },
];

const logiCriteria: Criterion[] = [
  { label: "Tech", score: 4 },
  { label: "Data", score: 3 },
  { label: "Model", score: 5 },
  { label: "Ops", score: 3 },
  { label: "Cost", score: 3 },
  { label: "Time", score: 2 },
  { label: "Ethics", score: 5 },
  { label: "Risk", score: 4 },
];

export const titles: TitleContent[] = [
  {
    id: "aquavir",
    kind: "title",
    theme: "hydro",
    kicker: "Title 01  ·  Agriculture",
    short: "AquaVir",
    title:
      "AquaVir: Multi-Zone Hydroponic Sensor Forecasting and Fault Detection with TFT and Random Forest",
    overview:
      "Zones already log pH, EC, temperature, humidity, and related readings. AquaVir reads that existing stream: a next-day forecast for each zone, and a separate fault check when labels exist. Hardware is not the contribution.",
    objectives: [
      "Forecast eligible sensors one day ahead, hourly, for each zone.",
      "Classify labeled sensor faults with random forest, only if verified labels exist.",
      "Show operators which zone moved, without calling a forecast miss a confirmed fault.",
    ],
    datasetScore: "2 / 5",
    dataset: [
      "No facility export or fault-label file is confirmed.",
      "The study asks for at least three zones and 10,000+ timestamped rows.",
      "Written permission is due before early Semester 2, or the study says to pivot.",
    ],
    algorithmScore: "5 / 5",
    algorithmStudy:
      "The study scored a zone baseline, a multivariate anomaly score, and change-point detection. That 5/5 is for those approaches, not for a model already run.",
    algorithmNow:
      "Working method, 29 Sep 2026: Temporal Fusion Transformer for the 24-hour forecast, and random forest for labeled faults. Outputs stay separate. Neither has been run on facility data.",
    criteria: hydroCriteria,
    chips: [
      { label: "Study score", value: "32 / 40" },
      { label: "Rank", value: "1 of 3" },
      { label: "Schedule", value: "3 trimesters" },
    ],
    footnote:
      "32/40 belongs to the study wording “Multi-Zone Hydroponic Sensor Analytics for Zone Consistency Monitoring and Anomaly Prioritization.” AquaVir is the later working title.",
  },
  {
    id: "environment",
    kind: "title",
    theme: "env",
    kicker: "Title 02  ·  Environment",
    short: "Native trees",
    title:
      "An Explainable GIS-Based Decision Support System Using MaxEnt, AHP, and Edge Sensing for Philippine Native Tree Site Suitability",
    overview:
      "A planting site needs a species that fits it. The system joins public maps, a few local sensors, and expert requirements, then ranks Philippine native trees and explains the rank. It supports a forester. It does not replace one.",
    objectives: [
      "Score and rank species for a site, with a short explanation.",
      "Map elevation, slope, rainfall, soil, and land cover, plus field readings.",
      "Leave the planting decision with a forestry expert.",
    ],
    datasetScore: "3 / 5",
    dataset: [
      "Public layers: Copernicus DEM GLO-30, WorldClim 2.1, CHIRPS, SoilGrids, WorldCover.",
      "Requirements for three to five species, from DENR, studies, and experts.",
      "ESP32 nodes for soil moisture, temperature, humidity, and light. Site and experts are not secured yet.",
    ],
    algorithmScore: "5 / 5",
    algorithmStudy:
      "The study’s primary method is Analytic Hierarchy Process with a GIS weighted overlay. It also scored fuzzy-logic suitability and random forest classification.",
    algorithmNow:
      "MaxEnt is named in the working title. The feasibility study did not compare it. AHP remains the method that received the 5/5.",
    criteria: envCriteria,
    chips: [
      { label: "Study score", value: "31 / 40" },
      { label: "Rank", value: "2 of 3" },
      { label: "Schedule", value: "3 trimesters" },
    ],
    footnote:
      "The study originally allowed two trimesters. This consultation plans three trimesters, the same duration as the other titles.",
  },
  {
    id: "logistics",
    kind: "title",
    theme: "logi",
    kicker: "Title 03  ·  Logistics",
    short: "Tomato shelf life",
    title:
      "Predictive Analytics for Estimating Tomato Shelf-Life from ESP32 Temperature-Humidity Data in Metro Manila Logistics",
    overview:
      "Heat and humidity inside a Metro Manila delivery change how fast tomatoes decline. An ESP32 records the trip. Daily checks after arrival become labels for an estimate of remaining shelf life, in days.",
    objectives: [
      "Estimate remaining acceptable shelf life in days.",
      "Pair the sensor trace with weather, route, and delay.",
      "Compare three regression models on the same labels.",
    ],
    datasetScore: "3 / 5",
    dataset: [
      "The group collects the deliveries and the daily quality checks.",
      "Study target: 300–500 labeled tomatoes, one variety, selected routes.",
      "Context from PAGASA, Google Routes, and TomTom, or from manual logs if APIs are dropped.",
    ],
    algorithmScore: "5 / 5",
    algorithmStudy:
      "The study compares linear regression, a decision tree, and random forest. Named metrics are MAE, RMSE, and R².",
    algorithmNow:
      "No delivery has been run. The 5/5 is a judgment that these three models are implementable, not a measured error.",
    criteria: logiCriteria,
    chips: [
      { label: "Study score", value: "29 / 40" },
      { label: "Rank", value: "3 of 3" },
      { label: "Schedule", value: "3 trimesters" },
    ],
    footnote:
      "The study scored Time 2/5. This consultation still plans three trimesters.",
  },
];

export const agenda = [
  {
    index: "01",
    name: "AquaVir",
    domain: "Hydroponics",
    score: "32/40",
    theme: "hydro" as const,
  },
  {
    index: "02",
    name: "Native-tree suitability",
    domain: "Environment",
    score: "31/40",
    theme: "env" as const,
  },
  {
    index: "03",
    name: "Tomato shelf life",
    domain: "Logistics",
    score: "29/40",
    theme: "logi" as const,
  },
];

export const comparison = [
  {
    name: "AquaVir",
    line: "Multi-zone sensor forecasting and fault detection",
    theme: "hydro" as const,
    score: "32",
    rank: "1",
    data: "2/5",
    time: "3 trimesters",
  },
  {
    name: "Native trees",
    line: "Explainable site suitability for Philippine species",
    theme: "env" as const,
    score: "31",
    rank: "2",
    data: "3/5",
    time: "3 trimesters",
  },
  {
    name: "Tomato shelf life",
    line: "Shelf-life estimate from delivery climate traces",
    theme: "logi" as const,
    score: "29",
    rank: "3",
    data: "3/5",
    time: "3 trimesters",
  },
];

export const consultantQuestions = [
  "What areas of these three titles could we explore further?",
  "What could your expertise offer across all three titles?",
];

export const recommendation = {
  lead: "The study recommends AquaVir, on one condition.",
  body: "It scored 32/40 because the work stays on analytics and uses a facility’s existing sensors. Dataset access is the weak mark. If a three-zone facility and usable records are not in hand by early Semester 2, the study’s fallback is the native-tree title, which can lean on public GIS layers.",
  steps: [
    "Confirm which title to pursue.",
    "If AquaVir: name the facility, the variables, and the access deadline.",
    "If native trees: confirm the site, the experts, and whether MaxEnt stays in the title.",
    "If logistics: lock one variety, the routes, and how many deliveries.",
  ],
};

export const slides: SlideContent[] = [
  { id: "intro", kind: "intro", theme: "editorial" },
  { id: "members", kind: "members", theme: "editorial" },
  titles[0],
  titles[1],
  titles[2],
  { id: "closing", kind: "closing", theme: "editorial" },
];
