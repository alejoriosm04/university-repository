from collections import deque


def mensaje(s):
    encrypted_message = s
    p = deque()
    counter = 0
    for i in range(0, len(encrypted_message)):
        if encrypted_message[i] == "(":
            p.append(encrypted_message[i])
        if encrypted_message[i] == ")" and len(p) != 0:
            p.pop()
            counter = counter + 2
    return counter


def main():
    s = input()
    print(mensaje(s))


if __name__ == '__main__':
    main()