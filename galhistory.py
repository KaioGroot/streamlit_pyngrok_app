import json
import streamlit as st


#acessar dados do arquivo json e mostar com streamlit.
try:
  with open("historias.json") as f:
    historia = json.load(f)
    for i,hist in enumerate(historia):
      st.html(f"<span id='comandos' class='comandos' style='color:orange;text-shadow:1px 2px 3px orange'>------------------{i}</span>")
      #st.markdown("---")
      st.write(historia[i]["historia"],i)
      st.markdown("---")
st.html('<script>alert("ioo")</script>')
except FileNotFoundError:
  st.error("Ocorreu um erro, arquivo não encontrado: ", FileNotFoundError)
