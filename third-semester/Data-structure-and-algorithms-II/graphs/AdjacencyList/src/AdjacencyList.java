import java.io.File;
import java.io.IOException;
import java.util.Scanner;
import java.util.LinkedList;

/**
 *
 * @author htrefftz
 */
public class AdjacencyList {
    
    // The graph is stored as an array of LinkedLists
    // Each LinkedList contains the 
    LinkedList<Edge> [] graph;
    
    // Number of vertices
    int V;
    
    // Number of edges
    int E;
    
    /**
     * Constructor.
     */
    public AdjacencyList(String filename) {
        try {
            Scanner in = new Scanner(new File(filename));
            // Read number of vertices and number of edges
            
            // Define the array lists of size V + 1
            // (from 0 to V)
            graph = new LinkedList[V+1];
            
            // Initialize each array position as a reference to an emtpy list
            
            // Read each edge from the file (there are E edges) and add it
            
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
        AdjacencyList al = new AdjacencyList("graph1.txt");
        System.out.println(al);
    }
    
}

/**
 * Store the information of an edge.
 * In future versions, the weight will be added
 */
class Edge {
    int to;

    public Edge(int to) {
        this.to = to;
    }
    
}