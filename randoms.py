from random import random, randrange, randint, choice, shuffle, Random

print(random())
print(randrange(1, 10))
print(randint(1, 6))

names = ["Alice", "Bob", "Charlie", "Diana"]
print(choice(names))

shuffle(names)
print(names)

generator = Random(42)
print(generator.randint(1, 100))
