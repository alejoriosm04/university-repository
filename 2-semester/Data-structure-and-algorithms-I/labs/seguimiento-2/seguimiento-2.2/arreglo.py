def arreglo(arr1, arr2):
    arr3 = []
    diccionario = dict()
    for i in range(len(arr1)):
        diccionario[arr1[i]] = 1
    
    for i in range(len(arr2)):
        if arr2[i] in diccionario:
            diccionario[arr2[i]] = 2
        else:
            diccionario[arr2[i]] = 1

    for key, value in diccionario.items():
        if value != 2:
            arr3.append(key)

    arr3.sort()

    return arr3


def main():
    arr1 = [3, 2, 1, 2, 1, 4, 5, 8, 6]
    arr2 = [1, 5, 7, 8, 3, 9, 100, 3, 4]
    print(arreglo(arr1, arr2))


if __name__ == '__main__':
    main()