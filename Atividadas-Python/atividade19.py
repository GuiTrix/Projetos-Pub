# Crie um programa q escolha aleatoriamente um nome de um aluno

import random
n1 = str(input("Nome do primeiro aluno: "))
n2 = str(input("Nome do segundo aluno: "))
n3 = str(input("Nome do terceiro aluno: "))
n4 = str(input("Nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print("Escolhendo um nome...")
print(f"Escolhi o(a) {escolhido}!")