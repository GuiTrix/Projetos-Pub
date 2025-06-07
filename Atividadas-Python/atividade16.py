#faça um programa que leia a parte inteira de um numero float

import math

numero = float(input("Digite um número: "))
inteiro = math.trunc(numero)

print(f"O número flutuante {numero} tem a parte inteira como {inteiro}")