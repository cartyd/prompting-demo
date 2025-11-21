"""
Sample data for offline demonstration mode.
Contains pre-loaded prompts and outputs for each framework.
"""

from constants import (
    FRAMEWORK_CHAIN_OF_THOUGHT,
    FRAMEWORK_TREE_OF_THOUGHT,
    FRAMEWORK_SELF_CONSISTENCY,
    FRAMEWORK_FEW_SHOT,
    FRAMEWORK_REFLECTION_REVISION
)
import prompt_templates as templates
# Base tasks for each framework - single source of truth
SAMPLE_TASKS = {
    FRAMEWORK_CHAIN_OF_THOUGHT: """Our department has been tasked with reducing operational costs by 15% over the next quarter. We currently spend $200,000 quarterly on the following items:

- software licenses ($80,000)
- office supplies ($30,000)
- travel ($50,000)
- external contractors ($40,000)

Where should we focus on our cost-cutting efforts?""",

    FRAMEWORK_TREE_OF_THOUGHT: """Improve the following monthly team performance report and make it more effective. Here is the report to improve:

Team Performance Report [January]

This month the team completed most of their tasks. We met for several meetings and discussed project issues. Some items were delayed, but we expect to finish them early next month. The team communicated well overall.

Blockers include limited QA availability and some confusion about priorities.
Next month we will try to finish the delayed tasks and stay on track.""",
    
    FRAMEWORK_SELF_CONSISTENCY: "Write an email summarizing key points from our website redesign project meeting.",
    
    FRAMEWORK_FEW_SHOT: """Write a weekly project update for the Data Migration Project. The project information follows:

Project: Data Migration Project

Current Status: Slightly Behind

This Week:

Completed migration of 4 legacy tables (Customer, Orders, Payments, Inventory).
Performed validation checks on 58% of migrated data.
Next Week:

Begin migrating Product and Pricing tables.
Conduct full validation sweep on completed tables.
Risks/Blockers:

Unresolved indexing issue causing slow query performance in staging.""",
    
    FRAMEWORK_REFLECTION_REVISION: "Write an email to stakeholders explaining that the product launch date will be delayed by two weeks."
}

# Build framework prompts from base tasks using the same templates
# This ensures consistency and eliminates duplication
def _build_framework_prompts():
    """Build framework prompts from base tasks to avoid duplication."""
    prompts = {}
    
    # Chain of Thought
    task = SAMPLE_TASKS[FRAMEWORK_CHAIN_OF_THOUGHT]
    prompts[FRAMEWORK_CHAIN_OF_THOUGHT] = f"{task}{templates.CHAIN_OF_THOUGHT_INSTRUCTIONS}"
    
    # Tree of Thought
    task = SAMPLE_TASKS[FRAMEWORK_TREE_OF_THOUGHT]
    prompts[FRAMEWORK_TREE_OF_THOUGHT] = f"{task}{templates.TREE_OF_THOUGHT_INSTRUCTIONS}"
    
    # Self-Consistency
    task = SAMPLE_TASKS[FRAMEWORK_SELF_CONSISTENCY]
    prompts[FRAMEWORK_SELF_CONSISTENCY] = f"{task}{templates.SELF_CONSISTENCY_INSTRUCTIONS}"
    
    # Few-Shot
    task = SAMPLE_TASKS[FRAMEWORK_FEW_SHOT]
    prompts[FRAMEWORK_FEW_SHOT] = templates.FEW_SHOT_EXAMPLES.format(task=task)
    
    # Reflection & Revision
    task = SAMPLE_TASKS[FRAMEWORK_REFLECTION_REVISION]
    prompts[FRAMEWORK_REFLECTION_REVISION] = f"""Step 1 - Initial Answer Prompt:
{task}{templates.REFLECTION_REVISION_INITIAL}

Step 2 - Critique Prompt:
(After receiving initial answer, critique it for weaknesses)

Step 3 - Revision Prompt:
(Based on critique, provide improved answer)"""
    
    return prompts

