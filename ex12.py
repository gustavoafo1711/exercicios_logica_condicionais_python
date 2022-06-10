"""
Faça um algoritmo que calcule o IMC de uma pessoa e mostre sua classificação
de acordo com a tabela abaixo:

==============================================
IMC           |  Classificação               |
----------------------------------------------
 < 18,5       | Abaixo do Peso               |
 18,6 - 24,9  | Saudável                     |
 25,0 - 29,9  | Peso em excesso              |
 30,0 - 34,9  | Obesidade Grau I             |
 35,0 - 39,9  | Obesidade Grau II (severa)   |
 >= 40,0      | Obesidade Grau III (mórbida) |
 =============================================

 Calculo IMC: IMC = Peso ÷ (Altura × Altura)
"""


def calc_imc(peso, altura):
    imc = round(peso / (altura ** 2), 2)
    return imc


def class_imc(imc):
    if imc < 18.5:
        return f'Vocẽ está abaixo do peso.\nSeu IMC é {imc}'
    elif 18.6 <= imc < 25:
        return f'Vocẽ está com o peso saudável.\nSeu IMC é {imc}'
    elif 25 <= imc < 30:
        return f'Vocẽ está com peso em excesso.\nSeu IMC é {imc}'
    elif 30 <= imc < 35:
        return f'Vocẽ está com obesidade Grau I.\nSeu IMC é {imc}'
    elif 35 <= imc < 40:
        return f'Vocẽ está com obesidade Grau II (severa).\nSeu IMC é {imc}'
    elif imc >= 40:
        return f'Vocẽ está com obesidade Grau III (mórbida).\nSeu IMC é {imc}'


def principal():
    try:
        print('========== Calcule o seu IMC ==========\n')
        peso = float(input('Informe o seu peso (Kg): '))
        altura = float(input('Informe sua altura: '))

        imc = calc_imc(peso, altura)
        print(class_imc(imc))
    except ValueError:
        print('Informe um valor válido!!!')
        principal()


principal()
