import math

# Definir la función f(x)
def f(x):
    return math.exp(-2*x+6) + math.log(x) - 6

# Implementar el método de la regla falsa con el cálculo del error y f(n)
def regla_falsa(a, b, tol=5e-4, max_iter=100):
    if f(a) * f(b) >= 0:
        print("El método de la regla falsa no es aplicable en este intervalo.")
        return None
    
    xm_values = []  # Lista para almacenar los valores de xm
    error_values = []  # Lista para almacenar los valores del error
    f_values = []  # Lista para almacenar los valores de f(xm)
    xm_prev = None  # Inicializar el valor anterior de xm
    
    for i in range(max_iter):
        # Calcular el valor de xm
        xm = (a * f(b) - b * f(a)) / (f(b) - f(a))
        xm_values.append(xm)  # Guardar el valor de xm en cada iteración
        f_values.append(f(xm))  # Guardar el valor de f(xm)
        
        # Calcular el error si no es la primera iteración
        if xm_prev is not None:
            error = abs((xm - xm_prev)/xm)
            error_values.append(error)
        else:
            error_values.append(None)  # No hay error en la primera iteración
        
        xm_prev = xm  # Actualizar el valor anterior de xm
        
        # Verificar si la raíz se ha encontrado
        if abs(f(xm)) < tol:
            print(f"Raíz encontrada: {xm} en la iteración {i+1}")
            return xm, xm_values, error_values, f_values
        
        # Actualizar el intervalo
        if f(a) * f(xm) < 0:
            b = xm
        else:
            a = xm
    
    print("No se encontró una raíz en el número máximo de iteraciones.")
    return None, xm_values, error_values, f_values

# Definir el intervalo [a, b]
a = 2
b = 4

# Ejecutar el método de la regla falsa
raiz, xm_values, error_values, f_values = regla_falsa(a, b)

if raiz is not None:
    print(f"\nLa raíz aproximada es: {raiz:.5g}")
    print("\nValores de xm, f(xm) y error en cada iteración:")
    for i, (xm, f_xm, error) in enumerate(zip(xm_values, f_values, error_values), 1):
        if error is not None:
            print(f"Iteración {i}: xm = {xm:.5g}, f(xm) = {f_xm:.5g}, Error = {error:.5g}")
        else:
            print(f"Iteración {i}: xm = {xm:.5g}, f(xm) = {f_xm:.5g}, Error = N/A (primera iteración)")
