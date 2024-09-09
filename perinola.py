from clase_perinola import Perinola

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


