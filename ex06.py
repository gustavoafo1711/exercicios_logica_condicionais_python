"""
Ler um número inteiro. Se o número for negativo escreva, 'Número inválido', se for positivo,
calcule o logaritmo deste número.

"""
try:
    logmd = int(input('Digite um número inteiro positivo para calcular o logarítmo: '))
    base = int(input('Informe a base: '))
    from math import log
    if logmd >= 0:
        res = log(logmd, base)
        print(f'O log de {logmd} na base {base} é: {res}')
    else:
        print('Número inválido!!!')
except ValueError as err:
    print(f'ocorreu o seguinte erro: {err}')
