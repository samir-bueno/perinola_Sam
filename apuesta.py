from clase_apuestas import Apuesta


#ejercicio apuesta
a = Apuesta()
print(a)
a.ponerFicha(4)
print(a)
a.ponerFicha()
print(a)
a.ponerFicha(1)
print(a)
a.ponerFicha(3)
print(a)

tomar = a.tomarTodas()
print(tomar)

tieneFichas = a.tieneFichas()
print(tieneFichas)


a.tomarFicha(9)
print(a)
estaVacio = a.estaVacio()
print(estaVacio)
