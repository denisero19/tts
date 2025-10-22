from gtts import gTTS
from pydub import AudioSegment

texto = "Olá, este é um exemplo de conversão de texto em fala usando gTTS e pydub. Vamos converter este texto em um arquivo de áudio MP3 e depois reproduzi-lo."

tts = gTTS(text=texto, lang='pt-br')
tts.save("audio_raw.mp3") 

audio = AudioSegment.from_mp3("audio_raw.mp3")
audio.export("audio_final.mp3", format="mp3")

print("Audio gerado com sucesso")