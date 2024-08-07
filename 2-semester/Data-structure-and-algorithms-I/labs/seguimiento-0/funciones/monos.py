def problemamonos(a_sonrie, b_sonrie):
    if (a_sonrie and b_sonrie) or (not a_sonrie and not b_sonrie):
        return True
    else:
        return False


def main():
    print(problemamonos(True, False)) # False
    print(problemamonos(False, False)) # True
    print(problemamonos(True, True)) # True
    print(problemamonos(False, True)) # False


if __name__ == '__main__':
    main()