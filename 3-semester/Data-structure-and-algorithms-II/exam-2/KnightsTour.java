


/**
 * Algorithm to solve the Knights-tour problem for a board of size N
 * 
 * @author htrefftz
 */
public class KnightsTour {

    static final int N = 5;

    Celda[][] tablero;
    int visitadas;                  // Cuantas se han visitado, para saber cuándo terminar
    int soluciones;                 // Posibles soluciones comenzando por esa celda

    //boolean DEBUG = false;

    // Posibles celdas hacia donde salta el caballo
    // Primer número, salto en filas
    // Segundo número, salto en columnas
    Posicion[] proximas = {
        new Posicion(+1, -2),
        new Posicion(+2, -1),
        new Posicion(+2, +1),
        new Posicion(+1, +2),
        new Posicion(-1, +2),
        new Posicion(-2, +1),
        new Posicion(-2, -1),
        new Posicion(-1, -2)
    };

    /**
     * Constructor
     *
     * All cells are non-visited and have no previous node in the path
     */
    public KnightsTour() {
        tablero = new Celda[N][N];
        for (int f = 0; f < N; f++) {
            for (int c = 0; c < N; c++) {
                tablero[f][c] = new Celda();        // All cells are non-visited
            }
        }
        visitadas = 0;                              // 0 visited
        soluciones = 0;                             // 0 solutions
    }

    /**
     * Si this a valid cell to explore?
     *
     * @param pos Cell to explore
     * @return true if the cell is within the board and has not been visited,
     * false otherwise
     */
    boolean esValida(Posicion pos) {
        if (pos.col < 0 || pos.col >= N) {
            return false;
        }
        if (pos.fila < 0 || pos.fila >= N) {
            return false;
        }
        if (tablero[pos.fila][pos.col].visitada) {
            return false;
        }
        return true;
    }

    /**
     * Advance using backtracking
     *
     * @param pos Position to be visited
     * @param anterior Previous position in the path
     * @return true if the cell is part of a valid solution
     */
    boolean test(Posicion pos, Posicion anterior) {
        // Non-valid position
        if (!esValida(pos)) {
            return false;
        }

        // Visit this cell
        tablero[pos.fila][pos.col] = new Celda(true, anterior); // Mark as visited
        this.visitadas++;

        // All cells visited?
        if (this.visitadas == N * N) {
            imprimirTour(pos);
            // Un-visit this cell
            tablero[pos.fila][pos.col].visitada = false;
            this.visitadas--;
            return true;
        }
        // Try with next cells to visit
        // *** PUT YOUR CODE HERE ***
        // Usar el arreglo 'proximas' para calcular las posibles
        //   siguientes celdas a visitar
        //   Para cada celda, invocar recursivamente el método
        //   Puede resultar útil el método 'saltar' de la clase 'Posicion'
        // ...
        for (int i = 0; i < proximas.length; i++) {
            Posicion siguiente = pos.saltar(proximas[i]);
            test(siguiente, pos);
        }
        
        // After considering all valid children, unvisit this cell
        tablero[pos.fila][pos.col].visitada = false;
        this.visitadas--;
        return false;
    }

    /**
     * Generate all solutions from a specific cell
     *
     * @param f row
     * @param c column
     */
    void testAux(int f, int c) {
        Posicion pos = new Posicion(f, c);
        test(pos, null);
    }

    /**
     * A solution has been found
     * 
     * Un-comment the code in order to print the valid solutions
     * 
     * @param pos 
     */
    void imprimirTour(Posicion pos) {
        /* 
        ArrayList<Posicion> al = new ArrayList<>();
        System.out.println("Solución: ");
        while(pos != null) {
            //System.out.println(pos);
            al.add(pos);
            pos = tablero[pos.fila][pos.col].anterior;
        }
        Collections.reverse(al);
        for(Posicion p: al) {
            System.out.println(p);
        }
        */
        soluciones++;
    }

    /**
     * Class to keep the information of a cell
     */
    private class Celda {

        boolean visitada;       // true if cell has been visited
        Posicion anterior;      // previous cell in a valid solution

        /**
         * Constructor. Visited is false by default
         */
        public Celda() {
            this.visitada = false;
            this.anterior = null;
        }

        /**
         * Constructor
         * 
         * @param v true if cell has been visited
         * @param a previous cell
         */
        public Celda(boolean v, Posicion a) {
            this.visitada = v;
            this.anterior = a;
        }
    }

    /**
     * Class to keep the information of a position
     */
    private class Posicion {

        int fila;
        int col;
        
        /**
         * Constructor
         * @param fila row
         * @param col column
         */
        public Posicion(int fila, int col) {
            this.fila = fila;
            this.col = col;
        }

        /**
         * Next position to explore
         * 
         * @param delta
         * @return 
         */
        public Posicion saltar(Posicion delta) {
            int f = this.fila + delta.fila;
            int c = this.col + delta.col;
            return new Posicion(f, c);
        }

        /**
         * Used to print each cell visited in a path
         * @return 
         */
        public String toString() {
            return "f: " + this.fila + " c: " + this.col;
        }
    }

    /**
     * Main program
     *
     * @param args Not used
     */
    public static void main(String[] args) {
        for (int f = 0; f < N; f++) {
            for (int c = 0; c < N; c++) {
                KnightsTour kt = new KnightsTour();
                kt.testAux(f, c);
                System.out.println("Fila: " + f + " Col: " + c + ", Soluciones: " + kt.soluciones);
            }
        }
    }

}
