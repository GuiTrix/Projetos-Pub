nascimento = int(input("Digite o ano de seu nascimento: "))
idade = 2025 - nascimento
ts = 18 - idade
tp = idade - 18

if idade <= 17:
  print(f"Você não tem idade suficiente para se alistar, mas podera em {ts} anos!")
elif idade == 18:
  print(f"Você tem {idade} anos e já é hora de se alistar!")
else:
  print(f"Você tem {idade} anos e passou {tp} anos que você deveria se alistar!")