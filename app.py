import streamlit as st

st.title("Обичаш ли Python?")

otgovor = st.radio(
    "Обичаш ли Python?",
    ["да", "не"]
)

if otgovor == "да":
    st.write("Супер!")
else:
    st.write("Ще го харесаш!")
