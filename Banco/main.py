from ClassMethodMENUBanco import ContaCorrente, CartaoCredito
from ClassMethodAgencia import AgenciaPremium, AgenciaComum, AgenciaVirtual
import time

conta_brian = ContaCorrente("Brian", "111.222.333-45", 1234, 24062)
conta_pessoa = ContaCorrente("Pessoa", "222.333.444-56", 2234, 24060)
cartao_brian = CartaoCredito("Brian", conta_brian)
agencia1 = (12346789, '00005', 1234)
agencia_virtual = AgenciaVirtual('www.agenciavirtual.com.br', 22224444, '00006')
agencia_premium = AgenciaPremium(22225555, '00007')
agencia_comum = AgenciaComum(22226666, '00008')

#help(ContaCorrente)
#help(CartaoCredito)

num = None

while num != 3:
    print('Seja bem-vindo(a) a interface do banco Python\n')
    print('Digite 1 para acessar sua conta Cliente\n')
    #print('Digite 2 para acessar sua conta Agência\n')
    print('Digite 3 para encerrar o programa')
    num = int(input('Digite aqui seu indice: '))
    if num == 1:
        print(f'\n\n\nBem-vindo(a) a sua conta, {conta_brian.nome} \n   O que deseja fazer?\n\nDeposito 1\nSaque 2\nTransferência 3\nExtrato 4\nInformações 5\nCartão 6\nParcelar 7\nSair 10\n')
        i = None

        while i != 10:
            i = int(input('Insira aqui seu indice: '))
            if i == 1:
                n = int(input('Qual valor deseja depositar: '))
                conta_brian.deposito(n)
            elif i == 2:
                n = int(input('Qual valor deseja sacar: '))
                conta_brian.saque(n)
                conta_brian.consultar_saldo()
            elif i == 3:
                n = int(input('Qual valor deseja tranferir: '))
                conta_brian.ted(n, conta_pessoa)
            elif i == 4:
                conta_brian.extrato()
            elif i == 5:
                conta_brian.info()
            elif i == 6:
                cartao_brian.info()
                print('\n')
                cartao_brian.extrato()
            elif i == 7:
                qtd = int(input('Digite a quantidade de parcelas: '))
                valor = int(input('Digite o valor das parcelas: '))
                total = int(input('Digite o valor da compra: '))
                juros = int(input('Digite o juros: '))
                cartao_brian.parcelar(qtd, valor, total, juros)
            # elif i == 8:
            #     novasenha = input('Digite sua nova senha (Somente 4 numeros): ')
            #     cartao_brian.senha = novasenha
            elif i == 10:
                time.sleep(1.5)
                print('Conta encerrada')
                time.sleep(1.5)
            else:
                print('Indice incorreto | Caso deseje sair do programa digite 3')
    elif num == 2:
        pass
    elif num == 3:
        time.sleep(1.5)
        print('Programa encerrado')
        time.sleep(1.5)
    else:
        print('Indice não encontrado | Caso queira encerrar o programa digite 3')
