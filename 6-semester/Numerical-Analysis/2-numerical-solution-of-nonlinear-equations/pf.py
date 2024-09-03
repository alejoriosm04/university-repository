import pandas as pd
import numpy as np
import math

print("X0:")
X0 = float(input())
print("Niter:")
Niter = float(input())
print("Function:")
Fun = input()
print("Function g:")
g = input()

fn = []
xn = []
N = []
x = X0
f = eval(Fun)
c = 0

fn.append(f)
xn.append(x)
N.append(c)

while f != 0 and c < Niter:
    x = eval(g)
    fe = eval(Fun)
    fn.append(fe)
    xn.append(x)
    c = c + 1
    N.append(c)
    f = fe  # Actualizar f con el valor de la nueva evaluación de la función
    
if fe == 0:
    s = x
    print(s, "es raíz de f(x)")
else:
    s = x
    print("Fracaso en", Niter, "iteraciones")

# Para mostrar los resultados de la tabla de iteraciones
df = pd.DataFrame({'N': N, 'xn': xn, 'fn': fn})
print(df)