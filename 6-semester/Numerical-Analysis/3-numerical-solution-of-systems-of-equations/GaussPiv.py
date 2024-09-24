import numpy as np

# Función para el pivoteo parcial
def pivpar(Ab, n, k):
    max_index = np.argmax(np.abs(Ab[k:n, k])) + k
    if max_index != k:
        Ab[[k, max_index]] = Ab[[max_index, k]]  # Intercambiar filas
    return Ab

# Función para el pivoteo total
def pivtot(Ab, mark, n, k):
    max_index = np.unravel_index(np.argmax(np.abs(Ab[k:n, k:n]), axis=None), Ab[k:n, k:n].shape)
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
        suma = sum(Ab[i, j] * x[j] for j in range(i+1, n))
        x[i] = (Ab[i, n] - suma) / Ab[i, i]
    return x

# Función principal para el método de Gauss con pivoteo opcional
def GaussPiv(A, b, n, Piv):
    Ab = np.hstack((A, b.reshape(-1, 1)))  # Aumentar A con el vector b
    mark = np.arange(n)  # Inicializar los marcadores para el pivoteo total
    
    for k in range(n-1):
        if Piv == 1:  # Pivoteo parcial
            Ab = pivpar(Ab, n, k)
        elif Piv == 2:  # Pivoteo total
            Ab, mark = pivtot(Ab, mark, n, k)
        
        # Eliminar filas inferiores
        for i in range(k+1, n):
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

# Función para calcular la norma infinita de una matriz o un vector
def norma_infinita(mat):
    # Si es un vector (1D), simplemente tomamos el máximo absoluto
    if len(mat.shape) == 1:
        return np.max(np.abs(mat))
    
    # Si es una matriz (2D), calculamos la norma infinita de las filas
    else:
        return np.max(np.sum(np.abs(mat), axis=1))

# Función para calcular el error escalar (residuo máximo)
def error_escalar(A, x, b):
    residuo = np.abs(np.dot(A, x) - b)  # Calcula el residuo (Ax - b)
    return np.max(residuo)  # Retorna el valor máximo del residuo (error escalar)

# Ejemplo de uso genérico
C = 6

# Matriz A y vector b
A = np.array([[C, 6, -3], [10, -15, -11], [5, -12, C]], dtype=float)
b = np.array([200, -47, 300], dtype=float)
n = len(b)
Piv = 2  # Pivoteo total (1 para parcial, 0 sin pivoteo)

# Resolver el sistema con pivoteo total
x, mark = GaussPiv(A, b, n, Piv)
print("Solución del sistema:", x)
print("Marcadores (solo con pivoteo total):", mark)

# Calcular el residuo (error) y su norma infinita
residuo = np.dot(A, x) - b
norma_inf_error = norma_infinita(residuo)

# Calcular el error escalar
error_esc = error_escalar(A, x, b)

# Calcular la norma infinita del vector solución x
norma_inf_x = norma_infinita(x)

# Mostrar resultados
print(f"Norma infinita del error (residuo): {norma_inf_error}")
print(f"Error escalar (residuo máximo): {error_esc}")
print(f"Norma infinita del vector solución x: {norma_inf_x}")
