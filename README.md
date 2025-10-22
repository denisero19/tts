# Conversor de Texto para Fala (TTS) 🎤

Este projeto é uma aplicação web em Python que converte texto em fala usando a biblioteca `gTTS` (Google Text-to-Speech). A interface é construída com Streamlit para uma experiência interativa. 🐍🔊🌐

## Descrição 📝

A aplicação `app.py` permite ao usuário inserir texto em português brasileiro e gerar um arquivo de áudio MP3. Ela utiliza o `gTTS` para gerar o áudio diretamente em formato MP3. A interface web permite reprodução e download direto do áudio. 🎵

## Requisitos 📋

- Python 3.x 🐍
- Bibliotecas:
  - `gtts` 🌐
  - `pydub` (opcional, para futuras expansões) 🔧
  - `streamlit` 🌟

## Instalação 🔧

1. Instale as dependências Python:
   ```
   pip install gtts pydub streamlit
   ```

## Uso ▶️

Execute a aplicação Streamlit:
```
streamlit run app.py
```

A aplicação será aberta no navegador. Insira o texto desejado na área de texto e clique em "Gerar Áudio". O áudio será gerado, reproduzido na página e disponível para download. 🎤

## Funcionalidades 🌟

- **Inserção de Texto:** Área de texto para inserir o conteúdo a ser convertido.
- **Geração de Áudio:** Botão para processar o texto e gerar o MP3.
- **Reprodução:** Player de áudio integrado para ouvir o resultado.
- **Download:** Opção para baixar o arquivo de áudio gerado.
- **Tratamento de Erros:** Exibe mensagens de erro em caso de falha na geração do áudio.
- **Nomes de Arquivo Únicos:** Cada áudio gerado tem um nome único com timestamp para evitar sobreposições.

## Exemplo de Texto 💬

O texto padrão é: "Olá, este é um exemplo de conversão de texto em fala usando gTTS. Vamos converter este texto em um arquivo de áudio MP3 e depois reproduzi-lo." 🌟

## Licença 📄

Este projeto é de uso livre. Sinta-se à vontade para modificar e distribuir. 🤝
