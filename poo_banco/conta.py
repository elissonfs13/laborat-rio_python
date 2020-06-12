from abc import ABC, abstractmethod


class Conta(ABC):
    def __init__(self, agencia, conta, saldo):
        self._agencia = agencia
        self._conta = conta
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += valor
        self.detalhes()

    def detalhes(self):
        print(f'Agência: {self._agencia} '
              f'Conta: {self._conta} '
              f'Saldo: {self._saldo}')

    @property
    def agencia(self):
        return self._agencia

    @abstractmethod
    def sacar(self): pass


class ContaPoupanca(Conta):
    def sacar(self, valor):
        if self._saldo < valor:
            print("Saldo insuficiente")
            return

        self._saldo -= valor
        self.detalhes()


class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo, limite=100):
        super().__init__(agencia, conta, saldo)
        self._limite = limite

    def sacar(self, valor):
        if (self._saldo + self._limite) < valor:
            print("Saldo insuficiente")
            return

        self._saldo -= valor
        self.detalhes()
