# import pygame
# pygame.init()
# pygame.mixer.music.load('musica.mp3')
# pygame.mixer.music.play()
# pygame.event.wait()

import pygame
import time

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
time.sleep(10)
pygame.mixer.music.fadeout(5000)

