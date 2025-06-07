#crie um programa de alugueis de carros

dias = int(input("Quantos dias alugados? "))
km = float(input("Quantos km você rodou? "))
pagar = (dias * 60) + (km * 0.15)

print(F"Você precisa pagar R${pagar}")