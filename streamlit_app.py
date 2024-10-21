import streamlit as st
import os
import random
import numpy as np
from transformers import pipeline

BUID= 57631318

generator = pipeline('text-generation', model='gpt2')
tok_number = st.number_input("Number of tokens for this answer:", min_value=1, value=100, max_value=1000)
prompt = st.text_input("What is your prompt today?")


### Generate the answer to the question "Damascus is a"
generator(prompt, max_length=tok_number, num_return_sequences=10, truncation=True)

# Set a seed for the built-in Python random module
random.seed(BUID)
# Set a seed for NumPy
np.random.seed(BUID)
# Set a seed for HuggingFace
set_seed(BUID)


st.title("Homework 6 - GPT-2 Chatbot")





