import streamlit as st

st.set_page_config(page_title="For You ❤️", page_icon="🌹", layout="centered")

# Title
st.title("Hi Love! 💖")

# Image
st.image("srishti.jpeg", caption="You are beautiful 😘", use_column_width=True)

# Message
st.markdown("""
### Just wanted to say...
You light up my world like nobody else ✨  
Your smile, your kindness, and your love mean everything to me.  
**I'm lucky to have you. ❤️**

""")

# Button
if st.button("Click me 💌"):
    st.success("I love you more every day 💕")
