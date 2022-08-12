def permutar(respuesta, caracteres):
    if len(caracteres) == 0:
        print(respuesta)
        return
    else:
        for i in range(len(caracteres)):
            permutar(respuesta+caracteres[i], caracteres[:i] + caracteres[i+1:])


def main():
    caracteres = [str(x) for x in input().split()]
    permutar("", caracteres)


if __name__ == '__main__':
    main()