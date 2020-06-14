import os

caminho_procura = input('Digite um caminho: ')
caminho_procura = caminho_procura.replace('"', '').replace("'", '').strip()

for root, dirs, files in os.walk(caminho_procura):
    for file in files:
        print(file)
