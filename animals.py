from datetime import date

# The petting area
class Llama:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Donkey:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Goat:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
        print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Emu:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Camel:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

# The glass tank
class Snake:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.slithering = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Lizard:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.shift = shift
        self.food = food
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Frog:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Turtle:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Tarantula:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

# The pond

class Mallard:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Flamingo:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Goldfish:

    def __init__(self, name, species, food):
        self.name = name
        self.species = species
        self.food = food
        self.swimming = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Hippopotamus:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

class Alligator:

    def __init__(self, name, species, shift, food):
        self.name = name
        self.species = species
        self.food = food
        self.shift = shift
        self.walking = True
        self.date_added = date.today()

    def feed(self):
      print(f'{self.name} was fed {self.food} on {date.today().strftime("%m/%d/%Y")}')

    def __str__(self):
        return f"{self.name} is a {self.species}"

Larry = Llama('Larry', 'Llama', 'morning', 'Llama food')
Derek = Donkey('Derek', 'Donkey', 'midday', 'Donkey food')
Gary = Goat('Gary', 'Goat', 'afternoon', 'Goat food')
Eli = Emu('Eli', 'Emu', 'morning', 'Emu food')
Carey = Camel('Carey', 'Camel', 'midday', 'Camel food')
Sybill = Snake('Sybill', 'Snake', 'Snake food')
Lizzy = Lizard('Lizzy', 'Lizard', 'afternoon', 'Lizard food')
Felix = Frog('Felix', 'Frog', 'morning', 'Frog food')
Tommy = Turtle('Tommy', 'Turtle', 'midday', 'Turtle food')
Terry = Tarantula('Terry', 'Tarantula', 'afternoon', 'Tarantula food')
Mallory = Mallard('Mallory', 'Mallard', 'morning', 'Mallard food')
Ferdinand = Flamingo('Ferdinand', 'Flamingo', 'midday', 'Flamingo food')
Gloria = Goldfish('Gloria', 'Goldfish', 'Goldfish food')
Harriet = Hippopotamus('Harriet', 'Hippopotamus', 'afternoon', 'Hippopotamus food')
Ally = Alligator('Ally', 'Alligator', 'morning', 'Alligator food')