$ErrorActionPreference = 'Stop'

$work = Join-Path $PSScriptRoot '.ta4_docx_work'
$path = Join-Path $work 'word\document.xml'
$xml = New-Object System.Xml.XmlDocument
$xml.PreserveWhitespace = $false
$xml.Load($path)
$w = 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'
$mgr = New-Object System.Xml.XmlNamespaceManager($xml.NameTable)
$mgr.AddNamespace('w', $w)
$body = $xml.SelectSingleNode('/w:document/w:body', $mgr)
$original = @($body.ChildNodes)

function WNode([string]$name) { return $xml.CreateElement('w', $name, $w) }
function WAttr($node, [string]$name, [string]$value) {
    $attr = $xml.CreateAttribute('w', $name, $w)
    $attr.Value = $value
    [void]$node.Attributes.Append($attr)
}
function AddRun($paragraph, [string]$value, [bool]$bold = $false, [string]$size = '22') {
    $run = WNode 'r'
    $properties = WNode 'rPr'
    $font = WNode 'rFonts'
    WAttr $font 'ascii' 'Arial Narrow'
    WAttr $font 'hAnsi' 'Arial Narrow'
    [void]$properties.AppendChild($font)
    if ($bold) { [void]$properties.AppendChild((WNode 'b')) }
    $fontSize = WNode 'sz'
    WAttr $fontSize 'val' $size
    [void]$properties.AppendChild($fontSize)
    [void]$run.AppendChild($properties)
    $t = WNode 't'
    $space = $xml.CreateAttribute('xml', 'space', 'http://www.w3.org/XML/1998/namespace')
    $space.Value = 'preserve'
    [void]$t.Attributes.Append($space)
    $t.InnerText = $value
    [void]$run.AppendChild($t)
    [void]$paragraph.AppendChild($run)
}
function AddParagraph([string]$value, [string]$label = '') {
    $p = WNode 'p'
    $pPr = WNode 'pPr'
    $spacing = WNode 'spacing'
    WAttr $spacing 'after' '140'
    WAttr $spacing 'line' '260'
    WAttr $spacing 'lineRule' 'auto'
    [void]$pPr.AppendChild($spacing)
    [void]$p.AppendChild($pPr)
    if ($label) { AddRun $p $label $true }
    AddRun $p $value
    [void]$body.AppendChild($p)
}
function AddHeading([string]$value) {
    $p = WNode 'p'
    $pPr = WNode 'pPr'
    $style = WNode 'pStyle'
    WAttr $style 'val' 'Heading2'
    [void]$pPr.AppendChild($style)
    $spacing = WNode 'spacing'
    WAttr $spacing 'before' '260'
    WAttr $spacing 'after' '100'
    [void]$pPr.AppendChild($spacing)
    [void]$p.AppendChild($pPr)
    AddRun $p $value $true '24'
    [void]$body.AppendChild($p)
}
function AddSubheading([string]$value) {
    $p = WNode 'p'
    $pPr = WNode 'pPr'
    $spacing = WNode 'spacing'
    WAttr $spacing 'before' '140'
    WAttr $spacing 'after' '60'
    [void]$pPr.AppendChild($spacing)
    [void]$p.AppendChild($pPr)
    AddRun $p $value $true '22'
    [void]$body.AppendChild($p)
}
function AddReference([string]$value) {
    $p = WNode 'p'
    $pPr = WNode 'pPr'
    $indent = WNode 'ind'
    WAttr $indent 'left' '620'
    WAttr $indent 'hanging' '620'
    [void]$pPr.AppendChild($indent)
    $spacing = WNode 'spacing'
    WAttr $spacing 'after' '100'
    [void]$pPr.AppendChild($spacing)
    [void]$p.AppendChild($pPr)
    AddRun $p $value $false '21'
    [void]$body.AppendChild($p)
}
function SetCell($cell, [string]$value, [int]$width, [bool]$bold = $false, [bool]$shade = $false) {
    $tcPr = $cell.SelectSingleNode('w:tcPr', $mgr)
    if (-not $tcPr) { $tcPr = WNode 'tcPr'; [void]$cell.PrependChild($tcPr) }
    $oldWidth = $tcPr.SelectSingleNode('w:tcW', $mgr)
    if ($oldWidth) { [void]$tcPr.RemoveChild($oldWidth) }
    $tcW = WNode 'tcW'
    WAttr $tcW 'w' ([string]$width)
    WAttr $tcW 'type' 'dxa'
    [void]$tcPr.PrependChild($tcW)
    $mar = $tcPr.SelectSingleNode('w:tcMar', $mgr)
    if (-not $mar) { $mar = WNode 'tcMar'; [void]$tcPr.AppendChild($mar) }
    foreach ($edge in @('top','left','bottom','right')) {
        $part = $mar.SelectSingleNode('w:' + $edge, $mgr)
        if (-not $part) { $part = WNode $edge; [void]$mar.AppendChild($part) }
        WAttr $part 'w' '70'
        WAttr $part 'type' 'dxa'
    }
    if ($shade) {
        $shd = $tcPr.SelectSingleNode('w:shd', $mgr)
        if (-not $shd) { $shd = WNode 'shd'; [void]$tcPr.AppendChild($shd) }
        WAttr $shd 'fill' 'E9EFF4'
        WAttr $shd 'val' 'clear'
    }
    foreach ($child in @($cell.ChildNodes)) { if ($child.LocalName -ne 'tcPr') { [void]$cell.RemoveChild($child) } }
    $p = WNode 'p'
    $pPr = WNode 'pPr'
    $spacing = WNode 'spacing'
    WAttr $spacing 'after' '0'
    WAttr $spacing 'line' '225'
    WAttr $spacing 'lineRule' 'auto'
    [void]$pPr.AppendChild($spacing)
    [void]$p.AppendChild($pPr)
    AddRun $p $value $bold '19'
    [void]$cell.AppendChild($p)
}
function FillTable($table, $data, [int[]]$widths) {
    $total = ($widths | Measure-Object -Sum).Sum
    $tblPr = $table.SelectSingleNode('w:tblPr', $mgr)
    $tblW = $tblPr.SelectSingleNode('w:tblW', $mgr)
    WAttr $tblW 'w' ([string]$total)
    WAttr $tblW 'type' 'dxa'
    $tblInd = $tblPr.SelectSingleNode('w:tblInd', $mgr)
    if ($tblInd) { WAttr $tblInd 'w' '0' }
    $grid = $table.SelectSingleNode('w:tblGrid', $mgr)
    foreach ($child in @($grid.ChildNodes)) { [void]$grid.RemoveChild($child) }
    foreach ($width in $widths) {
        $col = WNode 'gridCol'
        WAttr $col 'w' ([string]$width)
        [void]$grid.AppendChild($col)
    }
    $rows = @($table.SelectNodes('w:tr', $mgr))
    if ($rows.Count -ne $data.Count) { throw "Table row count mismatch: $($rows.Count) vs $($data.Count)" }
    for ($i = 0; $i -lt $rows.Count; $i++) {
        $trPr = $rows[$i].SelectSingleNode('w:trPr', $mgr)
        if ($trPr) {
            $height = $trPr.SelectSingleNode('w:trHeight', $mgr)
            if ($height) { [void]$trPr.RemoveChild($height) }
            if ($i -eq 0) {
                $header = $trPr.SelectSingleNode('w:tblHeader', $mgr)
                if (-not $header) { $header = WNode 'tblHeader'; [void]$trPr.AppendChild($header) }
                WAttr $header 'val' '1'
            }
        }
        $cells = @($rows[$i].SelectNodes('w:tc', $mgr))
        if ($cells.Count -ne $widths.Count) { throw "Cell count mismatch in row $i" }
        for ($j = 0; $j -lt $cells.Count; $j++) {
            SetCell $cells[$j] $data[$i][$j] $widths[$j] ($i -eq 0 -or $j -eq 0) ($i -eq 0)
        }
    }
}

