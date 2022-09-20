from collections import deque


def binarios(n):
    binary_list = deque()
    binary = deque()
    binary.appendleft("1")
    for i in range(0, int(n)):
        binary.appendleft(binary[-1]+"0")
        binary.appendleft(binary[-1]+"1")
        binary_list.append(binary.pop())
    return binary_list


n = input()
print(binarios(n))