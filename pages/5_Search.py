import streamlit as st
import Libs as glib
from langchain.callbacks import StreamlitCallbackHandler

# Cấu hình trang
st.set_page_config(page_title="EduChatBot", page_icon="📚", layout="wide")

# Tạo style cho trang
st.markdown("""
    <style>
        .main {
            background-color: #f5f5f5;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 24px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
            border-radius: 12px;
        }
        .stTextInput input {
            padding: 10px;
            width: 100%;
            box-sizing: border-box;
        }
    </style>
""", unsafe_allow_html=True)

# Tiêu đề trang
st.title("EduChatBot: Tìm kiếm cơ sở tri thức")
st.markdown("### Chatbot hệ thống giáo dục")

# Thêm các nút submit với câu hỏi mẫu
st.markdown("#### Một số câu hỏi gợi ý:")
col1, col2 = st.columns(2)

with col1:
    if st.button("Một số bệnh phổ biến của trẻ em là gì?"):
        input_text = "Một số bệnh phổ biến của trẻ em là gì?"
        st.session_state.input_text = input_text

    if st.button("Tóm tắt tài chính Apple?"):
        input_text = "Tóm tắt tài chính Apple?"
        st.session_state.input_text = input_text

with col2:
    if st.button("Những phương pháp học tập hiệu quả?"):
        input_text = "Những phương pháp học tập hiệu quả?"
        st.session_state.input_text = input_text

    if st.button("Các trường đại học hàng đầu thế giới?"):
        input_text = "Các trường đại học hàng đầu thế giới?"
        st.session_state.input_text = input_text

# Ô nhập liệu
st.markdown("#### Hoặc nhập câu hỏi của bạn:")
input_text = st.text_input("Nhập câu hỏi của bạn ở đây...", value=st.session_state.get('input_text', ''))

# Xử lý tìm kiếm và hiển thị kết quả
if input_text:
    st_callback = StreamlitCallbackHandler(st.container())
    response = glib.search(input_text, st_callback)
    st.write(f"### Kết quả cho câu hỏi: {input_text}")
    st.write(response["result"])
    st.json(response)
