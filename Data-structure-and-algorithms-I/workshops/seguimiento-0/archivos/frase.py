def guardarFrase():
    archivo = open("frase.txt", "w")
    texto = input()
    num = int(input())
    archivo.write(texto+str(num))
    archivo.close()


def main():
    guardarFrase()


if __name__ == '__main__':
    main()