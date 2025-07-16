Nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2025 - Nascimento

if idade <= 9:
  print(f"Você tem {idade} anos e irá participar pela categoria Mirim!")
elif idade <= 14:
  print(f"Você tem {idade} anos e irá participar pela categoria Infantil!")
elif idade <= 19:
  print(f"Você tem {idade} anos e irá participar pela categoria Junior!")
elif idade == 20:
  print(f"Você tem {idade} anos e irá participar pela categoria Sênior!")
else:
  print(f"Você tem {idade} anos e irá participar pela categora Master!")