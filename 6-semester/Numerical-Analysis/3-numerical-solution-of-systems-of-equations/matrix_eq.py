import numpy as np

# Coeficientes del sistema
A = np.array([[2.98, -6.21, -1.11],
              [-3.30, -1.51, 7.84],
              [-8.97, 1.12, -2.2]])

# Resultados del sistema
B = np.array([-38, -34, -20])

# Resolver el sistema de ecuaciones
solucion = np.linalg.solve(A, B)

# Mostrar la solución
x, y, z = solucion
print(f"El valor de x es: {x}")
print(f"El valor de y es: {y}")
print(f"El valor de z es: {z}")
