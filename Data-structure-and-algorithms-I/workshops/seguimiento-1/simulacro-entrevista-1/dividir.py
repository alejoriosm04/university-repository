def dividir_mitad(arr, length, i, izquierda, derecha):
    if length == i:
        return izquierda, derecha
    elif length // 2 <= i:
        derecha.append(arr[i])
        return dividir_mitad(arr, length, i+1, izquierda, derecha)
    else:
        izquierda.append(arr[i])
        return dividir_mitad(arr, length, i+1, izquierda, derecha)


def dividir_posicion_n(arr, length, n, i, izquierda, derecha):
    if length == i:
        return izquierda, derecha
    elif n <= i:
        derecha.append(arr[i])
        return dividir_posicion_n(arr, length, n, i+1, izquierda, derecha)
    else:
        izquierda.append(arr[i])
        return dividir_posicion_n(arr, length, n, i+1, izquierda, derecha)


def dividir_cinco_tres(arr, length, i, cinco, tres):
    if length == i:
        return cinco,tres
    elif arr[i] % 5 == 0:
        cinco.append(arr[i])
        return dividir_cinco_tres(arr, length, i+1, cinco, tres)
    elif arr[i] % 3 == 0:
        tres.append(arr[i])
        return dividir_cinco_tres(arr, length, i+1, cinco, tres)
    else:
        cinco.append(arr[i]) or tres.append(arr[i]) 
        return dividir_cinco_tres(arr, length, i+1, cinco, tres)
    

def main():
    # TEST NO. 1
    arr = [1, 2, 3, 4, 5, 6]
    izquierda = []
    derecha = []
    print(len(arr)//2)
    print(dividir_mitad(arr, len(arr), 0, izquierda, derecha))

    # TEST NO. 2
    arr2 = [1, 2, 3, 4, 5]
    izquierda2 = []
    derecha2 = []
    print(len(arr2)//2)
    print(dividir_mitad(arr2, len(arr2), 0, izquierda2, derecha2))

    #TEST NO. 3
    arr3 = [1, 2, 3, 4, 5, 6]
    izquierda = []
    derecha = []
    n = int(input())
    print(dividir_posicion_n(arr3, len(arr3), n, 0, izquierda, derecha))

    #TEST NO. 4
    arr4 = [1, 2, 3, 4, 5]
    izquierda = []
    derecha = []
    n = int(input())
    print(dividir_posicion_n(arr4, len(arr4), n, 0, izquierda, derecha))

    #TEST NO. 5
    arr5 = []
    izquierda = []
    derecha = []
    n = int(input())
    print(dividir_posicion_n(arr5, len(arr5), n, 0, izquierda, derecha))

    #TEST NO. 6
    arr6 = [5, 3, 15, 25, 81, 14, 29]
    izquierda = []
    derecha = []
    n = int(input())
    print(dividir_cinco_tres(arr6, len(arr6), 0, izquierda, derecha))


if __name__ == '__main__':
    main()