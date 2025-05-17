# 🕵️ AI Crime Scene Investigator - GPT-3.5 Turbo

An interactive Streamlit app powered by OpenAI's GPT-3.5 and LangGraph to decode crime scene reports.  
This tool simulates the investigative process — extracting clues, building timelines, identifying suspects, and deducing conclusions from user-provided crime reports.

---

## 🚀 Features

- 🔍 **Extracts Key Clues** from a crime scene report
- 🕒 **Builds Event Timelines** using AI
- 🧑‍💼 **Profiles Possible Suspects** based on clues and timeline
- 🎯 **Provides Logical Conclusion** pointing to the likely guilty party
- 🖥️ **Streamlit UI** for simple interaction
- 🔗 **LangGraph workflow** ensures structured flow

---

## 🛠️ Tech Stack

| Technology    | Purpose                          |
|---------------|----------------------------------|
| **Python 3.8+**     | Programming Language              |
| **Streamlit**       | Web UI for user interaction       |
| **LangGraph**       | Orchestrating stateful workflows  |
| **LangChain**       | Prompt templating and LLM access  |
| **OpenAI API**      | GPT-3.5 for reasoning and outputs |
| **dotenv**          | Secure API key management         |

---

## 🧪 How It Works

The system follows a step-by-step reasoning process:

1. **Clue Extraction** → From the input report  
2. **Timeline Generation** → From extracted clues  
3. **Suspect Profiling** → Based on clues & timeline  
4. **Final Reasoning** → Based on all above stages

Each step is handled by a node in a LangGraph-powered state machine.

---

## ⚙️ Installation & Setup

1. **Clone this repo**
   ```bash
   git clone https://github.com/your-username/ai-crime-scene-investigator.git
   cd ai-crime-scene-investigator

Thank you...
