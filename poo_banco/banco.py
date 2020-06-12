class Banco:
    def __init__(self):
        self._agencias = [1111, 2222, 3333]
        self._clientes = []
        self._contas = []

    def inserir_cliente(self, cliente):
        self._clientes.append(cliente)

    def inserir_conta(self, conta):
        self._contas.append(conta)

    def autenticar(self, cliente):
        if cliente not in self._clientes:
            return False

        if cliente.conta not in self._contas:
            return False

        if cliente.conta.agencia not in self._agencias:
            return False

        return True
