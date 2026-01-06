import streamlit as st
import requests

st.title("醫療問答 RAG UI")

question = st.text_input("請輸入問題：")

if st.button("送出"):
    res = requests.post("http://127.0.0.1:8080/ask", json={"question": question})
    st.write(res.json()["answer"])
    if "sources" in res.json():
        st.write("來源文件：", res.json()["sources"])
