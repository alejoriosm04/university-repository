while(True):
    nomJuzgado = input()
    declaraciones = int(input())
    if declaraciones > 10:
        print(nomJuzgado + " es culpable")
        break
    else:
        print(nomJuzgado + " es inocente")