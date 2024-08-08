import streamlit as st
from PyPDF2 import PdfReader
import Libs as glib

# Cấu hình trang
st.set_page_config(page_title="Summary a Lecture/Paper", page_icon=":books:", layout="wide")

# Tiêu đề và mô tả trang
st.title("Educational Chatbot :books:")
st.markdown("""
    <style>
        .title {
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #4CAF50;
        }
        .subtitle {
            text-align: center;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            color: #777777;
        }
        .upload-box {
            border: 2px dashed #4CAF50;
            padding: 20px;
            border-radius: 10px;
        }
        .response-box {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
        }
    </style>
    <h1 class="title">Summarize Your Lecture or Paper</h1>
    <p class="subtitle">Upload a PDF document and get a summarized version using our AI-powered chatbot.</p>
""", unsafe_allow_html=True)

# Khu vực tải lên tệp PDF
st.markdown('<div class="upload-box">', unsafe_allow_html=True)
uploaded_file = st.file_uploader("Upload Lecture/Paper in PDF", type="pdf")
st.markdown('</div>', unsafe_allow_html=True)

docs = []

# Nếu có tệp được tải lên
if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        docs.append(page.extract_text())
    
    # Hiển thị tiến trình xử lý
    with st.spinner('Processing your document...'):
        response = glib.summary_stream(docs)
    
    # Hiển thị kết quả tóm tắt
    st.markdown('<div class="response-box">', unsafe_allow_html=True)
    st.write(response)
    st.markdown('</div>', unsafe_allow_html=True)
else:
    st.info("Please upload a PDF document to get started.")
