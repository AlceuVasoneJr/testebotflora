
import streamlit as st
from app_core import responder_pergunta

st.set_page_config(page_title="Agente de Atendimento - Flora Energia")
st.markdown("# 🤖 Agente de Atendimento - Flora Energia")
st.markdown("Este agente responde dúvidas simuladas de clientes da Flora com base no FAQ oficial.")

pergunta = st.chat_input("Digite a pergunta do cliente...")

if pergunta:
    resposta = responder_pergunta(pergunta)
    st.chat_message("user").markdown(pergunta)
    st.chat_message("assistant").markdown(resposta)
