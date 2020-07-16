from datetime import date

# The petting area

class PettingZoo:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)   

varmint_village = PettingZoo('Varmint Village', 'cute and fuzzy critters to cuddle')

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

# The glass tank

class SnakePit:

    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

slither_inn = SnakePit('The Slither Inn', 'creepy, crawly critters to look at')    

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

# The pond

class Wetlands:
        
    def __init__(self, name, description):
        self.attraction_name = name
        self.description = description
        self.animals = list()

    def add(self, animal):
        self.animals.append(animal)

critter_cove = Wetlands('Critter Cove', 'feathery and flying critters to hang with') 

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

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
        return f"{self.name} the {self.species}"

Larry = Llama('Larry', 'Llama', 'morning', 'Llama food')
varmint_village.add(Larry)

Derek = Donkey('Derek', 'Donkey', 'midday', 'Donkey food')
varmint_village.add(Derek)

Gary = Goat('Gary', 'Goat', 'afternoon', 'Goat food')
varmint_village.add(Gary)

Eli = Emu('Eli', 'Emu', 'morning', 'Emu food')
varmint_village.add(Eli)

Carey = Camel('Carey', 'Camel', 'midday', 'Camel food')
varmint_village.add(Carey)

Sybill = Snake('Sybill', 'Snake', 'Snake food')
slither_inn.add(Sybill)

Lizzy = Lizard('Lizzy', 'Lizard', 'afternoon', 'Lizard food')
slither_inn.add(Lizzy)

Felix = Frog('Felix', 'Frog', 'morning', 'Frog food')
slither_inn.add(Felix)

Tommy = Turtle('Tommy', 'Turtle', 'midday', 'Turtle food')
slither_inn.add(Tommy)

Terry = Tarantula('Terry', 'Tarantula', 'afternoon', 'Tarantula food')
slither_inn.add(Terry)

Mallory = Mallard('Mallory', 'Mallard', 'morning', 'Mallard food')
critter_cove.add(Mallory)

Ferdinand = Flamingo('Ferdinand', 'Flamingo', 'midday', 'Flamingo food')
critter_cove.add(Ferdinand)

Gloria = Goldfish('Gloria', 'Goldfish', 'Goldfish food')
critter_cove.add(Gloria)

Harriet = Hippopotamus('Harriet', 'Hippopotamus', 'afternoon', 'Hippopotamus food')
critter_cove.add(Harriet)

Ally = Alligator('Ally', 'Alligator', 'morning', 'Alligator food')
critter_cove.add(Ally)

print(f'{varmint_village.attraction_name} is where you\'ll find {varmint_village.description}, like')
for animal in varmint_village.animals:
    print(animal)

print(f'{slither_inn.attraction_name} is where you\'ll find {slither_inn.description}, like')
for animal in slither_inn.animals:
    print(animal)

print(f'{critter_cove.attraction_name} is where you\'ll find {critter_cove.description}, like')
for animal in critter_cove.animals:
    print(animal)