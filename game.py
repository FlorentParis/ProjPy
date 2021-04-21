from personnage import personnage
import pygame


class Game:
    def __init__(self):
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
        ps = list(self.players)
        if ps[self.player1].health > 0 and ps[self.player2].health > 0:
            #Afficher une phrase aléa
            #if self.manche == 1 :
                #Appel fonction attribution carte x5 pour chaque joueur
            #else:
                #Attribuer qu'une carte a chaque joueur
            screen.blit(self.loadText(64, f"Manche {self.manche}"), (screenSize[0] / 2 - 400, 25))
            print(ps[self.player1].health)
            screen.blit(ps[self.player1].image,((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
            #TODO a mettre dans une autre fonction (a mettre apres avoir choisie le gagnant
            screen.blit(self.loadText(64, 'Manche suivante'), (screenSize[0] / 2 - 100, 530))
        else:
            screen.blit(self.loadText(64, f"Game over"), (screenSize[0] / 2 - 400, 25))


    def setNextManche(self):
        self.manche += 1
        #appel de la fonction vie ou sinn on rédit la vie directement ici
