import java.util.ArrayList;
public class Main {
  // Ignorar el metodo main. Es una simple prueba de escritorio, no hace parte de la solucion
  public static void main(String[] args) {
    ArrayList<Integer> numbers = new ArrayList<Integer>();
    numbers.add(1);
    numbers.add(1);
    numbers.add(4);
    numbers.add(1);
    numbers.add(1);
    System.out.println(detectorDeRepetidos(numbers));
  }
  public static int detectorDeRepetidos(ArrayList<Integer> a) {
    int counter = 0;
    int memory = a.get(0);
    boolean state = true;
    for (int i = 1; i < a.size(); i++) {
      if (a.get(i) == memory) {
        if (state) {
          counter++;
          state = false;
        }
      } else {
        state = true;
      }
      memory = a.get(i);
    }
    return counter;
  }
}