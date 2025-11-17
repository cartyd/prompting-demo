# Presentation Guide

## Quick Start

### Starting the Demo

```bash
streamlit run app.py
```

The app opens in **Offline (Demo)** mode by default - perfect for presentations!

## Demo Flow (10-person audience)

### 1. Introduction (2 minutes)
- Open the app (already in offline mode)
- Explain: "We're going to compare 5 different prompting frameworks"
- Show the sidebar: "We can switch between frameworks instantly"

### 2. Framework Demonstrations (2-3 minutes each)

#### Chain of Thought - "Budget Cost Reduction"
1. Select "Chain of Thought" from dropdown
2. **Show prompts side-by-side:**
   - Left: Simple ad-hoc prompt (just the task)
   - Right: Framework prompt with step-by-step instructions
3. **Compare outputs:**
   - Ad-hoc: Simplistic, vague recommendations
   - Framework: Detailed analysis with calculations and justified plan
4. **Key point:** "Notice how the framework forces systematic thinking"

#### Tree of Thought - "Sprint Deadline Issues"
1. Select "Tree of Thought"
2. **Show prompts:**
   - Ad-hoc: Just the problem
   - Framework: Explores 3 different branches
3. **Compare outputs:**
   - Ad-hoc: Generic meeting advice
   - Framework: Multiple approaches evaluated, hybrid solution
4. **Key point:** "Tree of Thought explores alternatives before deciding"

#### Self-Consistency - "Urgent Friday Request"
1. Select "Self-Consistency"
2. **Show prompts:**
   - Ad-hoc: Just the scenario
   - Framework: Same prompt run multiple times
3. **Compare outputs:**
   - Ad-hoc: Weak boundaries, unclear
   - Framework: Professional response with multiple options
4. **Show intermediate reasoning:** Click tabs to show 3 samples
5. **Key point:** "Multiple reasoning paths catch edge cases and improve reliability"

#### Few-Shot - "Meeting Summary"
1. Select "Few-Shot"
2. **Show prompts:**
   - Ad-hoc: Just the task
   - Framework: Includes 2 example summaries
3. **Compare outputs:**
   - Ad-hoc: Vague, unprofessional format
   - Framework: Structured, actionable, professional
4. **Key point:** "Examples teach the model the exact style you want"

#### Reflection & Revision - "Performance Review"
1. Select "Reflection & Revision"
2. **Show prompts:**
   - Ad-hoc: Simple request
   - Framework: 3-step process (answer → critique → revise)
3. **Compare outputs:**
   - Ad-hoc: Generic, no metrics
   - Framework: Quantified impact, specific achievements
4. **Show intermediate reasoning:** Show initial answer, critique, final answer
5. **Key point:** "Self-critique dramatically improves quality"

### 3. Key Takeaways (1 minute)
- "Each framework has specific use cases"
- "All frameworks significantly outperform ad-hoc prompts"
- "Choose the right framework for your task"

### 4. Live Demo (Optional, 2 minutes)
- Switch to "Online (Live API)" mode
- Click "Load Sample Prompt" for any framework
- Show how you can customize prompts
- Click "Run Demo" to show live API call

## Tips for Success

### Preparation
- ✅ Test the app before your presentation
- ✅ Have the app already open and running
- ✅ Keep it in offline mode (no API issues during demo)
- ✅ Pre-select your starting framework

### During Presentation
- 👉 Use the sidebar framework dropdown to switch quickly
- 👉 Focus on the side-by-side prompt comparison first
- 👉 Then show the output comparison
- 👉 Emphasize the "why" - what makes each framework superior
- 👉 Keep moving - each framework demo should be 2-3 minutes max

### Handling Questions
**Q: "Do I need to write these prompts manually?"**
A: "No! Tools and libraries can generate these for you. This demo shows what happens under the hood."

**Q: "Which framework should I use?"**
A: "It depends on your task:" (refer to the comparison table in SAMPLE_PROMPTS.md)

**Q: "How much does this cost?"**
A: "Self-Consistency is most expensive (multiple API calls). Others are 1-3 calls. Chain of Thought is cheapest."

**Q: "Can I try this myself?"**
A: "Yes! Switch to Online mode and use your own prompts. All code is in the GitHub repo."

## Troubleshooting

### App won't start
```bash
# Install dependencies
pip install -r requirements.txt

# Run again
streamlit run app.py
```

### "Module not found" error
```bash
# Make sure you're in the project directory
cd /path/to/prompting-demo
streamlit run app.py
```

### Want to show live API calls but no API key
- Stay in offline mode - it's designed for presentations!
- Or set up API key before demo:
  ```bash
  cp .env.example .env
  # Edit .env and add your key
  ```

## Advanced: Custom Examples

To add your own examples to offline mode, edit `sample_data.py`:

1. Add task to `SAMPLE_TASKS` dict
2. Add ad-hoc output to `ADHOC_OUTPUTS` dict
3. Add framework output to `FRAMEWORK_OUTPUTS` dict
4. (Optional) Add intermediate data to `INTERMEDIATE_DATA` dict

Restart the app to see your changes.
