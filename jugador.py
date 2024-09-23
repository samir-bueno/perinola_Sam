from clase_jugador import Jugador

j = Jugador()
print(j)

j.darFicha(2)
print(j)

j.sacarFichas(2)
print(j)

tieneFichas = j.tieneFicha()
print(tieneFichas)

j.sacarFichas(5)
print(j)
sinFichas = j.sinFichas()
print(sinFichas)


