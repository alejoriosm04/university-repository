def get_infectados(matriz, n, m):
    infectados = []
    for i in range(n):
        for j in range(n):
            if matriz[i][j] == 0:
                infectados.append((i,j))
    return infectados


def get_sanos(matriz, n, m):
    for i in range(n):
        for j in range(m):
            if matriz[i][j] == 1:
                return True
    return False


def contagio(matriz, x, y, n, m):
    matriz[x][y] = 0
    for fila in (0, 1, -1):
        newx = x + fila
        if 0 <= newx < n and matriz[newx][y] == 1:
            matriz[newx][y] = 0

    for columna in (0, 1, -1):
        newy = y + columna
        if 0 <= newy < m and matriz[x][newy] == 1:
            matriz[x][newy] = 0


def Ebola(matriz, n, m):
    tiempo = 0
    infectados = get_infectados(matriz, n, m)
    print(infectados)
    while get_sanos(matriz, n, m):
        for i in infectados:
            contagio(matriz, i[0], i[1], n, m)
        infectados = get_infectados(matriz, n, m)
        tiempo += 1
        print(matriz)
    return tiempo


def main():
    case2 = [[1,1,1],[1,0,1],[1,1,1]]
    M2 = 3
    N2 = 3

    print(Ebola(case2, M2, N2))


if __name__ == '__main__':
    main()
    