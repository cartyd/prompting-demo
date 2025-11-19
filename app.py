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
from typing import Dict, Any, Optional
import os
from dotenv import load_dotenv
import sample_data
import streamlit.components.v1 as components
from constants import (
    FRAMEWORK_CHAIN_OF_THOUGHT,
    FRAMEWORK_TREE_OF_THOUGHT,
    FRAMEWORK_SELF_CONSISTENCY,
    FRAMEWORK_FEW_SHOT,
    FRAMEWORK_REFLECTION_REVISION,
    ALL_FRAMEWORKS,
    TEXTAREA_RESIZE_INTERVAL_MS,
    AVAILABLE_MODELS
)
import prompt_templates as templates

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
        
    Raises:
        ValueError: If prompt is empty or None
    """
    # Input validation
    if not prompt or not prompt.strip():
        raise ValueError("Prompt cannot be empty")
    
    if not model:
        raise ValueError("Model must be specified")
    
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error calling LLM: {str(e)}"




def build_chain_of_thought_prompt(task: str) -> str:
    """
    Build a Chain of Thought prompt.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Chain of Thought enhanced prompt
    """
    return f"{task}{templates.CHAIN_OF_THOUGHT_INSTRUCTIONS}"


def build_tree_of_thought_prompt(task: str) -> str:
    """
    Build a Tree of Thought prompt that explores multiple reasoning paths.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Tree of Thought enhanced prompt
    """
    return f"{task}{templates.TREE_OF_THOUGHT_INSTRUCTIONS}"


def build_self_consistency_prompt(task: str) -> str:
    """
    Build a Self-Consistency prompt (will be called multiple times).
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Prompt designed for self-consistency sampling
    """
    return f"{task}{templates.SELF_CONSISTENCY_INSTRUCTIONS}"


def build_few_shot_prompt(task: str) -> str:
    """
    Build a Few-Shot prompt with example demonstrations.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Few-shot enhanced prompt with examples
    """
    return templates.FEW_SHOT_EXAMPLES.format(task=task)


def build_reflection_revision_prompt_initial(task: str) -> str:
    """
    Build the initial prompt for Reflection & Revision framework.
    
    Args:
        task: User's task or problem statement
        
    Returns:
        Initial prompt
    """
    return f"{task}{templates.REFLECTION_REVISION_INITIAL}"


def build_reflection_revision_prompt_critique(task: str, initial_answer: str) -> str:
    """
    Build the critique prompt for Reflection & Revision framework.
    
    Args:
        task: Original task
        initial_answer: The first answer from the LLM
        
    Returns:
        Critique prompt
    """
    return templates.REFLECTION_REVISION_CRITIQUE.format(task=task, initial_answer=initial_answer)


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
    return templates.REFLECTION_REVISION_REVISION.format(
        task=task, 
        initial_answer=initial_answer, 
        critique=critique
    )


# Simple functions to access sample data - no class needed

def get_sample_task(framework: str) -> str:
    """Get sample task for a framework.
    
    Args:
        framework: Framework name
        
    Returns:
        Sample task string
        
    Raises:
        ValueError: If framework not found
    """
    if framework not in sample_data.SAMPLE_TASKS:
        raise ValueError(f"No sample task found for framework: {framework}")
    return sample_data.SAMPLE_TASKS[framework]


def get_adhoc_output(framework: str) -> str:
    """Get adhoc output for a framework.
    
    Args:
        framework: Framework name
        
    Returns:
        Adhoc output string
        
    Raises:
        ValueError: If framework not found
    """
    if framework not in sample_data.ADHOC_OUTPUTS:
        raise ValueError(f"No adhoc output found for framework: {framework}")
    return sample_data.ADHOC_OUTPUTS[framework]


def get_framework_output(framework: str) -> str:
    """Get framework output for a framework.
    
    Args:
        framework: Framework name
        
    Returns:
        Framework output string
        
    Raises:
        ValueError: If framework not found
    """
    if framework not in sample_data.FRAMEWORK_OUTPUTS:
        raise ValueError(f"No framework output found for framework: {framework}")
    return sample_data.FRAMEWORK_OUTPUTS[framework]


def get_intermediate_data(framework: str) -> Optional[Dict[str, Any]]:
    """Get intermediate data for a framework if it exists.
    
    Args:
        framework: Framework name
        
    Returns:
        Intermediate data dict or None if not available
    """
    return sample_data.INTERMEDIATE_DATA.get(framework)


def get_framework_prompt(framework: str) -> str:
    """Get the framework-enhanced prompt for a framework.
    
    Args:
        framework: Framework name
        
    Returns:
        Framework prompt string
        
    Raises:
        ValueError: If framework not found
    """
    if framework not in sample_data.FRAMEWORK_PROMPTS:
        raise ValueError(f"No framework prompt found for framework: {framework}")
    return sample_data.FRAMEWORK_PROMPTS[framework]


def setup_page_config():
    """Configure page settings and inject custom CSS/JavaScript."""
    st.set_page_config(page_title="AI Prompt Framework Demo", layout="wide")
    
    # Custom CSS to double the font size for output text
    st.markdown("""
    <style>
    /* Double the font size for info and success boxes */
    .stAlert p, .stAlert div {
        font-size: 2rem !important;
        line-height: 1.6 !important;
    }
    /* Double the font size for code blocks (prompts) */
    .stCodeBlock code, .stCodeBlock pre {
        font-size: 2rem !important;
        line-height: 1.6 !important;
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
    }
    /* Double the font size for text areas (online mode prompts) */
    .stTextArea textarea {
        font-size: 2rem !important;
        line-height: 1.6 !important;
        resize: none !important;
        overflow: hidden !important;
        min-height: 100px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # JavaScript for auto-resizing text areas
    components.html(f"""
    <script>
    function autoResizeTextareas() {{
        const textareas = parent.document.querySelectorAll('.stTextArea textarea');
        textareas.forEach(textarea => {{
            textarea.style.height = 'auto';
            textarea.style.height = textarea.scrollHeight + 'px';
            
            textarea.removeEventListener('input', autoResizeOnInput);
            textarea.addEventListener('input', autoResizeOnInput);
        }});
    }}
    
    function autoResizeOnInput(e) {{
        e.target.style.height = 'auto';
        e.target.style.height = e.target.scrollHeight + 'px';
    }}
    
    autoResizeTextareas();
    setInterval(autoResizeTextareas, {TEXTAREA_RESIZE_INTERVAL_MS});
    </script>
    """, height=0)


def initialize_session_state():
    """Initialize all session state variables with default values."""
    defaults = {
        'mode': 'offline',
        'adhoc_prompt_input': '',
        'framework_prompt_input': '',
        'previous_framework': None,
        'show_clear_dialog': False
    }
    
    for key, default_value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = default_value


def render_sidebar(framework: str) -> tuple:
    """Render sidebar controls and return selected settings.
    
    Returns:
        Tuple of (model, temperature)
    """
    st.sidebar.header("⚙️ Configuration")
    
    if st.session_state.mode == 'online':
        # Show clear dialog if framework changed
        if st.session_state.show_clear_dialog:
            st.sidebar.markdown("---")
            st.sidebar.warning("Framework changed. Clear prompts?")
            col1, col2 = st.sidebar.columns(2)
            with col1:
                if st.button("Yes", key="clear_yes", use_container_width=True):
                    st.session_state.adhoc_prompt_input = ""
                    st.session_state.framework_prompt_input = ""
                    st.session_state.show_clear_dialog = False
                    st.rerun()
            with col2:
                if st.button("No", key="clear_no", use_container_width=True):
                    st.session_state.show_clear_dialog = False
                    st.rerun()
        
        st.sidebar.markdown("---")
        st.sidebar.subheader("Online Mode Settings")
        
        model = st.sidebar.selectbox(
            "Model",
            AVAILABLE_MODELS,
            index=2
        )
        
        temperature = st.sidebar.slider(
            "Temperature",
            min_value=0.0,
            max_value=2.0,
            value=0.7,
            step=0.1
        )
        
        load_sample_button = st.sidebar.button("📋 Load Sample Prompt", use_container_width=True)
        if load_sample_button:
            try:
                sample_task = get_sample_task(framework)
                st.session_state.adhoc_prompt_input = sample_task
                st.session_state.framework_prompt_input = build_framework_prompt(framework, sample_task)
            except ValueError as e:
                st.error(str(e))
        
        clear_button = st.sidebar.button("🗑️ Clear All Text", use_container_width=True)
        if clear_button:
            st.session_state.adhoc_prompt_input = ""
            st.session_state.framework_prompt_input = ""
    else:
        # Defaults for offline mode
        model = "gpt-4o-mini"
        temperature = 0.7
    
    return model, temperature


def render_intermediate_data(intermediate: Dict[str, Any], framework: str):
    """Render intermediate reasoning data for applicable frameworks."""
    if not intermediate:
        return
    
    st.markdown("### 🔍 Intermediate Reasoning")
    if framework == FRAMEWORK_SELF_CONSISTENCY:
        tabs = st.tabs([f"Sample {i+1}" for i in range(intermediate["num_samples"])])
        for i, tab in enumerate(tabs):
            with tab:
                st.write(intermediate["samples"][i])
    elif framework == FRAMEWORK_REFLECTION_REVISION:
        tab1, tab2, tab3 = st.tabs(["Initial Answer", "Critique", "Final Answer"])
        with tab1:
            st.write(intermediate["initial_answer"])
        with tab2:
            st.write(intermediate["critique"])
        with tab3:
            st.write(intermediate["final_answer"])


def render_offline_mode(framework: str):
    """Render offline mode with pre-loaded sample data."""
    try:
        # Get sample data
        task = get_sample_task(framework)
        adhoc_prompt = task
        framework_prompt = get_framework_prompt(framework)
        
        # Display prompts
        st.markdown("---")
        st.subheader("📝 Prompts")
        colp1, colp2 = st.columns(2)
        
        with colp1:
            st.markdown("### 📄 Basic Prompt")
            st.code(adhoc_prompt, language=None)
        with colp2:
            st.markdown(f"### 🎯 {framework} Prompt")
            st.code(framework_prompt, language=None)
        
        # Display outputs
        st.markdown("---")
        st.subheader("📊 Outputs Comparison")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 💬 Basic Output")
            st.info(get_adhoc_output(framework))
        with col2:
            st.markdown(f"### ✨ {framework} Output")
            st.success(get_framework_output(framework))
            
            # Intermediate data if applicable
            intermediate = get_intermediate_data(framework)
            render_intermediate_data(intermediate, framework)
    except ValueError as e:
        st.error(f"Error loading sample data: {str(e)}")
    except Exception as e:
        st.error(f"Unexpected error in offline mode: {str(e)}")


def render_online_mode(framework: str, model: str, temperature: float):
    """Render online mode with editable prompts and API calls."""
    # Display prompts
    st.markdown("---")
    st.subheader("📝 Prompts")
    colp1, colp2 = st.columns(2)
    
    with colp1:
        st.markdown("### 📄 Basic Prompt")
        st.session_state.adhoc_prompt_input = st.text_area(
            label="Basic Prompt",
            value=st.session_state.adhoc_prompt_input,
            height=None,
            label_visibility="collapsed",
            key="adhoc_prompt_input_widget",
        )
    with colp2:
        st.markdown(f"### 🎯 {framework} Prompt")
        # Auto-generate framework prompt if framework prompt is empty
        if not st.session_state.framework_prompt_input and st.session_state.adhoc_prompt_input.strip():
            st.session_state.framework_prompt_input = build_framework_prompt(framework, st.session_state.adhoc_prompt_input)
        
        st.session_state.framework_prompt_input = st.text_area(
            label=f"{framework} Prompt",
            value=st.session_state.framework_prompt_input,
            height=None,
            label_visibility="collapsed",
            key="framework_prompt_input_widget",
        )
    
    # Run Demo button and results
    run_button = st.sidebar.button("🚀 Run Demo", type="primary", use_container_width=True)
    if run_button:
        task = st.session_state.adhoc_prompt_input
        framework_task = st.session_state.framework_prompt_input
        
        if not task.strip():
            st.warning("Please enter a Basic Prompt.")
            return
        
        if not framework_task.strip():
            st.warning("Please enter a Framework Prompt.")
            return
        
        # Call API and display results
        try:
            client = get_openai_client()
            
            with st.spinner("Running basic approach..."):
                adhoc_output = call_llm(client, task, model, temperature)
            
            with st.spinner(f"Running {framework} framework..."):
                framework_output = call_llm(client, framework_task, model, temperature)
                intermediate = None
            
            # Display outputs side by side
            st.markdown("---")
            st.subheader("📊 Outputs Comparison")
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### 💬 Basic Output")
                st.info(adhoc_output)
            with col2:
                st.markdown(f"### ✨ {framework} Output")
                st.success(framework_output)
                render_intermediate_data(intermediate, framework)
        except ValueError as e:
            st.error(f"Validation error: {str(e)}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")


def main():
    """Main Streamlit application."""
    setup_page_config()
    initialize_session_state()
    
    # Header
    st.title("🧠 AI Prompt Framework Demo")
    st.markdown("""
    Compare how different prompting frameworks transform prompts and affect LLM outputs.
    """)
    
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
        ALL_FRAMEWORKS
    )
    
    # Detect framework change in online mode
    if st.session_state.mode == 'online':
        if st.session_state.previous_framework is not None and st.session_state.previous_framework != framework:
            if st.session_state.adhoc_prompt_input or st.session_state.framework_prompt_input:
                st.session_state.show_clear_dialog = True
        st.session_state.previous_framework = framework
    
    # Render sidebar and get settings
    model, temperature = render_sidebar(framework)
    
    # Render appropriate mode
    if st.session_state.mode == 'offline':
        render_offline_mode(framework)
    else:
        render_online_mode(framework, model, temperature)


def build_framework_prompt(framework: str, task: str) -> str:
    """Build the appropriate framework prompt based on the selected framework.
    
    Args:
        framework: The framework name (use Framework constants)
        task: The user's task or problem statement
        
    Returns:
        Enhanced prompt with framework-specific instructions
        
    Raises:
        ValueError: If framework or task is empty/None
    """
    if not framework:
        raise ValueError("Framework must be specified")
    if not task or not task.strip():
        raise ValueError("Task cannot be empty")
    
    if framework == FRAMEWORK_CHAIN_OF_THOUGHT:
        return build_chain_of_thought_prompt(task)
    elif framework == FRAMEWORK_TREE_OF_THOUGHT:
        return build_tree_of_thought_prompt(task)
    elif framework == FRAMEWORK_SELF_CONSISTENCY:
        return build_self_consistency_prompt(task)
    elif framework == FRAMEWORK_FEW_SHOT:
        return build_few_shot_prompt(task)
    elif framework == FRAMEWORK_REFLECTION_REVISION:
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
