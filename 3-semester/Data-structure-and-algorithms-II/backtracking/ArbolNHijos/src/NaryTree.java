

/**
 *
 * @author htrefftz
 */
import java.util.Scanner;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.List;
import java.util.Collections;

/**
 * Class to implement a tree with any number of nodes
 * 
 * @author htrefftz
 */
public class NaryTree {
    Node root;
    
    public NaryTree(Node node) {
        this.root = node;
    }
    
    /**
     * Read the tree from a text file
     * 
     * Format:
     * Each line contains a path and a datum
     * The path and the datum are separated by a dot
     * The path is the sequence of siblings taken at each level
     * If the path is empty, the line describes the data to be stored 
     * at the root node.
     * 
     * @param fileName filename to read the tree from
     */
    public void readTree(String fileName) {
        try {
            Scanner in = new Scanner(new File(fileName));
            while(in.hasNextLine()) {
                String line = in.nextLine();
                if(!line.contains(".")) continue;
                String [] arr = line.split("[.]");
                String location = arr[0];
                String value = arr[1];
                Scanner locIn = new Scanner(location);
                Scanner valIn = new Scanner(value);
                ArrayList<Integer> locationAL = new ArrayList<>();
                int newValue = valIn.nextInt();
                while(locIn.hasNextInt()) {
                    locationAL.add(locIn.nextInt());
                }
                if(locationAL.isEmpty()) {        // root
                    root = new Node(newValue, null);
                } else {                            // other nodes
                    Node n = root;
                    int childNumber;                // follow the path
                    for(int i = 0; i < locationAL.size() - 1; i++) {
                        childNumber = locationAL.get(i);
                        n = n.children.get(childNumber);
                    }
                    // Last number in the location array: position to add the new node
                    Node newNode = new Node(newValue, n);                   // node to add
                    childNumber = locationAL.get(locationAL.size() - 1);    // where to add it
                    n.children.add(childNumber, newNode);
                }
                //System.out.println(location);
                //System.out.println(value);
                
            }
        } catch (FileNotFoundException e) {
            System.out.println(e);
        }
    }
    
    /**
     * Helper function. It calls printTree(Node node, int level)
     * 
     */
    public void printTree() {
        printTree(root, 0);
    }
    
    /**
     * Prints the tree, starting at node n.
     * Level is used to indent the data at lower levels of the tree
     * @param n node to start printing the tree. Usually the root
     * @param level level of the node, starting from the n node
     */
    public void printTree(Node n, int level) {
        for(int i = 0; i < level; i++) {
            System.out.print("\t");
        }
        System.out.println(n.data);
        for(Node child: n.children) {
            printTree(child, level+1);
        }
    }
    
    /**
     * Print the path to the given node,
     * @param node node to print the path to
     */
    public void printPath(Node node) {
        System.out.println("Lo encontré: ");
        List<Integer> list = new ArrayList<>();
        while(node != null) {
            list.add(node.data);
            node = node.parent;
        }
        Collections.reverse(list);
        for(Integer i: list) {
            System.out.println(i);
        }
    }
    
    /**
     * Helper function
     * @param n datum to find in the tree
     * @return true if the value is found, else otherwise
     */
    public boolean find(int n) {
        return find(n, root);
    }
    
    /**
     * Find datum "n" within tree starting at node "node"
     * @param n datum to be found
     * @param node starting point of the tree 
     * @return 
     */
    public boolean find(int n, Node node) {
        // System.out.println("Node: " + node.data);
        if(node == null) return false;                  // empty tree
        if(node.data == n) {                            // Success
            printPath(node);
            return true;
        }
        for(Node child: node.children) {
            find(n, child);
        }
        return false;
    }
}
