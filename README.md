# AI Prompt Framework Demo

An interactive Streamlit application that demonstrates and compares different AI prompting frameworks side-by-side.

## Features

- **5 Prompting Frameworks:**
  - Chain of Thought
  - Tree of Thought
  - Self-Consistency
  - Few-Shot
  - Reflection & Revision

- **Two Modes:**
  - **Offline (Demo):** Pre-loaded office environment examples for instant demonstration without API calls
  - **Online (Live API):** Real-time API calls to OpenAI with your custom prompts

- **Side-by-side Comparison:** See prompts and outputs compared directly
- **Interactive Configuration:** Adjust model, temperature, and framework-specific parameters (online mode)
- **Intermediate Reasoning:** View detailed reasoning steps for applicable frameworks

## Quick Start

To run the app immediately in **offline mode** (no API key needed):

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open at `http://localhost:8501` with pre-loaded examples.

## Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key (only needed for online mode)

### Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the project root:
```bash
cp .env.example .env
```

3. Add your OpenAI API key to the `.env` file:
```
OPENAI_API_KEY=your-api-key-here
```

**Note:** The `.env` file is gitignored to prevent accidentally committing your API key.

## Running the App

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

## Usage

### Offline Mode (Default)

1. The app starts in **Offline (Demo)** mode
2. Select a framework from the sidebar
3. View the pre-loaded prompts side-by-side
4. See the comparison of ad-hoc vs. framework outputs instantly
5. Perfect for presentations without needing API access

### Online Mode

1. Switch to **Online (Live API)** mode in the sidebar
2. Enter your custom task in the ad-hoc prompt text area (or click "Load Sample Prompt")
3. The framework prompt updates automatically as you type
4. Select a model (e.g., gpt-4o-mini)
5. Adjust temperature and other parameters as needed
6. Click "Run Demo" to see live API results

## Framework Descriptions

### Chain of Thought
Adds explicit step-by-step reasoning instructions to guide the LLM through logical problem-solving.

### Tree of Thought
Explores multiple reasoning branches, evaluates them, and selects the best approach.

### Self-Consistency
Generates multiple independent solutions and synthesizes the most consistent answer.

### Few-Shot
Provides example demonstrations to guide the LLM's problem-solving approach.

### Reflection & Revision
Three-step process: initial answer → critique → improved revision.

## Architecture

The application is structured with:
- **Prompt builders:** Separate functions for each framework
- **LLM handlers:** Centralized API calling with error handling
- **Runner functions:** Framework-specific execution logic
- **Streamlit UI:** Responsive layout with side-by-side comparison

## License

MIT
