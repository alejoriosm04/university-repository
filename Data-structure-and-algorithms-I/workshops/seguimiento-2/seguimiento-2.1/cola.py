from collections import deque


def main():
    n = int(input())
    nums = list(map(int, input().split()))
    q = deque()
    for i in range(len(nums)):
        q.appendleft(nums[i])
    while len(q) != 0:
        element = q.pop()
        print(element)



if __name__ == '__main__':
    main()