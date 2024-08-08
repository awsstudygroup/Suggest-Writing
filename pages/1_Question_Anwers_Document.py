import streamlit as st
import Libs as glib
from PyPDF2 import PdfReader

# Configure the page
st.set_page_config(
    page_title="Lecture Chatbot",
    page_icon=":books:",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main { 
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
        }
        .header {
            text-align: center;
            color: #4A90E2;
            font-size: 3em;
            font-weight: bold;
        }
        .subheader {
            text-align: center;
            color: #7F8C8D;
            font-size: 1.5em;
        }
        .footer {
            text-align: center;
            color: #95A5A6;
            font-size: 0.9em;
        }
        .button-container {
            display: flex;
            justify-content: center;
            gap: 10px;
            margin-top: 10px;
        }
        .stButton>button {
            color: white;
            background-color: #4A90E2;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 1em;
        }
        .file-uploader {
            margin-top: 20px;
        }
        .question-input {
            margin-top: 20px;
        }
        .sample-questions {
            margin-top: 20px;
            font-size: 1.2em;
        }
        .question-input input {
            border-radius: 5px;
            padding: 10px;
            width: 100%;
        }
    </style>
""", unsafe_allow_html=True)

# Header and Introduction
st.markdown("<div class='main'>", unsafe_allow_html=True)
st.markdown("<h1 class='header'>Lecture Chatbot</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Upload your lecture in PDF format and ask any questions!</p>", unsafe_allow_html=True)

# File uploader for PDF
uploaded_file = st.file_uploader("Upload Your Lecture in PDF", type="pdf", help="Please upload your lecture notes in PDF format.")

# Sample questions section
st.markdown("<div class='sample-questions'><strong>Sample Questions:</strong></div>", unsafe_allow_html=True)
st.markdown("<ul class='sample-questions'><li>Summarize the lecture</li><li>What are the main points of the lecture?</li><li>Explain the key concepts discussed</li></ul>", unsafe_allow_html=True)

# User question input
input_text = st.text_input("Your question:", placeholder="Type your question here...")

# Additional action buttons
st.markdown("""
    <div class="button-container">
        <button onclick="document.getElementById('input').value='Summarize the lecture'">Summarize</button>
        <button onclick="document.getElementById('input').value='What are the main points of the lecture?'">Main Points</button>
        <button onclick="document.getElementById('input').value='Explain the key concepts discussed'">Key Concepts</button>
    </div>
""", unsafe_allow_html=True)

# Process and display the result if a file is uploaded and a question is asked
docs = []
if uploaded_file and input_text:
    if st.button("Submit Question"):
        with st.spinner('Processing your request...'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                docs.append(page.extract_text())
            
            response = glib.query_document(input_text, docs)
            st.success('Here is the answer to your question:')
            st.write(response)

# Add footer
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<p class='footer'>Developed by AWS Vietnam team</p>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
