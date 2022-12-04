def suma_por_grupos(start, arr, k):
    if k == 0:
        return True
    elif start == len(arr):
        return False

    if start != len(arr)-1 and arr[start] % 5 == 0 and arr[start+1] == 1:
        return suma_por_grupos(start+2, arr, k-arr[start]) or suma_por_grupos(start+2, arr, k)
    elif arr[start] % 5 == 0:
        return suma_por_grupos(start+1, arr, k-arr[start])
    else:
        return suma_por_grupos(start+1, arr, k-arr[start]) or suma_por_grupos(start+1, arr, k)


def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(input()))

    k = int(input())
    print(suma_por_grupos(0, arr, k))


if __name__ == '__main__':
    main()