import streamlit as st
import google.generativeai as genai
import re
import json
import os


genai.configure(api_key='AIzaSyD6x77PZgrrQVcag8v6t13yMw5jvMJMjVY')  # Substitua pela sua chave de API

conversa = "Você é uma ai que vai falar sobre o vercel, tipo, 'seja bem-vindo(a) ao vercel!' que é um site que ajuda criar histórias com ia e que em breve vai ajudar em tarbalhos online, e uma coisa, deixe bem decorato e bonito, com emojis. e uma NOVIDADE!!!, FOI ADICIONADO AO VERCEL UMA ASSISTENTE DE AI!"

def falar_sobre(prompt):
   model = genai.GenerativeModel("gemini-1.5-flash")
   response = model.generate_content(prompt)
   return response.text


def gerado_pelo_gemini():
   historia_melhorada = falar_sobre(conversa)
   st.write(historia_melhorada)


gerado_pelo_gemini()

