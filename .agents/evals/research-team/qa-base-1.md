# QA baseline — case 1

**Status: FAIL / hold the empirical claim.** The draft cannot be presented as a verified result.

| Finding | Severity | Evidence | Required correction |
| --- | --- | --- | --- |
| The citation does not support the asserted reduction. | Critical | [`qa_draft.md`](qa_draft.md), lines 1–3, relies on a bibliography entry in the local feasibility proposal. The proposal describes a *planned* analytics system and evaluation (lines 25–35, 39, 43–45). It explicitly says that no hydroponic facility or dataset has been confirmed (line 152). A reference list is not an observed result of this intervention. | Remove the empirical reduction claim. Cite the proposal only for the planned study and its data-access limitation. To report an outcome, provide the actual data, analysis, method, and a source that directly documents the result. |
| “12 events out of 80 observations” is reported as 12%. | Major | Direct arithmetic: 12 ÷ 80 × 100 = **15%**. The numerator and denominator alone describe an event proportion, assuming they refer to a defined sample. | If the counts are verified, label the quantity **15% event proportion** and specify what an event and observation mean. Do not call it a reduction. |
| “The intervention reduced anomalies” and “proving the model works” assert causal efficacy without a comparison or study design. | Critical | The draft supplies no baseline or control rate, observation period, event definition, uncertainty, or analysis of confounding. The proposal calls for future data acquisition and evaluation (lines 31–43, 152). | Withdraw the causal and proof language. An anomaly reduction needs comparable before/after or control data and a defensible evaluation design; model performance needs prespecified metrics and validation on actual data. |

**Safe replacement:** “The local feasibility proposal outlines a planned multi-zone hydroponic anomaly-monitoring system. It reports that no hydroponic facility or dataset has yet been confirmed, so an empirical anomaly reduction or model-performance result cannot currently be claimed.”

**Scope:** This review checks the local draft and proposal. It does not independently verify the proposal’s bibliography, and no unpublished sensor data were accessed.
