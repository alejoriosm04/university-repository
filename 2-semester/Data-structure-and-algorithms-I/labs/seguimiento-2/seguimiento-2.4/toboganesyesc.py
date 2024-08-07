def dfs(tablero, actual, N, pasos):
    if actual >= N:
        return 10000000000000    
    if actual == N - 1:
        return pasos    
        
    mejor = None    
    for i in range(1, 7): # 1 ... 6        
        siguiente = actual + i        
        if siguiente < N and tablero[siguiente] != -1 and tablero[siguiente] >= siguiente:
            valor_retorno = dfs(tablero, tablero[siguiente], N, pasos + 1)
        else:
            valor_retorno = dfs(tablero, siguiente, N, pasos + 1)
        mejor = valor_retorno if mejor == None else min(valor_retorno, mejor)
    return mejor
    

def toboganes(move,N):
    resultado = dfs(move, 0, N, 0)
    print(resultado)


def main():
    move1 = [-1, -1, 21, -1, 7, -1, -1, -1, -1, -1, 25, -1, -1, -1, -1, -1, 3, -1, 6, 28, 8, -1, -1, -1, -1, -1, 0, -1, -1, -1] 
    N1 = 30
    toboganes(move1, N1)


if __name__ == '__main__':
    main()