# Framework-enhanced prompts built dynamically from base tasks (for online mode)
FRAMEWORK_PROMPTS = _build_framework_prompts()

# Static prompts for offline mode - frozen snapshot for demos
# These are pre-built versions that won't change with template updates
OFFLINE_FRAMEWORK_PROMPTS = {
    FRAMEWORK_CHAIN_OF_THOUGHT: """Our department must reduce operational costs by 15% next quarter, given our current quarterly spend of $200,000, broken down as follows:

* Software licenses: $80,000
* Office supplies: $30,000
* Travel: $50,000
* External contractors: $40,000

I want you to think step-by-step about this problem.

1. Calculate the exact dollar amount that must be cut.
2. Analyze each spending category in terms of size, flexibility, and typical savings potential.
3. Identify which categories offer the best opportunities for meaningful reductions without harming essential operations.
4. Propose a cost-cutting plan that meets or exceeds the target, with specific suggestions and estimated savings per category.
5. Justify your recommendations with brief reasoning.

Provide your final answer as a clear, concise action plan, but use detailed internal reasoning to get there.""",

    FRAMEWORK_TREE_OF_THOUGHT: """Improve the following monthly team performance report using a Tree of Thought approach.

Break your reasoning into multiple branches that explore distinct improvement strategies, including:

- Structure (how the report is organized)
- Tone & clarity (how clearly and professionally it communicates)
- Data emphasis (metrics, KPIs, and measurable results)
- Actionability (SMART goals, owners, deadlines)

For each branch, provide:

1. A clear explanation of the improvement approach
2. Specific proposed changes
3. A brief rewritten sample of the section if relevant

After generating the branches, compare them, evaluate their strengths and weaknesses, and choose the best combined strategy.

Then produce a final, fully rewritten report that merges the strongest ideas from all branches. Here is the report to improve:

Team Performance Report [January]

This month the team completed most of their tasks. We met for several meetings and discussed project issues. Some items were delayed, but we expect to finish them early next month. The team communicated well overall.

Blockers include limited QA availability and some confusion about priorities.

Next month we will try to finish the delayed tasks and stay on track.""",

    FRAMEWORK_SELF_CONSISTENCY: """You are an expert corporate communicator. Use the Self-Consistency Framework to generate the best possible result.

- Step 1 -- Produce three distinct candidate email drafts, each with different tones and structures.

- Step 2 -- Compare the strengths and weaknesses of the candidates.

- Step 3 -- Synthesize a final email that combines the best elements of all candidates and is suitable for sending in a professional corporate setting.

The meeting was about the website redesign project.
Key points discussed:
- Timeline concerns
- Need for improved mobile responsiveness
- Upcoming stakeholder review next Wednesday
- Action items for Design, Engineering, and Marketing teams""",

    FRAMEWORK_FEW_SHOT: """Create a polished, executive-ready weekly project updates by following the structure and tone demonstrated in the examples below.

📘 Example 1
Project: Website Redesign

Status: On Track

This Week:

- Completed user testing sessions with 18 participants
- Finalized UI layouts for the checkout flow
Next Week:

Begin implementing updated components in the production environment.

Risks / Blockers:

Awaiting approval on two new design assets (ETA: Monday).
📘 Example 2
Project: CRM Optimization

Status: Slightly Behind

This Week:

Integrated lead scoring model into CRM sandbox
Tested 4 new automation rules with the sales team
Next Week:

Deploy final automation rules to production.
Risks / Blockers:

Dependency on IT for API rate limit increase.
📝 Instructions for the Model
Using the structure, level of detail, and tone demonstrated in the examples above, prepare a weekly update for the project described below.

📂 Project Details

Project: Data Migration Project

Current Status: Slightly Behind

This Week:

Completed migration of 4 legacy tables (Customer, Orders, Payments, Inventory).
Performed validation checks on 58% of migrated data.
Next Week:

Begin migrating Product and Pricing tables.
Conduct full validation sweep on completed tables.
Risks / Blockers:

Unresolved indexing issue causing slow query performance in staging.""",

    FRAMEWORK_REFLECTION_REVISION: """Draft an email to project stakeholders explaining that the product launch date will be delayed by two weeks.

Reflect on your draft and identify:

1. Missing context stakeholders would need
2. Tone improvements for professionalism and reassurance
3. Any unclear or vague language
4. Opportunities to offer next steps or mitigations

Revise the email accordingly. Provide the final improved version after reflection."""
}

