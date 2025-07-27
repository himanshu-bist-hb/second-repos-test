import streamlit as st
import pandas as pd
import numpy as np

# Title
st.title("My First Streamlit App")

# Description
st.write("This is a simple web app using Streamlit!")

# Text Input
name = st.text_input("Enter your name:", "Himanshu")
st.write(f"Hello, {name}! 👋")

# Slider
number = st.slider("Pick a number", 1, 100)
st.write(f"You selected: {number}")
