import streamlit as st
from openai import OpenAI
import os
import random
import numpy as np
import transformers
from transformers import set_seed
from transformers import pipeline

BUID= 57631318


# Set a seed for the built-in Python random module
random.seed(BUID)
# Set a seed for NumPy
np.random.seed(BUID)
# Set a seed for HuggingFace
set_seed(BUID)


### Create a GPT2 generator pipeline
generator = pipeline('text-generation', model='gpt2')

### Generate the answer to the question "Damascus is a"
generator("Damascus is a", max_length=20, num_return_sequences=10, truncation=True)

### Print all 10 completions:
for i in range(10):
  st.write(response.choices[i].message.content)

