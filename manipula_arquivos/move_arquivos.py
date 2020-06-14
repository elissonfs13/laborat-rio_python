import os
import shutil


caminho_origem = input('Digite o caminho de origem: ')
caminho_origem = caminho_origem.replace('"', '').replace("'", '').strip()

caminho_destino = input('Digite o caminho de destino: ')
caminho_destino = caminho_destino.replace('"', '').replace("'", '').strip()

try:
    os.mkdir(caminho_destino)
except FileExistsError as e:
    print(f'Pasta {caminho_destino} já existe.')

for root, dirs, files in os.walk(caminho_origem):
    for file in files:
        shutil.move(os.path.join(root, file), os.path.join(caminho_destino, file))
        print(f'Arquivo {file} movido com sucesso.')
