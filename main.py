import pygame
from game import Game
pygame.init()

def menuIntro():
  logo = pygame.image.load('assets/logoV1.png')
  logo = pygame.transform.scale(logo, (800, 550))
  screen.blit(logo, (200,200))

pygame.display.set_caption("Epic Noob Battle")
screen = pygame.display.set_mode((1280, 600))

background = pygame.image.load('assets/background.gif')

running = True

while running:
  screen.blit(background, (0,0))

  menuIntro()

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")
