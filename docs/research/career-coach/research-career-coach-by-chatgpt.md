# Evidence base for one-on-one career coaching conversations

## Executive summary

The evidence supports **coaching as a category**, but it supports individual techniques and mechanisms much more strongly than it supports any particular four-stage conversation model.

A useful distinction for an AI coaching tool is therefore:

> **Treat GROW as a conversational scaffold, not as an evidence-based intervention in its own right.**

Large reviews of workplace/executive coaching find moderate positive effects, including a 2023 meta-analysis restricted to randomized controlled trials. But there is much less evidence that the _specific GROW sequence_ is what produces those effects. Direct GROW studies exist, including randomized trials, but they tend to be small, context-specific, and bundle GROW with other ingredients such as strengths work, leadership training, or behavioral exercises. ([DOI][1])

The strongest evidence relevant to designing a career-coaching conversation comes instead from:

- **working alliance** and collaborative goal/task agreement;
- **specific, appropriately difficult goals**, with an important qualification for complex tasks;
- **questioning as a conversational process**, rather than a collection of magic “power questions”;
- **separation of divergent option generation from evaluation**;
- **implementation intentions (“if–then” plans)** to turn intentions into behavior;
- career-specific evidence on **self-efficacy, proactive behavior, job-search skills and social support**;
- network research showing that **network diversity and moderately weak ties** matter, while “just network more” is far too crude.

---

# 1. The GROW model: origin, popularity and actual evidence

## Origin

The historical record is less tidy than the standard “Whitmore invented GROW” story suggests.

GROW emerged in the UK in the late 1970s/1980s from work influenced by Timothy Gallwey's **Inner Game** approach and practical performance coaching. Graham Alexander and Sir John Whitmore were important early figures; Alan Fine has also documented himself as a co-developer. The acronym was subsequently popularized through Whitmore's _Coaching for Performance_, first published in 1992. ([WorldCat][2])

There is a further wrinkle: Whitmore later stated that **Max Landsberg coined the name “GROW”** during a conversation with Graham Alexander, while the underlying process had already been in use. Thus, it is more accurate to describe GROW as an **evolving practice developed collaboratively and subsequently named/popularized**, rather than as a clean single-inventor invention. ([UKCPD][3])

The familiar structure is:

**G**oal → **R**eality → **O**ptions → **W**ill / Way Forward

Different versions use _Opportunity_, _Wrap-up_, or _Way Forward_ rather than exactly “Options” and “Will.” That variability itself is a clue that GROW is better understood as a **family of conversational structures** than as a tightly specified intervention protocol.

## What the research says

The uncomfortable but important finding is that **GROW's popularity substantially exceeds the specificity of its evidence base**.

There is strong evidence that workplace coaching in general works. Jones, Woods, and Guillaume's meta-analysis of 17 workplace-coaching studies found positive overall effects, with a meta-analytic effect of δ = .36 across organizational outcomes. ([BPS PsychHub][4])

More compellingly, de Haan and Nilsson's 2023 meta-analysis restricted its analysis to **randomized controlled trials**. Across 39 RCT samples involving 2,528 participants, workplace/executive coaching had a significant overall effect, with an estimated standardized effect of approximately **g = .59**. The authors nevertheless found indications of publication bias, and effects were stronger for self-reported than observed outcomes. ([DOI][1])

That establishes a reasonable evidence base for **coaching**, not for GROW specifically.

### There are GROW-specific controlled studies

For example, Okorie et al. (2022) randomized **109 school administrators** to a Zoom-delivered GROW intervention or wait-list control. Across nine weeks, the intervention improved self-reported subjective well-being, with effects persisting at three-month follow-up. ([PubMed Central (PMC)][5])

A 2026 pilot RCT in primary care randomized just **30 adults** with anxiety/depressive disorders to usual care, face-to-face GROW coaching, or telephone GROW coaching. Both coaching conditions reduced anxiety relative to control; effects on depression were not significant. The authors explicitly characterize the study as a feasibility/pilot trial and call for larger studies. ([PubMed][6])

There is also a controlled study of a **RE-GROW** intervention among 41 executives and middle managers. Participants received a package combining strengths-based work, leadership training and individual coaching. The program improved coaching-based leadership skills, psychological capital, work engagement and performance. But because GROW was only one component of a much larger intervention, this is evidence for the **package**, not for the causal value of GROW itself. ([PubMed Central (PMC)][7])

A particularly relevant experiment comes from Hwang et al. (2021). Thirty-two adults were randomly assigned to GROW-based one-to-one coaching, exposure to example ideas, or control. GROW coaching improved the **novelty** of new-product ideas, whereas exposure to example ideas actually produced the lowest scores for novelty and appropriateness. This is interesting because it provides some direct experimental support for the idea that **eliciting the person's own thinking can be preferable to supplying suggestions prematurely**. ([KCI][8])

### What is missing

What we do **not** have is the more decisive evidence one would want:

> GROW versus another equally credible coaching conversation, with the same coach time and population, followed by outcomes attributable specifically to the GROW sequence.

Nor is there a convincing dismantling literature showing:

**Goal → Reality → Options → Will**

is superior to, say:

**Goal → reflection → alternatives → action planning**, or a flexible conversation that does not follow GROW order.

