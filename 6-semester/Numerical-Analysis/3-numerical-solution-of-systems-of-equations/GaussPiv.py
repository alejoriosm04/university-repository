import numpy as np

# Función para el pivoteo parcial
def pivpar(Ab, n, k):
    max_index = np.argmax(np.abs(Ab[k:n, k])) + k
    if max_index != k:
        Ab[[k, max_index]] = Ab[[max_index, k]]  # Intercambiar filas
    return Ab

# Función para el pivoteo total
def pivtot(Ab, mark, n, k):
    sub_matrix = np.abs(Ab[k:n, k:n])
    max_index = np.unravel_index(np.argmax(sub_matrix, axis=None), sub_matrix.shape)
    max_row = max_index[0] + k
    max_col = max_index[1] + k
    
    if max_row != k:
        Ab[[k, max_row]] = Ab[[max_row, k]]  # Intercambiar filas
    if max_col != k:
        Ab[:, [k, max_col]] = Ab[:, [max_col, k]]  # Intercambiar columnas
        mark[[k, max_col]] = mark[[max_col, k]]  # Intercambiar marcadores de las columnas
    return Ab, mark

# Función de sustitución regresiva (back substitution)
def sustreg(Ab, n):
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        suma = np.dot(Ab[i, i+1:n], x[i+1:n])
        x[i] = (Ab[i, n] - suma) / Ab[i, i]
    return x

# Función principal para el método de Gauss con pivoteo opcional
def GaussPiv(A, b, n, Piv):
    Ab = np.hstack((A.copy(), b.reshape(-1, 1)))  # Aumentar A con el vector b
    mark = np.arange(n)  # Inicializar los marcadores para el pivoteo total
    
    for k in range(n-1):
        if Piv == 1:  # Pivoteo parcial
            Ab = pivpar(Ab, n, k)
        elif Piv == 2:  # Pivoteo total
            Ab, mark = pivtot(Ab, mark, n, k)
        
        # Eliminar filas inferiores
        for i in range(k+1, n):
            if Ab[k, k] == 0:
                raise ValueError("División por cero en la posición ({}, {})".format(k, k))
            M = Ab[i, k] / Ab[k, k]
            Ab[i, k:] = Ab[i, k:] - M * Ab[k, k:]
    
    # Obtener el vector solución usando sustitución regresiva
    x = sustreg(Ab, n)
    
    # Si hay pivoteo total, reorganizar el resultado según los marcadores
    if Piv == 2:
        x_reorganizado = np.zeros_like(x)
        for i in range(n):
            x_reorganizado[mark[i]] = x[i]
        x = x_reorganizado
    
    return x, mark

# Función para calcular la norma infinita de un vector
def norma_infinita(vec):
    return np.max(np.abs(vec))

# Función para calcular el error escalar (residuo máximo)
def error_escalar(A, x, b):
    residuo = np.abs(np.dot(A, x) - b)  # Calcula el residuo (Ax - b)
    return np.max(residuo)  # Retorna el valor máximo del residuo (error escalar)

# Datos del problema
# x1: Pokémons en Cartagena
# x2: Pokémons en Santa Marta
# x3: Pokémons en Riohacha

# Matriz A y vector b del sistema de ecuaciones
A = np.array([
    [777, 300, 500],  # Ecuación 1
    [654, 932, 999],  # Ecuación 2
    [932, 866, 228]   # Ecuación 3
], dtype=float)

b = np.array([10000, 10000, 10000], dtype=float)

n = len(b)
Piv = 2  # Pivoteo total

# Resolver el sistema con pivoteo total
x, mark = GaussPiv(A, b, n, Piv)

# Imprimir la solución
ciudades = ['Cartagena', 'Santa Marta', 'Riohacha']
# Reordenar las ciudades según los marcadores
ciudades_reordenadas = [ciudades[i] for i in mark]

print("Solución del sistema:")
for i in range(n):
    print(f"x{i+1} ({ciudades_reordenadas[i]}): {x[i]:.4f} pokémones")

print("\nOrden en que Ash debe visitar las ciudades (de mayor a menor cantidad de pokémones):")
# Determinar el orden basado en los valores de x
orden = sorted(zip(ciudades_reordenadas, x), key=lambda pair: pair[1], reverse=True)
for idx, (ciudad, cantidad) in enumerate(orden, 1):
    print(f"{idx}. {ciudad} con {cantidad:.4f} pokémones")

# Calcular el residuo (error) y su norma infinita
residuo = np.dot(A, x) - b
norma_inf_error = norma_infinita(residuo)

# Calcular el error escalar
error_esc = error_escalar(A, x, b)

# Mostrar resultados del error
print(f"\nNorma infinita del error (residuo): {norma_inf_error:.6f}")
print(f"Error escalar (residuo máximo): {error_esc:.6f}")

# Calcular la norma infinita del vector solución x
norma_inf_x = norma_infinita(x)
print(f"Norma infinita del vector solución x: {norma_inf_x:.6f}")
