def chequeoarreglo(arr):
    if len(arr) >= 1 and arr[0] == arr[len(arr)-1]:
        return True
    else:
        return False


def main():
    arr = [1,2,4,1]
    print(chequeoarreglo(arr))


if __name__ == '__main__':
    main()