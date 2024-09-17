import numpy as np
import pandas as pd

# Definir la función
def secante_tabla(fx, xa, xb, tol):
    tramo = abs(xb - xa)
    tabla = []
    iteraciones = 1
    while tramo >= tol:
        fa = fx(xa)
        fb = fx(xb)
        xc = xa - fa * (xb - xa) / (fb - fa)
        tramo = abs(xc - xa)
        tabla.append([xa, xb, xc, tramo])
        xb = xa
        xa = xc
        iteraciones += 1
    tabla = np.array(tabla)
    return tabla, iteraciones

# Definir la función de la ecuación
fx = lambda x: ((abs(x))**(x-1)) - (2.5*x) - 5

# Condiciones iniciales
x0 = -3
x1 = -2
tolera = 1e-5  # Tolerancia para cinco decimales

# Ejecutar el método de la secante
tabla, iteraciones = secante_tabla(fx, x0, x1, tolera)
raiz = tabla[-1, 2]  # La raíz se encuentra en la última iteración

# Crear un DataFrame de pandas para visualizar mejor la tabla
df = pd.DataFrame(tabla, columns=["xa", "xb", "xc", "tramo"])

# Mostrar la tabla con pandas
pd.set_option('display.float_format', '{:.6f}'.format)
print(df)

# Mostrar el resultado de la raíz y el número de iteraciones
print(f'\nRaíz aproximada: {raiz:.6f}')
print(f'Número de iteraciones: {iteraciones}')
