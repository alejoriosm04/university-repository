from collections import deque


def main():
    n = int(input())
    s = deque()
    history = deque()
    for i in range(0, n):
        operation = input().split(" ")
        if operation[0] == "1":
            history.append(list(s))
            for letter in operation[1]:
                s.append(letter)
            print(s)
            print(history)
        if operation[0] == "2":
            history.append(list(s))
            for i in range(0, int(operation[1])):
                s.pop()
            print(s)
            print(history)
        if operation[0] == "3":
            print(s[int(operation[1])-1])
            print(s)
            print(history)
        if operation[0] == "4":
            s = deque(history.pop())


if __name__ == '__main__':
    main()