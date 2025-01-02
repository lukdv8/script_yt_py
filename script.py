from pytubefix import YouTube

import os

def baixar_audio(url):
    try:
        yt = YouTube(url)
    
        audio_stream = yt.streams.filter(only_audio=True).first()

        output = audio_stream.download()

        base, ext = output.rsplit('.', 1)

        novo_arquivo = base + '.mp3'

        os.rename(output, novo_arquivo)

        print(f"Áudio baixado com sucesso: {novo_arquivo}")

    except Exception as e:
        print(e)

url = ""

baixar_audio(url)