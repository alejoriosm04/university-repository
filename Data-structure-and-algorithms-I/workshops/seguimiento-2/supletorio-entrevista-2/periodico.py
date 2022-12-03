def main():
    n = int(input())
    for i in range(n):
        dict = {}
        k = int(input())
        for j in range(k):
            a = input().split(" ")
            dict[a[0]] = int(a[1]), 0

        m = int(input())
        for i in range(m):
            a = input()
            a = list(a)
            for j in a:
                if j in dict:
                    dict[j] = dict[j][0], dict[j][1] + dict[j][0]
                else:
                    continue

        counter = 0
        for value in dict.values():
            counter += value[1]

        counter = counter / 100

        print('{:.2f}'.format(counter) + "$")


if __name__ == '__main__':
    main()