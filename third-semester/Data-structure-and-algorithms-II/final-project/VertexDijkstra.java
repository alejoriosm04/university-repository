
/**
 * Maintains the information of a vertex
 * 
 * @author htrefftz
 */
public class VertexDijkstra implements Comparable<VertexDijkstra> {

    int node;                               // Number of this node
    int dist;                               // Shortest distance from source
                                            // computed by the algorithm

    public VertexDijkstra(int node, int dist) {
        this.node = node;
        this.dist = dist;
    }

    @Override
    public int compareTo(VertexDijkstra other) {
        return Integer.compare(dist, other.dist);
    }

}
