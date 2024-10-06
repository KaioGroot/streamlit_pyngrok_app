import streamlit as st
import google.generativeai as genai


genai.configure(api_key='AIzaSyD6x77PZgrrQVcag8v6t13yMw5jvMJMjVY')  # Substitua pela sua chave de API

prompt = "você é uma ai que vai gerar um texto de copyright, utilizado no mercado digital(marketing digital) pra gerar textos que geram milhões!, e um alerta, você cria só copyright e nada mais, textos que cativam pessoas à comprarem um produto, faça a pessoa ter necessidade de ter aquele produto ao qual será passado pra você,e uma coisa enfeite muito com emojis, a pessoa vai pedir como quer e vc faz seu ótimo trabalho ok?! obrigado. olha logo após esse prompt aqui, vai vir outro prompt que vai ficar aqui e não fale nada após isso, apenas crie a copy e uma coisa, não faça nada mais além de copys, se a pessoa colocar outro assunto, não responda, e uma outra coisa, caso não venha outro dados a partir de agora, dê um exemplo de suas copys. crie uma pra cativar, apenas caso não tiver algo depois desse prompt:"


def gerar_prompt(texto):
  model = genai.GenerativeModel("gemini-1.5-flash")
  response = model.generate_content(texto)

  return response.text


def pegar_texto(textoNovo):
  absorvido = gerar_prompt(textoNovo)
  st.write(absorvido)


with st.form("formzin"):
  st.write("Faça uma máquina de vendas com seu prompt!")
  inputAi = st.text_input("insira seu prompt")
  botaozin = st.form_submit_button("Gerar")
  if botaozin:
    pegar_texto(prompt+inputAi);
