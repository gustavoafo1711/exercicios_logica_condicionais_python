"""
Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a
prestação for maior que 20% do salário imprima: 'Empréstimo não concedido', caso
comtrário imprima 'Empréstimo concedido'
"""
try:
    soldo = float(input('Informe o salário: '))
    prest = float(input('Qual o valor da prestação do empréstimo: '))

    if prest > (soldo * 0.2):
        print('Empréstimo negado!')
    else:
        print('Empréstimo concedido :)')
except ValueError as err:
    print(f'A aplicação gerou o seguinte erro: {err}')
