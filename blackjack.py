from random import *
from itertools import *

cartas = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10
}

class blackjack():
    def __init__(self):
        self.mano = []
        self.banca = []
        self.baraja = list(cartas.keys()) * 4
    def darMano(self, cantidad, mano):
        for i in range(cantidad):
            shuffle(self.baraja)
            card = self.baraja.pop()
            mano.append(card)
    def testDef(self):
        blackjack().darMano(2, self.mano)
# print(cartas[baraja[1]])

blackjack().testDef()

# print(baraja)

# cartaElegida = [chr(x) for x in range(0x1f0a1, 0x1f0ae)]
# print(choice(cartaElegida))

# # for i in range(len(cartas)):
# #     print(list(cartas.keys())[i])