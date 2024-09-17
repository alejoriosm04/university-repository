import math

# Definir la función f(x)
def f(x):
    return abs(x**(x-1)) - 2.5*x - 5

# Valores iniciales
x0 = -3
x1 = -2

# Calcular x2 usando el método de la secante
x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))

# Mostrar el resultado
print(f"El valor de x2 en la primera iteración es: {x2:.14f}")
