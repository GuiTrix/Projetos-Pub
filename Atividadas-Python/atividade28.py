from random import randint
computador = randint(0, 5) 
print("===-===" * 20)
print("Pensando em um número entre 0 e 5...")
print("===-===" * 20)
jogador = int(input("Qual número eu pensei? "))

if jogador == computador:
  print("Parabéns você ganhou! cagada em")
else:
  print("Ganheiii, iihuu não foi dessa vez")  
  print("Pensei no {} haha".format(computador))