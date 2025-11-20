"""
Prompt templates for different AI prompting frameworks.

This module contains the instruction templates that are appended to user tasks
to create framework-specific prompts.
"""


# Chain of Thought template
CHAIN_OF_THOUGHT_INSTRUCTIONS = """
Let's approach this step-by-step:

1. First, identify the key components and requirements
2. Break down the problem into manageable parts
3. Analyze each part systematically
4. Consider relationships and dependencies
5. Synthesize findings into a coherent solution

Provide your reasoning for each step."""


# Tree of Thought template
TREE_OF_THOUGHT_INSTRUCTIONS = """
Let's explore multiple approaches to this problem:

Branch 1: Consider the most direct approach
- What is the straightforward solution?
- What are its advantages?
- What are its limitations?

Branch 2: Consider an alternative creative approach
- What's a different way to think about this?
- What unique insights does this provide?
- What trade-offs does this involve?

Branch 3: Consider a hybrid or optimal approach
- Can we combine the best of both previous approaches?
- What would be the most comprehensive solution?
- What makes this approach superior?

Now, evaluate each branch:
- Which branch provides the most robust solution?
- Why is this branch preferable?
- What is your final recommended approach?

Provide your complete reasoning and final answer."""


# Self-Consistency template
SELF_CONSISTENCY_INSTRUCTIONS = """
Please provide your reasoning and answer to this problem. Think through it carefully and explain your thought process."""


# Few-Shot examples and template
FEW_SHOT_EXAMPLES = """Here are some examples of how to approach similar problems:

Example 1:
Task: Calculate the total cost if I buy 3 apples at $2 each and 2 oranges at $3 each.
Solution: Let me break this down:
- Apples: 3 × $2 = $6
- Oranges: 2 × $3 = $6
- Total: $6 + $6 = $12
Answer: The total cost is $12.

Example 2:
Task: If a train travels 120 miles in 2 hours, what is its average speed?
Solution: To find average speed, I need to divide distance by time:
- Distance: 120 miles
- Time: 2 hours
- Speed = Distance ÷ Time = 120 ÷ 2 = 60 miles per hour
Answer: The average speed is 60 mph.

Now, solve this problem using the same step-by-step approach:

Task: {task}

Solution:"""


# Reflection & Revision template
REFLECTION_REVISION_INITIAL = """
Please provide your answer to this problem."""
