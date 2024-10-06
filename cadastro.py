from pyasn1.type.univ import Null
import streamlit as st
import json
from firebase_admin import credentials
from firebase_admin import storage
from firebase_admin import db
import pyrebase
import time


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
database = firebase.database()
auth  = firebase.auth()
darFetch = database.child().get()

lista = []

for i,item in enumerate(darFetch):
  lista.append(item.val())
  

with st.form("meuform"):
  st.title("Seja Bem-vindo(a)!")
  st.subheader("crie sua conta agora mesmo, fácil e rápido!")
  email = st.text_input("preencha seu email")
  senha = st.text_input("sua senha", type='password')
  confirmSenha = st.text_input("confirme sua senha", type="password")
  button = st.form_submit_button("Cadastrar")
  if button:
    for i,iten in enumerate(lista):
       if email == iten['email']:
        st.error("email já existe!")
        time.sleep(2)
        st.rerun()
    if senha != confirmSenha or not senha or not confirmSenha :
     st.error("preencha os dados corretamente!")
    else:
      auth.create_custom_token()
      database.push({"email": email, "senha":senha})
      st.success(f"email: {email} cadastrado com sucesso")
      auth.create_user_with_email_and_password(email=email, password=senha)