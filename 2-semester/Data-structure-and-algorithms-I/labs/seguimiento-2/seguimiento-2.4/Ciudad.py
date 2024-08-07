# from collections import deque


# def vecinosDe(mat,actual):
#     losVecinos = set()
#     for arista in mat:
#       primero, segundo = arista
#       if primero == actual:
#         losVecinos.add(segundo)
#       if segundo == actual:
#         losVecinos.add(primero)
#     return losVecinos


# def camino(mat,origen,destino):
#     cola = deque()
#     cola.appendleft(origen)
#     visitados = dict()
#     while len(cola) != 0:
#         actual = cola.pop()
#         visitados[actual] = True
#         if actual == destino:
#             return True
#         vecinos = vecinosDe(mat,actual)
#         for vecino in vecinos:
#                 if actual not in visitados:
#                     cola.appendleft(vecino)
#     return False


# def ciudadUnida(N,M,mat):
#     pares = 0
#     for i in range(M):
#         print(i)
#         for j in range(i+1,M):
#             print(j)
#             print(mat[i][j])
#             if not camino(mat,i,j):
#                 pares = pares + 1
#     return pares


import time


def convert(mat):
    diccionario = dict()
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            if mat[i][j] in diccionario:
                diccionario[mat[i][j]] = diccionario[mat[i][j]].union(set(mat[i]))
            else:
                diccionario[mat[i][j]] = set(mat[i])
    
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            diccionario[mat[i][j]] = list(diccionario[mat[i][j]])

    return diccionario


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


def dfs(visited, graph, actual):
    if actual not in visited:
        visited.append(actual)
        for neightbour in graph[actual]:
            dfs(visited,graph,neightbour)


def ciudadUnida(N, M, mat):
    counter = 0
    diccionario = convert(mat)
    visited = []
    for key1 in diccionario.keys():
        for key2 in diccionario.keys():
            # if bfs(key1, key2, diccionario) is False:
            #     counter += 1
            # else:
            #     continue
            dfs(visited, diccionario, key1)
            if key2 not in visited:
                counter += 1

    return counter


def main():
    start = time.time()
    N1 = 5
    M1 = 3
    mat1 = [[1,2],[3,4],[3,5]]
    print(ciudadUnida(N1, M1, mat1))
    print(f'Time Algorithm: {time.time() - start} segundos')

    start = time.time()
    N2 = 5 
    M2 = 3 
    mat2 = [[1, 2], [2, 4], [3, 5]]
    print(ciudadUnida(N2, M2, mat2))
    print(f'Time Algorithm: {time.time() - start} segundos')

    start = time.time()
    N3 = 6 
    M3 = 4 
    mat3 = [[1, 2], [2, 4], [2, 3], [5, 6]]
    print(ciudadUnida(N3, M3, mat3))
    print(f'Time Algorithm: {time.time() - start} segundos')


if __name__ == '__main__':
    main()