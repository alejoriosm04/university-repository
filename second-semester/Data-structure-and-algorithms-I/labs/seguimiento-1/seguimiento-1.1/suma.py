#Elimina el pass y escribe el codigo recursivo
def sumar(n:int)->int:
    if n <= 1:
        return 1
    else:
        return sumar(n-1) + n


def main():
    n=int(input())
    print(sumar(n))
    
main()