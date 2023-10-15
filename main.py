import streamlit as st

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")

with col2:
    st.title("Mithul Ashokkumar")

    content = """Hi, I am Mithul Ashokkumar! I am a sophomore in high school in the US. I was born in India, 
    and my family moved to the US when I was just 1 year old. My passion is to work at IT, specifically at Apple or 
    Google. Otherwise, I might work at NASA. I love science and computer science. I like to play the piano and travel 
    all around the world."""

    st.info(content)