def caracter(cadena):
    s = ""
    diccionario = dict()
    for i in range(len(cadena)):
        if cadena[i] in diccionario:
            s += cadena[i]
            break
        else:
            diccionario[cadena[i]] = 1
    return s


def main():
    print(caracter("sossaa"))
    print(caracter("julian el mejor"))


if __name__ == '__main__':
    main()