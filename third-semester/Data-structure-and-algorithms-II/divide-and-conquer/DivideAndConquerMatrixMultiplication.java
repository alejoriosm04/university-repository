
import java.util.Arrays;

/**
 *
 * @author htrefftz
 */
public class DivideAndConquerMatrixMultiplication {
    /**
     * Recursive algorithm for matrix multiplication based on
     * Divide and Conquer
     * 
     * @param A First Matrix
     * @param B Second Matrix
     * @return Result of multiplying A x B
     */
    public static int[][] multiply(int[][] A, int[][] B) {
        int n = A.length;

        if (n == 1) {
            int[][] C = new int[1][1];
            C[0][0] = A[0][0] * B[0][0];
            return C;
        } else {
            int[][] A11 = new int[n/2][n/2]; int[][] A12 = new int[n/2][n/2];
            int[][] A21 = new int[n/2][n/2]; int[][] A22 = new int[n/2][n/2];            
            int[][] B11 = new int[n/2][n/2]; int[][] B12 = new int[n/2][n/2];
            int[][] B21 = new int[n/2][n/2]; int[][] B22 = new int[n/2][n/2];
            
            split(A, A11, A12, A21, A22);
            split(B, B11, B12, B21, B22);
            
            int[][] P01 = multiply(A11, B11);
            int[][] P02 = multiply(A12, B21);
            int[][] P03 = multiply(A11, B12);
            int[][] P04 = multiply(A12, B22);
            int[][] P05 = multiply(A21, B11);
            int[][] P06 = multiply(A22, B21);
            int[][] P07 = multiply(A21, B12);
            int[][] P08 = multiply(A22, B22);
                    
            int[][] C11 = add(P01, P02);
            int[][] C12 = add(P03, P04);
            int[][] C21 = add(P05, P06);
            int[][] C22 = add(P07, P08);
                    
            int[][] C = new int[n][n];
            join(C11, C12, C21, C22, C);

            return C;
        }
    }


    public static int[][] multiplyStrassen(int[][] A, int[][] B) {
        int n = A.length;

        if (n == 1) {
            int[][] C = new int[1][1];
            C[0][0] = A[0][0] * B[0][0];
            return C;
        } else {
            int[][] A11 = new int[n/2][n/2]; int[][] A12 = new int[n/2][n/2];
            int[][] A21 = new int[n/2][n/2]; int[][] A22 = new int[n/2][n/2];            
            int[][] B11 = new int[n/2][n/2]; int[][] B12 = new int[n/2][n/2];
            int[][] B21 = new int[n/2][n/2]; int[][] B22 = new int[n/2][n/2];
            
            split(A, A11, A12, A21, A22);
            split(B, B11, B12, B21, B22);

            int[][] S01 = add(A11, A22);
            int[][] S02 = add(B11, B22);
            int[][] S03 = add(A21, A22);
            int[][] S04 = subtract(B12, B22);
            int[][] S05 = subtract(B21, B11);
            int[][] S06 = add(A11, A12);
            int[][] S07 = subtract(A21, A11);
            int[][] S08 = add(B11, B12);
            int[][] S09 = subtract(A12, A22);
            int[][] S010 = add(B21, B22);
            
            int[][] M01 = multiplyStrassen(S01, S02);
            int[][] M02 = multiplyStrassen(S03, B11);
            int[][] M03 = multiplyStrassen(A11, S04);
            int[][] M04 = multiplyStrassen(A22, S05);
            int[][] M05 = multiplyStrassen(S06, B22);
            int[][] M06 = multiplyStrassen(S07, S08);
            int[][] M07 = multiplyStrassen(S09, S010);
                    
            int[][] C11 = subtract(add(add(M01, M04), M07), M05);
            int[][] C12 = add(M03, M05);
            int[][] C21 = add(M02, M04);
            int[][] C22 = subtract(add(add(M03, M06), M01), M02);
                    
            int[][] C = new int[n][n];
            join(C11, C12, C21, C22, C);

            return C;
        }
    }


    /**
     * Return the matrix resulting from A - B
     * @param A First matrix
     * @param B Second matrix
     * @return First - Second matrices
     */
    private static int[][] subtract(int[][] A, int[][] B) {
        int n = A.length;
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] - B[i][j];
            }
        }

        return C;
    }

    
    /**
     * 
     * Splits matrix A into 4 sub-blocks of equal size.
     * 
     * System.arraycopy is a built-in method in Java that can be used to copy arrays.
     * It takes the following parameters:
     *   src - the source array to copy from.
     *   srcPos - the starting position in the source array from where to start copying.
     *   dest - the destination array to copy to.
     *   destPos - the starting position in the destination array where to start copying to.
     *   length - the number of elements to copy.
     * 
     * @param A     Original matrix to divide
     * @param A11   Upper-left block
     * @param A12   Upper-right block
     * @param A21   Lower-left block
     * @param A22   Lower-right block
     */
    
    private static void split(int[][] A, int[][] A11, int[][] A12, int[][] A21, int[][] A22) {
        int n = A.length / 2;

        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, A11[i], 0, n);
            System.arraycopy(A[i], n, A12[i], 0, n);
            System.arraycopy(A[i+n], 0, A21[i], 0, n);
            System.arraycopy(A[i+n], n, A22[i], 0, n);
        }
    }

    /**
     * Joins C11, C12, C21 and C22 to a resulting C matrix
     * @param C11 Upper-left block
     * @param C12 Upper-right block
     * @param C21 Lower-left block
     * @param C22 Lower-right block
     * @param C Resulting matrix
     */
    private static void join(int[][] C11, int[][] C12, int[][] C21, int[][] C22, int[][] C) {
        int n = C11.length;

        for (int i = 0; i < n; i++) {
            System.arraycopy(C11[i], 0, C[i], 0, n);
            System.arraycopy(C12[i], 0, C[i], n, n);
            System.arraycopy(C21[i], 0, C[i+n], 0, n);
            System.arraycopy(C22[i], 0, C[i+n], n, n);
        }
    }

    /**
     * Adds two matrices of the same size
     * @param A First matrix
     * @param B Second matrix
     * @return result of adding A + B
     */
    private static int[][] add(int[][] A, int[][] B) {
        int n = A.length;
        int[][] C = new int[n][n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                C[i][j] = A[i][j] + B[i][j];
            }
        }

        return C;
    }
    
    /**
     * Multiplication using the textbook method
     * @param a First matrix
     * @param b Second matrix
     * @return Result of multiplying a * b
     */
    public static int [][] normalMultiplication(int [][] a, int [][] b) {
        int n = a.length;
        int [][] c = new int [n][n];
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                int acum = 0;
                for(int k = 0; k < n; k++) {
                    acum += a[i][k] * b[k][j];
                }
                c[i][j] = acum;
            }
        }
        return c;
    }

    public static void main(String[] args) {
        int[][] A = {{2, 3, 4, 5}, {4, 5, 6, 7}, {7, 8, 9, 10}, {1, 2, 3, 4}};
        int[][] B = {{1, 2, 3, 4}, {5, 6, 7, 8}, {9, 10, 11, 12}, {1, 1, 1, 1}};

        int[][] C = multiply(A, B);
        int[][] D = multiplyStrassen(A, B);

        System.out.println(Arrays.deepToString(C));
        System.out.println(Arrays.deepToString(D));
        
        int [][] d = normalMultiplication(A, B);
        System.out.println(Arrays.deepToString(d));
    }
    
}
