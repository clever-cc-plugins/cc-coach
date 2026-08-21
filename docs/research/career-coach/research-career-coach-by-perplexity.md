## The GROW Model: Origin and Actual Effectiveness

The GROW model (Goal, Reality, Options, Will) has no single inventor; it emerged from the UK executive-coaching community of the mid-to-late 1980s, rooted in Timothy Gallwey's "Inner Game" tradition, which argued that self-observation outperforms external technical correction. Sir John Whitmore, Graham Alexander, and Alan Fine are the three individuals most consistently credited with co-development, having worked together — reportedly while consulting for McKinsey's London office — to codify a chronological sequence they had already been using informally. Whitmore, in a 2009 account, said an internal McKinsey communications specialist coined the acronym itself during a conversation with Alexander, though Whitmore was the first to publish the model, in the 1992 first edition of *Coaching for Performance*. Notably, the three co-developers never fully agreed on the final letter: Whitmore used "Will," Alexander used "Wrap-up" or "Way Forward," and Fine used "Way Forward" — a detail practitioner books rarely mention, underscoring that GROW was never a single, fixed, empirically validated protocol but a loosely shared heuristic that diverged even among its own originators.[^1][^2][^3][^4][^5][^6][^7]

Formal controlled research on GROW specifically is thin relative to its ubiquity in practitioner training. A systematic review of coaching-psychology studies found that nearly 70% of studies test particular psychological models, and several small studies have specifically examined GROW: a between-participant study of 60 managers found GROW coaching produced greater goal-attainment gains than no coaching, but no significant change in self-efficacy; a within-participant study of 26 senior managers (Burke & Linley, 2007) found increases in self-concordance and organizational commitment after a single GROW session; and Grant and colleagues (2010) found that 42 Sydney high-school teachers receiving 10 GROW-based sessions reported higher goal-achievement than a non-coaching comparison group, but no significant effect on psychological outcomes like resilience, depression, or anxiety. A quasi-experimental hospital study in Thailand found GROW-based coaching significantly improved teamwork and organizational learning culture, and a 2015 study found GROW coaching had moderate effects on safety leadership behaviors. A Zoom-delivered GROW randomized controlled trial with Nigerian school administrators found sustained improvements in subjective well-being at a 3-month follow-up. One Irish study incorporating GROW alongside solution-focused techniques and goal-setting theory found no significant impact on line managers' motivation or job satisfaction, and an extension study (the "GROWS" model, adding obstacle-recovery strategies) found the original GROW model less effective at sustaining behavioral change than its modified version in a small four-client pilot.[^8][^9][^10][^11][^12]

**The honest assessment**: GROW is overwhelmingly a *structuring heuristic* — a shared vocabulary for sequencing a conversation — rather than a mechanism with its own demonstrated causal effect distinct from general goal-directed coaching. Nearly every published GROW study is small (n=4 to 60), uncontrolled or weakly controlled, and conflates GROW's effect with the effect of the underlying goal-setting and coaching-relationship processes it packages. No large randomized trial has isolated GROW's four-stage structure against an alternative structure or against unstructured coaching conversations of equal length. Its popularity — as the most widely taught coaching model globally — considerably outpaces the rigor of its evidence base.[^13][^14]

## What Makes a Coaching Conversation Effective: Broader Psychological Evidence

### Working Alliance

The strongest, most consistently replicated predictor of coaching effectiveness is the *working alliance* — the coach-client bond, agreement on goals, and agreement on tasks, a construct imported from psychotherapy research. A meta-analysis synthesizing 27 samples (N=3,563 coaching processes) found a moderate, consistent overall relationship between working-alliance quality and coaching outcomes (r=.41, 95% CI [.34,.48]), with the strongest links to affective and cognitive outcomes, and a negative relationship to unintended negative effects of coaching (r=-.29). This mirrors psychotherapy research, where alliance-outcome correlations are similarly moderate (r≈.23-.31) and robust to adjustment for confounds. In career counseling specifically, a dedicated meta-analysis found alliance strongly associated with client-perceived quality (r=.62), moderately with career outcomes (r=.28), and more weakly with mental-health outcomes (r=.18). However, a more recent VU Amsterdam study complicates this picture, finding that while alliance correlates with effectiveness at the *start* of coaching, it does not significantly predict *increasing* outcomes across further sessions — suggesting alliance may matter most for setting a productive baseline rather than driving continued improvement. Rapport-building by the coach shows a medium effect on subsequent alliance quality (r=.39) in the broader helping-relationship literature.[^15][^16][^17][^18][^19][^20][^21]

