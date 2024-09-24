import math

# Definir la función f(x)
def f(x):
    return abs(x**(x-1)) - 2.5*x - 5

# Método de la secante ajustado para cinco decimales
def secante(x0, x1, tol=1e-5, max_iter=100):
    iteraciones = 0
    while iteraciones < max_iter:
        # Calcular el nuevo valor de x
        x2 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        # Verificar si el valor tiene la precisión requerida
        if abs(x2 - x1) < tol:
            break
        # Actualizar los valores
        x0, x1 = x1, x2
        iteraciones += 1
    
    return x2, iteraciones

# Condiciones iniciales
x0 = -3
x1 = -2

# Ejecutar el método de la secante con tolerancia de cinco decimales
solucion, iteraciones = secante(x0, x1)

# Mostrar el resultado
print(f"La solución aproximada es: {solucion:.6f} con {iteraciones} iteraciones")
