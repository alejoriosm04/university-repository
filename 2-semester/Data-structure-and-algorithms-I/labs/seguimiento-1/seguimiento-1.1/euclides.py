def euclides(a:int, b:int):
    if b == 0:
        return a
    else:
        return euclides(b, a%b)

def main():
    cases = int(input())
    for i in range(1, cases+1):
        a, b = map(int, input().split())
        print("Case " + str(i) + ": " + str(euclides(a, b)))


if __name__ == '__main__':
    main()