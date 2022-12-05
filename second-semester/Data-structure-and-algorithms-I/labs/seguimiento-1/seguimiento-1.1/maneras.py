def puntos(counter, n, puntos_turno):
    if n <= 0:
        if n == 0:
            return 1 + counter
        else:
            return counter
    else:
        return puntos(counter, n-puntos_turno[0], puntos_turno) + puntos(counter, n-puntos_turno[1], puntos_turno) + puntos(counter, n-puntos_turno[2], puntos_turno)


def main():
    puntos_turno = [3, 5, 7]
    print(puntos(0, int(input()), puntos_turno))


if __name__ == '__main__':
    main()