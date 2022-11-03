def pintar(mat, x, y, old_color, new_color):
    mat[x][y] = new_color

    n, m = len(mat), len(mat[0])
    for fila in (-1, 2, 1):
        for columna in (-1, 2, 1):
            newx, newy = x + fila, y + columna
            if 0 <= newx < n and 0 <= newy < m:
                if mat[newx][newy] == old_color:
                    pintar(mat, newx, newy, old_color, new_color)

    return mat


def main():
    x, y = map(int, input().split())
    old_color, new_color = map(str, input().split())
    n, m = map(int, input().split())
    mat = []

    for i in range(n):
        a = input().split(" ")
        mat.append(a)

    print(pintar(mat, x-1, y-1, old_color, new_color))


if __name__ == '__main__':
    main()