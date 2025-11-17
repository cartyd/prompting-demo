# Sample Prompts for Each Framework

This document provides curated office environment examples that demonstrate the superiority of each prompting framework compared to ad-hoc (zero-shot) prompts.

---

## 1. 🧠 Chain of Thought

### Task
"Our department has been asked to reduce operational costs by 15% over the next quarter. We currently spend $200K quarterly on: software licenses ($80K), office supplies ($30K), travel ($50K), external contractors ($40K). Where should we focus our cost-cutting efforts?"

### Ad-Hoc Prompt Output
"Focus on reducing travel and contractor costs since they're the largest discretionary expenses. Cut travel by 30% and reduce contractor usage by 20%."

**Analysis:** ❌ Simplistic. Doesn't consider impact on productivity, feasibility, or strategic importance.

### Chain of Thought Output
"Let me think through this step by step:

**Step 1: Calculate the target reduction**
- 15% of $200K = $30K reduction needed

**Step 2: Analyze each category by flexibility and business impact**

Software licenses ($80K):
- Often annual contracts, hard to change mid-term
- Critical for productivity
- Low flexibility: ~5% reduction possible = $4K

Office supplies ($30K):
- Moderate flexibility
- Low business impact if managed well
- Possible reduction: 20% = $6K

Travel ($50K):
- High flexibility
- Medium business impact (depends on client-facing needs)
- Possible reduction: 40% through virtual meetings = $20K

Contractors ($40K):
- High flexibility
- High business impact if they're filling critical gaps
- Need to assess: are they doing core work or auxiliary projects?
- Possible reduction: 25% by reprioritizing projects = $10K

**Step 3: Evaluate combinations to reach $30K**
- Option A: Travel ($20K) + Supplies ($6K) + Software ($4K) = $30K ✓
- Option B: Contractors ($10K) + Travel ($20K) = $30K ✓

**Step 4: Assess business impact**
- Option A spreads cuts across categories, minimizes disruption
- Option B preserves supplies and software but may impact project delivery

**Recommendation:**
Implement Option A:
1. Reduce travel by 40% ($20K) - mandate virtual-first meetings
2. Reduce supplies by 20% ($6K) - switch to lower-cost vendors, reduce waste
3. Optimize software licenses ($4K) - remove unused licenses, negotiate better rates

This approach minimizes business disruption while achieving the 15% target."

**Analysis:** ✅ Comprehensive, considers trade-offs, arrives at actionable plan with justification.

### Why Chain of Thought Is Superior

| Aspect | Ad-Hoc | Chain of Thought |
|--------|--------|------------------|
| **Analysis Depth** | Surface-level | Multi-dimensional |
| **Feasibility** | Not considered | Evaluated per category |
| **Business Impact** | Ignored | Central to decision |
| **Justification** | Weak | Clear reasoning at each step |
| **Actionability** | Vague | Specific with percentages |

---

## 2. 🌳 Tree of Thought

### Task
"Our team missed the last two sprint deadlines. The product manager says we're overcommitting, the developers say requirements keep changing, and QA says they don't have enough time for testing. As the team lead, how do you address this?"

### Ad-Hoc Prompt Output
"Have a team meeting to discuss the issues. Ask everyone to be more realistic about estimates and lock down requirements earlier. Make sure QA is involved from the start."

**Analysis:** ❌ Generic advice without exploring root causes or different intervention strategies.

### Tree of Thought Output
"Let me explore multiple approaches to this problem:

**Branch 1: Process-Focused Approach**
- Root cause: Lack of clear process and planning
- Solution: Implement stricter sprint planning, definition of done, requirement freeze
- Advantages: Clear structure, predictable outcomes
- Limitations: May slow down responsiveness to urgent changes, feels rigid
- Timeline: 2-3 sprints to stabilize

**Branch 2: Communication-Focused Approach**
- Root cause: Misalignment and unclear expectations
- Solution: Daily standups with all roles, shared sprint dashboard, weekly retrospectives
- Advantages: Increases transparency, surfaces issues early
- Limitations: Doesn't address underlying capacity or requirement issues
- Timeline: Immediate implementation, gradual improvement

