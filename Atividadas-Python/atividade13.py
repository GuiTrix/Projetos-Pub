#Faça um programa que calcule a o valor de um salario de um funcionario e de um aumento de uma valor selecionado

salario_antigo = float(input("Qual o valor do salário antigo dele? R$"))
porcentagem = float(input("Quantos porcento de aumento você pretende dar?"))
aumento = salario_antigo * (porcentagem/100)
salario_novo = salario_antigo + aumento

print("Um funcionário que ganhava R${} agora passa a receber R${:.2f}!".format(salario_antigo, salario_novo))