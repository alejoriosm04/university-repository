import time


def extension(arreglo, k):
    diccionario = dict()
    counter = 0
    for i in range(len(arreglo)):
        if arreglo[i] in diccionario:
            diccionario[arreglo[i]].append(0)
            diccionario[arreglo[i]].append(0)
        else:
            diccionario[arreglo[i]] = []
    print(diccionario)

    for key1 in diccionario.keys():
        for key2, value in diccionario.items():
            if key1 == key2:
                continue
            value.append(abs(key1-key2))
    print(diccionario)

    for value in diccionario.values():
        for i in range(len(value)):
            if value[i] == k:
                counter+=1
    
    counter /= 2
    return int(counter)


def main():
    start = time.time()
    arreglo = [1110, 956, 1780, 1030, 1020, 1120, 878]
    k = 10
    print(extension(arreglo, k))
    print(f'Time Algorithm: {time.time() - start} segundos')

    arreglo = [1, 5, 4, 1, 2]
    k = 0
    print(extension(arreglo, k))
    print(f'Time Algorithm: {time.time() - start} segundos')

    arreglo = [1, 5, 3]
    k = 2
    print(extension(arreglo, k))
    print(f'Time Algorithm: {time.time() - start} segundos')


if __name__ == '__main__':
    main()