from animals import Llama, Donkey, Goat, Emu, Camel, Snake, Lizard, Frog, Turtle, Tarantula, Mallard, Flamingo, Goldfish, Hippopotamus, Alligator, Goose
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo('Varmint Village', 'cute and fuzzy critters to cuddle')

slither_inn = SnakePit('The Slither Inn', 'creepy, crawly critters to look at')

critter_cove = Wetlands('Critter Cove', 'feathery and flying critters to hang with')

Larry = Llama('Larry', 'Llama', 'morning', 'Llama food', 123456789)
varmint_village.add_animal(Larry)

Derek = Donkey('Derek', 'Donkey', 'midday', 'Donkey food')
varmint_village.add_animal(Derek)

Gary = Goat('Gary', 'Goat', 'afternoon', 'Goat food')
varmint_village.add_animal(Gary)

Eli = Emu('Eli', 'Emu', 'morning', 'Emu food')
varmint_village.add_animal(Eli)

Carey = Camel('Carey', 'Camel', 'midday', 'Camel food')
varmint_village.add_animal(Carey)

Sybill = Snake('Sybill', 'Snake', 'Snake food')
slither_inn.add_animal(Sybill)

Lizzy = Lizard('Lizzy', 'Lizard', 'afternoon', 'Lizard food')
slither_inn.add_animal(Lizzy)

Felix = Frog('Felix', 'Frog', 'Frog food')
slither_inn.add_animal(Felix)

Tommy = Turtle('Tommy', 'Turtle', 'midday', 'Turtle food')
slither_inn.add_animal(Tommy)

Terry = Tarantula('Terry', 'Tarantula', 'afternoon', 'Tarantula food')
slither_inn.add_animal(Terry)

Mallory = Mallard('Mallory', 'Mallard', 'morning', 'Mallard food')
critter_cove.add_animal(Mallory)

Ferdinand = Flamingo('Ferdinand', 'Flamingo', 'Flamingo food')
critter_cove.add_animal(Ferdinand)

Gloria = Goldfish('Gloria', 'Goldfish', 'Goldfish food')
critter_cove.add_animal(Gloria)

Harriet = Hippopotamus('Harriet', 'Hippopotamus', 'Hippopotamus food')
critter_cove.add_animal(Harriet)

Ally = Alligator('Ally', 'Alligator', 'Alligator food')
critter_cove.add_animal(Ally)

Bob = Goose("Bob", "Canada goose", "watercress sandwiches")
varmint_village.add_animal(Bob)

print(f'{varmint_village.attraction_name} is where you\'ll find {varmint_village.description}, like')
for animal in varmint_village.animals:
    print(animal)

print(f'{slither_inn.attraction_name} is where you\'ll find {slither_inn.description}, like')
for animal in slither_inn.animals:
    print(animal)

print(f'{critter_cove.attraction_name} is where you\'ll find {critter_cove.description}, like')
for animal in critter_cove.animals:
    print(animal)

Ally.feed()
Sybill.feed()
Felix.feed()