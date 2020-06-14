from zipfile import ZipFile
import os


caminho_procura = input('Digite um caminho: ')
caminho_procura = caminho_procura.replace('"', '').replace("'", '').strip()
caminho_arquivo_saida = caminho_procura + "\\arquivo_compactado.zip"
caminho_descompactado = caminho_procura + "\\descompactado"

with ZipFile(caminho_arquivo_saida, 'w') as zip:
    for arquivo in os.listdir(caminho_procura):
        caminho_completo = os.path.join(caminho_procura, arquivo)
        if not caminho_completo == caminho_arquivo_saida:
            zip.write(caminho_completo, arquivo)

with ZipFile(caminho_arquivo_saida, 'r') as zip:
    for arquivo in zip.namelist():
        print(arquivo)

with ZipFile(caminho_arquivo_saida, 'r') as zip:
    zip.extractall(caminho_descompactado)
