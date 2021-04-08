import pygame
from personnage import personnage

class Menu:
  '''
  Menu va afficher le menu, gérer la selection des perso, lancer le jeu
  '''
  INTRO = 0
  SELECT = 1
  INGAME = 2

  def __init__(self):
    self.background = None
    self.lArrow = None
    self.rArrow = None
    #ratio positionnement fléches
    self.arrowsLeft = ((1/12, 1/2), (5/12, 1/2))
    self.arrowsRight = ((7/12, 1/2), (11/12, 1/2))
    self.arrowSize = (100, 100)
    self.players = set()
    self.playerIndex1 = 0
    self.playerIndex2 = 0
    self.state = Menu.INTRO

  def loadBackground(self, pathBackground):
    self.background = pygame.image.load(pathBackground)
    return self.background

  def loadArrow(self, pathArrowR):
    self.rArrow = pygame.image.load(pathArrowR)
    self.rArrow = pygame.transform.scale(self.rArrow, (100, 100))
    self.lArrow = pygame.transform.flip(self.rArrow, True, False)

  def show(self, screen, screenSize):
    #Affichage du background
    screen.blit(self.background, (0, 0))
    #Menu Intro
    if self.state == Menu.INTRO:
      pass
      #met ton code ici
    #Menu selection perso
    elif self.state == Menu.SELECT:
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsLeft[0][0], screenSize[1]*self.arrowsLeft[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsLeft[1][0], screenSize[1]*self.arrowsLeft[1][1]))
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsRight[0][0], screenSize[1]*self.arrowsRight[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsRight[1][0], screenSize[1]*self.arrowsRight[1][1]))
      if self.players != set():
        ps = list(self.players)
        screen.blit(ps[self.playerIndex1].image, ((screenSize[0]*3/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/6))
        screen.blit(ps[self.playerIndex2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))

  def loadPersonnage(self, player):
    self.players.add(player)

  @staticmethod
  def isOnArrow(mx, my, arrowSize, ax, ay):
    '''
      Retourne vrai si mx, my est dans le rectangle de la fléche
    :param mx: mouse
    :param my:
    :param arrowSize: taille
    :param ax: arrows
    :param ay:
    '''
    return mx < ax+arrowSize[0] and mx > ax and my < ay+arrowSize[1] and my > ay

  def onEvent(self, event, screenSize):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      (mouseX, mouseY) = event.pos
      if self.state == Menu.SELECT:
        #fléche gauche 1
        if self.isOnArrow(mouseX, mouseY, self.arrowSize, screenSize[0]*self.arrowsLeft[0][0], screenSize[1]*self.arrowsLeft[0][1]):
          self.playerIndex1-=1
          #fléche gauche2
        elif self.isOnArrow(mouseX, mouseY, self.arrowSize, screenSize[0]*self.arrowsLeft[1][0], screenSize[1]*self.arrowsLeft[1][1]):
          self.playerIndex1+=1
          #fleche droite 1
        elif self.isOnArrow(mouseX, mouseY, self.arrowSize, screenSize[0]*self.arrowsRight[0][0], screenSize[1]*self.arrowsRight[0][1]):
          self.playerIndex2-=1
        elif self.isOnArrow(mouseX, mouseY, self.arrowSize,screenSize[0]*self.arrowsRight[1][0], screenSize[1]*self.arrowsRight[1][1]):
          self.playerIndex2+=1

        size = len(self.players)-1
        if self.playerIndex1 < 0:
          self.playerIndex1 = size
        if self.playerIndex1 > size:
          self.playerIndex1 = 0
        if self.playerIndex2 < 0:
          self.playerIndex2 = size
        if self.playerIndex2 > size:
          self.playerIndex2 = 0



      




