usuario1 = input()
usuario2 = input()

if usuario1 == "piedra" and usuario2 == "tijeras":
    print("El ganador es el usuario1")
elif usuario2 == "piedra" and usuario1 == "tijeras":
    print("El ganador es el usuario2")
elif usuario1 == "papel" and usuario2 == "tijeras":
    print("El ganador es el usuario2")
elif usuario2 == "papel" and usuario1 == "tijeras":
    print("El ganador es el usuario1")
elif usuario1 == "piedra" and usuario2 == "papel":
    print("El ganador es el usuario2")
elif usuario2 == "piedra" and usuario1 == "papel":
    print("El ganador es el usuario1")
elif usuario1 == usuario2:
    print("Empate")