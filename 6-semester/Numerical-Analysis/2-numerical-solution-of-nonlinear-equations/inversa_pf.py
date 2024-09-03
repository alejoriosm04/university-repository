import math

# Definimos la función inversa de g(x) = 4 * ln(x)
def g_inverse(y):
    return math.exp(y / 4)

# Valor dado en la iteración 5
x5 = 0.16874522

# Calculamos el valor en la iteración 4 usando g_inverse(x5)
x4 = g_inverse(x5)

print(f"El valor de x en la iteración 4 es: {x4}")
