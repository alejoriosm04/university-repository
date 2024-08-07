# Eliminar 'pass' y reemplazar por el codigo
import math


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanciaAlOrigen(self):
        distancia_al_origen = round(math.sqrt((self.x**2)+(self.y**2)), 2)
        print(distancia_al_origen)
    
    def anguloConElEjeX(self):
        if self.x >= 0 and self.y > 0:
            angulo_eje_x = round(abs(math.acos(self.x/(math.sqrt((self.x**2)+(self.y**2))))), 2)
            print(angulo_eje_x)
        elif self.x < 0 and self.y >= 0:
            angulo_eje_x = abs(math.atan((self.y)/(self.x)))
            angulo_eje_x = round(math.pi - angulo_eje_x, 2)
            print(angulo_eje_x)
        elif self.x <= 0 and self.y < 0:
            angulo_eje_x = abs(math.acos(self.x/(math.sqrt((self.x**2)+(self.y**2)))))
            angulo_eje_x = round(math.pi + angulo_eje_x, 2)
            print(angulo_eje_x)
        elif self.x > 0 and self.y <= 0:
            angulo_eje_x = abs(math.atan((self.y)/(self.x)))
            angulo_eje_x = round((math.pi * 2) - angulo_eje_x, 2)
            print(angulo_eje_x)

    
    def distanciaAOtroPunto(self, punto2):
        distancia_entre_dos_puntos = round(math.sqrt(((self.x-punto2.x)**2)+((self.y-punto2.y)**2)), 2)
        print(distancia_entre_dos_puntos)

# INPUT
x1, y1 =  map(int, input().split())
x2, y2 =  map(int, input().split())

punto1 = Punto(x1, y1)
punto2 = Punto(x2, y2)

punto1.distanciaAlOrigen()
punto1.anguloConElEjeX()
punto1.distanciaAOtroPunto(punto2)