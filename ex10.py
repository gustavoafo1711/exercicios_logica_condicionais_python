"""
Faça um programa para verificar se um determinado número inteiro é divisível por
3 ou 5, mas não simultaneamente pelos dois.
"""
num = int(input('Digite um número inteiro: '))

if num % 3 == 0 and num % 5 == 0:
    print(f'O número {num}, é divisível por 3 e 5.')
elif num % 3 == 0:
    print(f'O número {num} é divisível somente por 3.')
elif num % 5 == 0:
    print(f'O número {num} é divisível somente por 5.')
else:
    print('Este número não é divisível por 3 ou 5!!!')
