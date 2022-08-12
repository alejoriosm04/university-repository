def subtexto(texto1, posicion_inicial, posicion_final, length):
    if length == posicion_inicial:
        return texto1[length]
    elif length > posicion_inicial and length <= posicion_final:
        return subtexto(texto1, posicion_inicial, posicion_final, length-1) +texto1[length]
    else:
        return subtexto(texto1, posicion_inicial, posicion_final, length-1)


def main():
    texto1 = input()
    posicion_inicial = int(input())
    posicion_final = int(input())
    length = len(texto1)
    print(subtexto(texto1, posicion_inicial, posicion_final, length-1))


if __name__ == '__main__':
    main()