# Retain the cover and its section break, then replace the assignment prompts.
for ($i = $body.ChildNodes.Count - 1; $i -ge 17; $i--) { [void]$body.RemoveChild($body.ChildNodes[$i]) }

AddHeading 'Part A. Selected Comparison'
AddParagraph 'Agile vs. Waterfall. I selected this comparison to judge how AquaVir should be developed while its data availability and some requirements remain uncertain. It also shows when a fixed plan and formal approvals would be more useful than frequent adaptation.' 'Selected comparison: '

AddHeading 'Part B. Overview of the Two Approaches'
AddParagraph 'Agile is a family of iterative and incremental approaches that emphasizes working software, customer collaboration, and response to change. A team selects a small set of priorities, builds and tests an increment, reviews it with stakeholders, and adjusts the next cycle. It fits projects where needs may evolve and stakeholders can give regular feedback (Beck et al., 2001; U.S. Government Accountability Office [GAO], 2023).' 'Agile. '
AddParagraph 'Waterfall is a predictive approach that organizes work into successive requirements, design, implementation, testing, and release phases, with defined deliverables and reviews. It fits well-understood work with stable scope and a need for documented approvals. Changes can still be managed, but late discoveries may require substantial rework (Burgan & Burgan, 2014; Royce, 1970).' 'Waterfall. '

