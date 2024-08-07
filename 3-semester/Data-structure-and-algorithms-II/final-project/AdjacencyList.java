import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.LinkedList;

/**
 *
 * @author htrefftz
 */

/**
 * Clase que implementa una lista de adyacencia para representar un grafo no dirigido
 */
public class AdjacencyList {
    
    // El grafo se almacena como un arreglo de LinkedLists
    // Cada LinkedList contiene las aristas de un vértice
    LinkedList<Edge>[] graph;
    
    // Número de vértices
    int V;
    
    // Número de aristas
    int E;
    
    /**
     * Constructor.
     * @param filename nombre del archivo que contiene la información del grafo
     */
    public AdjacencyList(String filename) {
        try {
            Scanner in = new Scanner(new File(filename));
            // Leer el número de vértices y aristas
            V = in.nextInt();
            E = in.nextInt();

            // Definir las listas de tamaño V + 1
            // (de 1 a V)
            graph = new LinkedList[V+1];
            
            // Inicializar cada posición del arreglo como una lista vacía
            for(int i = 1; i <= V; i++) {
                graph[i] = new LinkedList<Edge>();
            }
            
            // Leer cada arista del archivo (hay E aristas) y agregarla
            // a la lista de adyacencia
            for(int i = 0; i < E; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                Edge e = new Edge(v);
                addEdge(u, e);
            }
        } catch (IOException e) {
            System.out.println("Could not open file " + filename);
            System.exit(1);
        }
    }
    
    /**
     * Agregar una arista a la lista de adyacencia
     * @param u origen de la arista
     * @param e arista a agregar
     */
    public void addEdge(int u, Edge e) {
        // Agregar la arista a la lista del vértice u
        graph[u].add(e);
    }
    
    /**
     * Devuelve una cadena que contiene la información del grafo en un formato legible
     * @return la cadena que se puede imprimir
     */
    public String toString() {
        // Agregar el número de vértices y aristas
        String s = "\n" + "Número de vértices: " + V + "\n";
        s += "Número de aristas: " + E + "\n";
        // Agregar la lista de adyacencia
        for(int i = 1; i < V + 1; i++) {
            s += "Vértice " + i + " -> ";
            for(Edge e : graph[i]) {
                s += e.to + " ";
            }
            s += "\n";
        }
        return s;
    }
    
    /**
     * Programa principal para probar el código
     *

    /**
     * Main program
     * @param args 
     */
    public static void main(String [] args) {
        AdjacencyList al = new AdjacencyList("graph2.txt");
        System.out.println(al);
    }
    
}



