from numpy import sin
from scipy.integrate import quad

# Definimos la función
def f(x):
    return sin(x**2)

# Calculamos la integral de 0 a 2
resultado, error = quad(f, 0, 2)
print(f"Integral definida de sin(x²) entre 0 y 2 = {resultado:.5f}")
