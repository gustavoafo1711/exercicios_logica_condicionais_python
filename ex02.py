"""
Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número.
Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
from math import sqrt
try:
    num = float(input('Digite um número maior que 0: '))

    if num >= 0:
        # num = num ** 0.5
        res = sqrt(num)
        print(f'A raiz quadrada de {num} é {res}')
    else:
        print('Esse é um número inválido!!!')
except ValueError:
    print('Digite somente números!!!')
