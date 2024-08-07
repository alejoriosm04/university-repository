import java.io.File;
import java.io.IOException;
import java.util.Scanner;

/**
 *
 * @author htrefftz
 */
public class Graph {
    int V;
    int E;

    Edge[] edges;
    Vertex[] vertices;

    int numEdges;

    public Graph(String filename) {
        try {
            Scanner in = new Scanner(new File(filename));
            // Read number of vertices and number of edges
            V = in.nextInt();
            E = in.nextInt();

            // Define the array lists of size V + 1
            edges = new Edge[E];
            vertices = new Vertex[V + 1];
            numEdges = 0;

            // Read each edge from the file (there are E edges) and add it
            // to the array
            for (int i = 0; i < E; i++) {
                int u = in.nextInt();
                int v = in.nextInt();
                int w = in.nextInt();
                Edge e = new Edge(u, v, w);
                addEdge(e);
            }
        } catch (IOException e) {
            System.out.println("Could not open file " + filename);
            System.exit(1);
        }

    }

    public void initialize(int s) {
        for (int i = 1; i <= V; i++) {
            Vertex v = new Vertex(i, Integer.MAX_VALUE, null);
            vertices[i] = v;
        }
        vertices[s].d = 0;
    }

    public boolean computeDistances(int s) {
        initialize(s);
        for (int i = 1; i <= V - 1; i++) {
            for (int j = 0; j < E; j++) {
                relax(edges[j]);
            }
        }
        for (int j = 0; j < E; j++) {
            if (edgeFormsNegativeCycle(edges[j])) {
                return false;
            }
        }
        return true;
    }

    public String distances() {
        String s = "";
        for (int i = 1; i <= V; i++) {
            s += "Vertex " + i + " distance : " + vertices[i].d;
            if (vertices[i].pi == null) {
                s += " pi: nil\n";
            } else {
                s += " pi: " + vertices[i].pi.index + "\n";
            }
        }
        return s;
    }

    void relax(Edge e) {
        Vertex u = vertices[e.u];
        Vertex v = vertices[e.v];
        int w = e.w;
        if (u.d != Integer.MAX_VALUE && v.d > u.d + w) {
            v.d = u.d + w;
            v.pi = u;
        }
    }

    boolean edgeFormsNegativeCycle(Edge e) {
        Vertex u = vertices[e.u];
        Vertex v = vertices[e.v];
        int w = e.w;
        return u.d != Integer.MAX_VALUE && v.d > u.d + w;
    }

    void addEdge(Edge e) {
        edges[numEdges] = e;
        numEdges++;
    }

    public String toString() {
        String s = "";
        for (int i = 0; i < E; i++) {
            s += edges[i].u + " -> " + edges[i].v + " : " + edges[i].w + "\n";
        }
        return s;
    }
}