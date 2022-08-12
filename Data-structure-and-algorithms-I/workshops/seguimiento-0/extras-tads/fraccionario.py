#Modifica el Fraccionario f1 sin problema, volvera a su valor original
def lcm(x, y):
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

class Fraccionario:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def mostrar(self):
        print(str(self.a) + "/" + str(self.b))
    
    def sumar(self, fraccionario2):
        denominador = lcm(self.b, fraccionario2.b)
        numerador = (self.a * (int(denominador/self.b))) + (fraccionario2.a * (int(denominador/fraccionario2.b)))
        print(str(numerador) + "/" + str(denominador))
    
    def restar(self, fraccionario2):
        denominador = lcm(self.b, fraccionario2.b)
        numerador = (self.a * (int(denominador/self.b))) - (fraccionario2.a * (int(denominador/fraccionario2.b)))
        print(str(numerador) + "/" + str(denominador))
    
    def multiplicar(self, fraccionario2):
        multiplicacion_numerador = self.a * fraccionario2.a
        multiplicacion_denominador = self.b * fraccionario2.b
        print(str(multiplicacion_numerador) + "/" + str(multiplicacion_denominador))
    
    def dividir(self, fraccionario2):
        numerador = self.a * fraccionario2.b
        denominador = self.b * fraccionario2.a
        print(str(numerador) + "/" + str(denominador))

# Toma de datos e impresion
x, y = map(int, input().split())
f1 = Fraccionario(x, y)

a, b = map(int, input().split())
f2 = Fraccionario(a, b)

# Original
f1.mostrar()

# Al sumar
f1.sumar(f2)
f1 = Fraccionario(x, y)


# Al restar
f1.restar(f2)
f1 = Fraccionario(x, y)


# Al multiplicar
f1.multiplicar(f2)
f1 = Fraccionario(x, y)

# Al dividir
f1.dividir(f2)