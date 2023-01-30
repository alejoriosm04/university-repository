from generator import *


def createDummies(total):
    try:
        if total > 0:
            list = []
            for item in range(total):
                list.append(Person())
            return list
    except:
        return None


def seeList(list):
    i = 1
    for item in list:
        print(f'({i}) {item}')
        i+=1


def main():
    data = createDummies(int(input('How many data?: ')))
    seeList(data)


if __name__ == '__main__':
    main()