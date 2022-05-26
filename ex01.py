"""
Faça um programa que receba dois números e mostre qual deles é o maior.
"""

try:
    num1 = float(input('Digite o primeiro número: '))
    num2 = float(input('Digite o segundo número: '))
    if num1 > num2:
        print(f'O número {num1} é maior que {num2}.')
    else:
        print(f'O número {num2} é maior que {num1}.')
except ValueError:
    print('Você deve digitar somente números')
    exit
except NameError:
    exit
