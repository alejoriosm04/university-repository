def camino_conejo(i:int, j:int, n:int, m:int, tablero_juego, d:int, k:int):
    if i>=n or j>=m:
        return 0
    elif i == n-1 and j == m-1:
        return sat(i,j, tablero_juego, d, k)
    else:
        return sat(i, j, tablero_juego, d, k) + max(camino_conejo(i, j+1, n, m, tablero_juego, d, k), camino_conejo(i+1, j, n, m, tablero_juego, d, k))


def sat(i:int, j:int, tablero_juego, d:int, k:int):
    if tablero_juego[i][j] == '*':
        return d
    elif tablero_juego[i][j] == '#':
        return k
    else:
        return 0


def main():
    n, m = map(int, input().split())
    d, k = map(int, input().split())
    tablero_juego = []
    for i in range(n):
        tablero_juego.append(input().split())

    print(camino_conejo(0, 0, n, m, tablero_juego, d, k))


if __name__ == '__main__':
    main()