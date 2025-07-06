km = float(input("Qual a distancia da sua viagem em km? "))
kmC = km * 0.50
kmB = km * 0.45

if km <= 200:
  print(f"Olá, o preço da passagem ficou R${kmC}")
else:
  print(f"Olá, o preço da passagem ficou R${kmB}, pois viagens longas são mais baratas")