
import random

listeMots = ("Ta face de citron", "Une huitre périmée", "Ton père au ski"
                , "Faire un bisou à des toilettes", "Manger des doigts de pied"
                , "Pikachu bodybuilder en slip", "Les mauvais repas de ta maman"
                , "Le faire passer pour cassimir", "Thomas le train"
                , "dire chocolatine", "Des pates au sucre", "des t-shirt banane"
                , "la téléréalité", "Fortnite", "Sortir avec un Kikou")

listePhrases = ("Te voir c'est aussi décevant que ... "
                , "Je préfére ... que de te fréquenter. "
                , "Tu est un mélange entre ... et une chausette sale."
                , "Tout les apres-midi tu dois penser à ..."
                , "Je t'ai vu avec ... entrain de twerker"
                , "Manger avec toi c'est aussi degueu que ..."
                , "J'ai tellement honte de toi depuis que ... est devenu une de tes habitudes.")

#fonction qui print des cartes alea
def aleaMots(nbMots):
  if nbMots == 1:
    return print(random.choice(listeMots))
  else:
    for i in range(nbMots):
      print(random.choice(listeMots))



#Fonction qui print une phrase alea
def aleaPhrase():
  return print(random.choice(listePhrases))

#Fonction qui affiche le résultat / la combinaison des cartes
#Faire une fonction qui retournera la phrase + le mot choisi par le joueur, sans qu'on retrouve les "..."
#mettre en param  (choixJoueur)
# if listePhrases == 1 return "Te voir c'est aussi décevant que" + choixJoueur