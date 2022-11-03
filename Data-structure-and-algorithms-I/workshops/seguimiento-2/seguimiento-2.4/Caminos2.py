from collections import defaultdict
import time


def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           adjList[i].append(j)
    return adjList


def bfs(a, b, graph):
    visited = [False]*len(graph)
    queue = []

    queue.append(a)

    visited[a] = True

    while queue:
        n = queue.pop(0)

        if n == b:
            return True

        for i in graph[n]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    return False


def camino(a,b,mat):
    diccionario = convert(mat)
    return bfs(a, b, diccionario)


def main(): 
    start = time.time()
    a1 = 3
    b1 = 1
    mat1 = [[0, 1, 1, 0],[0, 0, 1, 0],[1, 0, 0, 1],[0, 0, 0, 1]]

    print(camino(a1, b1, mat1))
    print(f'Time Algorithm: {time.time() - start} segundos')

    start = time.time()
    a2 = 0
    b2 = 3
    mat2 = [[0, 1, 1, 0],[0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 1]]

    print(camino(a2, b2, mat2))
    print(f'Time Algorithm: {time.time() - start} segundos')


if __name__ == '__main__':
    main()