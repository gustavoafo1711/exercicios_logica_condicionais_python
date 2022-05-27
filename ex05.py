"""
Escreva um programa que leia um número inteiro maior que zero e devolva na tela a soma de todos
os seus algarismos. Ex: o número 251 corresponderá o valor 8(2+5+1). Se o número lido não for
maior que zero, o programa terminará com a mensagem 'Número inválido'.
"""
try:
    num = int(input('Digite um número inteiro: '))
    res = 0
    if num > 0:
        for digit in num:
            res = res + int(digit)

        print(f'A soma dos digitos do número {num} é: {res}')
    else:
        print('Número inválido!!!')
except ValueError as err:
    print(f'Ocorreu o seguinte erro: {err}')