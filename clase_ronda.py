from clase_jugador import Jugador

class Ronda:
    def __init__(self):
        self.jugadores = []
    def __repr__(self):
        return f"{self.jugadores}"
    
    def agregarJugador(self, jugador):
        if jugador.sinFichas:
            raise ValueError("El jugador debe tener al menos 1 ficha para ser agregado")
        self.jugadores.append(jugador)
         
