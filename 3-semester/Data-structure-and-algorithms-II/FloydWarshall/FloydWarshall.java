/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 * 
 * Implementation of the Floyd-Warthall algorithm for finding the shortest
 * paths from every pair of nodes in a graph.
 * 
 * @author htrefftz
 */
public class FloydWarshall {
    int [][] graph;
    int [][] dist;
    int [][] pred;
    int V;
    
    public FloydWarshall(String fileName) {
        AdjacencyMatrix am = new AdjacencyMatrix(fileName);
        this.graph = am.graph;
        V = graph.length - 1;
    }
    
    public void computeDistances() {
        // Copy matrix graph to matrix distance
        dist = new int [V+1][V+1];
        for(int fila = 0; fila <= V; fila++) {
            for(int col = 0; col <= V; col++) {
                dist[fila][col] = graph[fila][col];
            }
        }
        
        // Introduce vertices one bye one, from 1 to n
        for(int k = 1; k <= V; k++) {
            // Try to relax every entry in the matrix
            // going through vetex k
            for(int i = 1; i <= V; i++) {
                for(int j = 1; j <= V; j++) {
                    // Relax the entry going through vertex k
                    if(dist[i][k] != Integer.MAX_VALUE && dist[k][j] != Integer.MAX_VALUE) {
                        if(dist[i][k] + dist[k][j] < dist[i][j]) {
                            dist[i][j] =  dist[i][k] + dist[k][j];
                        }
                    }
                }
            }
            // Print the distance matrix after introducing vertex k
            System.out.println("K: " + k);
            printDistances();
        }
      
    }
    
    /**
     * Print the distance matrix
     */
    public void printDistances() {
        for(int fila = 1; fila <= V; fila++) {
            for(int col = 1; col <= V; col++) {
                if(dist[fila][col] != Integer.MAX_VALUE) {
                    //System.out.print(dist[fila][col] + " ");
                    System.out.printf("%3d ", dist[fila][col]);
                } else {
                    System.out.print("inf ");
                }
            }
            System.out.println();
        }
        System.out.println();
    }
}
