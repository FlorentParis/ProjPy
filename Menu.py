import pygame
from personnage import personnage

class Menu:
  '''
  Menu va afficher le menu, gérer la selection des perso, lancer le jeu
  '''
  INTRO = 0
  SELECT = 1
  REGLES = 2
  OPTION = 3
  INGAME = 4

  def __init__(self):
    self.background = None
    self.lArrow = None
    self.rArrow = None
    self.logo = None
    self.btnStart = None
    #ratio positionnement fléches
    self.btnStartSize = (450, 81)
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
    self.rArrow = pygame.transform.scale(self.rArrow, self.arrowSize)
    self.lArrow = pygame.transform.flip(self.rArrow, True, False)

  def loadMenuIntro(self, pathLogo, pathBtnStart):
    self.logo = pygame.image.load(pathLogo)
    self.logo = pygame.transform.scale(self.logo, (500, 350))

  def loadMenuText(self, text):
    font = pygame.font.SysFont(None, 64)
    img = font.render(text, True, "WHITE")
    return img

  def show(self, screen, screenSize):
    #Affichage du background
    screen.blit(self.background, (0, 0))
    #Menu Intro
    if self.state == Menu.INTRO:
      screen.blit(self.logo, (screenSize[0]/2 - 250, 5))
      screen.blit(self.loadMenuText('JOUER'), (screenSize[0]/2 - 75, 350))
      screen.blit(self.loadMenuText('REGLES'), (screenSize[0]/2 - 90, 410))
      screen.blit(self.loadMenuText('OPTIONS'), (screenSize[0]/2 - 105, 470))
      screen.blit(self.loadMenuText('QUITTER'), (screenSize[0]/2 - 100, 530))
    #Menu selection perso
    elif self.state == Menu.SELECT:
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsLeft[0][0], screenSize[1]*self.arrowsLeft[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsLeft[1][0], screenSize[1]*self.arrowsLeft[1][1]))
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsRight[0][0], screenSize[1]*self.arrowsRight[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsRight[1][0], screenSize[1]*self.arrowsRight[1][1]))
      screen.blit(self.loadMenuText('CHOISISSEZ VOTRE PERSONNAGE :'), (screenSize[0]/2 - 400, 25))
      screen.blit(self.loadMenuText('CONFIRMER'), (screenSize[0]/2 - 150, 575))
      if self.players != set():
        ps = list(self.players)
        screen.blit(ps[self.playerIndex1].image, ((screenSize[0]*3/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/6))
        screen.blit(ps[self.playerIndex2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
    #elif self.state == Menu.REGLES:
      #afficher régles du jeu
    #elif self.state == Menu.OPTION:
      #afficher les options


  def loadPersonnage(self, player):
    self.players.add(player)

  @staticmethod
  def isOnBtn(mx, my, btnSize, bx, by):
    '''
      Retourne vrai si mx, my est dans le rectangle de la fléche
    '''
    return mx < bx + btnSize[0] and mx > bx and my < by + btnSize[1] and my > by

  def onEvent(self, event, screenSize):
    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
      (mouseX, mouseY) = event.pos
      if self.state == Menu.INTRO:
        #bouton jouer
        if self.isOnBtn(mouseX, mouseY, [175, 64], screenSize[0]/2 - 75, 350):
          self.state = Menu.SELECT
        #bouton regles
        elif self.isOnBtn(mouseX, mouseY, [200, 64], screenSize[0]/2 - 90, 410):
          self.state = Menu.REGLES
        #bouton options
        elif self.isOnBtn(mouseX, mouseY, [200, 64], screenSize[0]/2 - 105, 470):
          self.state = Menu.OPTION
        #bouton quitter
        elif self.isOnBtn(mouseX, mouseY, [200, 64], screenSize[0]/2 - 100, 530):
          pygame.quit()
          print("Fermeture du jeu")
      elif self.state == Menu.SELECT:
        #fléche gauche 1
        if self.isOnBtn(mouseX, mouseY, self.arrowSize, screenSize[0] * self.arrowsLeft[0][0],
                        screenSize[1] * self.arrowsLeft[0][1]):
          self.playerIndex1-=1
          #fléche gauche2
        elif self.isOnBtn(mouseX, mouseY, self.arrowSize, screenSize[0] * self.arrowsLeft[1][0],
                          screenSize[1] * self.arrowsLeft[1][1]):
          self.playerIndex1+=1
          #fleche droite 1
        elif self.isOnBtn(mouseX, mouseY, self.arrowSize, screenSize[0] * self.arrowsRight[0][0],
                          screenSize[1] * self.arrowsRight[0][1]):
          self.playerIndex2-=1
          #fleche droite 2
        elif self.isOnBtn(mouseX, mouseY, self.arrowSize, screenSize[0] * self.arrowsRight[1][0],
                          screenSize[1] * self.arrowsRight[1][1]):
          self.playerIndex2+=1
        elif self.isOnBtn(mouseX, mouseY, [175, 64], screenSize[0]/2 - 150, 575):
          self.state = Menu.INGAME

        size = len(self.players)-1
        if self.playerIndex1 < 0:
          self.playerIndex1 = size
        if self.playerIndex1 > size:
          self.playerIndex1 = 0
        if self.playerIndex2 < 0:
          self.playerIndex2 = size
        if self.playerIndex2 > size:
          self.playerIndex2 = 0