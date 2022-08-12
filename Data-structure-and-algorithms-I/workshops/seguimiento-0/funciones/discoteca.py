def accesodiscoteca(edad, dinero, nombre):
    if edad >= 18 and dinero >= 100 and (nombre != "jimmy"):
        return True
    else:
        return False


def main():
    print(accesodiscoteca(25, 200, "alejo"))
    print(accesodiscoteca(25, 50, "alejo"))
    print(accesodiscoteca(17, 200, "alejo"))
    print(accesodiscoteca(28, 500, "jimmy"))


if __name__ == '__main__':
    main()