This matters because many of the elements embedded in GROW—goal clarification, self-reflection, autonomy, option generation and action planning—have much stronger independent psychological foundations than the acronym itself.

### Practical conclusion for an AI coach

Use GROW as a **navigation heuristic**:

> “Where are we in this conversation?”

Do **not** treat it as a mandatory sequence:

> “The user has answered three Reality questions, so it is time for Options.”

The strongest evidence is for the **ingredients**, not for the choreography.

---

# 2. What makes a coaching conversation effective?

## The working alliance is one of the strongest findings

The coach-client relationship is not merely pleasant interpersonal packaging around the “real” technique. It appears to be one of the real mechanisms through which coaching works.

Graßmann, Schölmerich, and Schermuly (2020) synthesized **27 samples comprising 3,563 coaching processes**. A high-quality working alliance was moderately associated with positive coaching outcomes:

**r = .41, 95% CI [.34, .48]**

The relationship was positive across desirable outcome categories and negative with unintended negative effects. ([Sage Journals][9])

That finding is particularly useful for an AI system because the alliance can be operationalized conversationally.

The classic dimensions are essentially:

**Goal:** Do we agree about what the client is trying to accomplish?

**Task:** Do we agree about what we are doing in this conversation?

**Bond:** Does the client experience the interaction as respectful, trustworthy and collaborative?

The large-scale work of de Haan and colleagues likewise found that working alliance—especially its **goal and task components**—was strongly related to perceived coaching effectiveness. Personality matching between coach and client was not comparably important. ([Erik de Haan][10])

That suggests an AI coach should spend less effort pretending to have the “right personality” and more effort establishing:

> “What would be useful to accomplish in this conversation?”

and

> “Does this way of exploring the issue actually help you?”

## Motivation and perceived competence matter

A systematic review of antecedents to coaching alliance found that client **motivation for change** and perceived coach competence were among the strongest predictors of alliance. Change motivation correlated approximately **r = .37**, and perceived competence approximately **r = .42**. Coach experience itself was not significantly related to alliance. ([DOI][11])

For an AI tool, this suggests that the conversation should not assume that a user is equally ready for exploration at all times.

A better opening may distinguish:

> “I want to think this through.”

from:

> “I already know what I need to do; I just need help executing it.”

Those are different coaching problems.

## Goal-setting theory applies, but not as “SMART everywhere”

Locke and Latham's goal-setting research provides a strong theoretical foundation for the **Goal** component of GROW. Across decades of research, specific and appropriately difficult goals generally outperform vague “do your best” goals. Goals work through mechanisms including direction, effort, persistence and strategy use, with self-efficacy and commitment acting as important moderators. ([PubMed][12])

Inside a conversation, however, the implication is more subtle than:

> “Convert everything into a SMART goal.”

The coach should clarify:

- **what outcome matters;**
- **what would count as progress;**
- **what level of challenge is meaningful;**
- **whether the person actually owns the goal.**

The last point matters because goal-setting theory explicitly considers different goal sources, including self-set and jointly set goals. ([DOI][13])

### Complexity is an important boundary condition

The classic “specific and difficult goals are better” rule becomes less straightforward for complex or unfamiliar tasks. Meta-analytic work on task complexity established that the effects of goal specificity/difficulty depend on task characteristics; for complex tasks, learning goals can be preferable to demanding performance goals. ([ResearchGate][14])

For career coaching, that matters greatly.

“Get promoted to engineering director by June” may be a reasonable outcome goal.

“Become dramatically better at executive influence” is much less directly controllable. A better coaching conversation may create **learning or process goals**:

> “Over the next month, I will deliberately seek feedback from three senior stakeholders and test one new approach to communicating strategic trade-offs.”

That distinction is particularly useful for career transitions, where the final outcome is partly controlled by employers, labor markets and other people.

## Powerful questioning: evidence is thinner than the mythology

The coaching literature has long treated questioning as a central intervention, but until recently there has been relatively little rigorous research on **which questions, asked in which sequence, actually cause better outcomes**.

The QueSCo project is notable precisely because it addresses this missing “black box.” Research on authentic workplace coaching conversations has analyzed thousands of actual question sequences rather than merely asking coaches which questions they believe are powerful. Recent findings show that questions function as **sequences**, involving what precedes the question, the client's response and what the coach does next. In one corpus, 83% of the data occurred within mostly successful questioning sequences, while clients produced more than answers in 73% of cases. ([Tandfonline][15])

The key implication is:

> A “powerful question” is not powerful because of its wording alone.

The same question can be useful, pointless or irritating depending on what the client has just said and what the coach does with the response.

For an AI coach, this argues against generating a stock list such as:

> “What would you do if you knew you could not fail?”

and instead prioritizing **responsive follow-up**:

> User: “I think my manager doesn't trust me.”

> Weak response: “What could you do differently?”

> Better response: “What makes you think that?”

> Then, after the answer: “Which part of what you've described is actually observable, and which part are you inferring?”

The latter is a conversational process, not a question-of-the-day gimmick.

---

# 3. Evidence-based practice for the Options stage

This is arguably the stage where an AI career coach can either add significant value or accidentally become the problem.

## The core danger: premature convergence

Humans tend to evaluate ideas as they generate them. This encourages **premature convergence**: the first plausible solution begins to dominate the conversation before the option space has been properly explored.

