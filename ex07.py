"""
A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10,
respectivamente, a um trabalho de laboratório, uma avaliação semestral e a um aexme final. A média das três
notas mencionadas anteriormente obedece aos pesos:
Trabalho de Laboratório: 2
Avaliação Semestral: 3
Exame Final: 5
De acordo com o resultado, mostre na tela se o aluno está:
Reprovado: média 0 - 2,9
Recuperação: 3 - 4,9
Aprovado: > 5
"""


def verificar_range_nota(num):
    if not 0 <= num <= 10:
        print(f'o número digitado deve estar entre 0 e 10')
        exit()


def calcular_media(mediafinal):
    if 0 <= mediafinal <= 2.9:
        return f'O aluno foi reprovado, sua média final é {mediafinal}'
    elif 3 <= mediafinal <= 4.9:
        return f'O aluno está de recuperação, sua média final é {mediafinal}'
    else:
        return f'O aluno foi aprovado, sua média final é {mediafinal}'


try:
    pesolab = 2
    pesosemestre = 3
    pesofinal = 5

    notalab = float(input("Insira o valor do Trabalho de Laboratório: "))
    verificar_range_nota(notalab)
    notasemestre = float(input("Insira o valor da Avaliação Semestral: "))
    verificar_range_nota(notasemestre)
    notafinal = float(input("Insira o valor do Exame Final: "))
    verificar_range_nota(notafinal)

    media = ((pesolab * notalab) + (pesosemestre * notasemestre) + (pesofinal * notafinal)) / \
            (pesolab + pesosemestre + pesofinal)

    print(calcular_media(media))

except ValueError as err:
    print(f'Ocorreu o seguinte erro: {err}')
