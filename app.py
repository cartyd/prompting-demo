"""
AI Prompt Framework Demo - Streamlit Application

This application demonstrates different AI prompting frameworks and compares
their outputs side-by-side with ad-hoc prompts.

Supports two modes:
- Offline: Pre-loaded sample data for demonstration without API calls
- Online: Live API calls to OpenAI with your custom prompts
"""

import streamlit as st
from openai import OpenAI
from typing import List, Dict, Any, Tuple, Optional
import os
from collections import Counter
from dotenv import load_dotenv
import sample_data

# Load environment variables from .env file
load_dotenv()


# Initialize OpenAI client
@st.cache_resource
def get_openai_client():
    """Initialize and cache the OpenAI client."""
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        st.error("OPENAI_API_KEY environment variable not set")
        st.stop()
    return OpenAI(api_key=api_key)


def call_llm(client: OpenAI, prompt: str, model: str, temperature: float = 0.7) -> str:
    """
    Call the OpenAI API with the given prompt.
    
    Args:
        client: OpenAI client instance
        prompt: The prompt to send
        model: Model identifier
        temperature: Sampling temperature
        
    Returns:
        The LLM response text
    """
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM: {str(e)}"


def build_adhoc_prompt(task: str) -> str:
    """
    Build a simple ad-hoc prompt from the task.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Ad-hoc prompt string
    """
    return task


def build_chain_of_thought_prompt(task: str) -> str:
    """
    Build a Chain of Thought prompt.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Chain of Thought enhanced prompt
    """
    return f"""{task}

Let's think step by step to solve this problem:

1. First, identify the key components and requirements
2. Then, break down the problem into smaller parts
3. Analyze each part carefully
4. Finally, synthesize the information to reach a conclusion

Please provide your reasoning for each step."""


def build_tree_of_thought_prompt(task: str) -> str:
    """
    Build a Tree of Thought prompt that explores multiple reasoning paths.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Tree of Thought enhanced prompt
    """
    return f"""{task}

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


def build_self_consistency_prompt(task: str) -> str:
    """
    Build a Self-Consistency prompt (will be called multiple times).
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Prompt designed for self-consistency sampling
    """
    return f"""{task}

Please provide your reasoning and answer to this problem. Think through it carefully and explain your thought process."""


def build_few_shot_prompt(task: str) -> str:
    """
    Build a Few-Shot prompt with example demonstrations.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Few-shot enhanced prompt with examples
    """
    return f"""Here are some examples of how to approach similar problems:

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


def build_reflection_revision_prompt_initial(task: str) -> str:
    """
    Build the initial prompt for Reflection & Revision framework.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Initial prompt
    """
    return f"""{task}

Please provide your answer to this problem."""


def build_reflection_revision_prompt_critique(task: str, initial_answer: str) -> str:
    """
    Build the critique prompt for Reflection & Revision framework.
    
    Args:
        task: Original task
        initial_answer: The first answer from the LLM
        
    Returns:
        Critique prompt
    """
    return f"""Original task: {task}

Here was my initial answer:
{initial_answer}

Now, critically analyze this answer:
- What are the strengths of this answer?
- What are the weaknesses or potential errors?
- What might be missing or incomplete?
- How could this answer be improved?

Provide a detailed critique."""


def build_reflection_revision_prompt_revision(task: str, initial_answer: str, critique: str) -> str:
    """
    Build the revision prompt for Reflection & Revision framework.
    
    Args:
        task: Original task
        initial_answer: The first answer
        critique: The critique of the first answer
        
    Returns:
        Revision prompt
    """
    return f"""Original task: {task}

Initial answer:
{initial_answer}

Critique of the initial answer:
{critique}

Based on this critique, provide an improved, revised answer that addresses the identified weaknesses and incorporates the suggested improvements."""


