import streamlit as st
import Libs as glib

# Thiết lập cấu hình trang
st.set_page_config(page_title="Improve Writing an Essay", page_icon="✍️", layout="centered")

# CSS tùy chỉnh cho giao diện đẹp hơn
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        .title {
            color: #4a90e2;
            text-align: center;
            font-weight: bold;
        }
        .subheader {
            text-align: center;
            font-style: italic;
            color: #6c757d;
        }
        .instructions {
            color: #333;
            margin-bottom: 20px;
            font-size: 1.1em;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            color: #6c757d;
        }
        .submit-button {
            background-color: #4a90e2;
            color: white;
            border: none;
            padding: 10px 20px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            border-radius: 12px;
            cursor: pointer;
        }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề và giới thiệu
st.markdown('<h1 class="title">📝 Improve Your Essay Writing</h1>', unsafe_allow_html=True)
st.markdown('<h3 class="subheader">An AI-powered tool to help you enhance your essay writing skills.</h3>', unsafe_allow_html=True)
st.markdown("""
<div class="instructions">
    Welcome to our educational chatbot designed to assist you in improving your essay writing.
    Simply input your essay or a part of it, and get suggestions to enhance your writing.
</div>
""", unsafe_allow_html=True)

# Phân cách để tách các phần của giao diện
st.markdown("---")

# Nhập văn bản bài luận
input_text = st.text_area("Input your whole or part of your essay:", height=250)

# Phân cách
st.markdown("---")

# Nút để gửi bài luận và nhận phản hồi
if st.button("Get Suggestions", key="submit-button"):
    if input_text:
        response = glib.suggest_writing_document(input_text)
        st.markdown("### Suggestions")
        st.write(response)
    else:
        st.warning("Please input your essay text to get suggestions.")

# Footer
st.markdown("---")
st.markdown('<div class="footer">© 2024 Educational Chatbot. All rights reserved.</div>', unsafe_allow_html=True)
