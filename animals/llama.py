from .animal import Animal
from movements import Walking

class Llama(Animal, Walking):

    def __init__(self, name, species, shift, food, chip_num):
        Animal.__init__(self, name, species, food)
        Walking.__init__(self)
        self.shift = shift
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, chip_num):
        pass