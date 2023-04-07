import random

#Funciones
#1: Crea los zombies y los mete en una lista
def crearZombies(): 
  print("\n--Creando los zombies en las ciudades 😎🥵🧟--")
  a = int(input("Ingresa la cantidad de Zombies en Sabaneta 😎 \n"))
  b = int(input("Ingresa la cantidad de Zombies en Envigado 😎\n"))
  c = int(input("Ingresa la cantidad de Zombies en Medellin 😎\n"))
  d = int(input("Ingresa la cantidad de Zombies en Itagui 🤢\n"))
  zombies = [a, b, c, d]
  return zombies #devuelve la misma lista que creamos.

#2: Muestra el Menu de la cantidad de Zombies de cada ciudad.
def mostrar(zombies):
  menuActual = f"""
    -------------
    S: {zombies[0]} | E: {zombies[1]}
    -------------
    M: {zombies[2]} | I: {zombies[3]}
    -------------

  """
  return print(menuActual)

#3: Resta -10 a la poblacion de zombies en una ciudad especifica
def disparar(zombies):
  posicionADisparar = int(input("Ingrese la posición de la ciudad a disparar (0, 1, 2 ó 3): "))
  if zombies[posicionADisparar] <= 0:
      print("\n¡Ya mataste a todos los zombies de esta ciudad!")
      zombies[posicionADisparar] = 0
  else: #rios es gay
      print("\n ¡Disparaste! Piu Piu")
      zombies[posicionADisparar] = zombies[posicionADisparar]-10

#4: Resta la mitad de la poblacion de zombies en todas partes
def pesticidas(zombies):
    contarMuertos = zombies.count(0)
    if contarMuertos == 4:
        print("Ya mataste a toda la poblacion!")
    else:
        print("\n ¡Lanzaste el pesticida a todas las ciudades!")
        print("\n ¡La mitad de la poblacion zombie murio en TODAS la ciudades!")
        i = 0
        while i <= 3:
            zombies[i] = int(zombies[i]/2)
            i = i + 1
    return zombies

#5: Revive 10 zombies en una ciduad RANDOM
def revivir(zombies):
    print("Has revivido a 10 zombies en una ciudad random!")
    ciudadRandom = random.randint(0, 3)
    zombies[ciudadRandom] = zombies[ciudadRandom] + 10
    return zombies

#6: Lluvia acida concentrada
def lluviaAcida(zombies):
    print("Has lanzado una lluvia acida en la ciudad seleccionada!")
    ciudad = int(input("Ingrese la posición de la ciudad a lanzar la lluvia acida (0, 1, 2 ó 3): "))
    zombies[ciudad] = 0
    return zombies

#7: Frase de la tia
def fraseTia():
    print("¡Mijo, no juegue esas cosas raras, que eso no es del Señor! Soldado avisado no muere en guerra. Si ve! Yo le dije")

#8: Verificar cantidad de zombies igual a cero. Finalizar juego.
def verificarZombies(zombies):
    if zombies[0] == 0 and zombies[1] == 0 and zombies[2] == 0 and zombies[3] == 0:
        print("Felicitaciones salvaste el Valle de Aburrá")
        return True
    else:
        print("¡Aun quedan zombies por matar!")
        return False

#9: Ayuda divina en una ciudad RANDOM.
def ayudaDivina(zombies):
    print("¡Has recibido ayuda divina! 🙌")
    ciudad = random.randint(0, 3)
    zombies[ciudad] = zombies[ciudad] + 5
    return zombies

#10: La cura sobre todo el Valle de Aburra.
def laCura(zombies):
    print("¡Has encontrado la cura! 🥳")
    i = 0
    while i <= 3:
        zombies[i] = zombies[i] - 10
        i = i + 1
    return zombies
    
# zombies en Sabaneta, Envigado, Medellín, e Itagüí respectivamente
zombies = crearZombies() #esto es igual a: zombies = [a, b, c, d]

#Algoritmo de ejecucion (Recordemos que Rios es gay)
while(True):
  mostrar(zombies)
  menuDeAcciones = """\n
        ---Acciones---
    1) para disparar a zombies de UNA ciudad particular.
    2) para lanzar pesticidas a los zombies de TODAS las ciudades.
    3) para revivir 10 zombies de una ciudad RANDOM.
    4) para lanzar lluvia acida sobre UNA ciudad particular.
    5) para imprimir una frase de la tia.
    6) para verificar si la cantidad de zombies es igual a 0 y finalizar el juego.
    7) para recibir ayuda divina sobre una ciudad RANDOM.
    8) para encontrar la cura sobre el Valle de Aburra.
    """
  print(menuDeAcciones)
  accion = int(input())
  if(accion == 1):
      disparar(zombies)
  elif accion == 2: 
      pesticidas(zombies)
  elif accion == 3:
      revivir(zombies)
  elif accion == 4:
      lluviaAcida(zombies)
  elif accion == 5:
      fraseTia()
  elif accion == 6:
      estado = verificarZombies(zombies)
      if estado is True:
        break
  elif accion == 7:
      ayudaDivina(zombies)
  elif accion == 8:
      laCura(zombies)
 