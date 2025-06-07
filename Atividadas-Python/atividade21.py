#faça o python tocar musica

import pygame
import time 

pygame.init()
file_path = 'att21.mp3'

try:
    pygame.mixer.music.load(file_path)
    print(f"Música '{file_path}' carregada com sucesso.")
    
    pygame.mixer.music.play()
    print("Música tocando... (irá parar em 176 segundos)")

    time.sleep(176) 

    pygame.mixer.music.stop()
    print("Música parada.")

except pygame.error as e:
    print(f"Erro ao carregar ou tocar a música: {e}")
    print("Verifique o caminho do arquivo e se ele não está corrompido.")
finally:
    pygame.quit() 
    print("Programa encerrado.")