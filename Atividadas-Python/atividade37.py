numero = int(input("Escreva um número: "))
x = numero
binario = bin(x)[2:]       
octal = oct(x)[2:]         
hexadecimal = hex(x)[2:]   
print("Basses de conversão:\n1 para binário\n2 para octal\n3 para hexadecimal\n\n")
tconversao = int(input("Qual base de  conversão você quer? "))

if tconversao == 1:
  print(f"O número {numero} convertido para binário é: {binario}")
elif tconversao == 2:
  print(f"O número {numero} convertido para octal é: {octal}")
elif tconversao == 3:
  print(f"O número {numero} convertido para hexadecimal é: {hexadecimal}")
else:
  print("Opção invalida, por favor selecione 1, 2 ou 3!")