from collections import deque


def balance(s):
    d = deque()
    bool = True
    for i in s:
        if len(s) == 0:
            bool = True

        if i in ["(", "[", "{"]:
            d.append(i)

        if i == ")":
            if len(d) == 0 or d.pop() != "(":
                bool = False
                break
            else:
                continue

        if i == "]":
            if len(d) == 0 or d.pop() != "[":
                bool = False
                break
            else:
                continue

        if i == "}":
            if len(d) == 0 or d.pop() != "{":
                bool = False
                break
            else:
                continue

    if len(d) != 0:
        bool = False

    return bool


def main():
    s1 = "{[()]}"
    s2 = "({[)}]"

    print(balance(s1))
    print(balance(s2))


if __name__ == '__main__':
    main()