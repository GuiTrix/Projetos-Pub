#Crie um programa que leia um valor em metros e converta para centimetros e milimetros!

metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
milimetros = metros * 1000

print(f"Olá, você tem {metros}m mas convertido você tem {centimetros}cm e {milimetros}mm.")