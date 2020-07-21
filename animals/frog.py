from .animal import Animal
from movements import Walking, Swimming
from datetime import date
class Frog(Animal):

    def __init__(self, name, species, food):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        Swimming.__init__(self)

    def feed(self):
        print(f'{self.name} was tossed {self.food} on {date.today().strftime("%m/%d/%Y")} that they caught out of the air with their crazy long tongue thing')

    def run(self):
        print(f'{self} hops')