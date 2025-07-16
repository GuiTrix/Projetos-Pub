b1 = float(input("Digite a sua nota do primeiro Bimestre: "))
b2 = float(input("Digite a sua nota do segundo Bimestre: "))
b3 = float(input("Digite a sua nota do terceiro Bimestre: "))
b4 = float(input("Digite a sua nota do quarto Bimestre: "))

soma = b1 + b2 + b3 + b4
media = soma / 4

if media >= 7:
  print(f"Parabéns, Você foi aprovado com a média de {media}!")
elif media >= 5:
  print(f"Sua média foi {media} e você ficou de recuperação!")
else:
  print(f"Sua média foi {media} e você reprovou!")