primera_respuesta = input()
segunda_respuesta = input()

if len(primera_respuesta) > len(segunda_respuesta):
    print("La respuesta de la primera presidenta es más larga")
elif len(primera_respuesta) < len(segunda_respuesta):
    print("La respuesta de la segunda presidenta es más larga")
else:
    print("Las respuestas de ambas presidentas son igual de largas")