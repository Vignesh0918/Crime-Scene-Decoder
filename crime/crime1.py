from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langgraph.graph import StateGraph, END
from typing import TypedDict, Optional
from dotenv import load_dotenv
import os
import streamlit as st

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    st.error("OPENAI_API_KEY not found in environment variables. Please set it in .env file.")
    st.stop()

class CrimeState(TypedDict):
    input: str
    clues: Optional[str]
    timeline: Optional[str]
    suspects: Optional[str]
    conclusion: Optional[str]

def extract_clues(state: CrimeState) -> CrimeState:
    input_text = state["input"]
    prompt = PromptTemplate.from_template("Given this report:\n{report}\n\nList key clues.")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    result = llm.invoke(prompt.format_prompt(report=input_text).to_messages())
    return {**state, "clues": result.content}

def build_timeline(state: CrimeState) -> CrimeState:
    prompt = PromptTemplate.from_template("Using these clues:\n{clues}\n\nCreate a detailed timeline of events.")
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    result = llm.invoke(prompt.format_prompt(clues=state["clues"]).to_messages())
    return {**state, "timeline": result.content}

def profile_suspects(state: CrimeState) -> CrimeState:
    prompt = PromptTemplate.from_template(
        "Based on the clues:\n{clues}\nAnd timeline:\n{timeline}\n\nList possible suspects with brief reasons."
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    result = llm.invoke(prompt.format_prompt(clues=state["clues"], timeline=state["timeline"]).to_messages())
    return {**state, "suspects": result.content}

def final_reasoning(state: CrimeState) -> CrimeState:
    prompt = PromptTemplate.from_template(
        "Given the suspects:\n{suspects}\n\nBased on the clues and timeline, who is most likely guilty? "
        "Provide a clear conclusion with reasons why."
    )
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    result = llm.invoke(prompt.format_prompt(suspects=state["suspects"]).to_messages())
    return {**state, "conclusion": result.content}

builder = StateGraph(CrimeState)

builder.add_node("ClueExtractor", extract_clues)
builder.add_node("TimelineBuilder", build_timeline)
builder.add_node("SuspectProfiler", profile_suspects)
builder.add_node("ReasoningAgent", final_reasoning)

builder.set_entry_point("ClueExtractor")
builder.add_edge("ClueExtractor", "TimelineBuilder")
builder.add_edge("TimelineBuilder", "SuspectProfiler")
builder.add_edge("SuspectProfiler", "ReasoningAgent")
builder.add_edge("ReasoningAgent", END)

graph = builder.compile()

st.title("🕵️ AI Crime Scene Investigator - GPT-3.5 Turbo")

user_input = st.text_area("Enter crime scene report:", height=200)

if st.button("Analyze Report"):
    if user_input.strip() == "":
        st.warning("Please enter a report.")
    else:
        with st.spinner("Analyzing report..."):
            initial_state: CrimeState = {"input": user_input}
            try:
                result = graph.invoke(initial_state)
                st.subheader("🔍 Clues:")
                st.write(result.get("clues", "No clues found."))

                st.subheader("🕒 Timeline:")
                st.write(result.get("timeline", "No timeline generated."))

                st.subheader("🕵️ Suspects:")
                st.write(result.get("suspects", "No suspects identified."))

                st.subheader("✅ Final Conclusion:")
                st.success(result.get("conclusion", "No conclusion drawn."))

            except Exception as e:
                st.error(f"Error during processing: {e}")
