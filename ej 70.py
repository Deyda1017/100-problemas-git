import math as mt

#seno(45) + coseno(pi)
a = mt.sin(45) + mt.cos(mt.pi)
print("a) Seno de 45 + coseno de pi =", a)

#raíz de e elevado a la 2
b = mt.sqrt(mt.e ** 2)
print("b) Raíz de e^2 =", b)

#redondear a 3 decimales (pi * raíz de 2)
c = round(mt.pi * mt.sqrt(2), 3)
print("c) pi * √2 =", c)
