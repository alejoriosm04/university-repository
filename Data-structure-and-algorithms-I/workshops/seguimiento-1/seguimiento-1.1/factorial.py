def factorial(n : int) -> int:
    """Elimina pass y completa con el código de la función factorial"""
    if n <= 1:
        return 1
    else:
        return factorial(n-1) * n

def main():
    n = int(input())
    print(factorial(n))
    
main()