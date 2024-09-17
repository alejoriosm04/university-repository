import math

# Definir la función g(x)
def g(x):
    return 4 * math.log(x)

# Dado que x_5 = 0.16874522, queremos encontrar x_4
x5 = 0.16874522

# Usamos la relación inversa de punto fijo, iterando para atrás desde la iteración 5
# Esto lo hacemos aplicando g hacia atrás

# Definimos una función inversa de g para calcular la iteración anterior
def g_inverse(x):
    return math.exp(x / 4)

# Encontramos el valor de x_4 aplicando la función inversa
x4 = g_inverse(x5)

print("El valor de x en la iteración 4 es:", x4)
