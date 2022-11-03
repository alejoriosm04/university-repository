## This problem was not finished

import sys


def top_three_repeated(arr):
    dict = {}
    for i in range(len(arr)):
        if arr[i] in dict:
            dict[arr[i]] += 1
        else:
            dict[arr[i]] = 1

    first = second = third = -sys.maxsize

    for value in dict.values():
        if value > first:
            third = second
            second = first
            first = value
        elif value > second:
            third = second
            second = value
        elif value > third:
            third = value

    

    return



def main():
    arr = [3, 4, 2, 3, 16, 3, 15, 16, 15, 15, 16, 2, 3]
    top_three_repeated(arr)


if __name__ == '__main__':
    main()