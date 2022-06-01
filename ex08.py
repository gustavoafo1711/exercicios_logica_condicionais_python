"""
Escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este número, isto é, janeiro se 1, fevereiro se 2
e assim por diante.
"""


def imprime_mes(mes):
    if mes == 1:
        return f'Janeiro é o mês {mes}'
    elif mes == 2:
        return f'Fevereiro é o mês {mes}'
    elif mes == 3:
        return f'Março é o mês {mes}'
    elif mes == 4:
        return f'Abril é o mês {mes}'
    elif mes == 5:
        return f'Maio é o mês {mes}'
    elif mes == 6:
        return f'Junho é o mês {mes}'
    elif mes == 7:
        return f'Julho é o mês {mes}'
    elif mes == 8:
        return f'Agosto é o mês {mes}'
    elif mes == 9:
        return f'Setembro é o mês {mes}'
    elif mes == 10:
        return f'Outubro é o mês {mes}'
    elif mes == 11:
        return f'Novembro é o mês {mes}'
    elif mes == 12:
        return f'Dezembro é o mês {mes}'


def inserir_mes():
    try:
        print('====== Digite um número referente ao mês ======')
        mes = int(input('Digite um número entre 1 e 12: '))
        if 1 <= mes <= 12:
            return mes
        else:
            print('\nNúmero inválido')
            exit()
    except ValueError as err:
        print(f'\nOcorreu o seguinte err: {err}')
        exit()


print(imprime_mes(inserir_mes()))