Classic brainstorming research found that interactive groups often generate fewer ideas than equivalent numbers of people working independently, partly because speaking turns interfere with people's own idea generation. Subsequent research identifies **production blocking** as a major mechanism. ([Universität Münster][16])

The practical lesson transfers surprisingly well to one-to-one coaching:

> **Separate generating possibilities from judging possibilities.**

That separation is especially useful for an AI because an AI can generate suggestions extremely quickly. Speed is not the same thing as good coaching.

## Structured generation beats “What options do you have?”

A vague question such as:

> “What could you do?”

may produce the first two familiar answers and nothing more.

A better technique is **forced divergence**:

> “Give me five different ways you could approach this. They don't have to be good yet.”

Then:

> “Now give me three options that feel unconventional.”

Then:

> “Which option would you normally dismiss too quickly?”

Only after that:

> “Let's evaluate them.”

That structure is consistent with the broader creativity literature separating **idea generation** from **idea evaluation**. Osborn's original brainstorming principles explicitly called for suspending judgment during generation; subsequent research has refined rather than simply validated that formulation. ([ScienceDirect][17])

## Brainwriting is especially interesting for AI coaching

Research on brainwriting provides a particularly useful model for conversational AI because it reduces the pressure to immediately react to an idea.

A 2025 randomized study comparing virtual brainwriting with video-based oral brainstorming found that brainwriting groups generated significantly more ideas, more original ideas, a greater proportion of good-quality ideas and greater elaboration. They also selected more original ideas later. ([Wiley Online Library][18])

Earlier workplace research similarly found benefits from alternating group and individual idea generation, with periodic exposure to other ideas producing useful stimulation without making people entirely dependent on interactive discussion. ([PubMed][19])

For an AI coach, the analogue is simple:

### First: client-generated options

Ask the client to generate several alternatives before the AI supplies its own.

### Second: AI expansion

Only then can the AI say:

> “You've generated four approaches. I see two additional routes you haven't mentioned…”

This preserves the client's authorship while still exploiting AI's generative capacity.

## There is unusually direct evidence against premature suggestions

The GROW-based new-product creativity experiment mentioned earlier is useful here. Participants receiving **example ideas** performed worse on novelty and appropriateness than both the coaching and control conditions. The authors concluded that giving participants examples can constrain rather than expand creative idea generation. ([KCI][8])

That does not prove that AI suggestions are inherently bad. It does show that **providing an attractive solution too early can narrow the search space**.

For career coaching, the risk is obvious.

Suppose the client says:

> “I'm unhappy in my current role.”

An AI that immediately says:

> “Have you considered becoming a product manager?”

has effectively anchored the conversation around its own hypothesis.

A better sequence is:

**Generate → expand → categorize → evaluate → choose.**

## A good Options protocol

For an AI coach, a strong evidence-informed pattern would therefore be:

**1. Generate independently.**
Ask the user for 3–5 possibilities before offering suggestions.

**2. Force range.**
Request a safe option, ambitious option, unconventional option and reversible experiment.

**3. Defer evaluation.**
Do not immediately comment on which option is “best.”

**4. Expand the set.**
The AI can now add alternatives, explicitly labeling them as _additional possibilities_, not recommendations.

**5. Evaluate against user-defined criteria.**
For example: learning value, career upside, financial risk, reversibility, political feasibility, energy required.

**6. Choose only after divergence.**

This is substantially more defensible than the simplistic coaching rule “never give advice.” Sometimes advice is useful. The evidence-supported distinction is more like:

> **Don't let the coach's answers collapse the client's search space before the client has explored it.**

---

# 4. The Will stage: turning a good intention into actual behavior

The weakest version of “Will” is:

> “So, what will you do?”

The client says:

> “I'll update my CV.”

Everyone feels productive.

Then nothing happens.

## Goal intentions are not enough

One of the strongest relevant findings comes from Peter Gollwitzer's work on **implementation intentions**.

An ordinary goal intention says:

> “I intend to do X.”

An implementation intention specifies:

> **“If situation Y occurs, then I will do X.”**

Gollwitzer and Sheeran's meta-analysis covered **94 independent tests and 8,461 participants** and found a medium-to-large effect on goal attainment:

**d = .65**

Implementation intentions helped with initiating actions, protecting them from interference and responding effectively to obstacles. ([ScienceDirect][20])

This is a much stronger empirical foundation for the GROW **Will** stage than generic “commitment” language.

## What this means for a coaching conversation

Instead of:

> “I'll contact three people this week.”

Use:

> “If it is Tuesday at 9:00, when I finish my first coffee, I will send the first networking message.”

And ideally:

> “If I start thinking that I need to rewrite the message again, I will send the current version anyway.”

The second sentence handles a predictable **barrier**, not just the desired behavior.

That matters because implementation intentions work partly by linking a recognizable situational cue with a predefined response. The critical situation becomes more cognitively accessible, and the response becomes easier to initiate automatically. ([Frontiers][21])

## The AI should therefore ask four questions

A strong Will stage can systematically establish:

**What exactly?**
The observable behavior.

**When/where?**
The situational cue.

**What might derail it?**
The predictable obstacle.

**What will you do then?**
The preplanned response.

For example:

> “I will contact former colleagues.”

becomes:

