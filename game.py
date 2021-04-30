import Cartes
from personnage import personnage
import pygame



class Game:

    FOND = pygame.Color(87, 95, 65)
    CLAIR = pygame.Color(140, 156, 93)

    def __init__(self):
        self.tourPlayer1 = True #Si True = tour du player1, sinon tour du player 2
        self.viewLifeP1 = 360
        self.viewLifeP2 = 360
        self.players = set()
        self.player1 = 0
        self.player2 = 0
        self.phrase = Cartes.Phrase
        self.deckPlayer1 = Cartes.deckPlayer1
        self.deckPlayer2 = Cartes.deckPlayer2
        self.manche = 1
        self.choixPlayer1 = ""
        self.choixPlayer2 = ""

    def setPlayer(self, players):
        self.players = players

    #Fonction deja existante dans Menu.py, faire un import
    #Affiche un texte en blanc
    def loadText(self, size, text):
        font = pygame.font.SysFont(None, size)
        img = font.render(text, True, "WHITE")
        return img

    #Affiche un texte noir
    def loadTextV2(self, size, text):
        font = pygame.font.SysFont(None, size)
        img = font.render(text, True, "BLACK")
        return img

    #Fonction qu'on appelera a chaque début de manche, affiche la vie restant des joueurs
    def loadHealth(self, screen, screenSize):
        #Affichage Vie de base (gris)
        pygame.draw.rect(screen, Game.FOND, (screenSize[0] / 12, screenSize[1] / 24, 360, 15))
        pygame.draw.rect(screen, Game.FOND, (screenSize[0] / 2 + screenSize[0] / 7, screenSize[1] / 24, 360, 15))
        #Affichage Vie restant (vert)
        pygame.draw.rect(screen, Game.CLAIR,(screenSize[0] / 12, screenSize[1] / 24, self.viewLifeP1, 15))
        pygame.draw.rect(screen, Game.CLAIR, (screenSize[0] / 2 + screenSize[0] / 7, screenSize[1] / 24, self.viewLifeP2, 15))

    def loadPhrase(self, screen, screenSize):
        Cartes.aleaPhrase()
        pygame.draw.rect(screen,(0,0,0),(screenSize[0] / 2 - 120,screenSize[1] / 2 -160,240,320))
        screen.blit(self.loadText(24, self.phrase[0]), (screenSize[0] / 2 - 160, screenSize[1] / 2))

    def loadMots(self, screen, screenSize, deck):
        Cartes.aleaMots()
        i = 0
        dispoMots = [(screenSize[0] / 2 - 660, screenSize[1] / 2 + 240), (screenSize[0] / 2 - 390, screenSize[1] / 2 + 240), (screenSize[0] / 2 - 120, screenSize[1] / 2 + 240), (screenSize[0] / 2 + 150, screenSize[1] / 2 + 240), (screenSize[0] / 2 + 420, screenSize[1] / 2 + 240)]
        pygame.draw.rect(screen, (255,255,255), (screenSize[0] / 2 - 660, screenSize[1] / 2 + 240, 240, 320))
        pygame.draw.rect(screen, (255,255,255), (screenSize[0] / 2 - 390, screenSize[1] / 2 + 240, 240, 320))
        pygame.draw.rect(screen, (255,255,255), (screenSize[0] / 2 - 120, screenSize[1] / 2 + 240, 240, 320))
        pygame.draw.rect(screen, (255,255,255), (screenSize[0] / 2 + 150, screenSize[1] / 2 + 240, 240, 320))
        pygame.draw.rect(screen, (255,255,255), (screenSize[0] / 2 + 420, screenSize[1] / 2 + 240, 240, 320))
        for mots in deck:
            screen.blit(self.loadTextV2(24, mots), dispoMots[i])
            i += 1

    def show(self, screen, screenSize):
        ps = list(self.players)
        self.loadHealth(screen, screenSize)
        if ps[self.player1].health > 0 and ps[self.player2].health > 0:
            #Donne une phrase aléatoire et l'affiche
            self.loadPhrase(screen, screenSize)
            print(self.choixPlayer1)
            #Donne des mots aléatoire et les affiches
            if (self.tourPlayer1):
                self.loadMots(screen, screenSize, self.deckPlayer1)
            else:
                self.loadMots(screen, screenSize, self.deckPlayer2)
            screen.blit(self.loadText(64, f"Manche {self.manche}"), (screenSize[0] / 2, screenSize[1] / 2))
            #Affichae des noms + image du joueur
            screen.blit(self.loadText(24, ps[self.player1].name), (screenSize[0] / 12, screenSize[1] / 12))
            screen.blit(self.loadText(72, 'VS'), (screenSize[0] / 2 - 36, screenSize[1] / 24))
            screen.blit(self.loadText(24, ps[self.player2].name), (screenSize[0] - screenSize[0] / 6, screenSize[1] / 12))
            screen.blit(ps[self.player1].image,((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
            #TODO a mettre dans une autre fonction (a mettre apres avoir choisie le gagnant
            screen.blit(self.loadText(64, 'Manche suivante'), (screenSize[0] / 2 - 100, 530))
        else:
            #TODO Afficher Texte + Gagnant
            screen.blit(self.loadText(64, f"Victoire"), (screenSize[0] * 5 / 12, screenSize[1]* 1/6))
            if ps[self.player1].health == 0:
                screen.blit(ps[self.player2].image, ((screenSize[0] * 6 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            else:
                screen.blit(ps[self.player1].image, ((screenSize[0] * 6 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1 / 6]))

    def onEvent(self, screenSize, mouseX, mouseY):
        from Menu import Menu
        if Menu.isOnBtn(mouseX, mouseY, [400, 64], screenSize[0]/2 - 100, 530):
          self.setNextManche()
        #Interaction Cartes deck Player2
        if (self.tourPlayer1):
            if Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 660, screenSize[1] / 2 + 240):
                self.choixPlayer1 = self.deckPlayer1[0]
                self.tourPlayer1 = False
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 390, screenSize[1] / 2 + 240):
                self.choixPlayer1 = self.deckPlayer1[1]
                self.tourPlayer1 = False
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 120, screenSize[1] / 2 + 240):
                self.choixPlayer1 = self.deckPlayer1[2]
                self.tourPlayer1 = False
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 + 150, screenSize[1] / 2 + 240):
                self.choixPlayer1 = self.deckPlayer1[3]
                self.tourPlayer1 = False
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 + 420, screenSize[1] / 2 + 240):
                self.choixPlayer1 = self.deckPlayer1[4]
                self.tourPlayer1 = False
        else: #Interaction Cartes deck Player2
            if Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 660, screenSize[1] / 2 + 240):
                self.choixPlayer2 = self.deckPlayer2[0]
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 390, screenSize[1] / 2 + 240):
                self.choixPlayer2 = self.deckPlayer2[1]
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 120, screenSize[1] / 2 + 240):
                self.choixPlayer2 = self.deckPlayer2[2]
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 + 150, screenSize[1] / 2 + 240):
                self.choixPlayer2 = self.deckPlayer2[3]
            elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 + 420, screenSize[1] / 2 + 240):
                self.choixPlayer2 = self.deckPlayer2[4]

    def setNextManche(self):
        ps = list(self.players)
        self.manche += 1
        if len(self.phrase) == 1:
            del self.phrase[-1]
        #A mettre dans une autre fonction qu'on appelera en fonction du perdant (param player)
        ps[self.player1].health -= 10
        print(ps[self.player1].health)
        self.viewLifeP1 -= 120