/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author htrefftz
 */
public class Main {
    public static void main(String [] args) {
        FloydWarshall fw = new FloydWarshall("graph.txt");
        fw.computeDistances();
    }
}