> “If it is Wednesday at 10:00, I will message Anna and Thomas on LinkedIn. If I hesitate because the message feels awkward, I will send a simple catch-up message rather than trying to engineer a perfect networking pitch.”

That is a materially different commitment.

## Add a review loop

There is another important implication for AI coaching: Will should not necessarily be the final state of the process.

A better cycle is:

**commit → act → review → learn → adjust**

rather than:

**commit → done**

The RE-GROW research program is illustrative here: its intervention explicitly incorporated progress review and modification of action plans across sessions rather than treating the original action plan as fixed. ([PubMed Central (PMC)][7])

---

# 5. Career-coaching-specific evidence

Career coaching deserves to be separated from generic executive or life coaching because career decisions involve **external constraints, uncertainty, labor-market competition and other decision-makers**.

The evidence base is smaller than the general coaching literature, but several findings are particularly relevant.

## Career decision-making

A particularly strong recent study is Fris et al. (2025), a **randomized wait-list controlled trial** involving 224 medical master's students.

The intervention consisted of five individual coaching sessions over eight months. Compared with the wait-list condition, coaching produced a small-to-moderate reduction in **career decision-making stress**, partly mediated by increased career decision self-efficacy. Participants also showed greater changes in career choice and greater certainty regarding their choices. ([PubMed][22])

This is one of the more useful studies for an AI career coach because it identifies a mechanism:

> **Coaching → increased career decision self-efficacy → reduced decision stress**

That is more informative than simply saying “career coaching works.”

## Job search

The strongest career-specific evidence is arguably not labelled “career coaching” at all.

Liu, Huang, and Wang's meta-analysis synthesized **47 experimental or quasi-experimental job-search interventions** and found that participants receiving interventions had **2.67 times higher odds of obtaining employment** than controls. ([PubMed][23])

Importantly, the researchers found that the most useful interventions combined **skills and motivation**. Components associated with better outcomes included:

- job-search skills;
- self-presentation;
- self-efficacy;
- proactivity;
- goal setting;
- social support.

Their meta-analytic path analysis suggested that improvements in job-search skills, self-efficacy and job-search behavior partly explained the effect on employment. ([PubMed][23])

This suggests that an AI career coach should not become purely reflective.

For someone actively job-searching, useful coaching may need to alternate between:

**reflection → decision → skill practice → action → feedback**

rather than endlessly asking deeper questions.

## Career transitions

Evidence for coaching during career transitions is much thinner.

Terblanche's work on transition coaching with senior leaders is largely qualitative and developmental. Research involving leaders moving into senior roles emphasizes that transitions require more than skill acquisition: people must often revise how they understand themselves and their role. ([Tandfonline][24])

A separate quasi-experimental intervention for experienced employees facing organizational restructuring found improvements in several dimensions of **career adaptability**, including self-awareness, career decidedness, exploration and career planning. However, the intervention was an ePortfolio plus half-day event rather than pure coaching. ([ScienceDirect][25])

That is an important evidence boundary:

> Career coaching research often studies **career interventions containing coaching**, rather than isolated coaching conversations.

## Promotion pushes

The evidence for “coaching someone to get promoted” is particularly thin.

There is substantial organizational-network research showing associations between network position, brokerage, visibility and promotion, and executive coaching can improve leadership-related outcomes. But a controlled evidence base showing that a particular coaching protocol directly increases an individual's promotion probability is lacking.

For an AI system, the implication is to coach the **controllable precursors**:

- evidence of impact;
- stakeholder relationships;
- visibility;
- strategic scope;
- leadership behaviors;
- promotion conversations;
- sponsorship/network access.

Rather than promising an outcome the client does not control.

---

# 6. Networking research: beyond practitioner advice

Networking is one of the areas where academic social-network research substantially improves upon generic career-book advice.

## Granovetter was essentially right—but the modern evidence is more nuanced

Granovetter's 1973 **strength-of-weak-ties** theory proposed that weak ties can bridge otherwise disconnected social groups and provide access to information unavailable within one's close circle. That makes them particularly valuable for mobility and opportunity. ([RCNi Company Limited][26])

For decades, however, much of the evidence was correlational.

Then came a remarkably large causal test.

Rajkumar et al. (2022) analyzed randomized changes to LinkedIn's “People You May Know” algorithm involving **more than 20 million people**, around **2 billion new ties** and approximately **600,000 job transitions** over five years. ([PubMed][27])

The results supported the weak-tie hypothesis, but with an important correction:

> The relationship between tie strength and job mobility was **nonlinear**.

The most useful connections were generally **weak or moderately weak**, rather than simply “the weakest possible ties.” Very weak ties eventually produced diminishing returns. Effects also differed by industry: weaker ties were particularly helpful in more digital industries, whereas stronger ties mattered more in less digital industries. ([PubMed][27])

That is considerably more useful than:

> “Network with weak ties.”

The better coaching principle is:

> **Increase exposure to people who know different people and information from those already in your circle.**

## Network diversity matters

This finding meshes with research on **structural holes** and network brokerage.

Burt's work showed that people whose networks bridge otherwise disconnected groups tend to have better access to diverse information and ideas; such brokerage positions have been associated with compensation, positive evaluations, promotions and creativity. ([RCNi Company Limited][28])

But network structure should not be interpreted as “more holes = always better.”

