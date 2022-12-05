def suma_grupo(start, k, arr):
    if k == 0:
        return True
    elif start == len(arr):
        return False
    return suma_grupo(start+1, k-arr[start], arr) or suma_grupo(start+1, k, arr)


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if suma_grupo(0, k, arr):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()