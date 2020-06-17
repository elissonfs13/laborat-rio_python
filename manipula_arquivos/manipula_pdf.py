import PyPDF2
import os


caminho_procura = input('Digite um caminho: ')
caminho_procura = caminho_procura.replace('"', '').replace("'", '').strip()
caminho_arquivo_saida = caminho_procura + "\\arquivo_unido.pdf"
caminho_saida = caminho_procura + "\\saida"

pdf_unido = PyPDF2.PdfFileMerger()

for root, dirs, files in os.walk(caminho_procura):
    for file in files:
        file_name, file_ext = os.path.splitext(file)
        if file_ext == '.pdf':
            arquivo_pdf = open(os.path.join(root, file), 'rb')
            pdf_unido.append(arquivo_pdf)

with open(caminho_arquivo_saida, 'wb') as meu_novo_pdf:
    pdf_unido.write(meu_novo_pdf)

print(f'{caminho_arquivo_saida} criado com sucesso!')

with open(caminho_arquivo_saida, 'rb') as arquivo_pdf:
    leitor = PyPDF2.PdfFileReader(arquivo_pdf)
    num_paginas = leitor.getNumPages()

    for num_pagina in range(num_paginas):
        escritor = PyPDF2.PdfFileWriter()
        pagina_atual = leitor.getPage(num_pagina)
        escritor.addPage(pagina_atual)

        with open(f'{caminho_saida}/{num_pagina}.pdf', 'wb') as novo_pdf:
            escritor.write(novo_pdf)