Research also shows that brokering across disconnected groups carries social and psychological costs. Recent research explicitly links spanning structural holes to burnout and other negative behaviors under some conditions. ([PubsOnline][29])

So an AI coach should not blindly prescribe:

> “Build the largest possible network.”

A better target is:

> **Build a network with useful diversity without turning yourself into the exhausted human version of LinkedIn's People You May Know algorithm.**

## Networking is associated with career success—but causal claims need care

Wolff and Moser's three-year longitudinal study found that networking was associated with salary and with salary growth over time. Networking was also related to contemporaneous career satisfaction, though it did not predict growth in satisfaction. ([PubMed][30])

This is stronger evidence than a single cross-sectional correlation, but it is still not equivalent to a randomized trial of “networking causes promotion.”

There is also a conceptual distinction worth preserving:

**building contacts ≠ maintaining relationships ≠ using relationships.**

Their study explicitly distinguished these dimensions, along with internal and external networking. ([PubMed][30])

That makes generic advice such as “go network” almost useless.

An AI coach should ask:

> “What type of relationship are you trying to build, with whom, and for what information or opportunity?”

## What about “give-first reciprocity”?

The practitioner idea that good networking means **giving before asking** is intuitively plausible and compatible with reciprocity theories, but the career-networking evidence does not establish a simple universal rule that “give first” produces better career outcomes.

The stronger evidence supports something broader:

- networks are valuable when they provide access to information and resources;
- relationships involve exchange and maintenance;
- diverse contacts provide nonredundant information;
- opportunities often travel through connections outside one's immediate circle.

So an AI coach should avoid turning reciprocity into a transactional script:

> “Give three favors and then ask for a referral.”

That is much less evidence-based than:

> “What could make this relationship genuinely useful for both people?”

## “Anchor connectors” are best understood as a network role, not a validated coaching construct

There is good research on **brokers**, central actors and people who span otherwise disconnected groups. There is not, however, a well-established peer-reviewed evidence base around the practitioner term **“anchor connector”** as a distinct intervention technique.

The underlying idea can therefore be retained, but translated into better-supported network concepts:

> Look for people who bridge **multiple relevant communities**.

For example, instead of identifying “the person who knows everyone,” look for someone who connects:

**your industry ↔ adjacent industry**

or

**technical community ↔ executive community**

or

**current company ↔ target employer ecosystem**

Those people are valuable because they may expose the client to **nonredundant information and otherwise inaccessible contacts**. That is much closer to the evidence on weak ties and brokerage. ([PubMed][27])

---

# Implications for an AI career-coaching system

Taken together, the research suggests a useful design principle:

## Use GROW as the skeleton; use stronger evidence to define the muscles.

### Goal

Don't merely ask for a SMART goal.

Establish **ownership, specificity, controllability and an appropriate level of challenge**. For complex career problems, distinguish an outcome goal from learning/process goals. (Locke & Latham, 2002, 2006.) ([PubMed][12])

### Reality

Prioritize **observable facts, interpretations, constraints, resources and assumptions**.

The coach should help separate:

> “My manager hasn't promoted me.”

from:

> “My manager does not value me.”

The first is an observation; the second is a hypothesis.

### Options

Use **divergence before evaluation**.

Have the client generate options first. Then deliberately expand the search space. Only after that should the AI contribute suggestions.

This is one place where AI can be unusually powerful without becoming overly directive.

### Will

Don't stop at commitment.

Convert commitments into:

**behavior + cue + time/place + obstacle + response**

using implementation intentions. (Gollwitzer & Sheeran, 2006.) ([ScienceDirect][20])

### Throughout

Continuously maintain the **working alliance**:

> “Is this useful?”

> “Are we solving the right problem?”

> “Do you want me to challenge that assumption or help you explore it?”

The evidence suggests that task and goal alignment are not soft extras; they are central components of effective coaching. ([Sage Journals][9])

### For career coaching specifically

The AI should distinguish at least three conversation modes:

**Career decision:** identity, preferences, self-efficacy, exploration, uncertainty.

**Job search:** skills, self-presentation, search behavior, goals, social support and execution.

**Career advancement:** evidence of impact, visibility, stakeholder relationships, sponsorship, network position and political/contextual constraints.

Those are related problems, but the evidence suggests they should not all receive the same coaching script. ([PubMed][22])

---

# Bottom line on the evidence

| Technique / mechanism                             | Evidence strength                                     | Appropriate AI design stance                                 |
| ------------------------------------------------- | ----------------------------------------------------- | ------------------------------------------------------------ |
| Coaching overall                                  | **Moderate**                                          | Use coaching as a credible intervention                      |
| Working alliance                                  | **Strong**                                            | Treat as a core design requirement                           |
| Goal setting                                      | **Strong**                                            | Use specific, owned goals; adapt for complexity              |
| GROW as a whole                                   | **Thin–moderate**                                     | Use as a scaffold, not as validated causal technology        |
| GROW sequence/order                               | **Thin**                                              | Keep flexible                                                |
| “Powerful questions”                              | **Emerging**                                          | Focus on responsive questioning sequences                    |
| Divergent option generation                       | **Moderate–strong** from creativity research          | Separate generation from evaluation                          |
| Client generates options before coach suggestions | **Promising, including direct GROW-related evidence** | Prefer client-first exploration                              |
| Implementation intentions                         | **Strong**                                            | Make them part of the Will stage                             |
| Career decision coaching                          | **Emerging but increasingly solid**                   | Use self-efficacy and decision clarity as mechanisms         |
| Job-search interventions                          | **Strong**                                            | Combine skills + motivation + goals + support                |
| Weak ties and network diversity                   | **Strong**                                            | Encourage nonredundant connections                           |
| “Give first” as a universal networking rule       | **Weak**                                              | Use reciprocal-value framing, not a formula                  |
| “Anchor connectors” as a distinct intervention    | **Thin**                                              | Translate into brokerage/bridging/network-diversity concepts |

