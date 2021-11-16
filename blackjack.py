import random
from random import choice, sample, shuffle

cartas = [chr(x) for x in range(0x1f0a1, 0x1f0af)]

print(choice(cartas))