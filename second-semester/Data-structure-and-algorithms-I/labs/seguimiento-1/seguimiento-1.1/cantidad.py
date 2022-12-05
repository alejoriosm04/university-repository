def cantidadx(s : str) -> str:
    if len(s) == 0:
        return 0
    elif s[0] == 'x':
        return 1 + cantidadx(s[1:])
    else:
        return cantidadx(s[1:])


def main():
    s = input()
    print(cantidadx(s))


if __name__ == '__main__':
    main()