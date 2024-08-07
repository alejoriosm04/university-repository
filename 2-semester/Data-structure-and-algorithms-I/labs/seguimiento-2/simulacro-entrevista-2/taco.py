from collections import deque


def main():
    n = int(input())
    n_tacos = 0
    customers = deque()

    for i in range(0, n):
        operation = input().split(" ")
        if operation[0] == "1":
            customers.appendleft(int(operation[1]))
        if operation[0] == "2":
            n_tacos += customers.pop()
        if operation[0] == "3":
            print(len(customers))
        if operation[0] == "4":
            print(n_tacos)   


if __name__ == '__main__':
    main()     