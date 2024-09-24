import numpy as np

def LU(A, b, n, Piv):
    P = np.eye(n)  # Matriz identidad
    L = np.copy(P)
    
    for k in range(n-1):
        if Piv == 1:
            A, P = pivLU(A, P, n, k)  # Llamada a la función de pivoteo parcial
        
        for i in range(k+1, n):
            M = A[i, k] / A[k, k]  # Calcula el multiplicador
            
            for j in range(k, n):
                A[i, j] = A[i, j] - M * A[k, j]
            
            A[i, k] = M  # Almacena el multiplicador en la matriz A
    
    U = np.triu(A)  # Obtiene la parte superior triangular de A
    L = L + np.tril(A, -1)  # Obtiene la parte inferior triangular de A con la diagonal cero
    B = np.dot(P, b)  # Aplica la permutación a b
    LB = np.column_stack((L, B))  # Junta L y B para la sustitución progresiva
    z = sustpro(LB, n)  # Solución de Ly = Pb mediante sustitución progresiva
    Uz = np.column_stack((U, z))  # Junta U y z para la sustitución regresiva
    x = sustreg(Uz, n)  # Solución de Ux = y mediante sustitución regresiva
    
    return x, L, U

def pivLU(A, P, n, k):
    # Función para realizar pivoteo parcial
    max_index = np.argmax(np.abs(A[k:, k])) + k
    if max_index != k:
        A[[k, max_index]] = A[[max_index, k]]  # Intercambia filas en A
        P[[k, max_index]] = P[[max_index, k]]  # Intercambia filas en P
    return A, P

def sustpro(LB, n):
    # Sustitución progresiva para resolver Ly = Pb
    L = LB[:, :-1]
    B = LB[:, -1]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (B[i] - np.dot(L[i, :i], z[:i])) / L[i, i]
    return z

def sustreg(Uz, n):
    # Sustitución regresiva para resolver Ux = y
    U = Uz[:, :-1]
    z = Uz[:, -1]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (z[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x

# Definición de la matriz A y el vector b
A = np.array([[2.0, 1.0, 1.0],
              [4.0, -6.0, 0.0],
              [-2.0, 7.0, 2.0]])

b = np.array([5.0, -2.0, 9.0])

n = A.shape[0]  # Tamaño de la matriz
Piv = 1  # Usar pivoteo parcial

# Llamada a la función LU para obtener la solución x y las matrices L y U
x, L, U = LU(A, b, n, Piv)

# Mostrar resultados
print("Solución del sistema Ax = b:")
print(x)
print("\nMatriz L (triangular inferior):")
print(L)
print("\nMatriz U (triangular superior):")
print(U)
# Verificar la multiplicación de L y U para obtener A
A_reconstructed = np.dot(L, U)
print("\nMatriz A reconstruida (L * U):")
print(A_reconstructed)