# Exercício 1: Tipos de triângulos

def determina_tipo_triangulo(a, b, c):
    if a == b == c:
        print("Equilátero")
    elif not((a + b) > c and (a + c) > b and (b + c) > a):
        print("Não é um triângulo")
    elif a == b or b == c or a == c:
        print("Isósceles")
    elif a != b != c:
        print("escaleno")


determina_tipo_triangulo(1, 1, 4)

# Exercício 2: Dias da semana

def dia_semana(dia):
    if dia == 1:
        print("domingo")
    elif dia == 2:
        print("segunda")
    elif dia == 3:
        print("terça")
    elif dia == 4:
        print("quarta")
    elif dia == 5:
        print("quinta")
    elif dia == 6:
        print("sexta")
    elif dia == 7:
        print("sábado")
    else:
        print("")

dia_semana(7)

# Exercício 3: Calculadora simples

def soma(a, b):
    print(a + b)
def subtracao(a, b):
    print(a - b)
def divisao(a, b):
    print(a / b)
def multiplicacao(a, b):
    print(a * b)

def calculadora():
    n1 = float(input("Informe o primeiro número: "))
    n2 = float(input("Informe o segundo número: "))
    operacao = input("Informe a operação" )
    if operacao == "soma":
        soma(n1, n2)
    elif operacao == "subtracao":
        subtracao(n1, n2)
    elif operacao == "multiplicacao":
        multiplicacao(n1, n2)
    elif operacao == "divisao":
        divisao(n1, n2)
    else:
        print("Operação inválida")

calculadora()

