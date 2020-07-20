from datetime import date

class Animal:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} the {self.species}"

# The petting area

class Llama(Animal):

    def __init__(self, name, species, shift, food, chip_num):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True
        self.__chip_number = chip_num

    @property
    def chip_number(self):
        return self.__chip_number

    @chip_number.setter
    def chip_number(self, chip_num):
        pass

class Donkey(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Goat(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Emu(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Camel(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

# The glass tank  

class Snake(Animal):

    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.slithering = True

class Lizard(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Frog(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Turtle(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Tarantula(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

# The pond

class Mallard(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Flamingo(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Goldfish(Animal):

    def __init__(self, name, species, food):
        super().__init__(name, species, food)
        self.food = food
        self.swimming = True

class Hippopotamus(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True

class Alligator(Animal):

    def __init__(self, name, species, shift, food):
        super().__init__(name, species, food)
        self.shift = shift
        self.walking = True