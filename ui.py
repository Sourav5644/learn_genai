import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create LLM
llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation"
)

# Wrap in Chat interface
model = ChatHuggingFace(llm=llm)

# Streamlit UI
st.header('Research Tool')

user_input = st.text_input('Enter your prompt')

if st.button('Summarize'):
    if user_input.strip():
        result = model.invoke(user_input)
        st.write(result.content)
    else:
        st.warning("Please enter a prompt first.")
