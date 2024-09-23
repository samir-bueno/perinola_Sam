class Jugador:
    def __init__(self):
        self.fichas = 5
        self.nombre = "Tomas"

    def __repr__(self):
        return f"{self.nombre}, tiene {self.fichas} fichas"
    
    def darFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas

    def sacarFichas(self, cuantas=1):
        if cuantas > self.fichas:
            raise ValueError(f"No hay tantas fichas quedan ({self.fichas})")
        self.fichas = self.fichas - cuantas

    def tieneFicha(self, cuantas=1):
        return self.fichas >= cuantas
    
    def sinFichas(self):
        return self.fichas == 0