**Branch 3: Capacity-Focused Approach**
- Root cause: Team is genuinely overcommitted relative to capacity
- Solution: Reduce sprint commitments by 30%, add buffer time, track velocity accurately
- Advantages: Realistic planning, reduces stress, builds credibility
- Limitations: Delivers less per sprint initially, may face stakeholder pushback
- Timeline: Immediate relief, 3-4 sprints to establish true velocity

**Evaluation:**
Which branch provides the most robust solution?

- Branch 1 assumes the problem is discipline (may not be accurate)
- Branch 2 assumes the problem is communication (helps but incomplete)
- Branch 3 addresses systemic capacity issues (most likely root cause)

**However, a hybrid approach is optimal:**

**Recommended Hybrid Solution:**

*Immediate (This Sprint):*
- Reduce current sprint commitment by 30% (Branch 3)
- Hold team retrospective to identify specific pain points (Branch 2)

*Next Sprint:*
- Implement requirement freeze 2 days into sprint (Branch 1)
- Include QA in planning and story refinement (Branch 2)
- Track actual velocity vs. planned (Branch 3)

*Ongoing:*
- Use historical velocity data to inform future commitments
- Create explicit buffer time (20%) for requirement clarifications
- Establish clear escalation path for mid-sprint changes

This approach acknowledges the capacity issue while improving process and communication."

**Analysis:** ✅ Explores multiple root causes, evaluates trade-offs, synthesizes optimal hybrid solution.

### Why Tree of Thought Is Superior

| Aspect | Ad-Hoc | Tree of Thought |
|--------|--------|-----------------|
| **Root Cause Analysis** | Assumes one cause | Explores multiple hypotheses |
| **Solution Depth** | Single approach | Multiple alternatives evaluated |
| **Trade-offs** | Not considered | Explicitly analyzed |
| **Implementation** | Vague | Phased with specific actions |
| **Risk Management** | Unaddressed | Limitations identified upfront |

---

## 3. 🎯 Self-Consistency

### Task
"A colleague emails you on Friday at 4:30 PM with an 'urgent' request to review a 40-page document before Monday's 9 AM executive meeting. You have dinner plans at 6 PM and a packed weekend. You don't report to this colleague, but they're influential in the company. How do you respond?"

### Ad-Hoc Prompt Output
"Tell them you have weekend plans but will try to review it Sunday evening. Ask them to highlight the most critical sections."

**Analysis:** ❌ Weak boundaries, sets bad precedent, unclear commitment.

### Self-Consistency Output (After Multiple Samples)

**Sample 1 - Professional Boundary Approach:**
"I can do a high-level review of the executive summary and key recommendations Monday morning at 7 AM, which would give you feedback before the 9 AM meeting. For a thorough review of the full document, I'd need until Tuesday. Which would be more valuable?"

**Sample 2 - Clarifying Urgency Approach:**
"I have personal commitments this weekend. Can you help me understand what specifically needs review? If there are 3-4 critical sections, I can prioritize those for early Monday. Otherwise, I can provide comprehensive feedback by Tuesday afternoon."

**Sample 3 - Collaborative Problem-Solving Approach:**
"I'm tied up this weekend, but I want to help. Could we schedule 30 minutes Monday at 7:30 AM to discuss the key points? That way you'd have real-time feedback before your meeting. Alternatively, is there someone else who could tag-team the review with me?"

**Synthesized Answer:**
"All three samples share common elements: setting boundaries, offering alternatives, and seeking clarity. The optimal response combines these:

'I appreciate you thinking of me for this review. I have personal commitments this weekend, but I want to help you prepare for Monday's meeting.

Here are a few options:

1. I can review the executive summary and key recommendations Monday morning at 7 AM and provide targeted feedback before your 9 AM meeting
2. We could schedule a 30-minute working session Monday at 7:30 AM to discuss the critical points in real-time
3. For a comprehensive review of the full document, I could deliver detailed feedback by Tuesday afternoon

Which option would be most valuable for your needs?'

