import streamlit as st

st.title("Hello Azure 👋")
st.write("My first Python web app deployed to Azure!")

name = st.text_input("Enter your name")
if name:
    st.success(f"Welcome {name} 🎉")