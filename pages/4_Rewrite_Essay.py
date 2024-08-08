import streamlit as st
import Libs as glib

st.set_page_config(page_title="Educational Chatbot", layout="centered", initial_sidebar_state="auto")

# Custom CSS for better UI design
st.markdown("""
    <style>
    body {
        background-color: #eaeff5;
    }
    .main {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 800px;
        margin: auto;
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        transition-duration: 0.4s;
        cursor: pointer;
        border-radius: 10px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    }
    .stButton > button:hover {
        background-color: #45a049;
    }
    .stTextInput textarea {
        border-radius: 10px;
        padding: 10px;
        border: 1px solid #ccc;
        box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.1);
    }
    .stTextInput {
        padding: 10px;
        margin-bottom: 10px;
    }
    .stMarkdown p {
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Educational Chatbot")
st.subheader("Rewrite Your Essay")

input_text = st.text_area("Input your whole or part of your essay", height=200)

if st.button("Submit"):
    if input_text:
        with st.spinner("Rewriting your essay..."):
            response = glib.rewrite_document(input_text)
        st.success("Here is your rewritten essay:")
        st.write(response)
    else:
        st.warning("Please enter some text before submitting.")

if st.button("Clear"):
    st.text_area("Input your whole or part of your essay", value="", key="clear")

st.sidebar.title("Educational Chatbot")
st.sidebar.info("Use this chatbot to rewrite your essays for better clarity and grammar. Simply input your text and click submit.")
