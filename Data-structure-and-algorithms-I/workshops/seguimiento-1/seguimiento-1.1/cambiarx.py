def cambiarx(s : str) -> str:
    if len(s) == 0:
        return s
    elif s[0] == 'x':
        return 'y' + cambiarx(s[1:])
    else:
        return s[0] + cambiarx(s[1:])


def main():
    s = input()
    print(cambiarx(s))


if __name__ == "__main__":
    main()