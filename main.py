#This game was created by Maxwell Penders and Jett Rosner

### Imports ###
import sys
import pygame as pg
from pygame.locals import *

import classes
import const
import simpl_functions as smplfn

if not pg.font:
    print("Warning, fonts disabled")
if not pg.mixer:
    print("Warning, sound disabled")

### Neccessary Variables and Loops ###
# Sets our display window
screen = pg.display.set_mode(const.window_size, pg.SCALED)

objects = []
player = smplfn.load_image("images/knight_image_sprite.jpg")
player = pg.transform.scale(player, (300, 300))
background = smplfn.load_image("images/liquid.jpg")
background = pg.transform.scale(background, const.window_size)
objects.append(classes.GameObject(player, 0, const.window_size[1]//2 - 150, (10,0)))

### Main Code ###

# Initializes all pygame modules
pg.init()

screen.blit(background, (0,0))

pg.display.update()
### Full loop ###

while True:
    for event in pg.event.get():
        # Adds exit case
        if event.type in (QUIT, KEYDOWN):
            sys.exit()
    for o in objects:
        screen.blit(background, o.pos, o.pos)
    for o in objects:
        o.move()
        screen.blit(o.image, o.pos)

    pg.display.update()
    pg.time.delay(100)