### Powerful Questioning

Questioning is empirically central but under-studied relative to its practitioner prominence. The QueSCo project — the first systematic linguistic-psychological study of authentic coaching questioning — coded 3,691 questions across 3,023 questioning sequences in 60 coaching sessions, finding that 83% of coded data fell into successful questioning sequences and that clients provided substantive answers (not deflections) 73% of the time. The authors note explicitly that prior claims about "powerful questions" have been "primarily experience-based, rather than evidence-based" — a caution directly relevant to any AI tool built on assumptions about question quality. A separate review of studies from 1990-2021 associates well-formed, open-ended questions with increased self-awareness, improved problem-solving, and stronger goal commitment, though this review draws on a mix of study qualities rather than uniformly rigorous experimental designs.[^22][^23][^24]

### Goal-Setting Theory (Locke & Latham) in Live Conversation

Locke and Latham's goal-setting theory — specificity and difficulty of goals drive performance — is frequently cited as GROW's theoretical backbone. Its application inside a *live conversation* (rather than a written plan) matters because the theory's core mechanisms — goal clarity, commitment, and feedback — must be generated interactively through dialogue rather than imposed. Coaching-psychology meta-analyses find that psychologically informed coaching (incorporating live goal-setting dialogue) produces large effects on goal attainment (g=1.29) and moderate effects on self-efficacy (g=0.59), with the effect on goal attainment stronger than on general well-being outcomes. This suggests goal-setting-theory mechanisms translate well into conversational coaching but their benefits concentrate specifically on the goal-related domain, not broader psychological change — a pattern consistent with the GROW-specific findings above.[^11][^25]

## Evidence-Based Practice for the "Options" Stage

Research on brainstorming directly challenges naive practitioner advice to "just ask for more options." A large body of experimental work (Diehl & Stroebe and successors) shows that *interactive* group brainstorming reliably underperforms *nominal* (individual, then pooled) brainstorming on both quantity and quality of ideas — a robust and long-replicated finding sometimes called the "illusion of group productivity". The mechanism is production blocking and evaluation apprehension: when people wait for a turn to speak or fear judgment, idea generation drops. This has a direct implication for one-on-one coaching Options stages: encouraging the client to generate ideas independently first (e.g., writing several before discussing) may outperform pure verbal back-and-forth.[^26]

A second consistent finding is that idea *generation* and idea *selection/evaluation* should be temporally and cognitively separated. Osborn's original brainstorming rules — deferring judgment — remain empirically supported: research finds a strong link between total ideas generated and the number of high-quality ideas in that set, meaning volume-first approaches out-perform quality-filtered approaches from the outset. Studies on "convergence techniques" in team ideation similarly find that structured techniques for narrowing options (rather than ad hoc discussion) improve perceived usefulness and shared understanding, but that mixing generation and evaluation into a single task increases premature evaluative pressure and reduces output. For an AI coaching tool, this argues for enforcing sequential phases — generate broadly without commentary, then evaluate — and for prompting the client (not the coach/AI) to produce the initial option set, directly addressing the risk of the coach's own suggestions anchoring or crowding out client-generated options. Recent work on AI-assisted ideation reinforces this concern: language-model-assisted brainstorming shows a documented risk of "premature convergence" and homogenization of ideas when a system's fluent suggestions substitute for open exploration — a caution with direct relevance to an AI coaching tool, since the AI is itself a potential source of premature-convergence bias in the Options stage.[^27][^28][^29][^26]

## Evidence-Based Practice for the "Will" Stage and Commitment Devices

The Will stage of GROW maps closely onto Gollwitzer's implementation-intentions research, which is far more rigorously evidenced than GROW itself. Implementation intentions are if-then plans ("if situation X occurs, then I will perform behavior Y") that pre-decide a response to an anticipated cue, delegating action initiation to automatic situational recognition rather than in-the-moment willpower. Gollwitzer and Sheeran's (2006) meta-analysis of 94 independent studies (over 8,000 participants) found a medium-to-large effect (d=0.65) of implementation intentions on goal attainment, over and above the effect of merely holding a goal intention. Goal intentions alone are a weak predictor of behavior: a meta-analysis of meta-analyses found that goal intentions account for only about 28% of variance in subsequent behavior, and that the intention-behavior gap is substantial even when intentions are strong.[^30][^31][^32]