AddHeading 'Part C. Comparative Analysis'
$matrix = @(
    @('Comparison Criterion','Agile','Waterfall','Analysis'),
    @('Development Approach','Iterative increments','Sequential phases','Increments reveal assumptions early; phase gates support baseline control.'),
    @('Requirements','Refined with feedback','Defined and baselined early','Uncertainty favors revision; stability favors traceability.'),
    @('Planning','Roadmap plus short-cycle plans','Detailed plan before major build','Rolling plans incorporate evidence; upfront plans support estimates.'),
    @('Team Structure','Collaborative, often cross-functional','Roles aligned with phase deliverables','Fast collaboration reduces handoffs; phase ownership clarifies accountability.'),
    @('Customer/Stakeholder Involvement','Frequent reviews and prioritization','Reviews at planned milestones','Frequent input enables correction; milestone input demands less time.'),
    @('Handling of Changes','Reprioritize future increments','Formal review of baseline changes','Flexibility helps uncertain work; control protects approved scope.'),
    @('Documentation','Sufficient, current records','Detailed phase artifacts','Both need records; the timing and detail serve different oversight needs.'),
    @('Testing/Quality Assurance','Test each increment','Planned verification, often after build','Early tests expose defects sooner; formal tests aid traceability.'),
    @('Delivery/Release','Frequent usable increments','Usually one main release after phases','Early value and feedback trade against a single acceptance point.'),
    @('Risk Management','Validate assumptions repeatedly','Analyze and review known risks early','Feedback reduces uncertainty; late test findings remain a concern in sequential work.'),
    @('Advantages','Adapts and delivers value early','Clear scope, milestones, and records','Each advantage matters only if it addresses the actual project constraints.'),
    @('Limitations','Needs engaged users and team discipline','Late changes can be costly','Weak engagement hurts Agile; unstable assumptions hurt Waterfall.'),
    @('Suitable Project Types','Evolving, feedback-rich products','Stable, well-specified projects with approvals','Select by volatility, stakeholder access, and governance needs.')
)
$comparisonTable = $original[43].CloneNode($true)
FillTable $comparisonTable $matrix @(1800,2200,2200,3800)
[void]$body.AppendChild($comparisonTable)
AddParagraph 'Note. The comparison synthesizes Beck et al. (2001), Burgan and Burgan (2014), GAO (2023), and Royce (1970). Royce cautioned that a rigid one-pass sequence can be risky; Waterfall here describes the common predictive, phase-based approach.'

AddHeading 'Part D. Scenario-Based Application'
AddSubheading 'Scenario 1: Stable Requirements'
AddParagraph 'I recommend Waterfall. The company can agree on requirements and acceptance criteria early, then use documented reviews at each major stage. This matches management approval needs and gives a clear basis for change control. Testing should still be planned early because discovering major problems only at the end raises rework risk (Burgan & Burgan, 2014; Royce, 1970).'
AddSubheading 'Scenario 2: Changing Requirements'
AddParagraph 'I recommend Agile. The startup can release small working features, test them, collect customer feedback, and reprioritize the next increment. A fixed early specification would make the expected changes harder to absorb. Each release still needs testing and enough documentation to maintain the product (Beck et al., 2001; GAO, 2023).'
AddSubheading 'Scenario 3: AquaVir'
AddParagraph 'AquaVir is planned to forecast hourly readings for the next 24 hours across hydroponic zones and detect sensor faults. Facility data and verified fault labels are not yet confirmed. I recommend Agile: first check data access and quality, then build a small usable feature, review it with intended users, and revise the forecast and fault-detection requirements as evidence arrives. If labels are unavailable, the team should gather them or revise the detector scope rather than claim a trained model. Waterfall would require firm specifications before these uncertainties are resolved and could cause avoidable rework. Documented acceptance criteria can still govern each increment (Burgan & Burgan, 2014; GAO, 2023).'