# Ad-hoc outputs for each framework
BASIC_OUTPUTS = {
    FRAMEWORK_CHAIN_OF_THOUGHT:
"""
You need to cut 15% of $200,000 = $30,000 in the next quarter. The biggest and most flexible buckets are the best focus areas:

-  **Software licenses ($80,000):** Aim for ~$10-12K in savings by removing unused licenses, renegotiating contracts, or consolidating tools.

-  **Travel ($50,000):** Target $8--10K savings by shifting to virtual meetings and tightening policies.

-  **External contractors ($40,000):** Reduce scope or pause non-critical work to save $8-10K.

-  **Office supplies ($30,000):** Possible but limited savings ($2--3K).
  
**Overall:** Focus on software, travel, and contractors; use supplies as a minor top-up to reach $30K.""",
    FRAMEWORK_TREE_OF_THOUGHT: """Monthly Team Performance Report [January]

The team performed well overall this month and completed most assigned tasks. We held regular meetings to review progress and address project issues. A few tasks were delayed, but we expect to complete them early next month. Team communication remained strong throughout the period.

Blockers:
- Limited QA availability
- Occasional uncertainty around task priorities

Next Steps:
We plan to complete the delayed tasks next month and maintain better alignment to avoid similar delays.

Characteristics:
- Cleaner writing
- Slightly improved structure
- No deep restructuring, no metrics, no strategic thinking""",
    
    FRAMEWORK_SELF_CONSISTENCY: """Subject: Website Redesign Meeting Summary

Hi team,

Here's a quick summary of our meeting today about the website redesign project. We talked about the project timeline and some concerns that were raised. We also mentioned that the mobile responsiveness needs improvement. There will be a stakeholder review next Wednesday. Design, Engineering, and Marketing teams each have action items to prepare for that review.

Let me know if I missed anything.

Thanks!""",
    
    FRAMEWORK_FEW_SHOT: """The Data Migration Project made some progress this week. We completed a number of migration tasks and continued working through validation. Next week we will keep moving forward with additional table migrations and review work. There are still some issues that we're monitoring, including performance challenges, but we expect to continue making progress.""",
    
    FRAMEWORK_REFLECTION_REVISION: """Subject: Update on Product Launch Timeline

Hi everyone,

I wanted to let you know that the product launch will be delayed by two weeks due to some unexpected issues. We are working on resolving them and will keep you updated.

Thanks,

[Your Name]"""
}

