import random

listeMots = ("Ta face de citron", "Une huitre périmée", "Ton père au ski"
                , "Faire un bisou à des toilettes", "Manger des doigts de pied"
                , "Pikachu bodybuilder en slip", "Les mauvais repas de ta maman"
                , "Le faire passer pour cassimir", "Thomas le train"
                , "dire chocolatine", "Des pates au sucre", "des t-shirt banane"
                , "la téléréalité", "Fortnite", "Sortir avec un Kikou")

listePhrases = ("Te voir c'est aussi décevant que ..."
                , "Je préfére ... que de te fréquenter."
                , "Tu est un mélange entre ... et une chausette sale."
                , "Tout les apres-midi tu dois penser à ..."
                , "Je t'ai vu avec ... entrain de twerker."
                , "Manger avec toi c'est aussi degueu que ..."
                , "J'ai tellement honte de toi depuis que ... est devenu une de tes habitudes.")

Phrase = []
historique = []
deckPlayer1 = []
deckPlayer2 = []

def aleaMots():
    for i in range(5):
      if len(deckPlayer1) == 5 and len(deckPlayer2) == 5:
        break
      else:
        deckPlayer1.append(random.choice(listeMots))
        deckPlayer2.append(random.choice(listeMots))

def aleaPhrase():
  newPhrase = random.choice(listePhrases)
  if len(historique) == 7:
    #réinitialiser la liste historique
    historique[:] = []
  else:
    if len(Phrase) < 1:
      if newPhrase in historique:
        aleaPhrase()
      else:
        Phrase.append(newPhrase)
        historique.append(newPhrase)




#Fonction qui affiche le résultat / la combinaison des cartes
#Faire une fonction qui retournera la phrase + le mot choisi par le joueur, sans qu'on retrouve les "..."
#mettre en param  (choixJoueur)
# if listePhrases == 1 return "Te voir c'est aussi décevant que" + choixJoueur