This response:
- Maintains professional boundaries without being dismissive
- Offers concrete alternatives rather than a vague 'I'll try'
- Puts the ball back in their court to assess true urgency
- Preserves your weekend while showing willingness to help"

**Analysis:** ✅ Multiple reasoning paths converge on maintaining boundaries while being helpful and professional.

### Why Self-Consistency Is Superior

| Aspect | Ad-Hoc | Self-Consistency |
|--------|--------|------------------|
| **Boundary Quality** | Weak, apologetic | Firm but professional |
| **Options Provided** | Vague | Multiple concrete alternatives |
| **Perspective** | Single angle | Multiple approaches synthesized |
| **Precedent Set** | Poor (enables future urgencies) | Healthy (teaches planning) |
| **Professionalism** | Moderate | High (helpful without sacrificing boundaries) |

---

## 4. 📚 Few-Shot

### Task
"Write a summary of the Q3 budget review meeting for distribution to stakeholders who couldn't attend."

### Ad-Hoc Prompt Output
"Q3 Budget Review Meeting Summary

The meeting covered our Q3 budget performance. We discussed where we overspent and where we saved money. Action items were assigned to various team leads. Overall, we're on track for the year.

Key points:
- Some departments over budget
- Cost-saving measures identified
- Q4 planning discussed"

**Analysis:** ❌ Vague, lacks specifics, no actionable information, unprofessional tone.

### Few-Shot Output

**Examples provided in prompt:**

**Example 1 - Product Launch Meeting:**
Subject: [SUMMARY] Product Launch Retrospective - Action Items Inside

Key Decisions:
• Moved launch date from Nov 15 to Nov 29 to address critical bugs
• Approved additional $15K for beta testing program

Outcomes:
• Beta program yielded 127 bugs (83 resolved, 44 in progress)
• Marketing materials completed and approved

Action Items:
• @Sarah Chen - Finalize vendor contracts by Oct 30
• @Mike Torres - Schedule customer advisory board by Nov 1
• @Dev Team - Resolve P0 bugs by Nov 15

Next Steps: Launch readiness review on Nov 22

---

**Example 2 - Quarterly Planning Meeting:**
Subject: [SUMMARY] Q4 Planning Session - Strategic Priorities Confirmed

Key Decisions:
• Prioritized customer retention initiatives over new acquisition for Q4
• Allocated 60% of eng resources to platform stability, 40% to new features

Outcomes:
• Agreed on 3 strategic OKRs for Q4 (see attached document)
• Identified $50K budget reallocation from events to digital marketing

Action Items:
• @Jennifer Liu - Draft detailed OKR rollout plan by Sept 15
• @Finance - Model budget scenarios for 2024 planning by Sept 20
• @All Directors - Submit team Q4 goals by Sept 18

Next Steps: OKR kickoff meeting on Sept 22

---

**Now, here's the Few-Shot output for the budget review meeting:**

"Subject: [SUMMARY] Q3 Budget Review - Variance Analysis & Q4 Adjustments

Key Decisions:
• Approved 12% budget increase for Sales ($45K) to support Q4 pipeline acceleration
• Froze Marketing events budget ($30K) and reallocated to digital campaigns
• Deferred IT infrastructure upgrade from Q4 to Q1 2024 ($80K savings)

Outcomes:
• Overall Q3 variance: -2.3% under budget ($68K savings)
• Engineering 8% over budget due to unexpected cloud costs
• Operations achieved 15% savings through vendor renegotiations

Department Highlights:
• Sales: 94% of budget utilized, strong ROI on trade shows
• Marketing: 89% of budget utilized, underperformed on digital spend
• Engineering: 108% of budget utilized, cloud migration costs exceeded estimates
• Operations: 85% of budget utilized, process automation driving savings

Action Items:
• @Finance - Prepare detailed cloud cost analysis by Oct 25
• @Marketing - Submit revised Q4 digital strategy by Oct 27
• @Operations - Document cost-saving playbook for company-wide adoption by Nov 3
• @All VPs - Review and approve Q4 adjusted budgets by Oct 30

Next Steps: Q4 budget adjustments finalized in next week's executive meeting

