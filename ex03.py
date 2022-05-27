"""
Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e
exiba na tela a média destas notas. Uma nota válida deve ser, obrigatóriamente, um
valor yntre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve
ser informado ao usuário e o programa termina.
"""
try:
    nota01 = float(input('Digite a primeira nota: '))
    nota02 = float(input('Digite a segunda nota: '))

    if 0 <= nota01 <= 10 and 0 <= nota02 <= 10:
        media = (nota01 + nota02) / 2
        print(f'A média das notas é: {media}')
    else:
        print('Digite um número entre 0 e 10!!!')
        exit
except ValueError:
    print('Digite somente números!!!')