Implementation intentions work by heightening the mental accessibility of the specified situational cue and forging a strong associative link between that cue and the intended response, effects that appear stable over time. Critically, difficult goals show the largest benefit: Gollwitzer and Brandstätter (1997) found difficult goal intentions were completed roughly three times as often when paired with an implementation intention versus a bare goal intention. A large 2024 update (Sheeran, Listrom, & Gollwitzer, spanning 642 tests) confirms the effect but shows it depends on plan format and underlying motivation strength rather than being a fixed constant — implementation intentions amplify existing goal intentions rather than manufacturing motivation from nothing. Practically, for a Will-stage coaching prompt, this means the highest-value question is not "what will you do?" in the abstract but "when and where, specifically, will you do X, and what cue will trigger it?" — and this technique should only be deployed once the coachee already holds a genuine goal intention, since implementation intentions show weak effects when the underlying goal intention is weak or ambivalent.[^33][^34][^30]

## Career-Coaching-Specific Research

Career coaching and counseling research is distinct from general life/executive coaching in having larger, more mature meta-analytic bases, partly because career interventions are easier to evaluate against objective outcomes (employment, decision self-efficacy). A meta-analytic replication of the influential Brown and Ryan Krane (2000) study, covering 57 studies, found a mean effect size of 0.352 for career choice interventions, with the largest effects on career decision-making self-efficacy (0.452), and found that counselor support and session frequency significantly predicted outcome size. A separate meta-analysis of individual career counseling (35 samples) found weighted mean effects of g=0.82 for career outcomes and g=0.68 for mental-health outcomes, identifying five specific components that predict effectiveness: psychoeducation about the decision process, cognitive restructuring, written exercises (occupational self-analyses), individualized feedback on career choice, and explicit attention to reducing potential obstacles. This last point — obstacle-focused planning — dovetails directly with the GROWS extension study noted earlier, which found that adding explicit obstacle-recovery strategies to GROW improved behavioral follow-through.[^10][^35][^36]

Job-search interventions specifically (distinct from career-choice/decision interventions) show a striking effect: a meta-analysis of 47 experimental/quasi-experimental studies found job seekers in interventions had 2.67 times the odds of obtaining employment compared to controls. Moderator analysis found the most effective interventions combined skill development (teaching search skills, self-presentation) *and* motivation enhancement (self-efficacy boosting, proactivity encouragement, goal setting, social-support enlistment) — interventions containing only one of these two components were markedly less effective. This is a direct, evidence-based argument against a coaching tool that offers only motivational encouragement or only tactical job-search skills in isolation; both must be present. Career-coaching interventions delivered by professional coaches (as distinct from counselors) show similar patterns of reducing career-decision-making difficulties, and working-alliance quality specifically predicts career-counseling outcomes with an overall r=.42, varying by outcome type and by when in the process alliance is measured.[^18][^37][^38][^39]

## Networking Research Beyond Practitioner Advice

Granovetter's 1973 "strength of weak ties" finding — that casual acquaintances outperform close contacts in generating job leads because they bridge to non-redundant information outside one's immediate circle — remains the foundational result, based on a survey of 282 professional/managerial workers in Newton, Massachusetts, in which 84% of contact-based job matches came through acquaintances rather than close ties. Contemporary large-scale digital-trace research has both confirmed and substantially refined this. A 2022 causal experiment on 20 million LinkedIn users (published in *Science*) found that the relationship between tie strength and job mobility is *not* monotonic but inverted-U shaped: ties with roughly 10 mutual connections ("moderately weak" ties) were the most effective for securing new jobs, outperforming both very weak ties (one mutual friend) and strong ties (25+ mutual friends). This directly refines — and complicates — the simplistic "weak ties are always better" message common in practitioner books; the practical implication is that cultivating a moderate number of shared connections with a contact (rather than either total strangers or intimate friends) maximizes job-mobility value. The effect also varies by industry: weak ties help more in digitally intensive, remote-work-friendly fields, while strong ties remain more valuable in analog industries.[^40][^41][^42][^43]

