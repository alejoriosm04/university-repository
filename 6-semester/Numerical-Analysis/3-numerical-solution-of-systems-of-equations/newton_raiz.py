import sympy as sp

# Definir la variable simbólica
x = sp.Symbol('x')

# Definir la función
f = x**4 - 7*x**3 + 16*x**2 - 12*x

# Calcular la derivada de la función
f_prime = sp.diff(f, x)

# Calcular las raíces de la función
roots = sp.solve(f, x)
print(f"Raíces de la función: {roots}")

# Verificar la multiplicidad de las raíces
raiz_mejor_para_newton_multiples = None
mayor_multiplicidad = 1

for root in roots:
    multiplicity = 1
    # Verificar si la raíz también es raíz de la derivada
    while sp.simplify(f.subs(x, root)) == 0 and sp.simplify(f_prime.subs(x, root)) == 0:
        multiplicity += 1
        f = sp.diff(f, x)  # Derivar de nuevo
        f_prime = sp.diff(f, x)  # Derivar la derivada también
    print(f"La raíz {root} tiene multiplicidad {multiplicity}")
    
    # Identificar la raíz con mayor multiplicidad
    if multiplicity > mayor_multiplicidad:
        mayor_multiplicidad = multiplicity
        raiz_mejor_para_newton_multiples = root

# Mostrar la raíz para la cual el método de Newton de raíces múltiples trabaja mejor
if raiz_mejor_para_newton_multiples:
    print(f"La raiz_mejor_para Newton de raíces múltiples es: {raiz_mejor_para_newton_multiples} con multiplicidad {mayor_multiplicidad}")
else:
    print("No hay raíces con multiplicidad mayor a 1.")
