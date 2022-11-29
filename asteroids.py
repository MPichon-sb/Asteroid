#Initialisation

import random
from pygame.math import Vector2
import core


#Premiere partie

#Afficher fenetre de jeu
def setup():
    print("Setup START---------")
    core.fps = 30
    core.WINDOW_SIZE = [1200, 1000]
    core.memory("position",vector2(400,400))
    core.memory("position",vector2(1, 0))

    print("Setup END-----------")

def run():
    core.cleanScreen()



#Afficher vaisseau




P1= core.memory("position")+core.memory("vitesse").rotate(90).scaletolenght(10)
P2= core.memory("position")+core.memory("vitesse").scaletolenght(40)
P3= core.memory("position")+core.memory("vitesse").rotate(-90).scaletolenght(10)

core.Draw((255,0,0),(P1,P2,P3))




#Mobilité

#Tir

#Apparition d'asteroide

#Hitbox

#Score

#Seconde partie





core.main(setup, run)