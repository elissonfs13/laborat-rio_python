from random import randint
from re import sub


# Função de geração de dígitos de um CPF
def gera_digitos(numero):
    reverso = 10
    total = 0
    for index in range(19):
        if index > 8:
            index -= 9
        total += int(numero[index]) * reverso
        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)
            if d > 9:
                d = 0
            total = 0
            numero += str(d)
    return numero


# Função de validação de CPF
def valida_cpf(cpf):
    if not cpf or len(cpf) != 11:
        return False

    novo_cpf = gera_digitos(cpf[:-2])
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)
    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False


# Função de geração de CPF
def gera_cpf():
    novo_cpf = gera_digitos(str(randint(100000000, 999999999)))
    return novo_cpf


# Função que formata um CPF passado
def formata(cpf):
    cpf = sub(r'[^0-9]', '', cpf)
    formatado = f'{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}'
    return formatado
