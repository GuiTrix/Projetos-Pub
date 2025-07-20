altura = float(input("Qual sua altura? "))
peso = float(input("Qual seu peso atual? "))
imc = peso / (altura ** 2)

if imc < 18.5:
  print(f"Você tem {imc:.2f} de imc e está abaixo do peso")
elif imc < 25:
  print(f"Você tem {imc:.2f} de imc e está no peso ideal")
elif imc < 30:
  print(f"Você tem {imc:.2f} de imc e está sobrepeso")
elif imc < 40:
  print(f"Você tem {imc:.2f} de imc e está obeso!")
else:
  print(f"Você tem {imc:.2f} de imc e está na obesidade mórbida")