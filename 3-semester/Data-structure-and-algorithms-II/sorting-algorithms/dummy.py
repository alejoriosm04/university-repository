from generator import *
from sorting import *
import time
import matplotlib.pyplot as plt


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


def graphing(data):
    t1 = []
    t2 = []
    t3 = []

    if len(data) <= 100:
        for i in range(1, len(data), 10):
            start_time = time.time()
            sortData = mergeSort(data[:i])
            mergesort_time = time.time() - start_time
            t1.append(mergesort_time)

            start_time = time.time()
            sortData = quickSort(data[:i])
            quicksort_time = time.time() - start_time
            t2.append(quicksort_time)

            start_time = time.time()
            sortData = bubbleSort(data[:i])
            bubblesort_time = time.time() - start_time
            t3.append(bubblesort_time)
        
        x = range(1, len(data)+1, 10)
        plt.plot(x, t1, label='MergeSort')
        plt.plot(x, t2, label='QuickSort')
        plt.plot(x, t3, label='BubbleSort')
        plt.xlabel('Number of data sorted')
        plt.ylabel('Execution time (seconds)')
        plt.title('Execution time of sorting algorithms')
        plt.legend()
        plt.show()
    else:
        for i in range(1, len(data), 100):
            start_time = time.time()
            sortData = mergeSort(data[:i])
            mergesort_time = time.time() - start_time
            t1.append(mergesort_time)

            start_time = time.time()
            sortData = quickSort(data[:i])
            quicksort_time = time.time() - start_time
            t2.append(quicksort_time)

            start_time = time.time()
            sortData = bubbleSort(data[:i])
            bubblesort_time = time.time() - start_time
            t3.append(bubblesort_time)

        x = range(1, len(data)+1, 100)
        plt.plot(x, t1, label='MergeSort')
        plt.plot(x, t2, label='QuickSort')
        plt.plot(x, t3, label='BubbleSort')
        plt.xlabel('Number of data sorted')
        plt.ylabel('Execution time (seconds)')
        plt.title('Execution time of sorting algorithms')
        plt.legend()
        plt.show()


def main():
    # Ask for creation of data
    data = createDummies(int(input('How many data?: ')))

    # # Testing data with numbers and strings
    # # data = [4, 9, 1, 78, 7, -8, 5, 4, 78]
    # # data = ['camisa', 'vaca', 'carro']

    # # Print data
    # # seeList(data)

    print("="*20)

    # # MergeSort
    # start_time = time.time()
    # sortData = mergeSort(data)
    # #seeList(sortData)
    # print(f"Time MergeSort: {time.time() - start_time} seconds")

    # print("="*20)

    # # QuickSort
    # start_time = time.time()
    # sortData = quickSort(data)
    # #seeList(sortData)
    # print(f"Time QuickSort: {time.time() - start_time} seconds")

    # print("="*20)

    # # BubbleSort
    # start_time = time.time()
    # sortData = bubbleSort(data)
    # #seeList(sortData)
    # print(f"Time BubbleSort: {time.time() - start_time} seconds")
    graphing(data)


if __name__ == '__main__':
    main()