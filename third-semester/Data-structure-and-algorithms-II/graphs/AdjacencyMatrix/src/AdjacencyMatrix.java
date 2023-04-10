
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */
public class AdjacencyMatrix {
    // The graph is stored as an array of LinkedLists
    // Each LinkedList contains the 
    Edge [][] graph;
    
    // Number of vertices
    int V;
    
    // Number of edges
    int E;
    
    /**
     * Constructor.
     */
    public AdjacencyMatrix(String filename) {
        try {
            Scanner in = new Scanner(new File(filename));
            // Read number of vertices and number of edges
            
            // Define matrix of Edges of size V x V
            graph = new Edge[V+1][V+1];
            
            // Initialize each array position as null
            
            // Read each edge from the file (there are E edges) and add it
            // to the adjacency matrix
            
        } catch (IOException e) {
            System.out.println("Could not open file " + filename);
            System.exit(1);
        }
    }
    
    /**
     * Add an edge to the adjacency list
     * @param u origin of the edge
     * @param v destination of the edge
     */
    public void addEdge(int u, Edge e) {
        
    }
    
    /**
     * Return a String that contains the graph information in a readable format
     * 
     * @return the string that can be printed
     */
    public String toString() {
        return "";
    }
    
    /**
     * Main program
     * @param args 
     */
    public static void main(String [] args) {
        AdjacencyMatrix am = new AdjacencyMatrix("graph1.txt");
        System.out.println(am);
    }
    
}

/**
 * Store the information of an edge.
 * In future versions, the weight will be added
 */
class Edge {
    int to;
    int weight;

    public Edge(int to, int weight) {
        this.to = to;
        this.weight = weight;
    }
    
}   