Attachments: Q3_Variance_Report.xlsx, Q4_Budget_Scenarios.pdf"

**Analysis:** ✅ Professional, specific, actionable, follows established format from examples.

### Why Few-Shot Is Superior

| Aspect | Ad-Hoc | Few-Shot |
|--------|--------|----------|
| **Format** | Inconsistent, unprofessional | Follows proven template |
| **Specificity** | Vague generalities | Concrete numbers and decisions |
| **Actionability** | Unclear next steps | Clear owners and deadlines |
| **Professionalism** | Casual | Business-appropriate |
| **Completeness** | Missing key information | Comprehensive structure |

---

## 5. 🔄 Reflection & Revision

### Task
"Write a performance review self-assessment highlighting your accomplishments this quarter."

### Ad-Hoc Prompt Output
"This quarter I worked on several important projects and met my goals. I collaborated well with my team and delivered quality work on time. I'm proud of what I accomplished and look forward to taking on more responsibility.

Key achievements:
- Completed all assigned projects
- Helped team members when needed
- Maintained good communication"

**Analysis:** ❌ Generic, no specifics, no quantifiable impact, sounds like everyone's self-assessment.

### Reflection & Revision Output

**Step 1: Initial Answer**
"Q3 Self-Assessment - Accomplishments

This quarter I made significant contributions to our team's success:

**Project Delivery:**
I successfully delivered the customer portal redesign project, which improved user experience and received positive feedback. I also contributed to the data migration initiative and helped resolve several critical issues.

**Team Collaboration:**
I mentored two junior developers and helped them get up to speed on our codebase. I regularly participated in code reviews and shared knowledge during team meetings.

**Process Improvement:**
I identified inefficiencies in our deployment process and worked with DevOps to streamline it.

**Professional Growth:**
I completed a certification in cloud architecture and applied those learnings to our infrastructure decisions.

I believe I met my quarterly goals and am ready for additional challenges."

**Step 2: Critique**
"Strengths:
- Covers multiple areas (projects, collaboration, process, growth)
- Mentions specific initiatives

Weaknesses:
- Lacks quantifiable metrics and business impact
- Vague language ('significant contributions,' 'positive feedback')
- Doesn't connect accomplishments to company/team goals
- Missing specifics on challenges overcome
- Passive voice diminishes ownership ('was delivered' vs 'I delivered')
- No evidence or examples provided
- 'Received positive feedback' - from whom? What specifically?
- 'Several critical issues' - which ones? What was the impact?
- Mentorship claim lacks details on outcomes
- Process improvement mentioned but impact not quantified"

**Step 3: Revised Answer**
"Q3 Self-Assessment - Accomplishments

**1. Customer Portal Redesign - Drove Revenue Impact**

*What I did:*
Led the end-to-end redesign of our customer portal, managing a 3-person team through 8-week delivery cycle.

*Business impact:*
- Reduced customer support tickets by 34% (from 450 to 297/month)
- Increased self-service adoption from 23% to 61%
- Improved customer satisfaction score from 3.2 to 4.4 out of 5
- Directly contributed to $127K in cost savings (support time reduction)

*Challenge overcome:*
When we discovered our original mobile design wouldn't work with legacy systems, I proposed and implemented a progressive web app approach that maintained our timeline while delivering 95% of planned functionality.

**2. Data Migration - Minimized Business Risk**

*What I did:*
Architected and executed migration of 2.3M customer records from legacy CRM to Salesforce with zero downtime.

*Business impact:*
- Zero data loss (validated 100% of migrated records)
- Completed 2 weeks ahead of schedule
- Enabled sales team to access real-time customer data, improving response time by 40%

*Challenge overcome:*
Identified critical data integrity issues during testing phase that would have corrupted 18% of records. Developed custom validation scripts and recovery procedures, preventing what would have been a major business disruption.

**3. Team Development - Multiplying Impact**

*What I did:*
Mentored Junior Developers Alex and Priya through structured 12-week onboarding program I created.

