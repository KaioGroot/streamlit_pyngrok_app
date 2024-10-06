import streamlit as st
import requests
import time  # Adicione isso para implementar o loop de espera

# Replace with your Shotstack API key
API_KEY = "iIQOiNh9zB4KYbz7a53C74AXSmujRGyKl5K7hq9M"

st.title("YouTube Video Cutter with API")

# Input for YouTube video URL
video_url = st.text_input("Enter YouTube Video URL:")

# Input for start and end times (in seconds)
start_time = st.number_input("Start Time (seconds):", min_value=0)
end_time = st.number_input("End Time (seconds):", min_value=0)
text_overley = st.text_input("texto do seu video")


if st.button("Cut Video"):
    if video_url:
        # Create the API request payload
        payload = {
            "timeline": {
                "tracks": [
                    {
                        "clips": [
                            {
                                "asset": {
                                    "type": "video",
                                    "src": video_url,
                                    "trim": start_time,  # Início do vídeo
                                },
                                "start": 0,  # Início do clipe de vídeo
                                "length": end_time - start_time,  # Duração do clipe
                            }
                        ]
                    },
                    # Adiciona um track separado para o texto (texto sobreposto ao vídeo)
                    {
                        "clips": [
                            {
                                "asset": {
                                    "type": "title",  # Define o tipo como título (texto)
                                    "text": text_overley,  # Texto fornecido pelo usuário
                                    "style": "minimal",  # Estilo básico predefinido
                                    "position": "center",  # Posição central na tela
                                    "color": "#fff"  # Cor do texto (branco)
                                },
                                "start": 0,  # Início do texto
                                "length": end_time - start_time,  # Mesma duração do vídeo
                            }
                        ]
                    }
                ]
            },
            "output": {
                "format": "mp4",
                "resolution": "sd"
            }
        }


        # Send the API request
        headers = {"x-api-key": API_KEY}
        response = requests.post("https://api.shotstack.io/stage/render", json=payload, headers=headers)

        # Handle the response
        if response.status_code == 201:
            render_id = response.json()["response"]["id"]
            st.write(f"Rendering video... (Render ID: {render_id})")

            # Loop to check render status
            while True:
                status_response = requests.get(f"https://api.shotstack.io/stage/render/{render_id}", headers=headers)
                if status_response.status_code == 200:
                    render_status = status_response.json()["response"]["status"]
                    if render_status == "done":
                        # Display the video URL
                        video_url = status_response.json()["response"]["url"]
                        st.video(video_url)
                        break
                    elif render_status == "failed":
                        st.error("Rendering failed.")
                        break
                    else:
                        st.write("Video is still processing... Please wait.")
                        time.sleep(10)  # Aguarde 5 segundos antes de verificar novamente
                else:
                    st.error("Error checking render status.")
                    break
        else:
            st.error(f"API Error: {response.status_code} - {response.text}")
    else:
        st.warning("Please enter a YouTube video URL.")
