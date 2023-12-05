
import java.io.File;
import java.io.IOException;
import java.util.Scanner;


/**
 *
 * @author htrefftz
 */
public class AdjacencyMatrix {
    // The graph is stored as an array of LinkedLists
    // Each LinkedList contains the 
    int [][] graph;
    
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
            V = in.nextInt();
            E = in.nextInt();
            
            // Define matrix of Edges of size V x V
            this.graph = new int[V+1][V+1];
            
            // Initialize each matrix position with infinite distance
            // except for the diagonal, in this case distance is 0
            for(int fila = 1; fila <= V; fila++) {
                for(int col = 1; col <= V; col++) {
                    if(fila != col) {
                        graph[fila][col] = Integer.MAX_VALUE;
                    } else {
                        graph[fila][col] = 0;
                    }
                }
            }
            
            // Read each edge from the file (there are E edges) and add it
            // to the adjacency matrix
            for(int i = 0; i < E; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                int w = in.nextInt();
                graph[u][v] = w;
            }
        } catch (IOException e) {
            System.out.println("Could not open file " + filename);
            System.exit(1);
        }
    }
    
} 
