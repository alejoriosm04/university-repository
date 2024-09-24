# Valores dados
xn = -1.85718386
xn_1 = -1.85718389
xn_2 = -1.85748754

# Calcular la constante de error asintótico
C = abs((xn - xn_1) / (xn_1 - xn_2)**1.62)
print(C)
# Mostrar el resultado
print(f"La constante de error asintótico es: {C:.8f}")