def run_adhoc_approach(client: OpenAI, task: str, model: str, temperature: float) -> Tuple[str, str]:
    """
    Run the ad-hoc approach.
    
    Returns:
        Tuple of (prompt, output)
    """
    prompt = build_adhoc_prompt(task)
    output = call_llm(client, prompt, model, temperature)
    return prompt, output


def run_chain_of_thought(client: OpenAI, task: str, model: str, temperature: float) -> Tuple[str, str]:
    """
    Run the Chain of Thought framework.
    
    Returns:
        Tuple of (prompt, output)
    """
    prompt = build_chain_of_thought_prompt(task)
    output = call_llm(client, prompt, model, temperature)
    return prompt, output


def run_tree_of_thought(client: OpenAI, task: str, model: str, temperature: float) -> Tuple[str, str]:
    """
    Run the Tree of Thought framework.
    
    Returns:
        Tuple of (prompt, output)
    """
    prompt = build_tree_of_thought_prompt(task)
    output = call_llm(client, prompt, model, temperature)
    return prompt, output


def run_self_consistency(client: OpenAI, task: str, model: str, temperature: float, num_samples: int) -> Tuple[str, str, Dict[str, Any]]:
    """
    Run the Self-Consistency framework with multiple samples.
    
    Returns:
        Tuple of (prompt, final_output, intermediate_data)
    """
    prompt = build_self_consistency_prompt(task)
    samples = []
    
    for i in range(num_samples):
        output = call_llm(client, prompt, model, temperature)
        samples.append(output)
    
    # Aggregate results - use the first sample as representative
    # In a real implementation, you might extract and vote on key conclusions
    vote_prompt = f"""Here are {num_samples} different attempts at solving the same problem:

{chr(10).join([f"Attempt {i+1}:{chr(10)}{sample}{chr(10)}" for i, sample in enumerate(samples)])}

Analyze these attempts and:
1. Identify the most common or consistent conclusions
2. Evaluate which reasoning is most sound
3. Synthesize the best elements from all attempts into a final answer

Provide the final synthesized answer."""
    
    final_output = call_llm(client, vote_prompt, model, 0.3)
    
    intermediate_data = {
        "samples": samples,
        "num_samples": num_samples
    }
    
    return prompt, final_output, intermediate_data


def run_few_shot(client: OpenAI, task: str, model: str, temperature: float) -> Tuple[str, str]:
    """
    Run the Few-Shot framework.
    
    Returns:
        Tuple of (prompt, output)
    """
    prompt = build_few_shot_prompt(task)
    output = call_llm(client, prompt, model, temperature)
    return prompt, output


def run_reflection_revision(client: OpenAI, task: str, model: str, temperature: float) -> Tuple[str, str, Dict[str, Any]]:
    """
    Run the Reflection & Revision framework.
    
    Returns:
        Tuple of (prompt, final_output, intermediate_data)
    """
    # Step 1: Initial answer
    initial_prompt = build_reflection_revision_prompt_initial(task)
    initial_answer = call_llm(client, initial_prompt, model, temperature)
    
    # Step 2: Critique
    critique_prompt = build_reflection_revision_prompt_critique(task, initial_answer)
    critique = call_llm(client, critique_prompt, model, temperature)
    
    # Step 3: Revision
    revision_prompt = build_reflection_revision_prompt_revision(task, initial_answer, critique)
    final_answer = call_llm(client, revision_prompt, model, temperature)
    
    # Combine all prompts for display
    full_prompt = f"""Step 1 - Initial Answer Prompt:
{initial_prompt}

Step 2 - Critique Prompt:
{critique_prompt}

Step 3 - Revision Prompt:
{revision_prompt}"""
    
    intermediate_data = {
        "initial_answer": initial_answer,
        "critique": critique,
        "final_answer": final_answer
    }
    
    return full_prompt, final_answer, intermediate_data


