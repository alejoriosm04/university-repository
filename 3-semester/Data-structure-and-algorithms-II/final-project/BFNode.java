public class BFNode {
    public int number;
    public int color;
    public int distance;
    public int pi;
    
    public BFNode(int number) {
        this.number = number;
    }
    
    public String toString() {
        String s = "";
        s += "Number: " + this.number + " ";
        s += "Distance: " + this.distance + " ";
        return s;
    }
}

