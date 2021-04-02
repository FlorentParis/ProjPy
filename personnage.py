import pygame

class personnage:
  SIZE = (300, 300)

  def __init__(self, name):
    self.name = f"Rappeur {name}"
    self.imagePath = f"assets/{name}.png"
    self.image = pygame.image.load(self.imagePath)
    self.image = pygame.transform.scale(self.image, self.SIZE)

  def __hash__(self):
    '''
      on override la fonction hash de Object
      pour garantir l'unicité des personnages
    '''
    return hash(self.name)

  def __eq__(self, other):
    return self.name == other.name