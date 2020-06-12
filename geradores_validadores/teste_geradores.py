import geradores_validadores.cnpj as cnpj
import geradores_validadores.cpf as cpf

print("##############################################")
print("Teste de Geradores e Validadores de CPF e CNPJ")
print("##############################################")
while True:
    print()
    print("Escolha uma opção: ")
    print("1 - Validar CPF")
    print("2 - Validar CNPJ")
    print("3 - Gerar CPF")
    print("4 - Gerar CNPJ")
    print("5 - Sair")
    escolha = input(">> ")
    print()

    if escolha == '1':
        cpf_validar = input("Digite o CPF: ")
        validado = cpf.valida_cpf(cpf_validar)
        if validado:
            print(f'O CPF {cpf.formata(cpf_validar)} é VÁLIDO')
        else:
            print(f'O CPF {cpf.formata(cpf_validar)} é INVÁLIDO')
    elif escolha == '2':
        cnpj_validar = input("Digite o CNPJ: ")
        validado = cnpj.valida_cnpj(cnpj_validar)
        if validado:
            print(f'O CNPJ {cnpj.formata(cnpj_validar)} é VÁLIDO')
        else:
            print(f'O CNPJ {cnpj.formata(cnpj_validar)} é INVÁLIDO')
    elif escolha == '3':
        cpf_gerado = cpf.gera_cpf()
        print(f'O CPF gerado foi: {cpf.formata(cpf_gerado)}')
    elif escolha == '4':
        cnpj_gerado = cnpj.gera_cnpj()
        print(f'O CNPJ gerado foi: {cnpj.formata(cnpj_gerado)}')
    elif escolha == '5':
        print("Fim da execução do teste")
        break
    else:
        print("Opção inválida!")
