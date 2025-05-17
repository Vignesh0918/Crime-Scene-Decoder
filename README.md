CRIME-SCENE-DECODER

---

🕵️ AI Crime Scene Investigator (LangGraph + GPT-3.5)

This is a Streamlit-based web app that uses LangGraph, LangChain, and OpenAI's GPT-3.5 Turbo to analyze crime scene reports and generate:

Key clues

Detailed timelines

Suspect profiles

Final conclusions



---

Features

LLM-powered step-by-step crime investigation

Modular graph architecture using LangGraph

Interactive web UI with Streamlit

Detects and visualizes:

Key clues

Event timeline

Suspect profiles

Logical conclusion




---

How It Works

1. User inputs a crime report into the app.


2. The system processes it in 4 LangGraph steps:

Clue Extraction

Timeline Building

Suspect Profiling

Final Reasoning



3. Each step uses OpenAI GPT-3.5 Turbo to reason over the information.


4. Output is displayed in a user-friendly format.




---

Tech Stack

LangGraph

LangChain

OpenAI GPT-3.5 Turbo

Streamlit

Python 3.9+



---

Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/ai-crime-investigator.git
cd ai-crime-investigator

2. Install Dependencies

Use a virtual environment (recommended):

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

3. Set up Environment Variable

Create a .env file in the project root with your OpenAI key:

OPENAI_API_KEY=your_openai_api_key_here

4. Run the App

streamlit run app.py


---

File Structure

.
├── app.py             # Main app file
├── .env               # Contains your OpenAI API key
├── requirements.txt   # Project dependencies
└── README.md          # This documentation


---

Example Report

A woman was found unconscious in her apartment. The front door was unlocked. Neighbors reported hearing shouting around 9 PM. Her phone was missing, and a broken vase was found near the sofa.

Sample Output:

Clues: Unlocked door, shouting at 9 PM, broken vase, missing phone

Timeline: Events from 8:30 PM to 9:30 PM reconstructed

Suspects: Neighbors, ex-partner, recent visitors

Conclusion: Most likely suspect with justification



---

Screenshot

(Insert a screenshot of the app running with sample input and output here)


---

License

MIT License


---

Future Improvements

PDF upload for crime reports

Visualization of the timeline

Integration with real-world case datasets



---

Let me know if you also want:

requirements.txt

GitHub badges

Deployment instructions (Streamlit Cloud / Docker)
