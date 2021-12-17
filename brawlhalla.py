import pygame
from pygame.locals import *
pygame.init()
screen = pygame.display.set_mode((1000, 1000))
running = True
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
background = GRAY
key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE,
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}
while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
                screen.fill(background)
                pygame.display.update()
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
