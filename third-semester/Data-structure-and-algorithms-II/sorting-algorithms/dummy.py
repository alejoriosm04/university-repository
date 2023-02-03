from generator import *
from sorting import *
import time


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
    # Ask for creation of data
    data = createDummies(int(input('How many data?: ')))

    # Testing data with numbers and strings
    # data = [4, 9, 1, 78, 7, -8, 5, 4, 78]
    # data = ['camisa', 'vaca', 'carro']

    # Print data
    # seeList(data)

    print("="*20)

    # MergeSort
    start_time = time.time()
    sortData = mergeSort(data)
    #seeList(sortData)
    print(f"Time MergeSort: {time.time() - start_time} seconds")

    print("="*20)

    # QuickSort
    start_time = time.time()
    sortData = quickSort(data)
    #seeList(sortData)
    print(f"Time QuickSort: {time.time() - start_time} seconds")

    print("="*20)

    # BubbleSort
    start_time = time.time()
    sortData = bubbleSort(data)
    #seeList(sortData)
    print(f"Time BubbleSort: {time.time() - start_time} seconds")


if __name__ == '__main__':
    main()