Cross-national replication work covering 55 countries found that while a majority of job-relevant contacts are technically weak ties, this is largely because weak ties are simply far more numerous in most people's networks — at the individual level, a single strong tie is often more valuable than a single weak tie, a pattern termed the "paradox of weak ties". This means volume of weak-tie cultivation matters as much as, or more than, tie quality per contact — a nuance beyond the give-first reciprocity and "anchor connector" heuristics common in practitioner books. Seibert, Kraimer, and Liden's social capital theory of career success (tested on 448 employees) found that network structure (weak ties and "structural holes" — bridging positions between otherwise unconnected groups) affects career success only indirectly, fully mediated by three specific network benefits: access to information, access to resources, and career sponsorship. This is an important refinement for a coaching tool: encouraging a client simply to "build more weak ties" is incomplete advice; the coaching conversation should probe whether a given relationship actually delivers information, resources, or active sponsorship, since ties without these mediating benefits show no career payoff.[^44][^45][^46]

A more recent and directly actionable line of research addresses *dormant ties* — professional contacts that have gone inactive — which practitioner books rarely address with empirical grounding. A multi-method study (qualitative field observation plus a vignette experiment) found that reconnection attempts fail, sometimes badly, when the two parties do not realign on three specific dimensions: how well each remembers the other, how they "catch up" on the intervening period, and whether they perceive the current state of the relationship similarly. This gives a career coaching tool a concrete, evidence-based checklist for coaching a client through the specific act of reconnecting with a lapsed contact, rather than generic "reach out to your network" advice. Complementing this, research on internal versus external networking behavior finds both types positively associated with career success, but through different pathways — external networking builds resources for career mobility, while internal networking builds job commitment within the current organization — suggesting coaching conversations about networking strategy should explicitly distinguish these two goals rather than treating "networking" as a single undifferentiated activity.[^47][^48][^49]

---

## References

