from .animal import Animal
from movements import Walking, Swimming
from datetime import date

class Alligator(Animal, Walking, Swimming):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} was thrown {self.food} from behind a fence for the safety of the feeder on {date.today().strftime("%m/%d/%Y")}')