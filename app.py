
import json
import streamlit as st
import google.generativeai as genai
import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
import pyrebase
import requests
from bs4 import BeautifulSoup
import time
# Configurar a API key do Gemini
genai.configure(api_key='AIzaSyD6x77PZgrrQVcag8v6t13yMw5jvMJMjVY')

#adicionar firebase

config = {
  "apiKey": "AIzaSyC5sVDH7Y-DQiphWDJy3-7jvy2I3IiT1i4",
  "authDomain": "primeiro-projeto-c4aa8.firebaseapp.com",
  "databaseURL":"https://primeiro-projeto-c4aa8-default-rtdb.firebaseio.com",
  "projectId": "primeiro-projeto-c4aa8",
  "storageBucket": "primeiro-projeto-c4aa8.appspot.com",
  "messagingSenderId": "739705657694",
  "appId": "1:739705657694:web:189dacfa741a30f013d7cf",
  "measurementId": "G-27NHSWDRRZ"
};

firebase = pyrebase.initialize_app(config)
#storage = firebase.storage()
database = firebase.database()
auth = firebase.auth()




logado = False;

if 'logado' not in st.session_state:
 st.session_state['logado'] = False


st.set_page_config(
    page_title="VercelAi",
    page_icon=":fire",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
#adicionar botão de temas claro e escuro

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)

remote_css(f"https://unpkg.com/blocks.css/dist/blocks.min.css") 



st.html("<button class='block accent'>VERCEL AI</button>")
def login_page():
  st.sidebar.title('Login')
  #pg.run()
  username = st.sidebar.text_input('Username')
  password = st.sidebar.text_input('Password', type='password')
  create_page = st.Page("sobre.py", title="Início", icon=":material/help:")
  cadastro = st.Page("cadastro.py", title="Cadastro", icon=":material/help:")
  delete_page = st.Page("delete.py", title="criar", icon=":material/create:")
  copy = st.Page("copyright.py", title="Gerador de copy", icon=":material/book:")
  gerado = st.Page("gerado.py", title="Gerado", icon=":material/book:")
  apis = st.Page("apis.py", title="Assistente ia", icon=":material/help:")
  noticias = st.Page("noticias.py", title="Noticias", icon=":material/help:")
  historiasGeradas = st.Page("galhistory.py", title="Historias Geradas", icon=":material/help:")

  #st.sidebar.markdown('---')

  pg = st.navigation([create_page,cadastro, delete_page,gerado,copy,apis,noticias,historiasGeradas])
  #st.set_page_config(page_title="Vencel", page_icon=":material/edit:")
  pg.run()

  if st.sidebar.button('Login'):
    try:
      user = auth.sign_in_with_email_and_password(username, password)
      id_token = user['idToken']
      st.write(id_token)
      verification = auth.send_email_verification(id_token)
      st.write(verification)
      st.session_state['logado'] = True
      st.sidebar.success('Logged in as {}'.format(username))
    except:
     st.error("deu um erro")

  return True


try:
 with open('historias.json', 'r',encoding='utf-8') as f:
   historinha = json.load(f)
except FileNotFoundError:
   historinha = []

# Função para gerar histórias com o Gemini
def gerar_historia_gemini(historia_base):
    prompt = f"Melhore esta história: {historia_base}, com base nos dados só melhora ela, gere com sua própria criatividade!, sem perguntas."
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(prompt)
    return response.text




def gerar_historia_input():
    st.title('Gerar versão input')
    historia_base = st.text_input('Digite a história base:')
    if st.button('Gerar História'):
        historia_melhorada = gerar_historia_gemini(historia_base)
        historinha.append({"historia":historia_melhorada})
        with open('historias.json', 'w') as f:
          json.dump(historinha,f,indent=2)
          st.write("ADICIONADo")
        st.write(historia_melhorada)
        st.balloons()

# Interface principal do gerador de histórias
def gerador_de_historias():
    st.title('Gerador de Histórias com Gemini')
    # Opções de personagens, lugares e eventos
    personagens = ['um cavaleiro', 'um dragão', 'uma princesa', 'um pirata', 'um mago']
    lugares = ['no castelo', 'na floresta', 'no navio', 'no deserto', 'na estação espacial']
    eventos = ['encontrou um tesouro', 'salvou o reino', 'lutou contra monstros', 'descobriu um segredo', 'se perdeu em uma ilha']

    # Formulário de seleção de história
    with st.form("form_historia"):
        personagem = st.selectbox('Escolha um personagem:', personagens)
        lugar = st.selectbox('Escolha um lugar:', lugares)
        evento = st.selectbox('Escolha um evento:', eventos)
        st.write('História base:')
        st.write(f"{personagem} {lugar} {evento}")
        submit_button = st.form_submit_button("Gerar História")
    if submit_button:
          historia_usuario = f"{personagem} {lugar} {evento}"
          historia_melhorada = gerar_historia_gemini(historia_usuario)
          historinha.append({"historia":historia_melhorada})
          with open('historias.json', 'w') as f:
            json.dump(historinha,f,indent=2)
          st.write(historia_melhorada)
          st.balloons()

# Função principal
def main():
  if st.session_state['logado']==True:
    login_page()
    gerar_historia_input()
    gerador_de_historias()
  else:
    login_page()

if __name__ == '__main__':
    main()
