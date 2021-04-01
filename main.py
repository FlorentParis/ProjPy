import pygame
pygame.init()

pygame.display.set_caption("Epic Noob Battle")
screen = pygame.display.set_mode((1280, 600))

background = pygame.image.load('assets/background.gif')

running = True

while running:
  screen.blit(background, (0,0))

  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
      pygame.quit()
      print("Fermeture du jeu")