The most defensible conceptual model for an AI tool is therefore **not “AI implements GROW.”**

It is:

> **AI facilitates a collaborative coaching conversation using GROW-like structure, while drawing its actual behavioral mechanisms from goal-setting theory, working-alliance research, divergent-convergent decision processes, implementation intentions, career self-efficacy research and social-network science.**

That gives you something much more robust than taking a popular coaching framework at face value.

---

# References

Burt, R. S. (2004). Structural holes and good ideas. _American Journal of Sociology, 110_(2), 349–399. [https://doi.org/10.1086/421787](https://doi.org/10.1086/421787) ([RCNi Company Limited][28])

de Haan, E., Grant, A. M., Burger, Y., & Eriksson, P.-O. (2016). A large-scale study of executive and workplace coaching: The relative contributions of relationship, personality match, and self-efficacy. _Consulting Psychology Journal: Practice and Research, 68_(3), 189–207. ([Erik de Haan][10])

de Haan, E., & Nilsson, V. O. (2023). What can we know about the effectiveness of coaching? A meta-analysis based only on randomized controlled trials. _Academy of Management Learning & Education, 22_(4), 641–659. [https://doi.org/10.5465/amle.2022.0107](https://doi.org/10.5465/amle.2022.0107) ([DOI][1])

Fang, R., Zhang, Z., & Shaw, J. D. (2021). Gender and social network brokerage: A meta-analysis and field investigation. _Journal of Applied Psychology, 106_(11), 1630–1654. [https://doi.org/10.1037/apl0000841](https://doi.org/10.1037/apl0000841) ([PubMed][31])

Fris, D. A. H., van Vianen, A. E. M., van Hooft, E. A. J., de Hoog, M., & de Pagter, A. P. J. (2025). Career coaching to support medical student career decision-making: A randomized controlled trial. _Advances in Health Sciences Education, 30_, 1497–1521. [https://doi.org/10.1007/s10459-025-10409-8](https://doi.org/10.1007/s10459-025-10409-8) ([Springer][32])

Graßmann, C., Schölmerich, F., & Schermuly, C. C. (2020). The relationship between working alliance and client outcomes in coaching: A meta-analysis. _Human Relations, 73_(1), 1–25. [https://doi.org/10.1177/0018726718819725](https://doi.org/10.1177/0018726718819725) ([Sage Journals][9])

Gollwitzer, P. M., & Sheeran, P. (2006). Implementation intentions and goal achievement: A meta-analysis of effects and processes. _Advances in Experimental Social Psychology, 38_, 69–119. [https://doi.org/10.1016/S0065-2601(06)38002-1](https://doi.org/10.1016/S0065-2601%2806%2938002-1) ([ScienceDirect][20])

Granovetter, M. S. (1973). The strength of weak ties. _American Journal of Sociology, 78_(6), 1360–1380. [https://doi.org/10.1086/225469](https://doi.org/10.1086/225469) ([RCNi Company Limited][26])

Hwang, H.-H., Jung, M., Kim, K.-B., & Kim, B.-M. (2021). The effect of the 1:1 coaching and the example ideas with the GROW model on the creativity of new product development ideas. _Korean Journal of Coaching Psychology, 5_(2), 1–24. [https://doi.org/10.51457/kjcp.2021.12.5.2.1](https://doi.org/10.51457/kjcp.2021.12.5.2.1) ([KCI][8])

Jones, R. J., Woods, S. A., & Guillaume, Y. R. F. (2016). The effectiveness of workplace coaching: A meta-analysis of learning and performance outcomes from coaching. _Journal of Occupational and Organizational Psychology, 89_(2), 249–277. [https://doi.org/10.1111/joop.12119](https://doi.org/10.1111/joop.12119) ([BPS PsychHub][4])

Kooh Givi, M. (2025). The impact of coaching interventions on employee performance, motivation, and organizational adaptability: An experimental study in the petrochemical industry. _International Journal of Business and Management_. ([CCSE][33])

Liu, S., Huang, J. L., & Wang, M. (2014). Effectiveness of job search interventions: A meta-analytic review. _Psychological Bulletin, 140_(4), 1009–1041. [https://doi.org/10.1037/a0035923](https://doi.org/10.1037/a0035923) ([PubMed][23])

Locke, E. A., & Latham, G. P. (2002). Building a practically useful theory of goal setting and task motivation: A 35-year odyssey. _American Psychologist, 57_(9), 705–717. [https://doi.org/10.1037/0003-066X.57.9.705](https://doi.org/10.1037/0003-066X.57.9.705) ([PubMed][12])

Locke, E. A., & Latham, G. P. (2006). New directions in goal-setting theory. _Current Directions in Psychological Science, 15_(5), 265–268. [https://doi.org/10.1111/j.1467-8721.2006.00449.x](https://doi.org/10.1111/j.1467-8721.2006.00449.x) ([DOI][13])

Michinov, N. (2012). Is electronic brainstorming or brainwriting the best way to improve creative performance in groups? An overlooked comparison of two idea-generation techniques. _Journal of Applied Social Psychology, 42_(S1), E222–E243. [https://doi.org/10.1111/j.1559-1816.2012.01024.x](https://doi.org/10.1111/j.1559-1816.2012.01024.x) ([Wiley Online Library][34])

Okorie, C. O., Ogba, F. N., Amujiri, B. A., et al. (2022). Zoom-based GROW coaching intervention for improving subjective well-being in a sample of school administrators: A randomized control trial. _Internet Interventions, 29_, 100549. [https://doi.org/10.1016/j.invent.2022.100549](https://doi.org/10.1016/j.invent.2022.100549) ([PubMed][35])

Rajkumar, K., Saint-Jacques, G., Bojinov, I., Brynjolfsson, E., & Aral, S. (2022). A causal test of the strength of weak ties. _Science, 377_(6612), 1304–1310. [https://doi.org/10.1126/science.abl4476](https://doi.org/10.1126/science.abl4476) ([PubMed][27])

Terblanche, N. H. D. (2022). Transformative transition coaching: A framework to facilitate transformative learning during career transitions. _The International Journal of Human Resource Management, 33_(2), 269–296. [https://doi.org/10.1080/09585192.2019.1688376](https://doi.org/10.1080/09585192.2019.1688376) ([Tandfonline][24])

van der Horst, A. C., & Klehe, U.-C. (2019). Enhancing career adaptive responses among experienced employees: A mid-career intervention. _Journal of Vocational Behavior, 111_, 91–106. [https://doi.org/10.1016/j.jvb.2018.08.004](https://doi.org/10.1016/j.jvb.2018.08.004) ([ScienceDirect][25])

Wolff, H.-G., & Moser, K. (2009). Effects of networking on career success: A longitudinal study. _Journal of Applied Psychology, 94_(1), 196–206. [https://doi.org/10.1037/a0013350](https://doi.org/10.1037/a0013350) ([PubMed][30])

[1]: https://doi.org/10.5465/AMLE.2022.0107?utm_source=chatgpt.com "What Can We Know about the Effectiveness of Coaching? A Meta-Analysis Based Only on Randomized Controlled Trials | Academy of Management Learning & Education"
[2]: https://search.worldcat.org/title/Coaching-for-performance-%3A-a-practical-guide-to-growing-your-own-skills/oclc/1255757953?utm_source=chatgpt.com "Coaching for performance : a practical guide to growing your own skills | WorldCat.org"
[3]: https://ukcpd.co.uk/the-history-and-development-of-the-grow-coaching-model?utm_source=chatgpt.com "The History and Development of the GROW Coaching Model | UKCPD"
[4]: https://bpspsychub.onlinelibrary.wiley.com/doi/10.1111/joop.12119?utm_source=chatgpt.com "The effectiveness of workplace coaching: A meta‐analysis of learning and performance outcomes from coaching - Jones - 2016 - Journal of Occupational and Organizational Psychology - Wiley Online Library"
[5]: https://pmc.ncbi.nlm.nih.gov/articles/PMC9452042/?utm_source=chatgpt.com "Zoom-based GROW coaching intervention for improving subjective well-being in a sample of school administrators: A randomized control trial - PMC"
[6]: https://pubmed.ncbi.nlm.nih.gov/42105425/?utm_source=chatgpt.com "Structured coaching interventions for anxiety and depressive disorders in Primary Care: A randomized controlled trial - PubMed"
[7]: https://pmc.ncbi.nlm.nih.gov/articles/PMC7011779/?utm_source=chatgpt.com "Coaching-Based Leadership Intervention Program: A Controlled Trial Study - PMC"
[8]: https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002802987&utm_source=chatgpt.com "GROW모델을 활용한 1:1 코칭과 예시 아이디어가 신제품 개발 아이디어 창의성에 미치는 영향"
[9]: https://journals.sagepub.com/doi/pdf/10.1177/0018726718819725?utm_source=chatgpt.com "The relationship between working alliance and client outcomes in coaching: A meta-analysis - Carolin Graßmann, Franziska Schölmerich, Carsten C Schermuly, 2020"
[10]: https://www.erikdehaan.com/a-large-scale-study-of-executive-and-workplace-coaching-the-relative-contributions-of-relationship-personality-match-and-self-efficacy/?utm_source=chatgpt.com "A Large-Scale Study of Executive and Workplace Coaching – Erik de Haan"
[11]: https://doi.org/10.5465/AMBPP.2020.259?utm_source=chatgpt.com "Understanding What Drives the Coaching Working Alliance: A Systematic Literature Review | Academy of Management Proceedings"
[12]: https://pubmed.ncbi.nlm.nih.gov/12237980/?utm_source=chatgpt.com "Building a practically useful theory of goal setting and task motivation. A 35-year odyssey - PubMed"
[13]: https://doi.org/10.1111/j.1467-8721.2006.00449.x?utm_source=chatgpt.com "New Directions in Goal-Setting Theory - Edwin A. Locke, Gary P. Latham, 2006"
[14]: https://www.researchgate.net/publication/280081888_Task_Complexity_as_a_Moderator_of_Goal_Effects_A_Meta-Analysis?utm_source=chatgpt.com "(PDF) Task Complexity as a Moderator of Goal Effects: A Meta-Analysis"
[15]: https://www.tandfonline.com/doi/full/10.1080/17521882.2025.2586495?utm_source=chatgpt.com "Full article: How coaches and clients do questioning in coaching – results from the interdisciplinary research project ‘QueSCo’ and their relevance for coaching practice and education"
[16]: https://www.uni-muenster.de/imperia/md/content/psyifp/aeechterhoff/wintersemester2011-12/seminarthemenfelderdersozialpsychologie/08_diehl_stoebe_productivityloss-brainstorming_jpsp1987.pdf?utm_source=chatgpt.com "Journal of Personality and Social Psychology"
[17]: https://www.sciencedirect.com/science/chapter/bookseries/pii/S006526011043004X?utm_source=chatgpt.com "Beyond Productivity Loss in Brainstorming Groups: The Evolution of a Question - ScienceDirect"
[18]: https://onlinelibrary.wiley.com/doi/abs/10.1002/jocb.70058?utm_source=chatgpt.com "Comparing Virtual Brainwriting and Video‐Based Brainstorming in Groups With Perceived Functional Diversity or Similarity - Baruah - 2025 - The Journal of Creative Behavior - Wiley Online Library"
[19]: https://pubmed.ncbi.nlm.nih.gov/25850113/?utm_source=chatgpt.com "Asynchronous Brainstorming in an Industrial Setting: Exploratory Studies - PubMed"
[20]: https://www.sciencedirect.com/science/article/abs/pii/S0065260106380021?utm_source=chatgpt.com "Implementation Intentions and Goal Achievement: A Meta‐analysis of Effects and Processes - ScienceDirect"
[21]: https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2015.00395/full?utm_source=chatgpt.com "Frontiers | Promoting the translation of intentions into action by implementation intentions: behavioral effects and physiological correlates"
[22]: https://pubmed.ncbi.nlm.nih.gov/40029552/?utm_source=chatgpt.com "Career coaching to support medical student career decision-making: a randomized controlled trial - PubMed"
[23]: https://pubmed.ncbi.nlm.nih.gov/24588365/?utm_source=chatgpt.com "Effectiveness of job search interventions: a meta-analytic review - PubMed"
[24]: https://www.tandfonline.com/doi/full/10.1080/09585192.2019.1688376?utm_source=chatgpt.com "Transformative transition coaching: a framework to facilitate transformative learning during career transitions: The International Journal of Human Resource Management: Vol 33 , No 2 - Get Access"
[25]: https://www.sciencedirect.com/science/article/pii/S0001879118300885?utm_source=chatgpt.com "Enhancing career adaptive responses among experienced employees: A mid-career intervention - ScienceDirect"
[26]: https://www.journals.uchicago.edu/doi/10.1086/225469?utm_source=chatgpt.com "The Strength of Weak Ties | American Journal of Sociology: Vol 78, No 6"
[27]: https://pubmed.ncbi.nlm.nih.gov/36107999/?utm_source=chatgpt.com "A causal test of the strength of weak ties - PubMed"
[28]: https://www.journals.uchicago.edu/doi/full/10.1086/421787?utm_source=chatgpt.com "Structural Holes and Good Ideas1 | American Journal of Sociology: Vol 110, No 2"
[29]: https://pubsonline.informs.org/doi/10.1287/orsc.2023.1664?utm_source=chatgpt.com "The Strain of Spanning Structural Holes: How Brokering Leads to Burnout and Abusive Behavior | Organization Science"
[30]: https://pubmed.ncbi.nlm.nih.gov/19186904/?utm_source=chatgpt.com "Effects of networking on career success: a longitudinal study - PubMed"
[31]: https://pubmed.ncbi.nlm.nih.gov/33030920/?utm_source=chatgpt.com "Gender and social network brokerage: A meta-analysis and field investigation - PubMed"
[32]: https://link.springer.com/article/10.1007/s10459-025-10409-8?utm_source=chatgpt.com "Career coaching to support medical student career decision-making: a randomized controlled trial | Advances in Health Sciences Education | Springer Nature Link"
[33]: https://ccsenet.org/journal/index.php/ijbm/article/view/0/52177?utm_source=chatgpt.com "The Impact of Coaching Interventions on Employee Performance, Motivation, and Organizational Adaptability: An Experimental Study in the Petrochemical Industry | Kooh Givi | International Journal of Business and Management | CCSE"
[34]: https://onlinelibrary.wiley.com/doi/10.1111/j.1559-1816.2012.01024.x?utm_source=chatgpt.com "Is Electronic Brainstorming or Brainwriting the Best Way to Improve Creative Performance in Groups? An Overlooked Comparison of Two Idea‐Generation Techniques - Michinov - 2012 - Journal of Applied Social Psychology - Wiley Online Library"
[35]: https://pubmed.ncbi.nlm.nih.gov/36092992/?utm_source=chatgpt.com "Zoom-based GROW coaching intervention for improving subjective well-being in a sample of school administrators: A randomized control trial - PubMed"