def main():
    """Main Streamlit application."""
    st.set_page_config(page_title="AI Prompt Framework Demo", layout="wide")

    # Initialize session state for mode and input
    if 'mode' not in st.session_state:
        st.session_state.mode = 'offline'  # start in offline mode by default
    if 'adhoc_prompt_input' not in st.session_state:
        st.session_state.adhoc_prompt_input = ""

    # Header
    st.title("🧠 AI Prompt Framework Demo")
    st.markdown("""
    Compare how different prompting frameworks transform prompts and affect LLM outputs.
    """)

    # Sidebar controls
    st.sidebar.header("⚙️ Configuration")

    # Mode toggle
    mode = st.sidebar.radio(
        "Mode",
        ["Offline (Demo)", "Online (Live API)"],
        index=0 if st.session_state.mode == 'offline' else 1,
        help="Offline mode uses pre-loaded examples. Online mode calls OpenAI API."
    )
    st.session_state.mode = 'offline' if 'Offline' in mode else 'online'

    framework = st.sidebar.selectbox(
        "Framework",
        ["Chain of Thought", "Tree of Thought", "Self-Consistency", "Few-Shot", "Reflection & Revision"]
    )

    # Online mode settings
    if st.session_state.mode == 'online':
        st.sidebar.markdown("---")
        st.sidebar.subheader("Online Mode Settings")

        model = st.sidebar.selectbox(
            "Model",
            ["gpt-4o", "gpt-4o-mini", "gpt-4-turbo", "gpt-3.5-turbo"],
            index=1
        )

        temperature = st.sidebar.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1
        )

        num_samples = st.sidebar.number_input(
            "Number of Samples (Self-Consistency only)",
            min_value=2,
            max_value=10,
            value=3,
            step=1
        )

        load_sample_button = st.sidebar.button("📋 Load Sample Prompt", use_container_width=True)
        if load_sample_button:
            st.session_state.adhoc_prompt_input = sample_data.SAMPLE_TASKS[framework]
    else:
        # Defaults for offline (not used for API calls)
        model = "gpt-4o-mini"
        temperature = 0.7
        num_samples = 3

    # Prompts side-by-side
    st.markdown("---")
    st.subheader("📝 Prompts")
    colp1, colp2 = st.columns(2)

    if st.session_state.mode == 'offline':
        # Offline mode: pre-load sample task and framework prompt; no editing, no API
        task = sample_data.SAMPLE_TASKS[framework]
        adhoc_prompt = task
        framework_prompt = build_framework_prompt(framework, task)

        with colp1:
            st.markdown("### 📄 Ad-Hoc Prompt")
            st.code(adhoc_prompt, language=None)
        with colp2:
            st.markdown(f"### 🎯 {framework} Prompt")
            st.code(framework_prompt, language=None)

        # Immediately show outputs using pre-loaded data
        st.markdown("---")
        st.subheader("📊 Outputs Comparison")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 💬 Ad-Hoc Output")
            st.info(sample_data.ADHOC_OUTPUTS[framework])
        with col2:
            st.markdown(f"### ✨ {framework} Output")
            st.success(sample_data.FRAMEWORK_OUTPUTS[framework])

            # Intermediate data if applicable
            intermediate = sample_data.INTERMEDIATE_DATA.get(framework)
            if intermediate:
                st.markdown("### 🔍 Intermediate Reasoning")
                if framework == "Self-Consistency":
                    tabs = st.tabs([f"Sample {i+1}" for i in range(intermediate["num_samples"])])
                    for i, tab in enumerate(tabs):
                        with tab:
                            st.write(intermediate["samples"][i])
                elif framework == "Reflection & Revision":
                    tab1, tab2, tab3 = st.tabs(["Initial Answer", "Critique", "Final Answer"])
                    with tab1:
                        st.write(intermediate["initial_answer"])
                    with tab2:
                        st.write(intermediate["critique"])
                    with tab3:
                        st.write(intermediate["final_answer"])

    else:
        # Online mode: editable ad-hoc prompt, auto-generated framework prompt preview
        with colp1:
            st.markdown("### 📄 Ad-Hoc Prompt")
            st.session_state.adhoc_prompt_input = st.text_area(
                label="Ad-Hoc Prompt",
                value=st.session_state.adhoc_prompt_input,
                height=150,
                label_visibility="collapsed",
                key="adhoc_prompt_input_widget",
            )
        with colp2:
            st.markdown(f"### 🎯 {framework} Prompt")
            preview = build_framework_prompt(framework, st.session_state.adhoc_prompt_input) if st.session_state.adhoc_prompt_input.strip() else ""
            st.text_area(
                label=f"{framework} Prompt",
                value=preview,
                height=150,
                disabled=True,
                label_visibility="collapsed",
                key="framework_prompt_preview_widget",
            )

        # Run Demo button and results
        run_button = st.sidebar.button("🚀 Run Demo", type="primary", use_container_width=True)
        if run_button:
            task = st.session_state.adhoc_prompt_input
            if not task.strip():
                st.warning("Please enter a task or problem statement.")
                return

            # Call API and display results
            client = get_openai_client()

            with st.spinner("Running ad-hoc approach..."):
                adhoc_prompt, adhoc_output = run_adhoc_approach(client, task, model, temperature)

            with st.spinner(f"Running {framework} framework..."):
                if framework == "Chain of Thought":
                    framework_prompt, framework_output = run_chain_of_thought(client, task, model, temperature)
                    intermediate = None
                elif framework == "Tree of Thought":
                    framework_prompt, framework_output = run_tree_of_thought(client, task, model, temperature)
                    intermediate = None
                elif framework == "Self-Consistency":
                    framework_prompt, framework_output, intermediate = run_self_consistency(
                        client, task, model, temperature, num_samples
                    )
                elif framework == "Few-Shot":
                    framework_prompt, framework_output = run_few_shot(client, task, model, temperature)
                    intermediate = None
                elif framework == "Reflection & Revision":
                    framework_prompt, framework_output, intermediate = run_reflection_revision(
                        client, task, model, temperature
                    )
                else:
                    st.error(f"Unknown framework: {framework}")
                    return

            # Display outputs side by side
            st.markdown("---")
            st.subheader("📊 Outputs Comparison")
            col1, col2 = st.columns(2)
            with col1:
                st.markdown("### 💬 Ad-Hoc Output")
                st.info(adhoc_output)
            with col2:
                st.markdown(f"### ✨ {framework} Output")
                st.success(framework_output)

                if intermediate:
                    st.markdown("### 🔍 Intermediate Reasoning")
                    if framework == "Self-Consistency":
                        tabs = st.tabs([f"Sample {i+1}" for i in range(intermediate["num_samples"])])
                        for i, tab in enumerate(tabs):
                            with tab:
                                st.write(intermediate["samples"][i])
                    elif framework == "Reflection & Revision":
                        tab1, tab2, tab3 = st.tabs(["Initial Answer", "Critique", "Final Answer"])
                        with tab1:
                            st.write(intermediate["initial_answer"])
                        with tab2:
                            st.write(intermediate["critique"])
                        with tab3:
                            st.write(intermediate["final_answer"])


def build_framework_prompt(framework: str, task: str) -> str:
    """Build the appropriate framework prompt based on the selected framework."""
    if framework == "Chain of Thought":
        return build_chain_of_thought_prompt(task)
    elif framework == "Tree of Thought":
        return build_tree_of_thought_prompt(task)
    elif framework == "Self-Consistency":
        return build_self_consistency_prompt(task)
    elif framework == "Few-Shot":
        return build_few_shot_prompt(task)
    elif framework == "Reflection & Revision":
        initial = build_reflection_revision_prompt_initial(task)
        critique = "(After receiving initial answer, critique it for weaknesses)"
        revision = "(Based on critique, provide improved answer)"
        return f"""Step 1 - Initial Answer Prompt:
{initial}

Step 2 - Critique Prompt:
{critique}

Step 3 - Revision Prompt:
{revision}"""
    return task


if __name__ == "__main__":
    main()
