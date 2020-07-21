from .animal import Animal
from movements import Walking

class Tarantula(Animal, Walking):

    def __init__(self, name, species, shift, food):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)