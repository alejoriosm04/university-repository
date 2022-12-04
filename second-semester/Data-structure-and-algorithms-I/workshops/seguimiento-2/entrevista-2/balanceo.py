from collections import deque


def validar(s):
    d = deque()
    answer = "Yes"
    for i in range(len(s)):
        if s[i] in ["(", "[", "{"]:
            d.append(s[i])

        if s[i] == ")":
            if len(d) == 0 or d.pop() != "(":
                answer = "No"
                break

        if s[i] == "]":
            if len(d) == 0 or d.pop() != "[":
                answer = "No"
                break

        if s[i] == "}":
            if len(d) == 0 or d.pop() != "{":
                answer = "No"
                break

    if len(d) != 0:
        answer = "No"

    return answer


def main():
    s1 = "()()()"
    s2 = "{[()]}"
    s3 = ")()(}{"
    print(validar(s1))
    print(validar(s2))
    print(validar(s3))


if __name__ == '__main__':
    main()