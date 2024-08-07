def dfs(mat, x, y):
    mat[x][y]  = 0
  
    n, m = len(mat), len(mat[0])
    for fila in (0, 1, -1):
        for col in (0, 1, -1):
            newx, newy = x + fila, y + col
            if 0 <= newx < n and 0 <= newy < m:
                if mat[newx][newy] == 0:
                    continue
                dfs(mat, newx, newy)


def countIslands(mat) -> int:
  ans = 0
  for i in range(len(mat)):
    for j in range(len(mat[0])):
      if mat[i][j] == 1:
        dfs(mat, i, j)
        ans += 1
  return ans    