import Cartes
from personnage import personnage
import pygame

FOND = pygame.Color(87, 95, 65)
CLAIR = pygame.Color(140, 156, 93)

class Game:
    def __init__(self):
        self.players = set()
        self.player1 = 0
        self.player2 = 0
        self.phrase = Cartes.Phrase
        self.deckPlayer1 = Cartes.deckPlayer1
        self.deckPlayer2 = Cartes.deckPlayer2
        self.manche = 1

    def setPlayer(self, players):
        self.players = players

    #Fonction deja existante dans Menu.py, faire un import
    def loadText(self, size, text):
        font = pygame.font.SysFont(None, size)
        img = font.render(text, True, "WHITE")
        return img

    def show(self, screen, screenSize):
        ps = list(self.players)
        if ps[self.player1].health > 0 and ps[self.player2].health > 0:
            Cartes.aleaMots()
            Cartes.aleaPhrase()
            self.displayPhrase(screen, screenSize)
            print(self.phrase)
            screen.blit(self.loadText(64, f"Manche {self.manche}"), (screenSize[0] / 2, screenSize[1] / 2))
            pygame.draw.rect(screen,FOND,(screenSize[0] / 12,screenSize[1] / 24,360,15))
            pygame.draw.rect(screen,CLAIR,(screenSize[0] / 12,screenSize[1] / 24,240,15))
            pygame.draw.rect(screen,FOND,(screenSize[0] / 2 + screenSize[0] / 7,screenSize[1] / 24,360,15))
            pygame.draw.rect(screen,CLAIR,(screenSize[0] / 2 + screenSize[0] / 7,screenSize[1] / 24,120,15))
            screen.blit(self.loadText(24, ps[self.player1].name), (screenSize[0] / 12, screenSize[1] / 12))
            screen.blit(self.loadText(72, 'VS'), (screenSize[0] / 2 - 36, screenSize[1] / 24))
            screen.blit(self.loadText(24, ps[self.player2].name), (screenSize[0] - screenSize[0] / 6, screenSize[1] / 12))
            screen.blit(ps[self.player1].image,((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
            #TODO a mettre dans une autre fonction (a mettre apres avoir choisie le gagnant
            screen.blit(self.loadText(64, 'Manche suivante'), (screenSize[0] / 2 - 100, 530))
        else:
            screen.blit(self.loadText(64, f"Game over"), (screenSize[0] / 2 - 400, 25))

    def setNextManche(self):
        self.manche += 1
        if len(self.phrase) == 1:
            del self.phrase[-1]
        #appel de la fonction vie ou sinn on rédit la vie directement ici

    #def displayCartes(self):
        #pass


    def displayPhrase(self, screen, screenSize):
        pygame.draw.rect(screen,(0,0,0),(screenSize[0] / 2 - 120,screenSize[1] / 2 -160,240,320))
        screen.blit(self.loadText(24, self.phrase[0]), (screenSize[0] / 2 - 160, screenSize[1] / 2))
