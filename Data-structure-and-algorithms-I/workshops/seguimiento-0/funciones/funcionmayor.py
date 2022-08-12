def mayor(num1, num2, num3):
    arr = [num1, num2, num3]
    max_arr = num1
    for i in range(1, len(arr)):
        if arr[i] > max_arr:
            max_arr = arr[i]
    
    return max_arr


def main():
    print(mayor(1,2,50))


if __name__ == '__main__':
    main()