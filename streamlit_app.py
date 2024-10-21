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

prompt = st.text_input("What is your prompt today?")

# Set a seed for the built-in Python random module
random.seed(BUID)
# Set a seed for NumPy
np.random.seed(BUID)
# Set a seed for HuggingFace
set_seed(BUID)


### Create a GPT2 generator pipeline
generator = pipeline(task='text-generation', model='gpt2')

### Generate the answer to the question "Damascus is a"
generator(prompt, max_length=20, num_return_sequences=10, truncation=True)

### Print all 10 completions:
for i in range(10):
  st.write(response.choices[i].message.content)


# Load model directly
