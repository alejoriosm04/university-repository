def incremental_search(f, x0, step_size, n):
    for i in range(n):
        if f(x0) == 0:
            return True
        x0 += step_size
    return False

# Definimos la función f(x)
def f(x):
    return x - 0.875  # Suponiendo que la ecuación a resolver es x = 0.875

# Definimos los casos a evaluar
cases = [
    {"x0": 0, "n": 10, "step_size": 0.1},
    {"x0": -0.5, "n": 14, "step_size": 0.1},
    {"x0": 0.8, "n": 1, "step_size": 0.1},
    {"x0": -0.8, "n": 16, "step_size": 0.1},
]

# Evaluamos cada caso
for i, case in enumerate(cases):
    result = incremental_search(f, case["x0"], case["step_size"], case["n"])
    print(f"Caso {i+1}: {'Éxito' if result else 'Fracaso'}")
