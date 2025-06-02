#Faça um programa q faça o dobro, triplo e raiz quadrada de um número

num = int(input("Digite um número: "))
dobro = num * 2
triplo = num * 3
raiz_Quadrada = num ** 0.5 #Lembre-se que raiz quadrada é 0.5!!!!

print("Seu número é {}\nO dobro é {}\nO triplo é {}\nE a raiz quadrada é {:.2f}".format(num, dobro, triplo, raiz_Quadrada))