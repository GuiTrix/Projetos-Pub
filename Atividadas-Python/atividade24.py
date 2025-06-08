#crie um programa que ve se o cara nasceu em alguma cidade q comeca com santo

q_city = str(input("Digite a cidade que você nasceu: ")).strip()
print(q_city[:5].upper() == 'SANTO')