*Impact:*
- Both are now independently shipping production code (previously required 60% oversight)
- Alex delivered the notification system refactor (user engagement up 28%)
- Priya resolved the payment processing bug that was costing $3K/week in failed transactions
- My mentorship approach was adopted as team-wide standard by Engineering Manager

**4. Process Optimization - Scaling Team Efficiency**

*What I did:*
Analyzed deployment bottlenecks and partnered with DevOps to redesign CI/CD pipeline.

*Impact:*
- Reduced deployment time from 47 minutes to 12 minutes (74% improvement)
- Decreased deployment failures from 12% to 2%
- Enabled team to ship 3x more frequently (2x per week → 6x per week)
- Documented new process, now used by 4 other engineering teams

**5. Strategic Skill Development**

*What I did:*
Earned AWS Solutions Architect certification and immediately applied knowledge to our infrastructure planning.

*Impact:*
- Identified $84K/year in potential cloud cost savings through reserved instances and auto-scaling optimization
- Presented findings to VP Engineering, now part of Q4 cost-reduction initiative
- Became go-to resource for architecture questions (consulted on 3 cross-team projects)

**Alignment to Company Goals:**
These accomplishments directly support our Q3 company priorities:
- Customer Experience (Portal redesign - satisfaction up 37%)
- Operational Excellence (Migration, deployment process)
- Team Growth (Mentorship, knowledge sharing)
- Cost Management (Support savings, cloud optimization)

**Looking Ahead:**
Given these results, I'm ready to take on increased scope. Specifically interested in leading the Q4 mobile app initiative or the customer data platform project."

**Analysis:** ✅ Specific, quantified, demonstrates impact, shows leadership, connects to business goals.

### Why Reflection & Revision Is Superior

| Aspect | Ad-Hoc | Reflection & Revision |
|--------|--------|-----------------------|
| **Specificity** | Vague claims | Concrete metrics and outcomes |
| **Impact** | Not demonstrated | Quantified business value |
| **Evidence** | None | Multiple data points |
| **Storytelling** | Absent | Clear challenge-solution-result |
| **Strategic Thinking** | Not shown | Links to company goals |
| **Career Positioning** | Weak | Strong case for advancement |

---

## 📊 Overall Framework Comparison for Office Tasks

| Framework | Best For | Key Advantage | Office Use Case |
|-----------|----------|---------------|-----------------|
| **Chain of Thought** | Analysis, planning, resource allocation | Transparent reasoning process | Budget planning, cost reduction, capacity planning |
| **Tree of Thought** | Complex problems, conflict resolution | Explores multiple solutions systematically | Team issues, strategic decisions, process design |
| **Self-Consistency** | Nuanced situations, professional communication | Validates approach through multiple perspectives | Difficult emails, stakeholder management, boundary-setting |
| **Few-Shot** | Professional writing, consistent formatting | Learns from examples to match quality/style | Meeting summaries, status reports, documentation |
| **Reflection & Revision** | High-stakes writing, self-advocacy | Iterative improvement through self-critique | Performance reviews, proposals, presentations |

---

## 🚀 Using These Examples in the Demo

Copy these office-relevant tasks into the Streamlit app:

1. **Chain of Thought:** "Our department has been asked to reduce operational costs by 15% over the next quarter. We currently spend $200K quarterly on: software licenses ($80K), office supplies ($30K), travel ($50K), external contractors ($40K). Where should we focus our cost-cutting efforts?"

2. **Tree of Thought:** "Our team missed the last two sprint deadlines. The product manager says we're overcommitting, the developers say requirements keep changing, and QA says they don't have enough time for testing. As the team lead, how do you address this?"

3. **Self-Consistency:** "A colleague emails you on Friday at 4:30 PM with an 'urgent' request to review a 40-page document before Monday's 9 AM executive meeting. You have dinner plans at 6 PM and a packed weekend. You don't report to this colleague, but they're influential in the company. How do you respond?"

4. **Few-Shot:** "Write a summary of the Q3 budget review meeting for distribution to stakeholders who couldn't attend."

5. **Reflection & Revision:** "Write a performance review self-assessment highlighting your accomplishments this quarter."
