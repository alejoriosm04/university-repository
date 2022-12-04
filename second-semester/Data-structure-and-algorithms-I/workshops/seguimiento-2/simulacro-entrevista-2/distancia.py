def max_distance(numbers):
    diccionario = dict()

    for i in range(len(numbers)):
        if numbers[i] in diccionario:
            original_position = diccionario[numbers[i]][1]
            difference = i-diccionario[numbers[i]][1]
            if difference > diccionario[numbers[i]][0]:
                diccionario[numbers[i]] = [difference, original_position]
        else:
            diccionario[numbers[i]] = [0, i]

    max_distance = 0
    for value in diccionario.values():
        if value[0] > max_distance:
            max_distance = value[0]

    return max_distance


def main():
    n = int(input())
    numbers = input().split(" ")
    print(max_distance(numbers))


if __name__ == '__main__':
    main()