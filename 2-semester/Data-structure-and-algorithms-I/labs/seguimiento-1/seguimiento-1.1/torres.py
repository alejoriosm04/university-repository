def torres_hanoi(n:int, beg:str, aux:str, end:str, m:int):
    if n == 1:
        print("Mover disco 1 de la vara " + beg + " a la vara " + end)
        return
    else:
        torres_hanoi(n-1, beg, end, aux, m)
        print("Mover disco " + str(n) + " de la vara " + beg + " a la vara " + end)
        torres_hanoi(n-1, aux, beg, end, m)
    return m


def main():
    n = int(input())
    m = (2**n)-1
    print(torres_hanoi(n, "1", "2", "3", m))


if __name__ == '__main__':
    main()