AddHeading 'Part E. Decision and Recommendation'
AddParagraph 'Neither approach is always better. I would choose Waterfall when requirements are stable and testable, stakeholders prefer milestone approvals, and traceability or a fixed baseline is important. I would choose Agile when requirements may change, users can review increments often, regular delivery has value, and the team can sustain testing and documentation in each cycle. Project size or quality demands alone do not settle the choice; both approaches need capable teams and explicit quality controls (Burgan & Burgan, 2014; GAO, 2023).'
AddParagraph 'For AquaVir, Agile is the better starting point because the available data and fault labels must first be verified. As requirements become clearer, the team can formalize acceptance criteria and release approval without losing the ability to learn from each increment.'

AddHeading 'Part F. Conclusion'
AddParagraph 'Agile offers early delivery and adaptation but depends on sustained feedback and discipline. Waterfall provides clear phase approvals and documentation but is vulnerable to costly late changes. I learned to select a development approach from the stability of requirements, the need for oversight, and the pace of learning rather than from a universal preference.'

AddHeading 'Part G. References'
AddReference 'Beck, K., Beedle, M., van Bennekum, A., Cockburn, A., Cunningham, W., Fowler, M., Grenning, J., Highsmith, J., Hunt, A., Jeffries, R., Kern, J., Marick, B., Martin, R. C., Mellor, S., Schwaber, K., Sutherland, J., & Thomas, D. (2001). Manifesto for Agile software development. https://agilemanifesto.org/'
AddReference 'Burgan, S. C., & Burgan, D. S. (2014, October 26). One size does not fit all: Choosing the right project approach [Conference paper]. PMI Global Congress 2014-North America. https://www.pmi.org/learning/library/choosing-right-project-approach-9346'
AddReference 'Royce, W. W. (1970). Managing the development of large software systems [Conference paper]. IEEE WESCON. https://blog.marsen.me/assets/royce1970.pdf'
AddReference 'U.S. Government Accountability Office. (2023). GAO Agile Assessment Guide: Best practices for adoption and implementation (GAO-24-105506). https://www.gao.gov/products/gao-24-105506'

AddHeading 'Part H. AI Interaction Log'
$log = @(
    @('AI Tool Used','Purpose','Sample/Key Prompt','Summary of AI Output','How You Verified/Revised the Output'),
    @('ChatGPT (OpenAI)','Clarify the activity','Read TA4; give concise answers with APA 7 citations; edit the DOCX.','Identified the required sections and asked me to confirm the comparison and scenario.','I confirmed Agile vs. Waterfall and AquaVir.'),
    @('ChatGPT (OpenAI)','Research and draft','Implement the plan for Agile vs. Waterfall using AquaVir.','Drafted the matrix, three scenarios, recommendation, and references.','Claims and citation details were checked against the sources listed; my final review is pending.'),
    @('ChatGPT (OpenAI)','Prepare document','Edit the named Word file in place as a submission-ready assessment.','Replaced template prompts with answers and populated both tables.','Document structure and layout were checked; my final review and signature are pending.')
)
$logTable = $original[98].CloneNode($true)
FillTable $logTable $log @(1300,1450,2200,2250,2800)
[void]$body.AppendChild($logTable)

AddHeading 'Part I. AI Usage Declaration'
AddParagraph 'I declare that any use of Generative AI in completing this assessment has been properly disclosed in my AI Interaction Log. I understand that AI serves only as an assistive tool and that I remain responsible for verifying the accuracy, relevance, and credibility of all information included in my submission.'
AddParagraph 'I confirm that the final comparison, analysis, recommendations, and conclusions reflect my own understanding and judgment.'
AddParagraph 'Student Name: Whitty, Juan Angelo Roy B.     Signature: ____________________     Date: ____________________'

[void]$body.AppendChild($original[136].CloneNode($true))
$xml.Save($path)
Write-Output 'Edited document.xml with completed assessment.'
