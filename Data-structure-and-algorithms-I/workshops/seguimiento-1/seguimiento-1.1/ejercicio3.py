def lcs(string1:str, string2:str, m, n):
    if m == 0 or n == 0:
        return 0
    elif string1[m-1] == string2[n-1]:
        return 1 + lcs(string1, string2, m-1, n-1)
    else:
        return max(lcs(string1, string2, m, n-1), lcs(string1, string2, m-1,n))


def main():
    string1 = input()
    string2 = input()
    print(lcs(string1, string2, len(string1), len(string2)))


if __name__ == '__main__':
    main()