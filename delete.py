import streamlit as st
import google.generativeai as genai
import re
import json
import os

genai.configure(api_key='AIzaSyD6x77PZgrrQVcag8v6t13yMw5jvMJMjVY')  # Substitua pela sua chave de API

# Função para carregar prompts existentes
def carregar_prompts():
    if os.path.exists("prompts.json"):
        with open("prompts.json", 'r') as f:
            return json.load(f)
    return []  # Retorna uma lista vazia se o arquivo não existir

# Função para salvar prompts no arquivo JSON
def salvar_prompts(prompts):
    with open("prompts.json", 'w') as f:
        json.dump(prompts, f)

def falar_sobre(texto):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(texto)
    clean_response = re.sub(r'```.*?\n', '', response.text)
    clean_response = clean_response.rstrip('`')
    return clean_response

def gerado_pelogemini(prompt):
    # Carrega os prompts existentes
    prompts = carregar_prompts()
    # Adiciona o novo prompt à lista
    prompts.append(prompt)
    # Salva a lista atualizada no arquivo
    salvar_prompts(prompts)
    resultado_final = falar_sobre(prompt)
    # Salvar o arquivo gerado
    with open("gerado.py", 'w') as f:
        f.write(resultado_final)

    # Renderizar o conteúdo no Streamlit
    st.markdown(resultado_final, unsafe_allow_html=True)

# Exemplo de uso
prompt = """
... agora você é uma ai que vai gerar um código todinho em streamlit ok?, só que assim,
você cria um código todo em streamlit, exemplo, uma landing page falando sobre o vercel
que o meu site de ai que ajuda as pessoas em seu trabalho online, vc cria todo o código e me passa.
depois disso não fale mais nada, só mande o código. se não vai atrapalhar, por que dá erro obrigado.
uma coisa, não coloque mais no código. faça tudo em pt-br; mande o código em formato de texto, 
não em formato de código saca?, pra não bugar por que eu quero colocar o seu código em um arquivo .py
e se mandar em formato de código vai ter 
python e da´erro. por favor não erre. não coloque imagens.
e uma coisa, faça um código pra evitar erros. repito novamente, faça um site mostrando o nome do meu site e quais suas inovações, e faça um site muito grande.
e não coloque o set_page_config() no código. por favor se o código houver set_page_config() troque por outro elemento, por favor apague.
e uma coisinha faça uma página de preços da ai, que é 5$ por mês, 12$ por mês e 24$ faça bem bonito e intuitivo.

"""
gerado_pelogemini(prompt)
