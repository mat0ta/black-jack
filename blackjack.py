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
        self.dealer = []
        self.baraja = list(cartas.keys()) * 4
    def darCartas(self, cantidad, mano):
        for i in range(cantidad):
            shuffle(self.baraja)
            card = self.baraja.pop()
            mano.append(card)
    def calcularMano(self, mano):
        puntos = 0
        for i in range(len(mano)):
            try:
                puntos += cartas[mano[i]]
                return puntos
            except:
                return print('Ha ocurrido un error.')
    def iniciarJuego(self):
        print('¡Bienvenido al Blackjack!\nA continuacion el Dealer te asignara tu mano.')
        blackjack().darCartas(2, self.mano)
        blackjack().darCartas(1, self.dealer)
        print('Tu mano:\n' + self.mano[0] + ' ' + self.mano[1] + '\nPuntos: ' + str(blackjack().calcularMano(self.mano)) + '\n\nDealer:\n' + self.dealer[0] + '\nPuntos: ' + str(blackjack().calcularMano(self.dealer)))
    def hit(self):
        print('Hit')
    def stand(self):
        print('Stand')
    def testDef(self):
        blackjack().darMano(2, self.mano)

blackjack().iniciarJuego()