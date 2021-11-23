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
        self.jugadores = 0
        self.nombres = []
    def iniciarJuego(self):
        self.jugadores = int(input('¿Cuantos jugadores van a jugar?: '))
        for i in range(self.jugadores):
            nombre = str(input('Nombre del jugador ' + str(i + 1) + ' :'))
            self.nombres.append(nombre)
        print(self.nombres)
        print('¡Bienvenido al Blackjack!\nA continuacion el Dealer te asignara tu mano.')
        blackjack().darCartas(2, self.mano)
        blackjack().darCartas(1, self.dealer)
        print('Tu mano:\n' + self.mano[0] + ' ' + self.mano[1] + '\nPuntos: ' + str(blackjack().calcularMano(self.mano)) + '\n\nDealer:\n' + self.dealer[0] + '\nPuntos: ' + str(blackjack().calcularMano(self.dealer)))
        decision = input('¿Que quieres hacer? (HIT/STAND): ')
        if str(decision).lower() == 'hit':
            blackjack().hit(self.mano)
        elif str(decision).lower() == 'stand':
            blackjack().stand(blackjack().calcularMano(self.mano), self.mano)
    def darCartas(self, cantidad, mazo):
        for i in range(cantidad):
            shuffle(self.baraja)
            card = self.baraja.pop()
            mazo.append(card)
    def calcularMano(self, mazo):
        puntos = 0
        for i in range(len(mazo)):
            try:
                puntos += cartas[mazo[i]]
            except:
                return print('Ha ocurrido un error.')
        return puntos
    def hit(self, mazo):
        blackjack().darCartas(1, mazo)
        puntos = blackjack().calcularMano(mazo)
        if puntos > 21:
            return print('Te has pasado. Tienes ' + str(puntos) + ' puntos.')
        else:
            print('\nTu mano:\n' + mazo[0] + ' ' + mazo[1] + '\nPuntos: ' + str(puntos))
            decision = input('\n¿Que quieres hacer? (HIT/STAND): ')
            if str(decision).lower() == 'hit':
                blackjack().hit(mazo)
            elif str(decision).lower() == 'stand':
                blackjack().stand(puntos, mazo)
    def stand(self, puntosMano, mano):
        blackjack().darCartas(1, self.dealer)
        puntos = blackjack().calcularMano(self.dealer)
        while puntos <= 16:
            blackjack().darCartas(1, self.dealer)
            puntos = blackjack().calcularMano(self.dealer)
        if puntos > 21:
            print('Tu mano:\n' + str(' '.join(mano)) + '\nPuntos: ' + str(puntosMano) + '\n\nDealer:\n' + str(' '.join(self.dealer)) + '\nPuntos: ' + str(puntos) + '\n')
            return print('El Dealer se ha pasado. ¡Has ganado!')
        else:
            if puntos >= puntosMano:
                print('Tu mano:\n' + str(' '.join(mano)) + '\nPuntos: ' + str(puntosMano) + '\n\nDealer:\n' + str(' '.join(self.dealer)) + '\nPuntos: ' + str(puntos) + '\n')
                return print('El Dealer te ha superado con ' + str(puntos) + ' puntos frente a tus ' + str(puntosMano) + ' puntos. ¡Has perdido!')
            else:
                print('Tu mano:\n' + str(' '.join(mano)) + '\nPuntos: ' + str(puntosMano) + '\n\nDealer:\n' + str(' '.join(self.dealer)) + '\nPuntos: ' + str(puntos) + '\n')
                return print('!Tu mano es la ganadora¡ Con ' + str(puntosMano) + ' puntos frente a los ' + str(puntos) + ' puntos del Dealer.')

if __name__ == "__main__":
   blackjack().iniciarJuego()