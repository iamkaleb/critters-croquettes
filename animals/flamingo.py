from .animal import Animal
from movements import Walking, Swimming

class Flamingo(Animal, Walking, Swimming):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        Swimming.__init__(self)