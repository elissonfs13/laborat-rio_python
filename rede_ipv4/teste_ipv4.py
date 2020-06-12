from rede_ipv4.ipv4 import IPv4


def exibe_info(info_ipv4):
    print()
    print(f'IP: {info_ipv4.ip}')
    print(f'Máscara: {info_ipv4.mascara}')
    print(f'Rede: {info_ipv4.rede}')
    print(f'Broadcast: {info_ipv4.broadcast}')
    print(f'Prefixo: {info_ipv4.prefixo}')
    print(f'Número de IPs da rede: {info_ipv4.numero_ips}')
    print('#' * 80)


print("##############################################")
print("        Teste de cálculos de rede IPv4        ")
print("##############################################")
while True:
    print()
    print("Escolha uma opção: ")
    print("1 - IP com Máscara")
    print("2 - IP com Prefixo")
    print("3 - Sair")
    escolha = input(">> ")
    print()

    if escolha == '1':
        ip_digitado = input("Digite o IP: ")
        mascara_digitada = input("Digite a máscara de rede: ")
        try:
            info_ipv4 = IPv4(ip=ip_digitado, mascara=mascara_digitada)
            exibe_info(info_ipv4)
        except (ValueError, TypeError) as error:
            print("Ocorreu um erro: " + error)

    elif escolha == '2':
        ip_digitado = input("Digite o IP: ")
        prefixo_digitado = input("Digite o prefixo de rede: ")
        try:
            info_ipv4 = IPv4(ip=ip_digitado, prefixo=prefixo_digitado)
            exibe_info(info_ipv4)
        except (ValueError, TypeError) as error:
            print("Ocorreu um erro: " + error)

    elif escolha == '3':
        print("Fim da execução do teste")
        break

    else:
        print("Opção inválida!")
