import math

# Definir la función f(x)
def f(x):
    return abs(x**(x-1)) - 2.5*x - 5

# Método de la secante con 5 iteraciones
def secante_5_iteraciones(x0, x1):
    for iteraciones in range(5):  # 5 iteraciones fijas
        # Calcular el nuevo valor de x
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        # Actualizar los valores para la siguiente iteración
        x0, x1 = x1, x2
    return x2

# Condiciones iniciales
x0 = -3
x1 = -2

# Ejecutar el método de la secante para 5 iteraciones
solucion_5 = secante_5_iteraciones(x0, x1)

# Mostrar el resultado
print(f"La solución aproximada con 5 iteraciones es: {solucion_5:.6f}")
