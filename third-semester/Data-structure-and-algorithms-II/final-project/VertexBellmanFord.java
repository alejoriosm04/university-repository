
/**
 *
 * @author htrefftz
 */
public class VertexBellmanFord {
    int index;
    int d;
    VertexBellmanFord pi;

    public VertexBellmanFord(int index, int d, VertexBellmanFord pi) {
        this.index = index;
        this.d = d;
        this.pi = pi;
    }

}
