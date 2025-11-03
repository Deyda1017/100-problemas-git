import sympy as sp
x = sp.Symbol('x')

# a) x^2 - 5x + 7 = 0
ecuacion_a = sp.Eq(x**2 - 5*x + 7, 0)
sol_a = sp.solve(ecuacion_a)
print("a) Solución:", sol_a)

# b) 7x^2 + 9x -7 = 8x^2 - 2x - 3
ecuacion_b = sp.Eq(7*x**2 + 9*x - 7, 8*x**2 - 2*x - 3)
sol_b = sp.solve(ecuacion_b)
print("b) Solución:", sol_b)