import matplotlib.pyplot as plt
import time
import random


def multiply(A, B):
    n = len(A)

    if n == 1:
        C = [[0]]
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11 = [[0 for i in range(n//2)] for j in range(n//2)]
        A12 = [[0 for i in range(n//2)] for j in range(n//2)]
        A21 = [[0 for i in range(n//2)] for j in range(n//2)]
        A22 = [[0 for i in range(n//2)] for j in range(n//2)]

        B11 = [[0 for i in range(n//2)] for j in range(n//2)]
        B12 = [[0 for i in range(n//2)] for j in range(n//2)]
        B21 = [[0 for i in range(n//2)] for j in range(n//2)]
        B22 = [[0 for i in range(n//2)] for j in range(n//2)]

        split(A, A11, A12, A21, A22)
        split(B, B11, B12, B21, B22)

        P01 = multiply(A11, B11)
        P02 = multiply(A12, B21)
        P03 = multiply(A11, B12)
        P04 = multiply(A12, B22)
        P05 = multiply(A21, B11)
        P06 = multiply(A22, B21)
        P07 = multiply(A21, B12)
        P08 = multiply(A22, B22)

        C11 = add(P01, P02)
        C12 = add(P03, P04)
        C21 = add(P05, P06)
        C22 = add(P07, P08)

        C = [[0 for i in range(n)] for j in range(n)]
        join(C11, C12, C21, C22, C)

        return C
        
        
def multiplyStrassen(A, B):
    n = len(A)
    
    if n == 1:
        C = [[0]]
        C[0][0] = A[0][0] * B[0][0]
        return C
    else:
        A11 = [[0 for x in range(n//2)] for y in range(n//2)]
        A12 = [[0 for x in range(n//2)] for y in range(n//2)]
        A21 = [[0 for x in range(n//2)] for y in range(n//2)]
        A22 = [[0 for x in range(n//2)] for y in range(n//2)]
        B11 = [[0 for x in range(n//2)] for y in range(n//2)]
        B12 = [[0 for x in range(n//2)] for y in range(n//2)]
        B21 = [[0 for x in range(n//2)] for y in range(n//2)]
        B22 = [[0 for x in range(n//2)] for y in range(n//2)]
        
        split(A, A11, A12, A21, A22)
        split(B, B11, B12, B21, B22)

        S01 = add(A11, A22)
        S02 = add(B11, B22)
        S03 = add(A21, A22)
        S04 = subtract(B12, B22)
        S05 = subtract(B21, B11)
        S06 = add(A11, A12)
        S07 = subtract(A21, A11)
        S08 = add(B11, B12)
        S09 = subtract(A12, A22)
        S010 = add(B21, B22)
        
        M01 = multiplyStrassen(S01, S02)
        M02 = multiplyStrassen(S03, B11)
        M03 = multiplyStrassen(A11, S04)
        M04 = multiplyStrassen(A22, S05)
        M05 = multiplyStrassen(S06, B22)
        M06 = multiplyStrassen(S07, S08)
        M07 = multiplyStrassen(S09, S010)
                
        C11 = subtract(add(add(M01, M04), M07), M05)
        C12 = add(M03, M05)
        C21 = add(M02, M04)
        C22 = subtract(add(add(M03, M06), M01), M02)
                
        C = [[0 for x in range(n)] for y in range(n)]
        join(C11, C12, C21, C22, C)

        return C
    

def subtract(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]

    return C


def split(A, A11, A12, A21, A22):
    n = len(A) // 2

    for i in range(n):
        A11[i][:n] = A[i][:n]
        A12[i][:n] = A[i][n:]
        A21[i][:n] = A[i+n][:n]
        A22[i][:n] = A[i+n][n:]


def join(C11, C12, C21, C22, C):
    n = len(C11)

    for i in range(n):
        C[i][0 : n] = C11[i][0 : n]
        C[i][n : 2 * n] = C12[i][0 : n]
        C[i + n][0 : n] = C21[i][0 : n]
        C[i + n][n : 2 * n] = C22[i][0 : n]


def add(A, B):
    n = len(A)
    C = [[0 for x in range(n)] for y in range(n)]

    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]

    return C


def normalMultiplication(A, B):
    C = [[0 for fila in range(len(B[0]))] for col in range(len(A))]
    
    # Realiza la multiplicación
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    return C


def graphing():
    t1_normalMultiplication = []
    t2_multiplyDivideConquer = []
    t3_multiplyStrassen = []

    n = 1
    for n in range(10):
        # Create matrices of size 2^n with random numbers from 1 to 10
        A = [[random.randint(1, 10) for i in range(2**n)] for j in range(2**n)]
        B = [[random.randint(1, 10) for i in range(2**n)] for j in range(2**n)]

        # # Normal multiplication
        # start = time.time()
        # normalMultiplication(A, B)
        # end = time.time()
        # t1_normalMultiplication.append(end - start)

        # Divide and conquer
        start = time.time()
        multiply(A, B)
        end = time.time()
        t2_multiplyDivideConquer.append(end - start)

        # Strassen
        start = time.time()
        multiplyStrassen(A, B)
        end = time.time()
        t3_multiplyStrassen.append(end - start)
        print(n)

    x = [2**n for n in range(10)]

    # plt.plot(x, t1_normalMultiplication, label='Normal multiplication')
    plt.plot(x, t2_multiplyDivideConquer, label='Divide and conquer')
    plt.plot(x, t3_multiplyStrassen, label='Strassen')
    plt.xlabel('Matrix size (2^n)')
    plt.ylabel('Time (s)')
    plt.title('Matrix multiplication algorithms')
    plt.legend()
    plt.savefig('divide-conquer.png')
    plt.show()
    plt.close()


def main():
    A = [[2, 3, 4, 5], [4, 5, 6, 7], [7, 8, 9, 10], [1, 2, 3, 4]]
    B = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [1, 1, 1, 1]]
    
    C = multiply(A, B)
    D = multiplyStrassen(A, B)
    
    print(C)
    print(D)
    
    d = normalMultiplication(A, B)
    print(d)

    graphing()


if __name__ == '__main__':
    main()
    