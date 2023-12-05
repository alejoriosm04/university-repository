
import java.util.LinkedList;
import java.util.Queue;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */
public class BreadthFirst {

    public static final int WHITE = 0;
    public static final int GRAY = 1;
    public static final int BLACK = 2;

    AdjacencyList al;

    Queue<BFNode> queue;
    BFNode[] vertices;

    public BreadthFirst(String fileName) {
        al = new AdjacencyList(fileName);
        vertices = new BFNode[al.V + 1];
        queue = new LinkedList<BFNode>(); // Inicializar la cola
    }    

    public String toString() {
        String s = "";
        for (int i = 1; i <= al.V; i++) {
            s += "Vertex: " + vertices[i].number + " "
                + "Distancia: ";
            if (vertices[i].distance == Integer.MAX_VALUE) {
                s += "∞";
            } else {
                s += vertices[i].distance;
            }
            s += "\n";
        }
        return s;
    }
    
    
    public void computeDistances(int source) {
        // Inicializar los vértices
        for(int i = 1; i <= al.V; i++) {
            vertices[i] = new BFNode(i);
            vertices[i].color = WHITE;
            vertices[i].distance = Integer.MAX_VALUE;
            vertices[i].pi = -1;
        }
        // Inicializar el vértice fuente
        vertices[source].color = GRAY;
        vertices[source].distance = 0;
        vertices[source].pi = -1;
        // Agregar el vértice fuente a la cola
        queue.add(vertices[source]);
        // Mientras la cola no esté vacía
        while(!queue.isEmpty()) {
            // Sacar un vértice de la cola
            BFNode u = queue.remove();
            // Para cada vértice adyacente a u
            for(Edge e : al.graph[u.number]) {
                // Si el vértice no ha sido visitado
                if(vertices[e.to].color == WHITE) {
                    // Marcarlo como visitado
                    vertices[e.to].color = GRAY;
                    // Agregarlo a la cola
                    queue.add(vertices[e.to]);
                    // Actualizar la distancia
                    vertices[e.to].distance = vertices[u.number].distance + 1;
                    // Actualizar el padre
                    vertices[e.to].pi = u.number;
                }
            }
            // Marcar el vértice como visitado
            u.color = BLACK;
        }
    }

    public static void main(String[] args) {
        BreadthFirst bf = new BreadthFirst("graphNew2.txt");
        System.out.println(bf.al);
        bf.computeDistances(1);
        System.out.println(bf);
    }
    
}
