

/**
 *
 * @author htrefftz
 */
public class OchoReinas {
    static final int N = 8;
    
    static int [][] tablero = new int[N][N];
    
    static int solucion = 0;

    //Find the 92 solutions
    static void ponerReina(int fila) {
        if(fila == N) {
            solucion++;
            System.out.println("Solucion: " + solucion);
            imprimirTablero();
            return;
        }
        
        for(int col = 0; col < N; col++) {
            if(validar(fila, col)) {
                tablero[fila][col] = 1;
                ponerReina(fila + 1);
                tablero[fila][col] = 0;
            }
        }
    }
    
    // static boolean ponerReina(int fila) {
    //     if(fila == N) {
    //         solucion++;
    //         System.out.println("Solucion: " + solucion);
    //         imprimirTablero();
    //         return true;
    //     }
        
    //     for(int col = 0; col < N; col++) {
    //         if(validar(fila, col)) {
    //             tablero[fila][col] = 1;
    //             if(ponerReina(fila + 1)) {
    //                 return true;
    //             }
    //             tablero[fila][col] = 0;
    //         }
    //     }

    //     return false;
    // }
    
    static boolean validar(int fila, int col) {
        // Validar la columna
        for(int f = 0; f < fila; f++) {
            if(tablero[f][col] == 1) return false;
        }
        
        // Validar diagonal 1
        int f = fila - 1; int c = col - 1;
        while(f >= 0 && c >= 0) {
            if(tablero[f][c] == 1) return false;
            f--;
            c--;
        }
        // Validar diagonal 2
        f = fila - 1; c = col + 1;
        while(f >= 0 && c < N) {
            if(tablero[f][c] == 1) return false;
            f--;
            c++;
        }
        return true;
    }
    
    static void imprimirTablero() {
        for(int fila = 0; fila < N; fila++) {
            for(int col = 0; col < N; col++) {
                System.out.print(tablero[fila][col] + " ");
            }
            System.out.println();
        }
        System.out.println();
    }
    
    public static void main(String [] args) {
        imprimirTablero();
        ponerReina(0);
    }
}
