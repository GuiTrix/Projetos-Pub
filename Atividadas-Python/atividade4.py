#Crie um programa que mostre o tipo primitivo de algo e outras informações

algo = input("Digite algo: ")
print("O tipo primitivo é", type(algo))
print("É um número?", algo.isnumeric())
print("É alfabético?", algo.isalpha())
print("É alphanúmerico?", algo.isalnum())
print("Está toda com espaços?", algo.isspace())
print("Está toda em maisculas?", algo.isupper())
print("Está toda em minusculas?", algo.islower())
print("Está toda capitalizada?", algo.istitle())