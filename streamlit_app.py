import streamlit as st
from openai import OpenAI
import os
import random
import numpy as np
import transformers
from transformers import set_seed
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModelForCausalLM.from_pretrained("openai-community/gpt2")

BUID= 57631318



# Set a seed for the built-in Python random module
random.seed(BUID)
# Set a seed for NumPy
np.random.seed(BUID)
# Set a seed for HuggingFace
set_seed(BUID)


st.title("GPT-2 Chatbot")
st.write("This is a chatbot that uses GPT-2 model to generate answers.")

token_length = st.number_input("Number of tokens for this repsonse:", min_value=1, value=50)
prompt = st.text_input("What is your prompt today?")


