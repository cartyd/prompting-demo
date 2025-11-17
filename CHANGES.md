# Changes Summary

## New Features

### 1. Offline/Online Mode Toggle
- **Default:** Application starts in **Offline (Demo)** mode
- **Offline Mode:** Uses pre-loaded sample data for instant demonstration without API calls
- **Online Mode:** Makes live API calls to OpenAI with user's custom prompts

### 2. Side-by-Side Prompt Display
- Ad-hoc prompt and framework prompt are now displayed side-by-side at the top
- In offline mode: both prompts are shown as read-only code blocks
- In online mode: ad-hoc prompt is editable, framework prompt shows live preview

### 3. Pre-loaded Office Examples
- New `sample_data.py` module with curated office environment examples
- Each framework has a specific task, ad-hoc output, and framework output
- Examples demonstrate clear superiority of frameworks over ad-hoc prompts
- Includes intermediate reasoning data for Self-Consistency and Reflection & Revision

### 4. Improved User Experience
- Removed redundant "Enter Your Task or Problem" subheader
- Cleaner layout with prompts at top, outputs below
- "Load Sample Prompt" button in online mode to quickly load examples
- Framework prompt auto-updates as user types in online mode

## File Changes

### Modified Files
- `app.py`: Complete refactor to support dual modes, side-by-side layout, session state management
- `README.md`: Updated documentation for offline/online modes and usage instructions

### New Files
- `sample_data.py`: Pre-loaded sample tasks, outputs, and intermediate data for all frameworks
- `CHANGES.md`: This file documenting the changes

## Technical Details

### Session State
- `st.session_state.mode`: Tracks current mode ('offline' or 'online')
- `st.session_state.adhoc_prompt_input`: Stores user input in online mode

### No API Calls in Offline Mode
- Offline mode directly displays pre-loaded data from `sample_data.py`
- No OpenAI client initialization or API calls when in offline mode
- Perfect for demos, presentations, or environments without API access

### Framework Prompt Builder
- New `build_framework_prompt()` helper function
- Generates framework-specific prompts for any given task
- Used for live preview in online mode and display in offline mode

## Usage

### For Presentations (Offline Mode)
1. Launch app - it starts in offline mode automatically
2. Select different frameworks to compare
3. Show audience how prompts transform and outputs improve
4. No API key needed, no internet required (after initial load)

### For Experimentation (Online Mode)
1. Toggle to "Online (Live API)" mode
2. Enter custom prompts or load sample prompts
3. Run live API calls to test frameworks
4. Requires valid OPENAI_API_KEY in .env file
