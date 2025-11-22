from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import OllamaLLM

# Prompt template
template = """Question: {question}

Answer: Let's think step by step.
"""

prompt = ChatPromptTemplate.from_template(template)

# NEW correct model class
model = OllamaLLM(model="deepseek-r1")

# Create chain
chain = prompt | model

# Input from user
question = input("Enter your question here: ")

if question:
    try:
        response = chain.invoke({"question": question})
        print("\nResponse:\n", response)
    except Exception as e:
        print("Error:", e)
