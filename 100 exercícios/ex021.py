# Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init() #inicializa todos os módulos da biblioteca

pygame.mixer.music.load('musica1.mp3') #localiza um arquivo de audio com a função load
pygame.mixer.music.play() #faz com que a musica comece a ser tocada com a função play
pygame.event.wait() # Esse comando faz com que o script espere até que um evento (uma ação do usuário) ocorra. Ele é útil para manter o script ativo enquanto a música toca.
input() #Pausa a execução do script e espera que o usuário pressione Enter