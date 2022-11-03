## Arboles - Profundidad Arbol Trinario

class Node:
    def __init__(self, val=0, left=None, middle=None, right=None):
        self.val = val
        self.left = left
        self.middle = middle
        self.right = right

def depth(root:Node = None):
    if root == None :                                                    return 0   #ZZZ
    if root.left == None and root.middle == None and root.right == None: return 1   #000
    if root.left == None and root.middle == None :    return depth(root.right) +1   #001
    if root.left == None and root.right == None :    return depth(root.middle) +1   #010
    if root.middle == None and root.right == None :    return depth(root.left) +1   #100
    if root.left == None:     return max(depth(root.middle),depth(root.right)) +1   #011 
    if root.middle == None:     return max(depth(root.left),depth(root.right)) +1   #101
    if root.right == None:     return max(depth(root.left),depth(root.middle)) +1   #110
    return          max(depth(root.left),depth(root.middle),depth(root.right)) +1   #111


def main():
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)

    n2 = Node(2,n4,n5)
    n3 = Node(3,n6,n7)
    
    n1 = Node(1,n2,n3)
    print(depth(n1))

#     1 
#   2   3
#  4 5 6 7

main()


## Pilas y Colas - Balanceador de Parentesis
from collections import deque

def balance(s : str) -> str:
    d = deque()
    for i in s:
        if i in ["(","[","{"]: d.append(i)

        if i is ")": 
            if len(d)==0: return "No"
            if d.pop() == "(": continue
            return "No"

        if i is "]": 
            if len(d)==0: return "No"
            if d.pop() == "[": continue
            return "No"

        if i == "}": 
            if len(d)==0: return "No"
            if d.pop() == "{": continue
            return "No"
    return "Yes" if len(d) == 0 else "No"

print(balance(input()))


# Tablas de Hash

thash = {}
basura_pa_que_existes_morite_ni_pa_input_sirves = input()

for i in list(map(int,input().split())): thash[i] = True

i = 1
while(True):
    if i not in thash:
        print(i)
        quit()
    i +=  1


## Grafos

def paintUWU(matriz, Y, X, ini, end):  
    matriz[Y][X] = end
    filas = len(matriz)                 # DIMENSIONES DE LA MATRIZ, PARA ASEGURARSE DE QUE NO LAS SOBREPASE
    columnas = len(matriz[0])
    for iter_Y in range(-1,2,1):        # ITERADORES PARA QUE EJECUTE EN UN RADIO DE 1 ESPACIO
        for iter_X in range(-1,2,1):    # EL RANGE RETORNA [-1,0,1], EL FOR LO RECORRE Y LOS COLOCA EN LOS ACTUALES
            Y_actual = Y + iter_Y
            X_actual = X + iter_X       # COLOCA LOS ITERADORES EN EL X y Y A EJECUTAR (A CONVERTIR EN END)

            if -1 < Y_actual < filas:
                if -1 < X_actual < columnas:   # PARA QUE LA POSICIÓN A EJECUTAR NO SOBREPASE LOS LÍMITES
                    if matriz[Y_actual][X_actual] == ini: 
                        paintUWU(matriz, Y_actual, X_actual,ini,end)   # PINTA EL RESTO DE LA ZONA
    return matriz   # CONVIRTIÓ LA MATRIZ, LA RETORNA YA PINTADA


m = [[1,1,1,1,1],
     [0,1,0,0,0],
     [1,0,0,1,1],
     [0,0,0,0,1],
     [1,0,1,1,1]]


print(paintUWU(m,0,0,1,0))