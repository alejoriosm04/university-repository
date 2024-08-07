/**
 * Example of backtracking.
 * The program searches for a trajectory leading from the start point
 * to the exit.
 *
 * @author htrefftz
 */
import java.util.Scanner;

public class Laberinto {

    static String[] laberintoString = {
        "* ******************",
        "* ******** *********",
        "*       **        **",
        "* ***** ** ****** **",
        "* *****       *** **",
        "* ***** ***** *** **",
        "*       ***** *** **",
        "* ********    *** **",
        "*    ************   ",
        "********************",};

    static Coordenada entrada = new Coordenada(0, 1);        // Start
    static Coordenada salida = new Coordenada(8, 19);      // Exit

    static char[][] laberinto;                 // Char labyrinth

    static Coordenada[] ordenBusqueda = {
        new Coordenada(0, -1), // izquierda
        new Coordenada(+1, 0), // abajo
        new Coordenada(0, +1), // derecha
        new Coordenada(-1, 0) // arriba
    };

    static Scanner in = new Scanner(System.in);

    static final boolean STEP_BY_STEP = false;

    /**
     * Convert labyrinth from String to char
     */
    static void stringToChar() {
        int m = laberintoString.length;
        int n = laberintoString[0].length();
        laberinto = new char[m][n];
        for (int fila = 0; fila < m; fila++) {
            for (int col = 0; col < n; col++) {
                laberinto[fila][col] = laberintoString[fila].charAt(col);
            }
        }
    }

    /**
     * Print the labyrinth
     */
    static void imprimirLaberinto() {
        int m = laberinto.length;
        int n = laberinto[0].length;
        for (int fila = 0; fila < m; fila++) {
            for (int col = 0; col < n; col++) {
                System.out.print(laberinto[fila][col]);
            }
            System.out.println();
        }
        System.out.println();
    }

    /**
     * Visit one cell of the labyrinth. If this cell is visited, it is empty,
     * the test is done before the invocation.
     *
     * @param fila row of the cell
     * @param col column of the cell
     * @return true if a trajectory to the exit of the labyrinth has been found.
     * false otherwise,
     */
    static boolean visitarCelda(int fila, int col) {
        laberinto[fila][col] = '.';                         // Mark as visited 
        if (STEP_BY_STEP) {
            imprimirLaberinto();
        }

        if (salida.equals(fila, col)) {                      // Found the exit
            System.out.println("¡Llegué a la salida!");
            laberinto[fila][col] = 'x';
            return true;
        }
        for (Coordenada ob : ordenBusqueda) {               // Try in all directions
            int proxFila = fila + ob.fila;
            int proxCol = col + ob.col;
            if (!enRango(proxFila, proxCol)) {
                continue;       // Do not visit invalid positions
            }
            // *** PONER SU CÓDIGO AQUÍ ***
            // Si la proxima celda está disponible (en blanco)
            // Visitar la próxima celda (invocación recursiva)
            // Si el método retorna true, poner una 'x' en esta celda
            //   para marcar que es parte del camino
            //   y retornar true

            if (laberinto[proxFila][proxCol] == ' ') {
                if (visitarCelda(proxFila, proxCol)) {
                    laberinto[fila][col] = 'x';
                    return true;
                }
            }
        }
        laberinto[fila][col] = ';';             // Visited but not part of the solution
        if (STEP_BY_STEP) {
            imprimirLaberinto();
        }
        return false;
    }

    /**
     * Test if the row, column coordinate is within the labyrinth
     *
     * @param fila row coordinate
     * @param col column coordinate
     * @return
     */
    static boolean enRango(int fila, int col) {
        return (0 <= fila && fila < laberintoString.length
                && 0 <= col && col < laberintoString[0].length());
    }

    /**
     * Main program
     *
     * @param args Not used
     */
    public static void main(String[] args) {
        stringToChar();
        imprimirLaberinto();
        if (visitarCelda(entrada.fila, entrada.col)) {
            System.out.println("Éxito");
            System.out.println();
        } else {
            System.out.println("No se encontró la salida");
            System.out.println();
        }
        imprimirLaberinto();

        System.out.println("Convenciones: ");
        System.out.println(" : No visitado");
        System.out.println("x: Parte de la trayectoria final");
        System.out.println(";: Visitado, pero 'backtracked'");
        System.out.println(".: Visitado");
    }

    /**
     * Inner class to encapsulate the row and column coordinates
     */
    static class Coordenada {

        int fila;
        int col;

        /**
         * Constructor
         *
         * @param f row index
         * @param c column index
         */
        public Coordenada(int f, int c) {
            this.fila = f;
            this.col = c;
        }

        /**
         * Test for equality of this coordinate with the received row and column
         * values
         *
         * @param fila row value
         * @param col column value
         * @return true if the coordinates are the same. False otherwise.
         */
        boolean equals(int fila, int col) {
            return this.fila == fila && this.col == col;
        }
    }
}
