frase =  str(input("Digite uma frase: ")).strip()
frase1 = frase.upper().count("A")
frase2 = frase.upper().find("A")+1
frase3 = frase.upper().rfind("A")+1
print(f"A letra A, aparece {frase1} vezes")
print(f"A Primeira letra A apareceu na posição {frase2}")
print(f"A ultima letra A apareceu na posição {frase3}")