velo = float(input("Qual velocidade registrada no radar?  "))
valorKm = 7.00
VelocidadeKm = (velo - 80) * 7

if velo <= 80:
  print("Liberado, Velocidade normal")
else:
  print("O motorista foi multado em R${}, porque estava {}Km!/h".format(VelocidadeKm, velo))
