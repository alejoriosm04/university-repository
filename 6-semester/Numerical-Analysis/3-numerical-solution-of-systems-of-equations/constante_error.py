# Valores dados
xn = 4.53640365
xn_1 = 4.53640366
xn_2 = 4.53679122

# Calcular la constante de error asintótico
C = abs((xn - xn_1) / (xn_1 - xn_2)**1.62)
print(C)
# Mostrar el resultado
print(f"La constante de error asintótico es: {C:.8f}")
