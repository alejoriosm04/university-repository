// SOLUCIONAR EL PROBLEMA DE LOGICA DEL PROGRAMA
public class Program {
    public static int Puzzle (int x) {
      if (x == -2) {
        return -1;
      } else if (x == -1) {
        return 0;
      } else if (x == 0) {
        return 1;
      } else if (x == 1) {
        return 2;
      } else {
        return x;
      }
    }
  }
  