from datetime import datetime
import pytz
from random import randint


class ContaCorrente:
    """
    Cria um objeto ContaCorrente para gerenciar as contas dos clientes

    Atributos:
        nome (str): Nome do cliente
        cpf (str): CPF do Cliente
        agencia (str): Agência responsável pela conta do Cliente
        num_conta (str): Número da conta do Cliente
        limite (float): Limite de Cheque especial do Cliente
        transacoes (list): Extrato do Cliente
    """

    @staticmethod
    def _data_hora():
        fuso = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso)
        return horario.strftime('%d/%m/%Y - %H:%M:%S')

    def __init__(self, nome, cpf, agencia, num_conta):
        self.nome = nome
        self._cpf = cpf
        self._saldo = 0
        self._limite = -1000
        self._agencia = agencia
        self._num_conta = num_conta
        self._transacoes = []
        self.cartoes = []

    def deposito(self, valor):
        self._saldo += valor
        self.consultar_saldo()
        self._transacoes.append((valor, self._saldo, ContaCorrente._data_hora()))

    def consultar_saldo(self):
        print(f'Seu saldo atul é de R${self._saldo:,.2f}')

    def consultar_limite(self):
        print(f'Seu limite atul é de R${self._limite:,.2f}')

    def _limite_conta(self):
        self._limite = -2000
        return self._limite

    def saque(self, valor):
        if self._saldo - valor < self._limite_conta():
            print('O valor solicitado para saque não está disponível na conta')
            self.consultar_saldo()
        else:
            self._saldo -= valor
            self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))

    def extrato(self):
        print('Seu extrato: ')
        print('Valor, Saldo, Data e Hora')
        for trasacao in self._transacoes:
            print(trasacao)

    def info(self):
        print("""Cliente: 
{} - CPF: {}     Agência: {}   Conta: {}
Saldo: R${:,.2f}
Limite: R${:,.2f}
Total disponível: R${:,.2f}
""".format(self.nome, self._cpf, self._agencia, self._num_conta, self._saldo, self._limite, (self._saldo - self._limite)))

    def ted(self, valor, conta_destino):
        self._saldo -= valor
        self._transacoes.append((-valor, self._saldo, ContaCorrente._data_hora()))
        conta_destino._saldo += valor
        conta_destino._transacoes.append((valor, conta_destino._saldo, ContaCorrente._data_hora()))


class CartaoCredito:

    @staticmethod
    def _data_hora():
        fuso = pytz.timezone('Brazil/East')
        horario = datetime.now(fuso)
        return horario

    def __init__(self, titular, conta_corrente):
        self.numero = randint(1000000000000000, 9999999999999999)
        self.titular = titular
        self.validade = '{}/{}' .format(CartaoCredito._data_hora().month, CartaoCredito._data_hora().year + 8)
        self.cod_seguranca = '{}{}{}'.format(randint(0, 9), randint(0, 9), randint(0, 9))
        self.limite = 2000
        self._senha = '1234'
        self._extrato = []
        self.conta_corrente = conta_corrente
        conta_corrente.cartoes.append(self)

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, valor):
        if len(valor) == 4 and valor.isnumeric():
            self.senha = valor
        else:
            print('Nova senha inválida')

    def info(self):
        print("""Número: {}  -  Titular: {}
Código de Segurança: {}  -  Validade: {}
Limite: {}""".format(self.numero, self.titular, self.cod_seguranca, self.validade, self.limite))

    def parcelar(self, qtd, valor, total, juros):
        if total > self.limite:
            print('Infelizmente você não possui limite sulficiente para realizar a compra')
        else:
            self.limite -= valor * juros
            print('Você realizou uma compra de R${:,.2f}, parcelando em {} vezes de R${:,.2f}'.format(total, qtd, valor))
            self._extrato.append((-valor, self.limite, CartaoCredito._data_hora()))

    def extrato(self):
        print('Seu extrato: ')
        print('Valor, Saldo, Data e Hora')
        for trasacao in self._extrato:
            print(trasacao)
