from Menu import *
from personnage import personnage
import pygame


class Game:
    def __init__(self):
        # Est ce que le jeu est lancé ou pas ?
        self.is_launched = False
        self.players = set()
        self.player1 = 0
        self.player2 = 0
        self.manche = 1

    def setPlayer(self, players):
        self.players = players

    def loadText(self, size, text):
        font = pygame.font.SysFont(None, 64)
        img = font.render(text, True, "WHITE")
        return img

    def show(self, screen, screenSize):
        for self.manche in range(5):
            ps = list(self.players)
            screen.blit(ps[self.player1].image,((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
            screen.blit(self.loadText(64, 'Suivant'), (screenSize[0] / 2 - 100, 530))

    def onEvent(self, event, screenSize):
        pass

    #Fonction Vie

    #Fonction GameOver

    #Fonction attribution des cartes

    #Fonction Manche