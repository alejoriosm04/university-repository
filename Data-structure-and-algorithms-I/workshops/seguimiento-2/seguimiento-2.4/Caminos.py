# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)

#     print(start)

#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


# graph = {'0': set(['1', '2']),
#          '1': set(['0', '3', '4']),
#          '2': set(['0']),
#          '3': set(['1']),
#          '4': set(['2', '3'])}

# dfs(graph, '0')

# def dfs(curr, hijos, visitados):
#     if len(hijos[curr]) == 0:
#         return
#     if curr in visitados:
#         return
#     visitados.append(curr)
#     for hijo in hijos:
#         dfs(hijo, hijos, visitados)


# def dfs(matriz, x, y):
#   matriz[x][y]  = 0  
#   n, m = len(matriz), len(matriz[0])
#   for fila in (0, 1, -1):
#     for col in (0, 1, -1):
#       newx, newy = x + fila, y + col
#       if 0 <= newx < n and 0 <= newy < m:
#         if matriz[newx][newy] == 0:
#           continue
#         dfs(matriz, newx, newy)


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = set()
#     visited.add(start)

#     print(start)

#     for next in graph[start] - visited:
#         dfs(graph, next, visited)
#     return visited


# def camino(a,b,mat):
#     bool = False
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == 1:
#                 dfs(mat, i, j)
#     return bool


# def dfs(mat, x, y, a, b):
#     if mat[a][b] == 1:
#         return True
#     mat[x][y]  = 0
  
#     n, m = len(mat), len(mat[0])
#     for fila in (0, 1, -1):
#         for col in (0, 1, -1):
#             newx, newy = x + fila, y + col
#             if 0 <= newx < n and 0 <= newy < m:
#                 if mat[newx][newy] == 0:
#                     continue
#                 dfs(mat, newx, newy)


# def camino(a, b, matriz) -> int:
#   for a in range(len(matriz)):
#     for b in range(len(matriz[0])):
#       if matriz[a][b] == 1:
#         return True
#     else:
#         return False


#  

# 3 1 
#   [[0, 1, 1, 0], 
#   [0, 0, 1, 0], 
#   [1, 0, 0, 1], 
#   [0, 0, 0, 1]]



# 0 3      0 1 2 3
#      0 [[0, 1, 1, 0], 
#      1 [0, 0, 1, 0], 
#      2 [1, 0, 0, 1], 
#      3 [0, 0, 0, 1]]

# from collections import defaultdict


# def dfs(visited, graph, actual):
#     if actual not in visited:
#         visited.add(actual)

#         for neighbour in graph[node]:
#             dfs(visited, graph, neighbour)


# def camino(a, b, mat):
#     adjList = defaultdict(list)
#     for i in range(len(mat)):
#         for j in range(len(mat[0])):
#             if mat[i][j] == 1:
#                 adjList[i].append(j)


import time
from collections import defaultdict


def convert(a):
    adjList = defaultdict(list)
    for i in range(len(a)):
        for j in range(len(a[i])):
                       if a[i][j]== 1:
                           adjList[i].append(j)
    return adjList
    

def dfs(visited,graph,actual):
    if actual not in visited:
        visited.append(actual)
        for neightbour in graph[actual]:
            dfs(visited,graph,neightbour)


def camino(a,b,mat):
    diccionario = convert(mat)
    visited = []
    dfs(visited,diccionario,a)
    if b in visited:
        return True
    else:
        return False


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