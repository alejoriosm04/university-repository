/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */
import java.util.Queue;
import java.util.LinkedList;

public class QueuesInJava {
    static Queue<BFNode> queue = new LinkedList<>(); 
    

    public static void main(String [] args) {
        queue.add(new BFNode(100));
        queue.add(new BFNode(200));
        queue.add(new BFNode(300));
        while(!queue.isEmpty()) {
            System.out.println(queue.poll());
        }
    }
    
}


class Node {
    int number;
    
    public Node(int i) {
        number = i;
    }
    
    public String toString() {
        String s = "";
        s += this.number + " ";
        return s;
    }
}
