def chequeodiccionario(dict)->bool:
    if dict["nombre"][0] != "C" and dict["precio"] >= 300:
        return True
    else:
        return False


def main():
    dict1 = {"nombre": "Caladora","precio":400}
    dict2 = {"nombre": "Banano","precio":400}
    dict3 = {"nombre": "Almacen","precio":200}
    print(chequeodiccionario(dict1))
    print(chequeodiccionario(dict2))
    print(chequeodiccionario(dict3))


if __name__ == '__main__':
    main()