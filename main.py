from personnage import personnage
from Menu import *
import pygame

#Const
TITLE = "Epic Noob Battle"
PATH_BACKGROUND = 'assets/background.gif'
PATH_R_ARROW = 'assets/right-arrow.png'
PATH_ARROW = 'assets/icons/Arrow.svg'
PATH_LOGO = 'assets/logoV2.png'
SCREENSIZE = (1280, 630)
PERSONNAGES = ["bleu", 'blond', "brun", "noir", "rouge", "violet"]
PATH_POLY = 'assets/icons/poly.svg'

#init pygame
pygame.init()

pygame.display.set_caption(TITLE)
screen = pygame.display.set_mode(SCREENSIZE)


#init Menu
menu = Menu()
menu.loadMenuIntro(PATH_LOGO)
menu.loadRules(PATH_ARROW)
background = menu.loadBackground(PATH_BACKGROUND)
menu.loadArrow(PATH_R_ARROW)
menu.loadMenuOptions(PATH_POLY, PATH_ARROW)


#Ajout des personnages
for name in PERSONNAGES:
  menu.loadPersonnage(personnage(name))

running = True

while running:
  menu.show(screen, SCREENSIZE)
  pygame.display.flip()

  for event in pygame.event.get():
    menu.onEvent(event, SCREENSIZE)
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")