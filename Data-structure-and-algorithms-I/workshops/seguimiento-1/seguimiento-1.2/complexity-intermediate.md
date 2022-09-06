## 1. ¿Cuál es la complejidad asintótica, en el peor de los casos, del algoritmo de la subsecuencia común más larga entre X (de longitud m) y Y (de longitud p) presentado a continuación? Considera que el tamaño del problema n=m+p.

```python
def lcsAUX(X, Y, m, p):
    if m == 0 or p == 0:
      return 0 -> Retorno constante
    elif X[m-1] == Y[p-1]:
      return 1 + lcsAUX(X, Y, m-1, p-1) -> Esto ocurre en un caso positivo
                                        -> No lo tomamos en cuenta
    else:
      return max(lcsAUX(X, Y, m, p-1),
                 lcsAUX(X, Y, m-1, p))
            -> En el peor caso posible, tiene que realizar 2 retornos de n-1
def lcs(X,Y):
    return lcsAUX(X,Y,len(X),len(Y))
```
### ``` O(2^n) ```

## 2. ¿Cuál es la complejidad asintótica, en el peor de los casos, del algoritmo de la distancia de Levenshtein entre la cadena X (de longitud m) y la cadena Y (de longitud n), implementado a continuación?

```python
def editDist(str1, str2, m, n):
    dp = [[0 for x in range(n + 1)]
          for x in range(m + 1)] 
          -> Todo esto es una asignacion de varoles, constante
     for i in range(m + 1): -> Ciclo con m
        for j in range(n + 1): -> Ciclo con n
           if i == 0:
                dp[i][j] = j   
           elif j == 0:
                dp[i][j] = i    
           elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]
           else:
                dp[i][j] = 1 + min(dp[i][j-1],      
                                   dp[i-1][j],       
                                   dp[i-1][j-1])    
    return dp[m][n] 
    -> Todos los if fueron asignaciones de valores que son constantes
 
def levenshteinDistance(X, Y):
    return editDist(X, Y, len(X), len(Y))
```
### ``` O(m*n) ```

## 3. ¿Cuál es la complejidad asintótica, para el peor de los casos, de determinar si es posible encontrar un subgrupo de la lista set (que tiene n elementos) que sume el valor sum, con el siguiente algoritmo?

```python
def isSubsetSum(set, n, sum):
    subset =([[False for i in range(sum + 1)]
            for i in range(n + 1)])
    for i in range(n + 1): -> Asignacion de valores constante
        subset[i][0] = True
    for i in range(1, sum + 1): -> Asignacion de valores constante
         subset[0][i]= False
    for i in range(1, n + 1): -> Ciclo con n
        for j in range(1, sum + 1): -> Ciclo con sum
            if j<set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-
                                      set[i-1]])
    return subset[n][sum]
    -> Retorno constante e ifs con asignacion de valores constante

def sumaGrupo(set, sum):
       return isSubsetSum(set, len(set), sum)
```
### ``` O(n*sum) ```