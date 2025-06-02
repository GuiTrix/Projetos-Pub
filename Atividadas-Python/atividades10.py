#Crie um programa que converte as moedas exemplo US$
#Dolar hoje dia 6/02/2025 está R$5,67

reais = float(input("Digite o valor que você pretende converter: R$"))
dolar = reais / 5.67

print("Você possui R${} e pode comprar US${:.2f}!".format(reais, dolar))