1. [GROW model - Wikipedia](https://en.wikipedia.org/wiki/GROW_model)

2. [The GROW Coaching Model: coach, don't solve | HotPMO](https://www.hotpmo.com/management_models/grow-coaching-model/) - The GROW coaching model gives PMO managers a four-stage structure for coaching project managers inst...

3. [GROW Coaching Model: The Fascinating Backstory](https://workplacepsychology.wordpress.com/2018/04/09/grow-coaching-model-the-fascinating-backstory/) - One of the most popular coaching models in the world is the G.R.O.W. Model (Whitmore, 2017). GROW is...

4. [The History and Development of the GROW Coaching Model | UKCPD](https://ukcpd.co.uk/the-history-and-development-of-the-grow-coaching-model) - Exploring the GROW Coaching Model

5. [The G.R.O.W. Model for Performance Coaching](https://www.disruptiveleadership.institute/grow_model/) - Leading the Future in Unprecedented Times

6. [GROW Coaching Model: 80+ Questions, Real Examples & ...](https://www.evalflow.com/blog/grow-coaching-model) - Master the GROW coaching model with 80+ ready-to-use questions, 5 real-world scenarios, and a head-t...

7. [The G.R.O.W. Model In Business Coaching – Simple, Concise, and ...](https://www.stevenguyenphd.com/post/the-g-r-o-w-model-in-business-coaching-simple-concise-and-powerful) - Business coaching is enhancing a client’s (person in a business) awareness and behavior in order to ...

8. [Chapter%2012%20Research%20v5%20-%20clean.docx](https://eprints.bbk.ac.uk/id/eprint/49412/1/Chapter%2012%20Research%20v5%20-%20clean.docx)

9. [[PDF] กลไกการเปลี่ยนแปลงของการโค้ชตาม GROW Model ต่อการท - ThaiJo](https://so06.tci-thaijo.org/index.php/hej/article/download/291455/193715/1332201)

10. [extending the GROW coaching model to support behavioural ...](https://centaur.reading.ac.uk/104381/1/Final%20Revision%20-%20Panchal%20and%20Riddell%20Research%20Paper_27th%20Feb%202020%5B1%5D.pdf)

11. [The Effectiveness of Workplace Coaching among Line ...](https://esource.dbs.ie/server/api/core/bitstreams/1533495a-66d3-45c6-9d60-a35c912ff2a6/content)

12. [Zoom-based GROW coaching intervention for improving ...](https://pmc.ncbi.nlm.nih.gov/articles/PMC9452042/) - Poor subjective well-being is a risk factor for poor health; and threatens school administrators' le...

13. [The GROW Model: A Coaching Framework That Works - MindTools](https://www.mindtools.com/your-toolkit/coaching-goals/grow-model/) - Learn how to use the GROW coaching model. A step-by-step guide to Goal, Reality, Options, and Will f...

14. [Sources](https://blog.hptbydts.com/in-a-nutshell-grow-coaching-model) - The GROW model is the most influential model used in coaching. It was popularised by Sir John Whitmo...

15. [A multilevel meta-analysis of client and therapist predictors for alliance quality: Absolute and relative associations with working alliance.](https://doi.apa.org/doi/10.1037/pst0000603) - Extensive research, including meta-analytic studies, has underscored the role of working alliance in...

16. [The relationship between working alliance and client outcomes in coaching: A meta-analysis](https://journals.sagepub.com/doi/10.1177/0018726718819725) - A growing number of studies emphasize the working alliance between the client and the coach to be a ...

17. [The relationship between working alliance and client outcomes in ...](http://fox.leuphana.de/portal/en/publications/the-relationship-between-working-alliance-and-client-outcomes-in-coaching(4ada720d-0dab-4158-a93d-c4a1fe925a06).html) - The meta-analytic results indicate a moderate and consistent overall relationship between a high-qua...

18. [A Meta-Analytic Investigation of the Association Between Working Alliance and Outcomes of Individual Career Counseling - Francis Milot-Lapointe, Yann Le Corff, Nicole Arifoulline, 2021](https://journals.sagepub.com/doi/abs/10.1177/1069072720985037) - This article reports on the results of the first meta-analysis of the association between working al...

19. [VU Research Portal](https://research.vu.nl/ws/portalfiles/portal/260828798/New_findings_on_the_effectiveness_of_the_coaching_relationship_time_to_think_differently_about_active_ingredients.pdf)

20. [A multilevel meta-analysis of client and therapist predictors for alliance quality: Absolute and relative associations with working alliance - PubMed](https://pubmed.ncbi.nlm.nih.gov/41114940/) - Extensive research, including meta-analytic studies, has underscored the role of working alliance in...

21. [Assessing the alliance-outcome association adjusted for patient characteristics and treatment processes: A meta-analytic summary of direct comparisons](https://pmc.ncbi.nlm.nih.gov/articles/PMC7529648/pdf/nihms-1554404.pdf)

22. [[PDF] Enhancing Coaching Outcomes with Powerful Questions - IJCRT.org](https://ijcrt.org/papers/IJCRT2302425.pdf)

23. [Full article: How coaches and clients do questioning in coaching](https://www.tandfonline.com/doi/full/10.1080/17521882.2025.2586495) - However, beyond isolated psychological research, the evidence base of questioning in coaching and it...

24. [How coaches and clients do questioning in coaching – results from ...](https://www.tandfonline.com/doi/abs/10.1080/17521882.2025.2586495) - Questions are a central intervention in coaching. However, beyond isolated psychological research, t...

25. [[PDF] a meta-analysis of contemporary psychologically informed coaching ...](https://eprints.bbk.ac.uk/id/eprint/44164/1/Coaching%20Psychology%20Meta%20Analysis%20YL%20and%20AM.pdf) - Recent meta-analysis. (GraЯmann et al., 2020) confirmed the working alliance which refers to the coa...

26. [Productivity is not enough: A comparison of interactive and nominal brainstorming groups on idea generation and selection ☆](https://www.sciencedirect.com/science/article/abs/pii/S0022103105000600) - The conclusion that nominal brainstorming groups outperform interactive brainstorming groups has bee...

27. [La IA en el brainstorming creativo: entre la expansión de ideas y el riesgo de herding](https://tesla.puertomaderoeditorial.com.ar/index.php/tesla/article/view/696) - The incorporation of generative artificial intelligence into creative ideation has reconfigured cont...

28. [Can LLM-Powered Multi-Agent Systems Augment Human Creativity? Evidence from Brainstorming Tasks](https://dl.acm.org/doi/10.1145/3715928.3737479) - This paper investigates whether LLM-powered multi-agent systems can effectively augment human creati...

29. [Brainstorming is Just the Beginning: Effects of Convergence Techniques on Satisfaction, Perceived Usefulness of Moderation, and Shared Understanding in Teams](https://ieeexplore.ieee.org/document/7069725/)

30. [162](https://bpb-us-e1.wpmucdn.com/wp.nyu.edu/dist/c/6235/files/2019/02/gollwitzer-oettingen-2011-planning-promotes-goal-striving.pdf)

31. [Implementation Implementation Intentions](https://bpb-us-e1.wpmucdn.com/wp.nyu.edu/dist/c/6235/files/2019/02/gollwitzer-oettingen-2013-implementation-intentions.pdf)

32. [[PDF] Implementation Intentions Peter M. Gollwitzer New York University ...](https://cancercontrol.cancer.gov/sites/default/files/2020-06/goal_intent_attain.pdf)

33. [Implementation Intentions and Goal Achievement: Meta-Analysis](https://studylib.net/doc/28131566/gollwitzersheeran2016) - Meta-analysis of 94 studies on implementation intentions and goal achievement, showing medium-to-lar...

34. [Implementation Intentions: Gollwitzer & Sheeran 2006 (d=0.65)](https://goalsandprogress.com/implementation-intentions-gollwitzer-how-to/) - Implementation intentions are if-then plans. Gollwitzer and Sheeran (2006) found a medium-to-large e...

35. [Effectiveness of career choice interventions: A meta-analytic replication and extension](https://www.sciencedirect.com/science/article/abs/pii/S0001879117300283) - This meta-analysis of career choice intervention is a replication of Brown and Ryan Krane's (2000) n...

36. [A Meta-Analysis of the Effectiveness of Individual Career ...](https://www.fachportal-paedagogik.de/literatur/vollanzeige.html?FId=3542446) - Volltext lesen zu:Entscheidung; Psychischer Faktor; Psychodiagnostik; Gesundheitszustand; Determinan...

37. [Effectiveness of job search interventions: a meta-analytic review](https://research.monash.edu/en/publications/effectiveness-of-job-search-interventions-a-meta-analytic-review/)

38. [Effectiveness of job search interventions: a meta-analytic review.](https://europepmc.org/article/med/24588365) - Europe PMC is an archive of life sciences journal literature.

39. [The effectiveness of a career coaching intervention conducted by a ...](https://www.sciencedirect.com/science/article/pii/S0001879126000588) - Across studies, career coaching has been associated with improvements in focal outcomes, including d...

40. [The strength of weak ties | Stanford Report](https://news.stanford.edu/stories/2023/07/strength-weak-ties) - In 1973, Stanford sociologist Mark Granovetter showed just how important casual acquaintances are.

41. [[PDF] Weak ties, failed tries, and success](https://ide.mit.edu/wp-content/uploads/2022/09/v2add0692-min.pdf?x65156&x96981)

42. [Why Weak Ties' Help and Strong Ties' Don't](https://irle.berkeley.edu/wp-content/uploads/2012/07/Why-Weak-Ties-Help-and-Strong-Ties-Dont.pdf)

43. [Study: 'Weak ties' make a difference in finding a job online | MIT Sloan](https://mitsloan.mit.edu/ideas-made-to-matter/study-weak-ties-make-a-difference-finding-a-job-online) - New research looking at LinkedIn connections shows that acquaintances can be more helpful in finding...

44. [The paradox of weak ties in 55 countries](https://www.sciencedirect.com/science/article/pii/S0167268116302864)

45. [seibert.PDF](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=78a5402e5cd184c233802098734172e8b2a37be2)

46. [A Social Capital Theory of Career Success](https://journals.aom.org/doi/10.5465/3069452) - A model integrating competing theories of social capital with research on career success was develop...

47. [Internal and external networking behaviors and employee ...](https://acuresearchbank.acu.edu.au/download/0e774fff782462a83c937f97b2b8d2500bf55d6d76f62b938d0ab0ae94a4e853/455082/AM_Wanigasekara_2022_Internal_and_external_networking_behaviors_and.pdf)

48. [Reconnecting When Network Ties Go Dormant](https://sloanreview.mit.edu/article/reconnecting-when-network-ties-go-dormant/) - New research identifies three elements that are key to successfully reviving an inactive professiona...

49. [The Reconnection Process: Mobilizing the Social Capital of Dormant Ties | Organization Science](https://pubsonline.informs.org/doi/10.1287/orsc.2023.1685) - Prior research has identified the value of reconnecting dormant ties (i.e., people you used to know)...

