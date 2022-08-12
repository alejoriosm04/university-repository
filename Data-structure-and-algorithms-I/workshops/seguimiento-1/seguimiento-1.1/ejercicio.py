def palindromo(palabra:str):
    if len(palabra) == 0:
        return palabra
    else:
        return palabra[len(palabra)-1] + palindromo(palabra[:len(palabra)-1])


def main():
    palabra = input()
    if palabra == palindromo(palabra):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()