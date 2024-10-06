import requests
from bs4 import BeautifulSoup
import streamlit as st

url = 'https://www.bbc.com/portuguese'

#fazer requisição e verificar se deu certo
resposta = requests.get(url)
resposta.raise_for_status()

sopa = BeautifulSoup(resposta.text, 'html.parser')
noticias = sopa.findAll("h3")
imagens = sopa.findAll("img")

history = []
for l in imagens:
 history.append(l)
 #st.html(f"{l}")

indice = 0
for i in noticias:
  indice += 1
  #st.write(indice)
  if i.text != '':
    print(i.text)
    st.write(i.text)
    st.html(f"{history[indice]}")
    if i.a:
      st.write(f"---Link da Noticia:{i.a['href']}\n\n")
    if i.img:
      st.write(f"---imagem {i.a['img']} ")
  else:
    st.write('não tem texto')
