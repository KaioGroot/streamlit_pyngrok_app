from google.generativeai.protos import Content,Part
import streamlit as st
import os
import google.generativeai as genai
import json

genai.configure(api_key='AIzaSyA2aCg6s9dr5PlNVaJZxnMzd6qYwSM0eM0')  # Substitua pela sua chave de API

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
st.write("vercel também cria CÓDIGOS!")


try:
  with open('prompt.json', 'r', encoding='utf-8') as f:
    history = json.load(f)
except FileNotFoundError:
  history = []

for msg in history:
    if msg["role"] == "user":
        st.chat_message("user").write(msg["parts"][0])  # Mensagem do usuário
    else:
        st.chat_message("assistant").write(msg["parts"][0])  # Mensagem da IA


model = genai.GenerativeModel(model_name="gemini-1.5-pro",generation_config=generation_config,)

chat_session = model.start_chat(history=history)

chat = st.chat_input("apenas diga o que fazer...")
if chat:
    with st.spinner("Aguarde..."):
      response = chat_session.send_message(chat)

    # Atualizar o histórico com as novas mensagens
    history.append({"role": "user", "parts":[chat],})  
    history.append({"role": "model", "parts":[response.text],})


    # Salva o histórico atualizado no arquivo
    with open("prompt.json", "w", encoding="utf-8") as f:
     json.dump(history, f, indent=2)
    for msg in history:
     if msg["role"] == "user":
        st.chat_message("user").write(msg["parts"][0])  # Mensagem do usuário
     else:
        st.chat_message("assistant").write(msg["parts"][0])  # Mensagem da IA
    #st.write(history)
