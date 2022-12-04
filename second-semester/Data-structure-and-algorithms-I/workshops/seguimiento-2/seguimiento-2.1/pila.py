from collections import deque


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    cola = deque(nums)
    while len(cola) != 0:
        element = cola.pop()
        print(element)


if __name__ == '__main__':
    main()