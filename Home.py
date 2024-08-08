import streamlit as st
import Libs as glib

# Cấu hình trang
st.set_page_config(page_title="Educational Chatbot", layout="wide")

# CSS tùy chỉnh cho giao diện
st.markdown("""
<style>
    .main {
        background-color: #f5f5f5;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput, .stButton {
        width: 100%;
        margin-bottom: 10px;
    }
    .st-chat-message {
        padding: 10px;
        margin-bottom: 10px;
        border-radius: 10px;
    }
    .st-chat-message.user {
        background-color: #d1e7dd;
        text-align: left;
        border: 1px solid #bcd0c7;
    }
    .st-chat-message.bot {
        background-color: #f8d7da;
        text-align: right;
        border: 1px solid #f5c2c7;
    }
    .title {
        font-size: 3em;
        color: #4CAF50;
        text-align: center;
        margin-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2em;
        color: #333;
        margin-bottom: 20px;
    }
    .examples {
        margin-bottom: 20px;
    }
    .examples ul {
        list-style-type: none;
        padding: 0;
    }
    .examples li {
        margin: 5px 0;
        padding: 10px;
        background: #fff;
        border-radius: 5px;
        border: 1px solid #ddd;
    }
    .footer {
        text-align: center;
        font-size: 0.8em;
        color: #aaa;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Tiêu đề và mô tả trang
st.markdown('<div class="title">Educational Chatbot</div>', unsafe_allow_html=True)
st.markdown('<div class="description">Ask me anything related to educational topics!</div>', unsafe_allow_html=True)

# Các ví dụ gợi ý
st.markdown("""
<div class="examples">
    <p>Here are some examples to get you started:</p>
    <ul>
        <li>Top 10 interview questions for OOP in Java</li>
        <li>Write a recursive function.</li>
        <li>Phân biệt giữa classification và object detection trong computer vision.</li>
        <li>Thuật toán nào được dùng để xây dựng hệ thống recommendation.</li>
    </ul>
</div>
""", unsafe_allow_html=True)

# Khung nhập liệu của người dùng
input_text = st.text_input("Type your question here", placeholder="Enter your question...")

# Xử lý khi có câu hỏi từ người dùng
if input_text:
    with st.chat_message("user"):
        st.markdown(f"**You:** {input_text}")
    
    response_placeholder = st.empty()

    response_stream = glib.call_claude_sonet_stream(input_text)
    
    response = ""
    for chunk in response_stream:
        if chunk:
            response += chunk
            response_placeholder.markdown(f"**Bot:** {response}")

    with st.chat_message("bot"):
        st.markdown(f"**Bot:** {response}")

# Footer
st.markdown('<div class="footer">Developed by AWS Vietnam Team. Powered by Streamlit and Claude Sonet.</div>', unsafe_allow_html=True)
