import pygame

from game import Game
from personnage import personnage

game = Game()
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
    self.music = 5
    self.effect = 5
    self.language = 'fr'

  def loadBackground(self, pathBackground):
    self.background = pygame.image.load(pathBackground)
    return self.background

  def loadArrow(self, pathArrowR):
    self.rArrow = pygame.image.load(pathArrowR)
    self.rArrow = pygame.transform.scale(self.rArrow, self.arrowSize)
    self.lArrow = pygame.transform.flip(self.rArrow, True, False)

  def loadMenuIntro(self, pathLogo):
    self.logo = pygame.image.load(pathLogo)
    self.logo = pygame.transform.scale(self.logo, (500, 300))

  def loadRules(self, pathArrow):
    self.arrow = pygame.image.load(pathArrow)
    self.arrow = pygame.transform.scale(self.arrow, (60, 50))

  def loadMenuOptions(self, pathPoly, pathArrow):
    self.polyL = pygame.image.load(pathPoly)
    self.polyL = pygame.transform.rotate(self.polyL, 180)
    self.polyR = pygame.image.load(pathPoly)
    self.arrow = pygame.image.load(pathArrow)
    self.arrow = pygame.transform.scale(self.arrow, (60, 50))

  def loadMenuText(self, size, text):
    font = pygame.font.SysFont(None, size)
    img = font.render(text, True, "WHITE")
    return img

  def show(self, screen, screenSize):
    #Affichage du background
    screen.blit(self.background, (0, 0))
    #Menu INTRO
    if self.state == Menu.INTRO:
      screen.blit(self.logo, (screenSize[0]/2 - 250, 5))
      screen.blit(self.loadMenuText(64, 'JOUER'), (screenSize[0]/2 - 75, 350))
      screen.blit(self.loadMenuText(64, 'REGLES'), (screenSize[0]/2 - 90, 410))
      screen.blit(self.loadMenuText(64, 'OPTIONS'), (screenSize[0]/2 - 105, 470))
      screen.blit(self.loadMenuText(64, 'QUITTER'), (screenSize[0]/2 - 100, 530))
    #Menu SELECT
    elif self.state == Menu.SELECT:
      screen.blit(self.loadMenuText(64, 'CHOISISSEZ VOTRE PERSONNAGE :'), (screenSize[0]/2 - 400, 25))
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsLeft[0][0], screenSize[1]*self.arrowsLeft[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsLeft[1][0], screenSize[1]*self.arrowsLeft[1][1]))
      screen.blit(self.lArrow, (screenSize[0]*self.arrowsRight[0][0], screenSize[1]*self.arrowsRight[0][1]))
      screen.blit(self.rArrow, (screenSize[0]*self.arrowsRight[1][0], screenSize[1]*self.arrowsRight[1][1]))
      if self.players != set():
        ps = list(self.players)
        screen.blit(ps[self.playerIndex1].image, ((screenSize[0]*3/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/6))
        screen.blit(ps[self.playerIndex2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
    #Menu REGLES
    elif self.state == Menu.REGLES:
      screen.blit(self.arrow, (10, 10))
      """ Voir plus tard pour tout afficher en un seul blit. """
      screen.blit(self.loadMenuText(64, 'REGLES'), (screenSize[0]/2 - 100, 20))
      screen.blit(self.loadMenuText(48, "Chaque joueur reçoit 3 cartes blanches."), (screenSize[0]/2 - 350, 100))
      screen.blit(self.loadMenuText(48, "Une carte noire est dévoilée (texte à trou)."), (screenSize[0]/2 - 350, 150))
      screen.blit(self.loadMenuText(48, "Chacun son tour, les joueurs choisissent"), (screenSize[0]/2 - 350, 200))
      screen.blit(self.loadMenuText(48, "une carte blanche afin de compléter la phrase."), (screenSize[0]/2 - 350, 235))
      screen.blit(self.loadMenuText(48, "Les joueurs se concerteront apres pour"), (screenSize[0]/2 - 350, 285))
      screen.blit(self.loadMenuText(48, "désigner le gagnant de cette manche !"), (screenSize[0]/2 - 350, 320))
      screen.blit(self.loadMenuText(48, "A la fin de la manche, chaque joueur repioche une"), (screenSize[0]/2 - 350, 370))
      screen.blit(self.loadMenuText(48, "nouvelle carte."), (screenSize[0]/2 - 350, 405))
      screen.blit(self.loadMenuText(48, "Afin de remporter la partie, il faut enlever"), (screenSize[0]/2 - 350, 455))
      screen.blit(self.loadMenuText(48, "tout les points de vie de l’adversaire."), (screenSize[0]/2 - 350, 500))
    elif self.state == Menu.OPTION:
      screen.blit(self.arrow, (10, 10))
      screen.blit(self.loadMenuText(64, 'OPTIONS'), (screenSize[0]/2 - 100, 20))
      screen.blit(self.loadMenuText(48, 'MUSIQUE'), (screenSize[0]/2 - 300 , screenSize[1]/2 - 95))
      screen.blit(self.polyL, (screenSize[0]/2 , screenSize[1]/2 - 100))
      screen.blit(self.loadMenuText(48, str(self.music)), (screenSize[0]/2 + 110 , screenSize[1]/2 - 95))
      screen.blit(self.polyR, (screenSize[0]/2 + 200, screenSize[1]/2 - 100))
      screen.blit(self.loadMenuText(48, 'EFFETS'), (screenSize[0]/2 - 300, screenSize[1]/2 + 5))
      screen.blit(self.polyL, (screenSize[0]/2 , screenSize[1]/2))
      screen.blit(self.loadMenuText(48, str(self.effect)), (screenSize[0]/2 + 110 , screenSize[1]/2 + 5))
      screen.blit(self.polyR, (screenSize[0]/2 + 200, screenSize[1]/2))
      screen.blit(self.loadMenuText(48, 'LANGUE'), (screenSize[0]/2 - 300, screenSize[1]/2 + 105))
      screen.blit(self.polyL, (screenSize[0]/2 , screenSize[1]/2 + 100))
      screen.blit(self.loadMenuText(48, self.language), (screenSize[0]/2 + 110 , screenSize[1]/2 + 105))
      screen.blit(self.polyR, (screenSize[0]/2 + 200, screenSize[1]/2 + 100))
    elif self.state == Menu.INGAME:
      game.setPlayer(self.players)
      game.show(screen, screenSize)
      #afficher les options


  def loadPersonnage(self, player):
    self.players.add(player)

  @staticmethod
  def isOnBtn(mx, my, btnSize, bx, by):
    '''
      Retourne vrai si mx, my est dans l'élément.
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
        #btn commencer
        elif self.isOnBtn(mouseX, mouseY, [175, 64], screenSize[0]/2 - 150, 575):
          game.player1 = self.playerIndex1
          game.player2 = self.playerIndex2
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
      elif self.state == Menu.INGAME:
        game.onEvent(event, screenSize)
      elif self.state == Menu.REGLES:
        if self.isOnBtn(mouseX, mouseY, (60, 50), 10, 10):
          self.state = Menu.INTRO
      elif self.state == Menu.OPTION:
        if self.isOnBtn(mouseX, mouseY, (60, 50), 10, 10):
          self.state = Menu.INTRO

