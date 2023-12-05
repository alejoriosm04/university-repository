
import java.util.Arrays;
import java.util.Queue;
import java.util.LinkedList;
import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * Main program to test Dijkstra's algorithm
 * 
 * @author htrefftz
 */
public class Main {

    static Queue<BFNode> queue = new LinkedList<>(); 
    /**
     * Main program to test the algorithm
     * @param args 
     */
    public static void main(String[] args) {

        Map<Integer, String> modificacion = new HashMap<>();
        modificacion.put(1, "Idiomas EAFIT");
        modificacion.put(2, "Puente de Idiomas");
        modificacion.put(3, "Escuela de Humanidades y de Ciencias (Bloque 38)");
        modificacion.put(4, "Biblioteca Luis Echavarría Villegas");
        modificacion.put(5, "Bloque 35");
        modificacion.put(6, "Bloque 34");
        modificacion.put(7, "Bloque 33");
        modificacion.put(8, "Plazoleta del Estudiante");
        modificacion.put(9, "Dogger");
        modificacion.put(10, "Bicicletas eléctricas");
        modificacion.put(11, "Portería norte de Las Vegas");
        modificacion.put(12, "Admisiones (Bloque 29)");
        modificacion.put(13, "Auditorio Fundadores");
        modificacion.put(14, "Escuela de Administración, Economía, y Finanzas");
        modificacion.put(15, "Bloque 18 de Rectoría");
        modificacion.put(16, "Centro Argos para la Innovación");
        modificacion.put(17, "Escultura Propileos");
        modificacion.put(18, "Café Con.verso");
        modificacion.put(19, "Ágora");
        modificacion.put(20, "Jardín Efímero");
        modificacion.put(21, "Centro de Visitantes (Bloque 31)");
        modificacion.put(22, "Cancha de voleibol");
        modificacion.put(23, "Piscina");
        modificacion.put(24, "Bloque 3");
        modificacion.put(25, "Cajeros Automáticos (ATM)");
        modificacion.put(26, "Bloque de Derecho");
        modificacion.put(27, "Bloque de Música");
        modificacion.put(28, "Camerinos (Bloque 39)");
        modificacion.put(29, "Instituto de Capacitación e Investigación del Plástico y el Caucho (ICIPC)");
        modificacion.put(30, "Canchas de tenis");
        modificacion.put(31, "Cafetería secundaria");
        modificacion.put(32, "Gimnasio al aire libre");
        modificacion.put(33, "Canchas atléticas");
        modificacion.put(34, "Parqueadero norte de autos");
        modificacion.put(35, "Cafetería Principal");
        modificacion.put(36, "Bloque 7");
        modificacion.put(37, "Bloque 17");
        modificacion.put(38, "Bloque 16");
        modificacion.put(39, "Cancha sintética (de fútbol y frisbee)");
        modificacion.put(40, "Bloque 15");
        modificacion.put(41, "Bloque 14");
        modificacion.put(42, "Bloque 13");
        modificacion.put(43, "Subway");
        modificacion.put(44, "Parqueadero de motos");
        modificacion.put(45, "Parqueadero sur de autos (visitantes)");
        modificacion.put(46, "Portería sur de Las Vegas");
        modificacion.put(47, "Desarrollo Artístico (Bloque 12)");
        modificacion.put(48, "Bloque 9 (Universidad de los Niños)");
        modificacion.put(49, "Bloque 10");
        modificacion.put(50, "Portería de la Avenida Regional");
        modificacion.put(51, "Bloque 19 de Ingeniería");
        modificacion.put(52, "Librería Acentos");
        modificacion.put(53, "Café Las Hermosas");
        modificacion.put(54, "Estación de carga Celsia");
        modificacion.put(55, "Gimnasio Vivo");
        modificacion.put(56, "Portería de Idiomas");
        modificacion.put(57, "La Bodeguita Minimarket");
        modificacion.put(58, "Sala de descanso");
        modificacion.put(59, "Laboratorio financiero");
        modificacion.put(60, "Bloque 23");
        modificacion.put(61, "Taller de Metalmecánica (Bloque 22)");
        modificacion.put(62, "Laboratorio de Sismorresistencia");
        modificacion.put(63, "Auditorio Fabricato");
        modificacion.put(64, "La Carpita Roja");
        modificacion.put(65, "Casa 6 del Consultorio Jurídico y Centro de Conciliación");
        modificacion.put(66, "Casa 4 de proyectos Innovación EAFIT");
        modificacion.put(67, "Casa 5 del Instituto Confucio");
        modificacion.put(68, "Casa 7 del Centro de Estudios Urbanos y Ambientales (Urbam)");
        modificacion.put(69, "Casa de Innovación y Casa de Egresados");
        modificacion.put(70, "Centro de Administración Documental");
        

        
       

        Scanner scanner = new Scanner(System.in);
        System.out.println("1: Idiomas EAFIT| 2: Puente de Idiomas| 3: Escuela de Humanidades y de Ciencias (Bloque 38)| 4: Biblioteca Luis Echavarría Villegas");
        System.out.println("5: Bloque 35| 6: Bloque 34| 7: Bloque 33| 8: Plazoleta del Estudiante| 9: Dogger| 10: Bicicletas eléctricas");
        System.out.println("11: Portería norte de Las Vegas| 12: Admisiones (Bloque 29)| 13: Auditorio Fundadores| 14: Escuela de Administración| Economía| y Finanzas\n15: Bloque 18 de Rectoría| 16: Centro Argos para la Innovación| 17: Escultura Propileos| 18: Café Con.verso| 19: Ágora");
        System.out.println("20: Jardín Efímero| 21: Centro de Visitantes (Bloque 31)| 22: Cancha de voleibol| 23: Piscina| 24: Bloque 3\n25: Cajeros Automáticos (ATM)| 26: Bloque de Derecho| 27: Bloque de Música| 28: Camerinos (Bloque 39)");
        System.out.println("29: Instituto de Capacitación e Investigación del Plástico y el Caucho (ICIPC)| 30: Canchas de tenis| 31: Cafetería secundaria\n32: Gimnasio al aire libre| 33: Canchas atléticas| 34: Parqueadero norte de autos| 35: Cafetería Principal| 36: Bloque 7| 37: Bloque 17\n38: Bloque 16| 39: Cancha sintética (de fútbol y frisbee)| 40: Bloque 15| 41: Bloque 14| 42: Bloque 13| 43: Subway| 44: Parqueadero de motos\n45: Parqueadero sur de autos (visitantes)| 46: Portería sur de Las Vegas| 47: Desarrollo Artístico (Bloque 12)\n48: Bloque 9 (Universidad de los Niños)| 49: Bloque 10| 50: Portería de la Avenida Regional| 51: Bloque 19 de Ingeniería\n52: Librería Acentos| 53: Café Las Hermosas| 54: Estación de carga Celsia| 55: Gimnasio Vivo| 56: Portería de Idiomas\n57: La Bodeguita Minimarket| 58: Sala de descanso| 59: Laboratorio financiero| 60: Bloque 23| 61: Taller de Metalmecánica (Bloque 22)\n62: Laboratorio de Sismorresistencia| 63: Auditorio Fabricato\n64: La Carpita Roja| 65: Casa 6 del Consultorio Jurídico y Centro de Conciliación| 66: Casa 4 de proyectos Innovación EAFIT\n67: Casa 5 del Instituto Confucio| 68: Casa 7 del Centro de Estudios Urbanos y Ambientales (Urbam)\n69: Casa de Innovación y Casa de Egresados| 70: Centro de Administración Documental");

        System.out.print("Elija su Punto de Partida: ");
        int opcion1 = scanner.nextInt();

        String inicio = modificacion.get(opcion1);
        System.out.println("Su punto de Partida es: " + inicio);

        // "old" format: one line in the text file per vertex
        //Dijkstra dijkstra = new Dijkstra("graph.txt", "old");
        // "new" format: one line in the text file per edge
        Dijkstra dijkstra = new Dijkstra("graphNew.txt", "new");
        long start = System.nanoTime();
        dijkstra.findShortestPaths(opcion1);
        long end = System.nanoTime();
        double tiempoEnSegundos = (end - start) / 1_000_000_000.0;
        System.out.println("Time Dijkstra: " + tiempoEnSegundos + " seconds");
        //ArrayList<Integer> path = dijkstra.getPath(200);
        //System.out.print(path);
        //System.out.println(" distance: " + dijkstra.dist[200]);

        long start2 = System.nanoTime();
        FloydWarshall fw = new FloydWarshall("graphNew.txt");
        fw.computeDistances();
        long end2 = System.nanoTime();
        double tiempoEnSegundos2 = (end2 - start2) / 1_000_000_000.0;
        System.out.println("Time FloydMarshall: " + tiempoEnSegundos2 + " seconds");

        long start3 = System.nanoTime();
        Graph graph = new Graph("graphNew.txt");
        graph.initialize(opcion1);
        long end3 = System.nanoTime();
        double tiempoEnSegundos3 = (end3 - start3) / 1_000_000_000.0;
        System.out.println("Time Bellman Ford: " + tiempoEnSegundos3 + " seconds");

        long start4 = System.nanoTime();
        queue.add(new BFNode(100));
        queue.add(new BFNode(200));
        queue.add(new BFNode(300));
        long end4 = System.nanoTime();
        double tiempoEnSegundos4 = (end4 - start4) / 1_000_000_000.0;
        System.out.println("Time BFS: " + tiempoEnSegundos4 + " seconds");
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
