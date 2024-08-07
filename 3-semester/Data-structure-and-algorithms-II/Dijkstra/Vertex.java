
/**
 * Maintains the information of a vertex
 * 
 * @author htrefftz
 */
public class Vertex implements Comparable<Vertex> {

    int node;                               // Number of this node
    int dist;                               // Shortest distance from source
                                            // computed by the algorithm

    public Vertex(int node, int dist) {
        this.node = node;
        this.dist = dist;
    }

    @Override
    public int compareTo(Vertex other) {
        return Integer.compare(dist, other.dist);
    }

}
