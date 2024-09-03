import math

# Definir la función f(x)
def f(x):
    return (math.exp(x) / x) + 3

# Implementar el método de la regla falsa
def regla_falsa(a, b, tol=1e-7, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de la regla falsa no es aplicable en este intervalo.")
        return None
    
    xm_values = []  # Lista para almacenar los valores de xm
    
    for i in range(max_iter):
        # Calcular el valor de xm
        xm = (a * f(b) - b * f(a)) / (f(b) - f(a))
        xm_values.append(xm)  # Guardar el valor de xm en cada iteración
        
        # Verificar si la raíz se ha encontrado
        if abs(f(xm)) < tol:
            print(f"Raíz encontrada: {xm} en la iteración {i+1}")
            return xm, xm_values
        
        # Actualizar el intervalo
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    print("No se encontró una raíz en el número máximo de iteraciones.")
    return None, xm_values

# Definir el intervalo [a, b]
a = -2
b = -0.1

# Ejecutar el método de la regla falsa
raiz, xm_values = regla_falsa(a, b)

if raiz is not None:
    print(f"La raíz aproximada es: {raiz}")
    print("Valores de xm en cada iteración:")
    for i, xm in enumerate(xm_values, 1):
        print(f"Iteración {i}: xm = {xm}")