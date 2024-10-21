import streamlit as st
import os
from transformers import pipeline

BUID= 57631318
st.title("Homework 6 - GPT-2 Chatbot")

generator = pipeline('text-generation', model='gpt2')
tok_number = st.number_input("Number of tokens for this answer:", min_value=1, value=100, max_value=1000)
prompt = st.text_input("What is your sentence?")


### Generate the answer to the question "Damascus is a"
A1 = generator(prompt, max_length=tok_number, temperature = 1.0, num_return_sequences=1, truncation=True)
A2 = generator(prompt, max_length=tok_number, temperature = 0.3, num_return_sequences=1, truncation=True)



st.write("Text 1 (Creative)")
st.write(
    A1[0]['generated_text']
)

st.write("Text 2 (Predictable) ")
st.write(
    A2[0]['generated_text']
)



