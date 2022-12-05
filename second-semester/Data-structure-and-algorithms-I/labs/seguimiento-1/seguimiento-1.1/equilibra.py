def equilibra(personas, contador, array1, array2):
    if contador >= len(personas):
        return array1, array2
    # elif sum(array1) == sum(array2) and len(array1) != 0:
    #     return array1, array2
    return equilibra(personas, contador+1, array1 + [personas[contador]], array2) or equilibra(personas, contador+1, array1, array2.append(personas[contador]))


def main():
    personas = [80,59,60,81,57,58,76,75]
    array1 = []
    array2 = []
    print(equilibra(personas, 0, array1, array2))

if __name__ == '__main__':
    main()