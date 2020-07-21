from .animal import Animal
from movements import Slithering, Swimming
from datetime import date

class Snake(Animal, Slithering, Swimming):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Slithering.__init__(self)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} gobbled their {self.food} whole on {date.today().strftime("%m/%d/%Y")}')