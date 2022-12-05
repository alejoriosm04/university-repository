def segundoyultimo(arr):
    if arr[1] > arr[len(arr)-1]:
        print(arr[1] * arr[len(arr)-1])
    else:
        print(arr[1] + arr[len(arr)-1])


def main():
    arr = [200,450,300,700,400,800]
    segundoyultimo(arr)


if __name__ == '__main__':
    main()