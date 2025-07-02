valorc = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual é seu salário? R$"))
anos = int(input("Quantos anos você irar demorar para pagar?"))
prestação =  valorc / (anos * 12)
minimo = salario * 30 / 100

print("O valor da prestação ficou em {:.2f}! Então o empréstimo foi...".format(prestação))
print("carregando...")

if prestação <= minimo:
  print("O empréstimo foi concedido.")
else:
  print("O empréstimo foi recusado!")
