from re import sub
from random import randint


# Função de geração de dígitos de um CNPJ
def gera_digito(cnpj, digito):
    regressivos = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    if (digito == 1):
        regressivos = regressivos[:1]
        novo_cnpj = cnpj[:-2]
    elif (digito == 2):
        novo_cnpj = cnpj
    else:
        return None
    total = 0
    for indice, regressivo in enumerate(regressivos):
        total += int(cnpj[indice]) * regressivo
    digito = 11 - (total % 11)
    digito = digito if digito <= 9 else 0
    return f'{novo_cnpj}{digito}'


# Função de validação de CNPJ
def valida_cnpj(cnpj):
    cnpj = sub(r'[^0-9]', '', cnpj)
    try:
        novo_cnpj = gera_digito(cnpj=cnpj, digito=1)
        novo_cnpj = gera_digito(cnpj=novo_cnpj, digito=2)
    except Exception as e:
        return False
    sequencia = novo_cnpj == str(novo_cnpj[0]) * len(cnpj)
    if cnpj == novo_cnpj and not sequencia:
        return True
    else:
        return False


# Função de geração de CNPJ
def gera_cnpj():
    d1 = randint(0,9)
    d2 = randint(0,9)
    b2 = randint(100,999)
    b3 = randint(100,999)
    b4 = '0001'
    cnpj_inicio = f'{d1}{d2}{b2}{b3}{b4}00'
    novo_cnpj = gera_digito(cnpj=cnpj_inicio, digito=1)
    novo_cnpj = gera_digito(cnpj=novo_cnpj, digito=2)
    return novo_cnpj


# Função que formata um CNPJ passado
def formata(cnpj):
    cnpj = sub(r'[^0-9]', '', cnpj)
    formatado = f'{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:14]}'
    return formatado
