import math

# Función f(h)
def f(h, T):
    return -math.exp(-h) + h * (-1 + h) - h ** (2 / 3) - T

# Derivada de f(h)
def f_prima(h):
    if h == 0:
        return float('inf')  # Evita división por cero
    else:
        return math.exp(-h) - 1 + 2 * h - (2 / 3) * h ** (-1 / 3)

# Parámetros iniciales
T = float(input("Ingrese el valor de T (último dígito de su cédula): "))
h0 = float(input("Ingrese el valor inicial de h (altura en Km, por ejemplo, 0.623): "))
tol = 0.5e-6  # Tolerancia para seis cifras significativas
max_iter = 100  # Máximo número de iteraciones

# Inicialización de variables
h = h0
error_relativo = float('inf')
iteraciones = []

# Método de Newton-Raphson
for i in range(max_iter):
    f_h = f(h, T)
    f_h_prima = f_prima(h)
    
    if f_h_prima == 0:
        print("La derivada es cero en h = {:.10f}. El método de Newton no puede continuar.".format(h))
        break
    
    h_nuevo = h - f_h / f_h_prima
    error_relativo = abs((h_nuevo - h) / h_nuevo)
    
    # Guardar resultados de la iteración
    iteraciones.append({
        'iteración': i,
        'h_i': h,
        'f(h_i)': f_h,
        'error relativo': error_relativo
    })
    
    # Verificar criterio de convergencia
    if error_relativo < tol:
        h = h_nuevo
        break
    
    h = h_nuevo

# Imprimir tabla de resultados
print("\nTabla de resultados:")
print("{:<10} {:<15} {:<20} {:<15}".format('Iteración', 'h_i (Km)', 'f(h_i)', 'Error relativo'))
for item in iteraciones:
    print("{:<10} {:<15.10f} {:<20.10f} {:<15.10f}".format(
        item['iteración'],
        item['h_i'],
        item['f(h_i)'],
        item['error relativo']
    ))

# Resultado final
if error_relativo < tol:
    print("\nAsh debe volar a una altura de {:.10f} Km para alcanzar una temperatura de {:.2f}°C.".format(h, T))
else:
    print("\nEl método de Newton no convergió en {} iteraciones. Intente con un valor inicial diferente.".format(max_iter))