# Framework outputs for each framework
FRAMEWORK_OUTPUTS = {
    FRAMEWORK_CHAIN_OF_THOUGHT: """
    
1. **Target reduction**

* Current quarterly spend   : $200,000
* Required reduction (15%)  : $30,000
* New target spend          : $170,000

2. **Recommended focus areas** 
We'll prioritize categories that are:
* Large enough to yield meaningful savings
* More flexible/discretionary than core operations

**That typically means:** travel, external contractors, and to a lesser extent software licenses. Office supplies are relatively small and often already lean.


3. **Proposed cost-cutting plan**

    A. *Travel*

    * Current: $50,000
    * Proposed reduction: $12,000 (24%)
    * New spend: $38,000

    *Actions (Travel):*

    * Tighten travel policy (default to virtual meetings where possible).
    * Require pre-approval for all air travel and hotels.
    * Switch to lower-cost hotels and advance booking for better fares.

    B. *External contractors*

     Current: $40,000
     Proposed reduction: $10,000 (25%)
     New spend: $30,000

    *Actions (External contractors):*
    
    * Prioritize which contractor work is truly critical next quarter.
    * Bring suitable tasks back in-house where team capacity allows.
    * Renegotiate rates or scale back hours on lower-impact projects.

    C. *Software licenses*

    * Current: $80,000
    * Proposed reduction: $7,000 (≈8.75%)
    * New spend: $73,000

    *Actions (Software licenses):*

    * Audit licenses to remove unused or underused seats.
    * Consolidate overlapping tools (e.g., multiple project management or chat tools).
    * Move some users to lower-tier plans where advanced features aren't needed.

    D. *Office supplies*
    * Current: $30,000
    * Proposed reduction: $1,000 (≈3.3%)
    * New spend: $29,000

    **Actions (Office Supplies):**

    * Standardize items (no premium "nice-to-have" variants).
    * Set simple quarterly limits per team and encourage digital alternatives (e-signatures, electronic note-taking).
   
4. **Summary action plan (meets 15% target)**  

    **Total reductions:**
    * Travel: $12,000
    * External contractors: $10,000
    * Software licenses: $7,000
    * Office supplies: $1,000
    
    **Total:** $30,000 (15% of $200,000)

**Why this mix?**

  * Focuses bigger cuts on discretionary or flexible categories (travel, contractors).
  * Uses optimization rather than elimination for software, which is often critical to productivity.
  * Keeps office supply cuts modest to avoid day-to-day friction, but still sends a cost-conscious signal.""",
    
    FRAMEWORK_TREE_OF_THOUGHT: """Monthly Team Performance Report [January]

Executive Summary

The team achieved strong progress, completing 87% of planned tasks. Collaboration and communication remained effective, though QA constraints impacted the schedule for two deliverables.

**Key Performance Indicators (KPIs)**

- Tasks completed: 26 / 30 (87%)
- On-time delivery rate: 81%
- Outstanding items carried to next month: 4

**Accomplishments**

- Resolved 12 high-priority backlog items
- Completed integration testing for Module B
- Improved meeting cadence resulting in faster issue escalation

**Blockers & Risks**

- Limited QA capacity → slowed verification cycles
- Priority misalignment across engineering and product teams
- Risk: Delayed QA may impact next sprint's release readiness

**Action Plan (SMART)**

- Increase QA coverage by adding 10 hours/week of contractor testing (Owner: QA Lead, Due: Feb 15)
- Publish weekly priority alignment doc to prevent miscommunication (Owner: PM, Start: Feb 1)
- Complete all rolled-over tasks by Feb 10 with daily micro-standups (Owner: Eng Lead)

**Forecast**

With improved alignment and additional QA support, we expect to reach 95% task completion next month.""",
    
    FRAMEWORK_SELF_CONSISTENCY: """Step 1 -- Three Candidate Drafts

Candidate A -- Concise & Formal

Subject: Summary of Today's Website Redesign Meeting

Hello team,

During today's meeting, we reviewed timeline risks, identified mobile responsiveness as the top priority enhancement, and confirmed the stakeholder review scheduled for next Wednesday. Action items were assigned to Design (responsive layout revisions), Engineering (performance investigation), and Marketing (stakeholder materials).

Best regards,

================================================


Candidate B -- Detailed & Structured

Subject: Website Redesign Project -- Meeting Recap

Hi everyone,

Thanks for attending our redesign project touchpoint.

Key Points:

- Timeline pressure due to expanded scope
- Mobile responsiveness issues remain unresolved
- Stakeholder review next Wednesday
- Action Items:
  - Design: Updated mockups
  - Engineering: Fix mobile breakpoints
  - Marketing: Prepare messaging and visuals

Please reach out with questions.

================================================

Candidate C -- More Conversational & Motivational

Subject: Today's Redesign Meeting Highlights

Team,

Great collaboration today. We aligned on immediate priorities: tackling mobile responsiveness and tightening our timeline. With the stakeholder review coming next Wednesday, Design, Engineering, and Marketing each have clear deliverables to complete. Appreciate everyone's commitment--let's keep momentum going.

================================================

Step 2 -- Comparison

Strengths Identified:

- Candidate A: clarity, corporate tone
- Candidate B: structured information for fast consumption
- Candidate C: positive tone and motivation

Weaknesses Identified:

- A: could be more readable
- B: a bit dry, missing tone
- C: lacks structure

Step 3 -- Synthesized Final Email

Final Synthesized Email (Self-Consistency Result):

Subject: Website Redesign Project -- Meeting Summary & Next Steps

Hi team,

Thanks for the productive discussion today. Here is a consolidated summary of our key points and upcoming milestones for the website redesign project:

Main Discussion Points

1. We identified increasing timeline pressure given the expanding scope of the redesign.
2. Improving mobile responsiveness remains our top technical and design priority.
3. The stakeholder review is scheduled for next Wednesday, and all teams confirmed readiness to provide updates.

Action Items

- Design: Deliver revised responsive layouts and updated mockups.
- Engineering: Address mobile breakpoint issues and validate overall performance.
- Marketing: Prepare messaging, visuals, and the stakeholder-facing overview deck.

Let me know if any clarifications are needed. Appreciate everyone's continued collaboration as we head into next week's review.

Best regards,""",
    
    FRAMEWORK_FEW_SHOT: """Project: Data Migration Project

Status: Slightly Behind

This Week:
Migrated 4 legacy tables (Customer, Orders, Payments, Inventory)
Completed validation checks on 58% of migrated data.

Next Week:
Begin migration of Product and Pricing tables
Conduct full validation sweep on previously migrated tables.

Risks / Blockers:
Indexing issue in the staging environment is causing slow query performance.
Remediation is pending from the DBA team (ETA: Tuesday).""",
    
    FRAMEWORK_REFLECTION_REVISION: """Reflection:

- The email should specify the cause of delay in a professional, non-defensive way.
- Stakeholders expect clarity on impact, new timeline, and next steps.
- Tone should remain accountable and reassuring.
- Should include a commitment to transparency and a date for the next update.

Revised Email:

Subject: Updated Timeline for Upcoming Product Launch

Hi everyone,

I want to share an update regarding the upcoming product launch. During final integration testing, our team identified several issues that require additional development and QA time. To ensure a stable and reliable release, we are adjusting the launch date by two weeks. The new target launch date is [Insert Date].

Our teams are actively working through the issues, and we have implemented a focused mitigation plan to keep the schedule tight. I will provide the next status update by [Insert Date] or sooner if we complete key milestones ahead of plan.

Thank you for your understanding and support. Please feel free to reach out with any questions.

Best regards,

[Your Name]"""
}

# Intermediate data for frameworks that need it
INTERMEDIATE_DATA = {
    FRAMEWORK_SELF_CONSISTENCY: {
        "samples": [
            "I can do a high-level review of the executive summary and key recommendations Monday morning at 7 AM, which would give you feedback before the 9 AM meeting. For a thorough review of the full document, I'd need until Tuesday. Which would be more valuable?",
            "I have personal commitments this weekend. Can you help me understand what specifically needs review? If there are 3-4 critical sections, I can prioritize those for early Monday. Otherwise, I can provide comprehensive feedback by Tuesday afternoon.",
            "I'm tied up this weekend, but I want to help. Could we schedule 30 minutes Monday at 7:30 AM to discuss the key points? That way you'd have real-time feedback before your meeting. Alternatively, is there someone else who could tag-team the review with me?"
        ],
        "num_samples": 3
    },
    FRAMEWORK_REFLECTION_REVISION: {
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
        
        "final_answer": FRAMEWORK_OUTPUTS[FRAMEWORK_REFLECTION_REVISION]
    }
}
