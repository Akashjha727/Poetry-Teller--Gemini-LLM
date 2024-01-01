# Poetry-Teller--Gemini-LLM
 **Here's a README for the code, but please fill in the placeholders with the appropriate information:**

**# Interactive Poetry Teller**

**## Overview**

This repository contains the code for an interactive poetry generation app built using Streamlit and Google AI's Gemini text-generation model. The app allows users to create custom poems by:

- Choosing a verse structure (couplet, quatrain, or free verse).
- Providing a starting verse.
- Guiding the poem's direction through tone and imagery choices.
- Saving the generated poem as a text file.

**## Key Features**

- **Interactive poem generation:** Users can collaborate with the AI to create unique poems.
- **Verse structure options:** Supports different verse formats for poetic diversity.
- **Tone and imagery choices:** Users can influence the poem's mood and style.
- **Poem saving:** Generated poems can be saved for future reference or sharing.

**## Getting Started**

**Prerequisites:**

- Python 3.10 & above
- A Google Cloud Platform account with a valid API key for the Google AI Generative Language service

**Installation:**

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repository-name>.git
   ```
2. Create a virtual environment (recommended) and activate it.
3. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project directory and add your Google API key:
   ```
   GOOGLE_API_KEY=<your-api-key>
   ```

**Running the App:**

1. Navigate to the project directory in your terminal.
2. Run the following command:
   ```bash
   streamlit run app.py
   ```
3. Access the app in your web browser at the provided local URL.

**## Image**
<img width="642" alt="Screenshot" src="https://github.com/Akashjha727/Poetry-Teller--Gemini-LLM/assets/143934503/f2b2993e-1213-4e10-a6a6-59aa6797aee0">


**## Usage**

1. Follow the prompts in the app to provide a topic, verse structure, and initial verse.
2. Choose the desired tone for the poem.
3. Click the "Generate Next Verse" button to continue building the poem.
4. Optionally, save the poem as a text file using the "Copy Poem to Clipboard" button.

**## Contributing**

We welcome contributions! Please see the `CONTRIBUTING.md` file for more information.

**## Contact**

For questions or feedback, please reach out to jhaaakash727@gmail.com.
