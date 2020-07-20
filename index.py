from animals import Llama, Donkey, Goat, Emu, Camel, Snake, Lizard, Frog, Turtle, Tarantula, Mallard, Flamingo, Goldfish, Hippopotamus, Alligator
from attractions import PettingZoo, SnakePit, Wetlands

varmint_village = PettingZoo('Varmint Village', 'cute and fuzzy critters to cuddle')

slither_inn = SnakePit('The Slither Inn', 'creepy, crawly critters to look at')

critter_cove = Wetlands('Critter Cove', 'feathery and flying critters to hang with')

Larry = Llama('Larry', 'Llama', 'morning', 'Llama food', 123456789)
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

Ally.feed()
Sybill.feed()
Felix.feed()
