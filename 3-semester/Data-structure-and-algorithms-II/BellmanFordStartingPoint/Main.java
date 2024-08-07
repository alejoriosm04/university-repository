/**
 *
 * @author htrefftz
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Graph graph = new Graph("graph.txt");
        System.out.println(graph);
        graph.initialize(1);
        System.out.println("Well-defined minimal paths: " + graph.computeDistances(1));
        System.out.println();
        System.out.println(graph.distances());
    }

}
