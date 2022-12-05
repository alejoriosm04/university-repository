def par(n : int) -> int:
    if n <= 2:
        print(2)
    else:
        if n%2==0:
            par(n-2)
            if n == 6 or n == 8:
                return
            else:
                print(n)
        else:
            par(n-1)


def main():
    n = int(input())
    print(par(n))


if __name__ == '__main__':
    main()