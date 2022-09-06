## 1. ¿Cuál es la complejidad asintótica, en el peor de los casos, del siguiente algoritmo?

```python
def f(n):
   if n == 0:
       return 1 -> Constante
   else:
       return n*f(n-1) -> Un retorno n-1
```
### ``` O(n) ```

## 2. ¿Cuál es la complejidad asintótica, en el peor de los casos, del algoritmo f?

```python
def f(n):
    i = 1
    while i*i < n: -> 
       j = 1
       while j*j < n: -> 
          for k in range(0,n): -> Un ciclo con n
              for h in range(0,n+1): -> Un ciclo con n
                  print("hola")
           j = j + 1
       i = i + 1                -> (n/2)*(n/2)*n*n
```
### ``` O(n*n*n) ```

## 3. ¿Cuál es la complejidad asintótica, en el peor de los casos, del algoritmo mistery?

```python
def mistery(n):
   res = 0
   for i in range(0,n): -> Ciclo con n
      for j in range(0,n**3): -> Ciclo con n^3
          res = res * 2     -> n*n^3=n^4
```
### ``` O(n^4) ```

## 4. ¿Cuál es la complejidad asintótica, en el peor de los casos, de Suma Dígitos?

```python
def sumaDigitos(n):
  if n == 0:
    return 0 -> Retorno Constante
  else:
    return n%10 + sumaDigitos(n/10) -> Una llamado de n/10 (Tabla)
```
### ``` O(log n) ```

## 5. ¿Cuál es la complejidad asintótica, en el peor de los casos, de suma grupo?

```python
def sumaGrupo(i, numeros, meta):
    if i == len(numeros):
         return meta == 0 -> Retorno constante
    else:
         return sumaGrupo(i+1,numeros,meta) or
                    sumaGrupo(i+1,numeros,meta-numeros[i])
        -> Algunas veces, retorno de n-1 o 2 retornos de n-1
        -> El peor caso posible, son 2 retornos de n-1 (Tabla)
```
### ``` O(2^n) ```