# faça um programa que fale a uni,  dezena e centena de um numero


num = int(input("Digite um número: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
print(f"Analizando o número {num}...")
print(f"A unidade de {num} é {u}")
print(f"A dezena de {num} é {d}")
print(f"A centena de {num} é {c}")
