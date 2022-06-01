"""
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas
(as básicas). O usuário escolhe uma das opções e o seu programa então pede dois valores numéricos
e realiza a operaçõa, mostrando o resultado e saindo.
"""


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError as err:
        print(f'Ocorreu o seguinte erro: {err}')
        exit()


print('============== Escolha sua operação Matemática ==============\n')
print('SOMA: (1)\nSUBTRAÇÃO: (2)\nMULTIPLIACAÇÃO: (3)\nDIVISÃO: (4)')

try:
    operacao = int(input('Escolha sua operação: '))
    if 1 <= operacao <= 4:
        num1 = float(input('Informe o primeiro número: '))
        num2 = float(input('Informe o segundo número: '))
    else:
        print('Informe uma operação válida!!!')

    if operacao == 1:
        print(somar(num1, num2))
    elif operacao == 2:
        print(subtrair(num1, num2))
    elif operacao == 3:
        print(multiplicar(num1, num2))
    elif operacao == 4:
        print(dividir(num1, num2))

except ValueError or NameError as err:
    print(f'Ocorreu o seguinte erro: {err}')