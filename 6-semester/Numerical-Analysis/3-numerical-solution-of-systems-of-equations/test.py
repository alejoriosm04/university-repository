import numpy as np

# Definir un vector
vector = np.array([1, 2])

# Calcular la norma infinita del vector
norma_infinita_vector = np.linalg.norm(vector, ord=np.inf)

print("Norma infinita del vector:", norma_infinita_vector)
