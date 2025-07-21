preco_normal = float(input("Qual o preço do produto? R$"))
print("==" * 20)
print(F"FORMA DE PAGAMENTO?")
print(f"[ 1 ] à vista em dinheiro ou pix\n[ 2 ] à vista no cartão de débito\n[ 3 ] 2x no cartão de crédito\n[ 4 ] 3x no cartão de crédito")
selecionado = int(input(f"Qual a forma de pagamento? \n"))

if selecionado == 1:
  op1 = (preco_normal * 10) / 100
  final1 = preco_normal - op1
  print(f"Como a compra irá ser à vista você ganhou 10% de desconto!, sua compra ficou R${final1}")
if selecionado == 2:
  op2 = (preco_normal * 5) / 100
  final2 = preco_normal - op2
  print(f"Como a compra irá ser à vista você ganhou 15% de desconto!, sua compra ficou R${final1}")
if selecionado == 3:
  op3 = preco_normal / 2
  print(f"Você irá pagar duas parcelas de R${op3}")
if selecionado == 4:
  op4 = (preco_normal * 20) / 100
  final4 = preco_normal + op4
  print(f"Você irá pagar três parcelas de R${final4}")
else:
  print("Número invalido")