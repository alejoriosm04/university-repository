def primeraMitad(texto):
    slice_texto = int(len(texto)/2)
    return texto[:slice_texto]


def main():
    print(primeraMitad("tetero"))


if __name__ == '__main__':
    main()