#Faça um programa que faz desconto de produtos

preço = float(input("Qual o preço do produto? R$"))
desconto = preço * (5/100)
preço_final = preço - desconto

print("O seu produto que antes custava R${}, na promoção com 5% de desconto  ficou por R${:.2f}".format(preço, preço_final))