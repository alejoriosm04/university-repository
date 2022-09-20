from collections import deque


def main():
    soldiers = deque()
    while True:
        try:
            orders = input().split(" ")
            if orders[0] == "LLAMA":
                soldiers.appendleft(orders[1])
                print(orders[1])
            if orders[0] == "MANDA":
                if len(soldiers) == 0:
                    print("IMPOSIBLE")
                    continue
                print(soldiers.pop())
        except:
            break


if __name__ == '__main__':
    main()