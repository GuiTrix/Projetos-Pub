#Faça um programa que ajude pintores

largura = float(input("Qual a largura da parede? "))
altura = float(input("Qual a altura da parede? "))
area = largura * altura
tinta_necessaria = area / 2

print(f"Olá, sua parede tem a dimensão de {largura}x{altura} e sua área é de {area}m².\nPara pintar essa parede voçê precisa de {tinta_necessaria}l de tinta!")