archivo = open("notas.txt")
texto = archivo.read()
archivo.close()

lista_de_notas = texto.splitlines()

promedio = 0

for notas in lista_de_notas:
    nota1, nota2, nota3, nota4, nota5 = notas.split(",")
    nota1 = int(nota1)
    nota2 = int(nota2)
    nota3 = int(nota3)
    nota4 = int(nota4)
    nota5 = int(nota5)
    promedio = (nota1+nota2+nota3+nota4+nota5)/5


print(promedio)