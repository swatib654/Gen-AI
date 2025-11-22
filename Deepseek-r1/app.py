import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

st.title("NareshIT Bot using DeepSeek-R1")

# Prompt template
template = """Question: {question}

Answer: Let's think step by step.
"""
prompt = ChatPromptTemplate.from_template(template)

# Correct model class (from langchain-ollama)
model = OllamaLLM(model="deepseek-r1")

# Build chain
chain = prompt | model

# Streamlit input box
question = st.text_input("Enter your question here")

# Generate answer
if question:
    try:
        response = chain.invoke({"question": question})
        st.write(response)
    except Exception as e:
        st.error(f"Error: {e}")
