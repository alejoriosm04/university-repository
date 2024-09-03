import math

# Datos proporcionados
a = -4
b = 0
epsilon = 0.0003 # se calcula restando los X

# Cálculo del número mínimo de iteraciones
n = math.ceil(math.log((b - a) / epsilon) / math.log(2))
print(n)