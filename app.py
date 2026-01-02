import streamlit as st
from config.config import APP_CONFIG

st.set_page_config(
    page_title=APP_CONFIG['name'],
    layout='centered',
    initial_sidebar_state='collapsed'
)

st.title(f'{APP_CONFIG["name"]}')
st.markdown(f'**Version:** {APP_CONFIG["version"]}')
st.markdown('---')

st.write('AI Chatbot tạo lộ trình học tập cá nhân hoá')

if st.session_state.get('debug', False):
    st.write('**Debug Info:**')
    st.json(APP_CONFIG)