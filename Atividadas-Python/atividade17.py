#faça um programa q calcule a hipotenusa

import math

cateto_oposto = float(input("Digite o cateto oposto"))
cateto_adjacente = float(input("Digite o cateto adjacente"))
hipotenusa = math.sqrt(cateto_oposto**2 + cateto_adjacente**2)

print(f"A hipotenusa é igual a {hipotenusa}")