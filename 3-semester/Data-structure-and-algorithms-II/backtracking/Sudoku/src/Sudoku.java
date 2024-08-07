/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */
import java.io.File;
import java.util.Scanner;
import java.io.FileNotFoundException;

public class Sudoku {
    public static boolean DEBUG = false;
    
    int [][] entrada = new int[9][9];
    
    int numBackTracks = 0;
    String asterisks = "*";
    
    /*
    int [][] entrada = {
        {6, 0, 0, 0, 0, 8, 0, 4, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 5},
        {0, 0, 0, 9, 1, 0, 2, 0, 0},
        
        {0, 0, 7, 0, 6, 0, 0, 0, 9},
        {0, 0, 9, 5, 8, 2, 1, 0, 0},
        {3, 0, 0, 0, 7, 0, 5, 0, 0},

        {0, 0, 6, 0, 2, 4, 0, 0, 0},
        {5, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 3, 0, 1, 0, 0, 0, 0, 7},
    };
    */
    
    int [][] enCurso = new int [9][9];
    
    void imprimirMatriz(int [][] mat) {
        System.out.println("Matriz:");
        for(int fila = 0; fila < 9; fila++) {
            for(int col = 0; col < 9; col++) {
                System.out.print(mat[fila][col] + " ");
            }
            System.out.println();
        }
    }
    
    boolean testFila(int fila, int n) {
        for(int col = 0; col < 9; col++) {
            if(enCurso[fila][col] == n) {
                return false;
            }
        }
        return true;
    }
    
    boolean testColumna (int col, int n) {
        for(int fila = 0; fila < 9; fila++) {
            if(enCurso[fila][col] == n) {
                return false;
            }
        }
        return true;
    }
    
    boolean testBarrio(int fila, int col, int n) {
        int filaIni = (fila / 3) * 3;
        int colIni = (col / 3) * 3;
        for(int f = filaIni; f < filaIni + 3; f++) {
            for(int c = colIni; c < colIni + 3; c++) {
                if(enCurso[f][c] == n) {
                    return false;
                }
            }
        }
        return true;
    }
    
    boolean test(int fila,int col) {
        // Hay una solución, se puede imprimir
        if(fila == 9) {
            imprimirMatriz(enCurso);
            System.out.print(asterisks + " ");
            System.out.println(asterisks.length());
            return true;
        }
        // Esa casilla ya está asignada desde la entrada
        // Pasar a la siguiente y retornar lo que retorne el test
        // de la siguiente celda
        if(entrada[fila][col] != 0) {
            Posicion pos = new Posicion(fila, col);
            pos.siguiente();
            return(test(pos.fila, pos.col));
        }
        // Esta casilla no está asignada desde la entrada
        // Ensayar con los números de 1 a 9
        for(int n = 1; n <= 9; n++) {
            if(testFila(fila, n)) {
                if(testColumna(col, n)) {
                    if(testBarrio(fila, col, n)) {
                        // Asignar este número en esa posición
                        enCurso[fila][col] = n;
                        // Añadimos asteriscos cada vez que se pone un número
                        asterisks += "*";
                        // Imprimir la cantidad de asteriscos asignados correctamente
                        System.out.print(asterisks.substring(0, asterisks.length()-1) + " ");
                        System.out.println(asterisks.length()-1);
                        if(DEBUG) {
                            System.out.println("fila: " + fila + " col: " + col + " " + n);
                        }
                        // Pasar a la siguiente posición
                        Posicion pos = new Posicion(fila, col);
                        pos.siguiente();
                        if(test(pos.fila, pos.col)) {       // found a solution
                            return true;
                        } else {
                            // No funcionó, quitamos el asterisco
                            asterisks = asterisks.substring(0, asterisks.length() - 1);
                            // No funcionó, ensayar en esta celda
                            // con el siguiente número entre 1 y 9
                            numBackTracks++;
                        }
                    }
                }
            }
        }
        // Si llega a este punto, se llegó a una inconsistencia
        // Ningún número entre 1 y 9 funcionó
        // Poner esta entrada en 0 para no dañar los tests 
        // mientras de hace el backtrack
        enCurso[fila][col] = 0;
        return false;
    }
    
    void inicializar() {
        for(int fila = 0; fila < 9; fila++) {
            for(int col = 0; col < 9; col++) {
                enCurso[fila][col] = entrada[fila][col];
            }
        }
    }
    
    private class Posicion {
        int fila;
        int col;
        
        public Posicion(int fila, int col) {
            this.fila = fila;
            this.col = col;
        }
        
        public void siguiente() {
            this.col++;
            if(this.col == 9) {
                this.col = 0;
                this.fila++;
            }
        }
     }
    
    public void leerArchivo(String nombre) {
        File archivo = new File(nombre);
        try {
            Scanner in = new Scanner(archivo);
            int fila = 0;
            while(in.hasNextLine()) {
                String linea = in.nextLine();
                for(int pos = 0; pos < 9; pos++) {
                    this.entrada[fila][pos] = Character.getNumericValue(linea.charAt(pos));
                }
                fila++;
            }
        } catch (FileNotFoundException ex) {
            System.out.println("Debe haber un archivo con el nombre sudoku.txt");
            // Logger.getLogger(Sudoku.class.getName()).log(Level.SEVERE, null, ex);
        }
        imprimirMatriz(entrada);
    }
    
    public static void main(String [] args) {
        Sudoku s = new Sudoku();
        s.leerArchivo("sudoku.txt");
        s.inicializar();
        s.imprimirMatriz(s.enCurso);
        // Ensayar con la primera celda
        s.test(0, 0);
        /*
        if(DEBUG) {
            System.out.println(s.testBarrio(3, 5, 1));
            System.out.println(s.testBarrio(3, 5, 2));
        }
        */
        System.out.println("Backtracks: " + s.numBackTracks);
    }
}



