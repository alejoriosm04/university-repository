# Definir la función de la ecuación
fx = lambda x: (2**-x)*(-1+x)+(x**(2/3)) - 32

# Definir la función secante con almacenamiento de tabla
def secante_tabla(fx, x0, x1, tol=5e-6, max_iter=100):
    iteraciones = 0
    tabla = []
    
    # Calcular el primer valor de error relativo entre x1 y x0
    error_relativo = abs((x1 - x0) / x1)  # Error relativo entre x0 y x1
    
    # Almacenar los valores de x1 en la tabla
    tabla.append([iteraciones + 1, x1, fx(x1), error_relativo])
    
    # Iniciar el ciclo de iteraciones posteriores
    while iteraciones < max_iter:
        # Calcular el nuevo valor de x
        x2 = x1 - (fx(x1) * (x1 - x0)) / (fx(x1) - fx(x0))
        
        # Calcular el error relativo porcentual comparando x2 con x1
        error_relativo = abs((x2 - x1) / x2)
        
        # Almacenar los valores de x2 en la tabla
        iteraciones += 1
        tabla.append([iteraciones + 1, x2, fx(x2), error_relativo])
        
        # Verificar si el valor tiene la precisión requerida
        if error_relativo < tol:
            break
        
        # Actualizar los valores para la siguiente iteración
        x0, x1 = x1, x2
    
    return tabla, x2, iteraciones

# Condiciones iniciales
x0 = 32
x1 = 42
tol = 5e-6  # Tolerancia para cinco decimales

# Ejecutar el método de la secante con tolerancia de cinco decimales
tabla, solucion, iteraciones = secante_tabla(fx, x0, x1, tol)

# Mostrar la tabla de resultados con columnas Iteración, Xn, f(Xn), y Error (%)
print(f"{'Iteración':<10} | {'Xn':<20} | {'f(Xn)':<20} | {'Error':<20}")
print("-" * 70)
for fila in tabla:
    print(f"{fila[0]:<10} | {fila[1]:<20.10f} | {fila[2]:<20.10f} | {fila[3]:<20.10f}")

# Mostrar el resultado final
print(f"\nRaíz aproximada: {solucion:.6g}")
print(f"Número de iteraciones: {iteraciones}")

# Mostrar el error en la última iteración
error_final = tabla[-1][3]  # El error relativo de la última fila
# Imprimir el error final con 6 cifras significativas
print(f"Error final: {error_final:.6g}") # TODO PREGUNTAR PROFE