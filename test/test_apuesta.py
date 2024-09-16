from clase_apuestas import Apuesta
import pytest
def test_prueba():
    assert(True)


def test_constructor():
    a = Apuesta()
    assert(a.fichas==0)

def test_repr():
    a = Apuesta()
    msj = a.__repr__()
    assert("apuesta" in msj)
    assert("fichas" in msj)
    assert("0" in msj)

def test_ponerFicha():
   
    a = Apuesta()
    a.ponerFicha(1)
    assert(a.fichas == 1)
    
    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2) 


def test_ponerFichaVarias():
    a = Apuesta()
    a.ponerFicha(2) 
    a.ponerFicha(3)
    assert(a.fichas == 5)
    

def test_tomarFicha_valor_sin_argumentos():
    a = Apuesta()
    a.fichas = 5
    a.tomarFicha()
    assert(a.fichas == 4)


def test_tomarFichaError():
    with pytest.raises(ValueError):
        a = Apuesta()
        a.fichas = 5
        a.tomarFicha(6)
    
    a = Apuesta()
    a.fichas = 5
    a.tomarFicha(5)
    assert(a.fichas==0)

def test_tomarTodasfichas():
    a = Apuesta()

    a.ponerFicha(1)
    a.ponerFicha(2)

    assert(a.fichas==a.fichas)

def test_tieneFichas():
    a = Apuesta()

    a.ponerFicha(1)
    assert(a.fichas>0)

def test_estaVacio():
    a = Apuesta()

    a.ponerFicha(1)
    a.tomarFicha(1)

    assert(a.fichas==0)







