# importa a classe YouTube da biblioteca 'pytubefix' para manipular videos do youtube
from pytubefix import YouTube
# importa a biblioteca 'os' para manipulacao de arquivos
import os

# funcao que baixa apenas o audio de um video do youtube
def baixar_audio(url):
    try:
        # cria um objeto 'YouTube' com a url
        # permite acessar informacoes e streams do video
        yt = YouTube(url)
    
        # filtra as streams para pegar apenas streams de audio disponiveis
        # o metodo filter(only_audio=True) retorna apenas streams que contem apenas audio
        # .first() seleciona a primeira stream disponivel, geralmente a com mais qualidade
        audio_stream = yt.streams.filter(only_audio=True).first()

        # faz o download do audio para o diretorio atual
        # a funcao 'download()' salva o arquivo de audio no formato padrao (.mp4 ou .webm)
        output = audio_stream.download()

        # renomeia o arquivo para .mp3
        # extrai o nome do arquivo e a extensão usando o método 'rsplit'
        # 'rsplit' divide a string do nome do arquivo a partir do ponto (.) e extrai a ultima parte como extensao
        base, ext = output.rsplit('.', 1)

        # cria um novo nome de arquivo, substituindo a extensao original por '.mp3'
        # permite que o audio baixado seja salvo com a extensao '.mp3'
        novo_arquivo = base + '.mp3'

        # renomeia o arquivo baixado para que tenha a extensao '.mp3'
        # necessario porque por padrao o pytubefix salva o audio como '.mp4' ou '.webm'
        os.rename(output, novo_arquivo)

        print(f"Áudio baixado com sucesso: {novo_arquivo}")

    # captura e exibe erros
    except Exception as e:
        print(e)

# url do video desejado
url = ""

# chama a funcao para baixar o audio utilizando a url como argumento
baixar_audio(url)