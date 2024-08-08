import streamlit as st
from PyPDF2 import PdfReader
import Libs as glib

# Page configuration
st.set_page_config(page_title="Create Questions from Lecture/Paper", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
        color: #333333;
        font-family: 'Helvetica', sans-serif;
    }
    .stButton button {
        background-color: #007bff;
        color: white;
        border: none;
        padding: 10px 24px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .stFileUploader label {
        font-size: 18px;
        font-weight: bold;
        color: #007bff;
    }
    .stInfo {
        font-size: 18px;
        font-weight: bold;
        color: #007bff;
    }
    .stSuccess {
        font-size: 18px;
        font-weight: bold;
        color: #28a745;
    }
    .stError {
        font-size: 18px;
        font-weight: bold;
        color: #dc3545;
    }
    .header {
        background-color: #007bff;
        padding: 20px;
        text-align: center;
        color: white;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    .footer {
        background-color: #007bff;
        padding: 10px;
        text-align: center;
        color: white;
        border-radius: 5px;
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
    }
    .sidebar .sidebar-content {
        padding: 10px;
        background-color: #f8f9fa;
        border-right: 1px solid #ddd;
    }
    .sidebar .sidebar-content .menu-item {
        font-size: 16px;
        font-weight: bold;
        color: #333;
        padding: 10px;
        border-bottom: 1px solid #ddd;
        transition: background-color 0.3s ease;
    }
    .sidebar .sidebar-content .menu-item:hover {
        background-color: #e9ecef;
    }
    .response {
        white-space: pre-line;
        font-size: 16px;
    }
    </style>
    """, unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><h2>Create Multiple Choice Questions from Lecture/Paper</h2></div>', unsafe_allow_html=True)
st.markdown("Upload your lecture to create multiple choice questions!")

# Sidebar
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    menu_items = ["Dashboard", "Virtual Classrooms", "Manage Courses", "File Library", "Quizzes", 
                  "Questions", "Results", "Polls", "Attendance", "My Groups", "Messages", 
                  "Account & Settings", "Orders"]
    for item in menu_items:
        st.markdown(f'<div class="menu-item">{item}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# File uploader
uploaded_file = st.file_uploader("Upload Lecture/Paper in PDF", type="pdf")

# Process and display PDF content
if uploaded_file is not None:
    # Display upload success message
    st.markdown('<div class="stInfo">File {} uploaded successfully!</div>'.format(uploaded_file.name), unsafe_allow_html=True)

    # Read PDF content
    reader = PdfReader(uploaded_file)
    docs = [page.extract_text() for page in reader.pages]

    # Call function to create questions
    response = glib.create_questions(docs)

    # Filter None values and convert generator to string
    response_text = ''.join([str(item) for item in response if item is not None])

    # Display result
    if response_text:
        st.markdown('<div class="stSuccess">Questions created successfully!</div>', unsafe_allow_html=True)
        st.markdown('<div class="response">{}</div>'.format(response_text.replace('\n', '<br>')), unsafe_allow_html=True)
    else:
        st.markdown('<div class="stError">Failed to create questions. Please try again.</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">© 2024 AWS Quiz System. All rights reserved.</div>', unsafe_allow_html=True)
