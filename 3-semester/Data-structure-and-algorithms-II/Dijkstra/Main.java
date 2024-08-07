
import java.util.Arrays;

/**
 * Main program to test Dijkstra's algorithm
 * 
 * @author htrefftz
 */
public class Main {
    /**
     * Main program to test the algorithm
     * @param args 
     */
    public static void main(String[] args) {
        // "old" format: one line in the text file per vertex
        //Dijkstra dijkstra = new Dijkstra("graph.txt", "old");
        // "new" format: one line in the text file per edge
        Dijkstra dijkstra = new Dijkstra("graphNew.txt", "new");
        long start = System.nanoTime();
        dijkstra.findShortestPaths(1);
        long end = System.nanoTime();
        System.out.println("Time: " + (end - start));
        //ArrayList<Integer> path = dijkstra.getPath(200);
        //System.out.print(path);
        //System.out.println(" distance: " + dijkstra.dist[200]);
        System.out.println(Arrays.toString(dijkstra.dist));
    }
    
}
