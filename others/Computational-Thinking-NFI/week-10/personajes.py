personajes  = []
numPersonajes = int(input())

i = 1
while(i <= numPersonajes):
    nombrePersonaje = input()
    if nombrePersonaje[0] == "L":
        pass
    else:
        personajes.append(nombrePersonaje)
    i = i + 1

print(personajes)