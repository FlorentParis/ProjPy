import Cartes
from personnage import personnage
import pygame
import time


class Game:

    FOND = pygame.Color(87, 95, 65)
    CLAIR = pygame.Color(140, 156, 93)

    def __init__(self):
        self.transActive = False
        self.timer = 0
        self.tourPlayer1 = True #Si True = tour du player1, sinon tour du player 2
        self.selectionGagnant = False #Si False n'affiche pas les résultat et désactive les Event
        self.viewLifeP1 = 360
        self.viewLifeP2 = 360
        self.players = set()
        self.player1 = 0
        self.player2 = 0
        self.phrase = Cartes.Phrase
        self.deckPlayer1 = Cartes.deckPlayer1
        self.deckPlayer2 = Cartes.deckPlayer2
        self.manche = 0
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
        if self.selectionGagnant:
            pygame.draw.rect(screen, (255, 255, 255), (screenSize[0] / 2 - 390, screenSize[1] / 2 + 240, 240, 320))
            pygame.draw.rect(screen, (255, 255, 255), (screenSize[0] / 2 - 120, screenSize[1] / 2 + 240, 240, 320))
            pygame.draw.rect(screen, (255, 255, 255), (screenSize[0] / 2 + 150, screenSize[1] / 2 + 240, 240, 320))
            screen.blit(self.loadTextV2(24, self.choixPlayer1), (screenSize[0] / 2 - 390, screenSize[1] / 2 + 240))
            screen.blit(self.loadTextV2(24, "Egalité"), (screenSize[0] / 2 - 120, screenSize[1] / 2 + 240))
            screen.blit(self.loadTextV2(24, self.choixPlayer2), (screenSize[0] / 2 + 150, screenSize[1] / 2 + 240))
        else:
            i = 0
            dispoMots = [(screenSize[0] * 1 / 36, screenSize[1] - screenSize[1] /8), (screenSize[0] * 8 / 36, screenSize[1] - screenSize[1] /8), (screenSize[0] * 5 / 12, screenSize[1] - screenSize[1] /8), (screenSize[0] * 22 / 36, screenSize[1] - screenSize[1] /8), (screenSize[0] * 29 / 36, screenSize[1] - screenSize[1] /8)]
            pygame.draw.rect(screen, (255,255,255), (screenSize[0] * 1 / 36, screenSize[1] - screenSize[1] /8, screenSize[0] /6, 320))
            pygame.draw.rect(screen, (255,255,255), (screenSize[0] * 8 / 36, screenSize[1] - screenSize[1] /8, screenSize[0] /6, 320))
            pygame.draw.rect(screen, (255,255,255), (screenSize[0] * 5 / 12, screenSize[1] - screenSize[1] /8, screenSize[0] /6, 320))
            pygame.draw.rect(screen, (255,255,255), (screenSize[0] * 22 / 36, screenSize[1] - screenSize[1] /8, screenSize[0] /6, 320))
            pygame.draw.rect(screen, (255,255,255), (screenSize[0] * 29 / 36, screenSize[1] - screenSize[1] /8, screenSize[0] /6, 320))
            for mots in deck:
                screen.blit(self.loadTextV2(24, mots), dispoMots[i])
                i += 1

    def show(self, screen, screenSize):
        ps = list(self.players)
        self.loadHealth(screen, screenSize)
        if self.manche == 0:
            screen.blit(self.loadText(64, f"Manche {self.manche}"), (screenSize[0] / 2, screenSize[1] / 2))
            #Affichage des noms + image du joueur
            screen.blit(self.loadText(24, ps[self.player1].name), (screenSize[0] / 12, screenSize[1] / 12))
            screen.blit(self.loadText(72, 'VS'), (screenSize[0] / 2 - 36, screenSize[1] / 24))
            screen.blit(self.loadText(24, ps[self.player2].name), (screenSize[0] - screenSize[0] / 6, screenSize[1] / 12))
            screen.blit(ps[self.player1].image,((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
            screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)-personnage.SIZE[1]/5))
            screen.blit(self.loadText(64, 'Commencer'), (screenSize[0] / 2 - 100, 530))
        else:
            if self.transActive and  not (ps[self.player1].health == 0 or ps[self.player2].health == 0) :
                if self.tourPlayer1:
                    self.transition(f"Manche {self.manche} : Tour Joueur 1", screen, screenSize)
                elif self.selectionGagnant:
                    self.transition("Tour du Juge", screen, screenSize)
                else:
                    self.transition("Tour joueur 2", screen, screenSize)
            elif ps[self.player1].health > 0 and ps[self.player2].health > 0 and self.selectionGagnant == False:
                # Affiche une phrase aléatoire
                self.loadPhrase(screen, screenSize)
                if (self.tourPlayer1): #Tour joueur 1
                    self.loadMots(screen, screenSize, self.deckPlayer1)
                    screen.blit(self.loadText(24, ps[self.player1].name), (screenSize[0] / 12, screenSize[1] / 12))
                    screen.blit(ps[self.player1].image, ((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
                else: #Tour joueur 2
                    self.loadMots(screen, screenSize, self.deckPlayer2)
                    screen.blit(self.loadText(24, ps[self.player2].name),(screenSize[0] - screenSize[0] / 6, screenSize[1] / 12))
                    screen.blit(ps[self.player2].image, ((screenSize[0]*9/12)-personnage.SIZE[0]/3, (screenSize[1]/2)- personnage.SIZE[1]/5))
            elif self.selectionGagnant:
                self.loadPhrase(screen, screenSize)
                self.loadMots(screen, screenSize, self.deckPlayer2)
                screen.blit(self.loadText(24, ps[self.player1].name), (screenSize[0] / 12, screenSize[1] / 12))
                screen.blit(self.loadText(72, 'VS'), (screenSize[0] / 2 - 36, screenSize[1] / 24))
                screen.blit(self.loadText(24, ps[self.player2].name),(screenSize[0] - screenSize[0] / 6, screenSize[1] / 12))
                screen.blit(ps[self.player1].image, ((screenSize[0] * 3 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
                screen.blit(ps[self.player2].image, ((screenSize[0] * 9 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 5))
                #TODO Afficher les deux réponse en dessous des personnages + un carré entre les deux pour "égalité"
            elif ps[self.player1].health == 0 or ps[self.player2].health == 0:
                screen.blit(self.loadText(64, "Victoire"), (screenSize[0] * 5 / 12, screenSize[1] * 1/6))
                if ps[self.player1].health == 0:
                    screen.blit(ps[self.player2].image, ((screenSize[0] * 6 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 6))
                else:
                    screen.blit(ps[self.player1].image, ((screenSize[0] * 6 / 12) - personnage.SIZE[0] / 3, (screenSize[1] / 2) - personnage.SIZE[1] / 5))
                screen.blit(self.loadText(64, 'Retour au Menu'), (screenSize[0] / 2 - 100, 530))
            else:
                screen.blit(self.loadText(64, "Erreur! relancer le jeu"), (screenSize[0] * 5 / 12, screenSize[1] * 1 / 6))

    def onEvent(self, screenSize, mouseX, mouseY, state):
        from Menu import Menu
        ps = list(self.players)
        if ps[self.player1].health > 0 and ps[self.player2].health > 0:
            if self.manche == 0:
                if Menu.isOnBtn(mouseX, mouseY, [400, 64], screenSize[0]/2 - 100, 530):
                  self.setTimer()
                  self.setNextManche(None)
            #Interaction Cartes deck Player1
            elif self.transActive == False:
                if not self.selectionGagnant:
                    if (self.tourPlayer1):
                        if Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 1 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer1 = self.deckPlayer1[0]
                            self.tourPlayer1 = False
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 8 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer1 = self.deckPlayer1[1]
                            self.tourPlayer1 = False
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 5 / 12, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer1 = self.deckPlayer1[2]
                            self.tourPlayer1 = False
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 22 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer1 = self.deckPlayer1[3]
                            self.tourPlayer1 = False
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 29 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer1 = self.deckPlayer1[4]
                            self.tourPlayer1 = False
                            self.setTimer()
                    else: #Interaction Cartes deck Player2
                        if Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 1 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer2 = self.deckPlayer2[0]
                            self.selectionGagnant = True
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 8 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer2 = self.deckPlayer2[1]
                            self.selectionGagnant = True
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 5 / 12, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer2 = self.deckPlayer2[2]
                            self.selectionGagnant = True
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 22 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer2 = self.deckPlayer2[3]
                            self.selectionGagnant = True
                            self.setTimer()
                        elif Menu.isOnBtn(mouseX, mouseY, [screenSize[0] /6, 320], screenSize[0] * 29 / 36, screenSize[1] - screenSize[1] /8):
                            self.choixPlayer2 = self.deckPlayer2[4]
                            self.selectionGagnant = True
                            self.setTimer()
                elif self.selectionGagnant: #Interaction Selection du gagnant
                    if Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 390, screenSize[1] / 2 + 240):
                        self.choixPlayer2 = self.deckPlayer2[1]
                        self.setNextManche(self.player2)
                        self.setTimer()
                    elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 - 120, screenSize[1] / 2 + 240):
                        self.choixPlayer2 = self.deckPlayer2[2]
                        self.setNextManche(None)
                        self.setTimer()
                    elif Menu.isOnBtn(mouseX, mouseY, [240, 320], screenSize[0] / 2 + 150, screenSize[1] / 2 + 240):
                        self.choixPlayer2 = self.deckPlayer2[3]
                        self.setNextManche(self.player1)
                        self.setTimer()
        else: #Interaction fin de game
            if Menu.isOnBtn(mouseX, mouseY, [200, 64], screenSize[0]/2 - 100, 530):
                state = Menu.INTRO
                return state

    def setNextManche(self, playerPerdant):
        if self.manche >= 1:
            ps = list(self.players)
            self.selectionGagnant = False
            self.tourPlayer1 = True
            index1 = self.deckPlayer1.index(self.choixPlayer1)
            index2 = self.deckPlayer2.index(self.choixPlayer2)
            del self.deckPlayer1[index1]
            del self.deckPlayer2[index2]
            if len(self.phrase) == 1:
                del self.phrase[-1]
            if playerPerdant == self.player1:
                ps[self.player1].health -= 10
                print(ps[self.player1].health)
                self.viewLifeP1 -= 120
            if playerPerdant == self.player2:
                ps[self.player2].health -= 10
                self.viewLifeP2 -= 120
        self.manche += 1


    def transition(self, text, screen, screenSize):
        pygame.draw.rect(screen, (0, 0, 0), (screenSize[0] / 2 - 500, screenSize[1] / 2 - 100, 1000, 200))
        screen.blit(self.loadText(48, text), (screenSize[0] / 2 - 160, screenSize[1] / 2))
        if pygame.time.get_ticks() - self.timer > 1000:
            self.transActive = False

    def setTimer(self):
        self.transActive = True
        self.timer = pygame.time.get_ticks()