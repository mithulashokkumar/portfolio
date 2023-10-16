import streamlit as st
import pandas

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

content2 = """
Below you can find some of the apps I have built using Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
