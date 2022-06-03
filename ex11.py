"""
Dados três valores A, B, C, verificar se eles podem ser valores dos lados de um triângulo
e se forem, se é um triângulo escaleno, equilátero ou isósceles, considerando os seguintes
conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados;
- Chama-se equilátero o triângulo que tem trẽs lados iguais;
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais;
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.

Saber se são verdadeiras as medidas de um triângulo
| b - c | < a < b + c
| a - c | < b < a + c
| a - b | < c < a + b

Exemplo:
|10 – 9| < 5 < 10 + 9
1 < 5 <19 (VERDADEIRO)

|9 – 5| < 10 < 9 + 5
4 < 10 < 14 (VERDADEIRO)

|5 – 10| < 9 < 10 + 5
5 < 9 < 15 (VERDADEIRO) 
"""


def inserir():
    """
    - Insere os valores, verifica se é válido e chama a função para testar
    se as condições são verdadeiras para existir um triângulo com a
    função testar_triangulo().
    - Caso não seja válido reinicia chamando a função inserir()
    """
    try:
        print('=============== DESCOBRINDO TRIÂNGULOS ===============')
        num_a = float(input('Digite o primeiro valor: '))
        num_b = float(input('Digite o segundo valor: '))
        num_c = float(input('Digite o terceiro valor: '))

        testar_triangulo(num_a, num_b, num_c)
    except ValueError:
        print('Digite um número válido!!!')
        inserir()


def tipo_triangulo(num_a, num_b, num_c):
    if num_a == num_b == num_c:
        print('Triângulo equilátero')
    elif num_a != num_b != num_c:
        print('Triângulo escaleno')
    else:
        print('Triângulo isósceles')


def testar_triangulo(num_a, num_b, num_c):
    """
    Saber se são verdadeiras as medidas de um triângulo
    | b - c | < a < b + c
    | a - c | < b < a + c
    | a - b | < c < a + b

    - Caso os três testes forem verdadeiros chama a função tipo_triangulo(), senão
    informa que os valores não verdadeiros para um triângulo.
    """
    if abs(num_b - num_c) < num_a < (num_b + num_c):
        teste1 = True
    else:
        teste1 = False

    if abs(num_a - num_c) < num_b < (num_a + num_c):
        teste2 = True
    else:
        teste2 = False

    if abs(num_a - num_b) < num_c < (num_a + num_c):
        teste3 = True
    else:
        teste3 = False

    if teste1 and teste2 and teste3:
        tipo_triangulo(num_a, num_b, num_c)
    else:
        print('Valores não verdadeiros para um triângulo.')


inserir()

