import streamlit as st

st.set_page_config(page_title="For You ❤️", page_icon="🌹", layout="centered")

# Title
st.title("Hello ! 💖")


# Message
st.markdown("""
### Just wanted to say...
You are the most beautiful girl in the world ✨  
Your smile, your kindness, and your intelligence everything is so good.  
**I'm lucky to be a friend of the purest soul ❤️**

""")

# Button
if st.button("Click me 💌"):
    st.success("You are the prettiest girl 💕")
