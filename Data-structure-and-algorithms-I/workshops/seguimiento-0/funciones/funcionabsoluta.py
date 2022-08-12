def absoluta(num):
    if num > 21:
        return 2 * abs(num-21)
    else:
        return abs(num-21)


def main():
    print(absoluta(65))
    print(absoluta(14))


if __name__ == '__main__':
    main()