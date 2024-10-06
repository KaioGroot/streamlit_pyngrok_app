import streamlit as st
import requests
import os 
import base64
import random
import io 
import time


API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
headers = {"Authorization": "Bearer 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"}


def query(image):
  with open(image,'rb') as f:
    data = f.read()
  response = requests.post(API_URL, headers=headers,data=data)
  return response.json()

arquivoPath = "drive/MyDrive/fotosai"

for arquivo in os.listdir(arquivoPath):
    if os.path.isfile(os.path.join(arquivoPath, arquivo)):
      st.image(os.path.join(arquivoPath,arquivo))
      botaoz = st.button("Gerar   prompt",key=arquivo)
      if(botaoz):
        outpot = query(arquivoPath+'/'+arquivo)
        st.write(outpot)
      
