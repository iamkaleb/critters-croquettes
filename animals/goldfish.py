from .animal import Animal
from movements import Swimming

class Goldfish(Animal, Swimming):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Swimming.__init__(self)