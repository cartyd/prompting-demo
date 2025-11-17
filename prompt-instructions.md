

# ✅ **AI PROMPT FRAMEWORK DEMO**

**BEGIN PROMPT**

You are an expert Python developer and Streamlit application architect.
Your task is to generate a complete Streamlit application in Python that demonstrates and compares different AI prompting frameworks.

### **APPLICATION PURPOSE**

Create an interactive demo app that lets a presenter show, side-by-side, how different prompting frameworks change the prompt and change the LLM's output.

The audience will be about ten people watching a live demo.

---

# **APPLICATION REQUIREMENTS**

### **1. Main Functionality**

The app must:

* Accept a user-entered **task or problem statement**.

* Generate an **ad-hoc prompt** version and call the LLM with it.

* Generate a **framework-enhanced prompt** using ONE of the following frameworks (selectable in a dropdown):

  * Tree of Thought
  * Self-Consistency
  * Chain of Thought
  * Few-Shot
  * Reflection & Revision

* For the chosen framework:

  * Build the transformed prompt.
  * Call the LLM with that framework prompt.
  * Display the output.

### **2. UI Layout Requirements**

Use Streamlit and organize the app like this:

#### **Sidebar**

* Model selection dropdown (e.g., gpt-4.1, gpt-4o-mini, etc.)
* Framework selection dropdown
* Temperature slider
* Number of samples (only used for Self-Consistency)
* "Run Demo" button

#### **Main Area**

1. Header + description of what the app does.
2. Text area for user to input the task/problem.
3. After running:

   * Two side-by-side columns using `st.columns(2)`:

     * **Left Column: Ad-Hoc Prompt**

       * Show the ad-hoc prompt text
       * Show the LLM output
     * **Right Column: Framework Prompt**

       * Show the generated framework prompt
       * Show the framework output
       * If applicable, show intermediate reasoning steps (e.g., for Tree of Thought or Self-Consistency).

---

# **3. Framework Behavior Requirements**

### **Chain of Thought**

* Add explicit “let’s think step-by-step” reasoning instructions.

### **Tree of Thought**

* Generate at least 3 reasoning branches.
* Ask the LLM to evaluate branches.
* Ask the LLM to pick the best branch.

### **Self-Consistency**

* Run N samples with high temperature.
* Perform “majority vote” or reasoning-based selection.
* Display:

  * all samples
  * selected final result

### **Few-Shot**

* Include at least 2 example input/output pairs.

### **Reflection & Revision**

* Step 1: Ask LLM for first answer.
* Step 2: Ask LLM to critique the answer.
* Step 3: Ask LLM to rewrite an improved answer.

Displayed as:

* First answer
* Critique
* Final improved answer

---

# **4. Code Requirements**

The generated code should:

* Be complete and runnable as a single file: `app.py`
* Use the official OpenAI Python client
* Be modular:

  * separate prompt-building logic into helper functions
  * separate LLM call handling
* Contain docstrings and clean explanations so the presenter can modify it
* Contain no pseudocode — *only fully working code*
* Use `st.spinner()` for loading indicators
* Use tab components where useful (e.g., for intermediate reasoning)
* Handle errors gracefully

---

# **5. Output Format**

Produce:

1. Full and complete Python code for `app.py`
2. Instructions for running the app locally:

   ```
   pip install streamlit openai
   streamlit run app.py
   ```

Do **not** add extra commentary.
Do **not** abbreviate the code.
Output everything needed to execute immediately.

**END PROMPT**


