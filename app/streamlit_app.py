import streamlit as st
import openai
import os
from app_core import responder_pergunta

st.set_page_config(page_title="🌱 Atendimento - Flora Energia")

st.title("🌱 Agente de Atendimento - Flora Energia")
st.markdown("Este agente responde dúvidas com base em documentos oficiais da Flora Energia e site.")

openai.api_key = st.secrets["OPENAI_API_KEY"]

pergunta = st.chat_input("Digite sua pergunta sobre a Flora...")

if pergunta:
    with st.chat_message("user"):
        st.markdown(pergunta)
    with st.chat_message("assistant"):
        resposta = responder_pergunta(pergunta)
        st.markdown(resposta)