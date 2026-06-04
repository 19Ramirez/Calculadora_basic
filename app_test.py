from app import suma, resta, multiplicacion, division, potencia

def test_suma():
    assert suma(5, 3) == 8
    assert suma(-1, 1) == 0
    assert suma(0, 0) == 0

def test_resta():
    assert resta(10, 4) == 6
    assert resta(0, 5) == -5
    assert resta(7, 7) == 0

def test_multiplicacion():
    assert multiplicacion(4, 3) == 12
    assert multiplicacion(-2, 5) == -10
    assert multiplicacion(0, 100) == 0

def test_division():
    assert division(10, 2) == 5
    assert division(9, 3) == 3
    assert division(5, 0) == "Error: División entre cero"

def test_hola():
    mensaje = "Buscar en esta cadena la palabra HOLA"
    assert "HOLA" in mensaje

def test_potencia():
    assert potencia(2, 3) == 8
    assert potencia(5, 0) == 1
    assert potencia(3, 2) == 9