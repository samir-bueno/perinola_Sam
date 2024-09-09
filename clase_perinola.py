from random import choice

#PERINOLA
class Perinola:
    caras = ("Pon 1", "Toma 2", "Todos Ponen",
                "Toma 1", "Pon 2", "Toma Todo")   
    def __init__(self):
        self.cara_visible =  choice(self.caras)
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):   
        self.cara_visible = choice(self.caras)
        return self.cara_visible
 
