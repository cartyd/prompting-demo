"""
Sample data for offline demonstration mode.
Contains pre-loaded prompts and outputs for each framework.
"""

# Sample tasks for each framework
SAMPLE_TASKS = {
    "Chain of Thought": "Our department has been asked to reduce operational costs by 15% over the next quarter. We currently spend $200K quarterly on: software licenses ($80K), office supplies ($30K), travel ($50K), external contractors ($40K). Where should we focus our cost-cutting efforts?",
    
    "Tree of Thought": "Our team missed the last two sprint deadlines. The product manager says we're overcommitting, the developers say requirements keep changing, and QA says they don't have enough time for testing. As the team lead, how do you address this?",
    
    "Self-Consistency": "A colleague emails you on Friday at 4:30 PM with an 'urgent' request to review a 40-page document before Monday's 9 AM executive meeting. You have dinner plans at 6 PM and a packed weekend. You don't report to this colleague, but they're influential in the company. How do you respond?",
    
    "Few-Shot": "Write a summary of the Q3 budget review meeting for distribution to stakeholders who couldn't attend.",
    
    "Reflection & Revision": "Write a performance review self-assessment highlighting your accomplishments this quarter."
}

# Ad-hoc outputs for each framework
ADHOC_OUTPUTS = {
    "Chain of Thought": "Focus on reducing travel and contractor costs since they're the largest discretionary expenses. Cut travel by 30% and reduce contractor usage by 20%.",
    
    "Tree of Thought": "Have a team meeting to discuss the issues. Ask everyone to be more realistic about estimates and lock down requirements earlier. Make sure QA is involved from the start.",
    
    "Self-Consistency": "Tell them you have weekend plans but will try to review it Sunday evening. Ask them to highlight the most critical sections.",
    
    "Few-Shot": """Q3 Budget Review Meeting Summary

The meeting covered our Q3 budget performance. We discussed where we overspent and where we saved money. Action items were assigned to various team leads. Overall, we're on track for the year.

Key points:
- Some departments over budget
- Cost-saving measures identified
- Q4 planning discussed""",
    
    "Reflection & Revision": """This quarter I worked on several important projects and met my goals. I collaborated well with my team and delivered quality work on time. I'm proud of what I accomplished and look forward to taking on more responsibility.

Key achievements:
- Completed all assigned projects
- Helped team members when needed
- Maintained good communication"""
}

# Framework outputs for each framework
FRAMEWORK_OUTPUTS = {
    "Chain of Thought": """Let me think through this step by step:

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

This approach minimizes business disruption while achieving the 15% target.""",
    
    "Tree of Thought": """Let me explore multiple approaches to this problem:

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

This approach acknowledges the capacity issue while improving process and communication.""",
    
    "Self-Consistency": """All three samples share common elements: setting boundaries, offering alternatives, and seeking clarity. The optimal response combines these:

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
- Preserves your weekend while showing willingness to help""",
    
    "Few-Shot": """Subject: [SUMMARY] Q3 Budget Review - Variance Analysis & Q4 Adjustments

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

Attachments: Q3_Variance_Report.xlsx, Q4_Budget_Scenarios.pdf""",
    
    "Reflection & Revision": """Q3 Self-Assessment - Accomplishments

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
Given these results, I'm ready to take on increased scope. Specifically interested in leading the Q4 mobile app initiative or the customer data platform project."""
}

# Intermediate data for frameworks that need it
INTERMEDIATE_DATA = {
    "Self-Consistency": {
        "samples": [
            "I can do a high-level review of the executive summary and key recommendations Monday morning at 7 AM, which would give you feedback before the 9 AM meeting. For a thorough review of the full document, I'd need until Tuesday. Which would be more valuable?",
            "I have personal commitments this weekend. Can you help me understand what specifically needs review? If there are 3-4 critical sections, I can prioritize those for early Monday. Otherwise, I can provide comprehensive feedback by Tuesday afternoon.",
            "I'm tied up this weekend, but I want to help. Could we schedule 30 minutes Monday at 7:30 AM to discuss the key points? That way you'd have real-time feedback before your meeting. Alternatively, is there someone else who could tag-team the review with me?"
        ],
        "num_samples": 3
    },
    "Reflection & Revision": {
        "initial_answer": """Q3 Self-Assessment - Accomplishments

This quarter I made significant contributions to our team's success:

**Project Delivery:**
I successfully delivered the customer portal redesign project, which improved user experience and received positive feedback. I also contributed to the data migration initiative and helped resolve several critical issues.

**Team Collaboration:**
I mentored two junior developers and helped them get up to speed on our codebase. I regularly participated in code reviews and shared knowledge during team meetings.

**Process Improvement:**
I identified inefficiencies in our deployment process and worked with DevOps to streamline it.

**Professional Growth:**
I completed a certification in cloud architecture and applied those learnings to our infrastructure decisions.

I believe I met my quarterly goals and am ready for additional challenges.""",
        
        "critique": """Strengths:
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
- Process improvement mentioned but impact not quantified""",
        
        "final_answer": FRAMEWORK_OUTPUTS["Reflection & Revision"]
    }
}
