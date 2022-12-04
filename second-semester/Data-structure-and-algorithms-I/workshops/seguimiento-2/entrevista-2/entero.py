def menor_entero(numbers):
    dict = {}

    for i in numbers:
        i = int(i)
        dict[i] = 0

    menor_entero_number = 1
    while True:
        if menor_entero_number not in dict:
            return menor_entero_number
        menor_entero_number += 1   


def main():
    n = int(input())
    numbers = input().split(" ")
    print(menor_entero(numbers))


if __name__ == '__main__':
    main()