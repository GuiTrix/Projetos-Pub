import random
Jogador = input("Selecione entre pedra, papel e tesoura: ")
computador = random.choice(["pedra", "papel", "tesoura"])

if Jogador == "tesoura" and computador == "papel":
  print(f"Parabéns você ganhou, Você jogou {Jogador} e eu joguei {computador}!")
elif Jogador == "papel" and computador == "pedra":
  print(f"Parabéns você ganhou, Você jogou {Jogador} e eu joguei {computador}!")
elif Jogador == "pedra" and computador == "tesoura":
  print(f"Parabéns você ganhou, Você jogou {Jogador} e eu joguei {computador}!")
elif Jogador == computador and computador == Jogador:
  print(f"Deu empate, pois nois dois jogamos {Jogador}")
else:
  print(f"Você perdeu, Você jogou {Jogador} e eu joguei {computador} hahaha!")