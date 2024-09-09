from clase_perinola import Perinola
from clase_apuestas import Apuesta




#ejercicio perinola
p = Perinola()   
#primera tirada   
print(p) 
print(p.cara_visible)
#segunda tirada
resultado = p.tirar()
print(resultado)
print(p)
#lo mismo que resultado
print(p.cara_visible)


#ejercicio apuesta
a = Apuesta()
print(a)
a.ponerFicha(4)
print(a)
a.ponerFicha()
print(a)
a.tomarFicha(1)
print(a)
a.tomarFicha(8)
print(a)
