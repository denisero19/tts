import streamlit as st
from gtts import gTTS
from pydub import AudioSegment
import time

st.title("Conversor de Texto para Fala 🎤")

st.markdown("Insira o texto em português brasileiro que deseja converter em áudio:")

texto = st.text_area("Texto:", "Olá, este é um exemplo de conversão de texto em fala usando gTTS. Vamos converter este texto em um arquivo de áudio MP3 e depois reproduzi-lo.", height=150)

if st.button("Gerar Áudio"):
    if texto.strip():
        with st.spinner("Gerando áudio..."):
            try:
                # Gerar áudio com gTTS
                tts = gTTS(text=texto, lang='pt-br')
                timestamp = int(time.time())
                audio_file = f"audio_final_{timestamp}.mp3"
                tts.save(audio_file)

                st.success("Áudio gerado com sucesso! ✅")

                # Reproduzir áudio
                st.audio(audio_file, format="audio/mpeg")

                # Opção de download
                with open(audio_file, "rb") as file:
                    st.download_button(
                        label="Baixar Áudio",
                        data=file,
                        file_name=audio_file,
                        mime="audio/mpeg"
                    )
            except Exception as e:
                st.error(f"Erro ao gerar áudio: {str(e)}")
    else:
        st.error("Por favor, insira um texto válido.")
