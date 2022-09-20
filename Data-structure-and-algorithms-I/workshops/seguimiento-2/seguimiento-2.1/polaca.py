from collections import deque


def main():
    pila = deque()
    ecuation = input().split(" ")
    operators = ["+", "-", "*", "/"]
    for i in range(len(ecuation)):
        if ecuation[i] in operators:
            number1 = pila.pop()
            number2 = pila.pop()
            # print(number2 + ecuation[i] + number1)
            answer = str(eval(number2 + ecuation[i] + number1))
            pila.append(answer)
        else:
            pila.append(ecuation[i])
    print(pila.pop())


if __name__ == '__main__':
    main()