# Eliminar 'pass' y reemplazar por el codigo
from datetime import datetime


class Fecha:
    def __init__(self, d, m, a):
        self.d = d
        self.m = m
        self.a = a
    
    def string(self):
        print(str(self.d) + "-" + str(self.m) + "-" + str(self.a))
        
    def comparar(self, fecha2):
        str_date1 = str(self.d) + "-" + str(self.m) + "-" + str(self.a)
        date1 = datetime.strptime(str_date1, '%d-%m-%Y')

        str_date2 = str(fecha2.d) + "-" + str(fecha2.m) + "-" + str(fecha2.a)
        date2 = datetime.strptime(str_date2, '%d-%m-%Y')

        if date1 > date2:
            print("despues")
        elif date1 < date2:
            print("antes")
        else:
            print("iguales")

d, m, a = map(int, input().split())
f1 = Fecha(d, m, a)

d, m, a = map(int, input().split())
f2 = Fecha(d, m, a)

f1.string()
f1.comparar(f2)