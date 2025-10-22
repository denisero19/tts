# Conversor de Texto para Fala (TTS) 🎤

Este projeto é um script simples em Python que converte texto em fala usando a biblioteca `gTTS` (Google Text-to-Speech) e processa o áudio gerado com a biblioteca `pydub`. 🐍🔊

## Descrição 📝

O script `app.py` converte um texto em português brasileiro em um arquivo de áudio MP3. Ele utiliza o `gTTS` para gerar o áudio inicial e o `pydub` para exportar o arquivo final em formato MP3. 🎵

## Requisitos 📋

- Python 3.x 🐍
- Bibliotecas:
  - `gtts` 🌐
  - `pydub` 🎧
  - `ffmpeg` (necessário para o pydub processar áudios MP3) 🔧

## Instalação 🔧

1. Instale as dependências Python:
   ```
   pip install gtts pydub
   ```

2. Instale o `ffmpeg` (se não estiver instalado):
   - No Windows: Baixe e instale do site oficial do FFmpeg. 💻
   - No Linux: `sudo apt install ffmpeg` 🐧
   - No macOS: `brew install ffmpeg` 🍎

## Uso ▶️

Execute o script Python:
```
python app.py
```

O script irá gerar dois arquivos de áudio:
- `audio_raw.mp3`: Áudio bruto gerado pelo gTTS. 🎤
- `audio_final.mp3`: Áudio processado e exportado pelo pydub. 🎵

## Saída 📤

Após a execução, você verá a mensagem "Audio gerado com sucesso" no console. Os arquivos de áudio estarão disponíveis no diretório do projeto. ✅

## Exemplo de Texto 💬

O texto usado no exemplo é: "Olá, este é um exemplo de conversão de texto em fala usando gTTS e pydub. Vamos converter este texto em um arquivo de áudio MP3 e depois reproduzi-lo." 🌟

## Licença 📄

Este projeto é de uso livre. Sinta-se à vontade para modificar e distribuir. 🤝
