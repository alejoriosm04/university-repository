# Valor de A (últimos tres dígitos de la cédula)
A = int(input("Ingrese el valor de A (últimos tres dígitos de su cédula): "))

# Datos conocidos
delta_x = {
    0: 2.00050,
    1: 1.00050,
    2: 0.39578,
    3: 0.03943,
    4: 0.00348,
    5: (A * 1e-5)  # Convertir A a la forma A * 10^-5
}

f_x = {
    0: 3.63193,
    4: 0.00018,
    5: 0.00002
}

# Función para calcular f(x_i) en retroceso
def calcular_f_x_anterior(f_x_n, delta_x_n, delta_x_n1):
    return f_x_n + (f_x_n * delta_x_n) / delta_x_n1

# Lista para almacenar los resultados
resultados = []

# Iteración para calcular f(x_i) en retroceso desde i=5 hasta i=1
for i in range(5, 0, -1):
    if i - 1 not in f_x:
        # Obtener los valores necesarios
        f_x_n = f_x[i]
        delta_x_n = delta_x[i - 1]
        delta_x_n1 = delta_x[i]
        
        # Calcular f(x_{n-1})
        f_x_n1 = calcular_f_x_anterior(f_x_n, delta_x_n, delta_x_n1)
        
        # Almacenar el resultado
        f_x[i - 1] = f_x_n1
    else:
        # Si ya tenemos f(x_{n-1}), continuar
        pass

# Ordenar y mostrar los resultados
print("\nTabla de resultados completada:")
print("{:<10} {:<12} {:<20}".format('Iteración', 'f(x_i)', '|x_i - x_{i-1}|'))
for i in range(0, 6):
    f_x_i = f_x.get(i, '---')
    delta_x_i = delta_x.get(i, '---')
    if isinstance(f_x_i, float):
        f_x_i = "{:.5f}".format(f_x_i)
    if isinstance(delta_x_i, float):
        delta_x_i = "{:.5f}".format(delta_x_i)
    print("{:<10} {:<12} {:<20}".format(i, f_x_i, delta_x_i))
