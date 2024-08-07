import java.util.Scanner;
  public class Main {
    public static void main(String[] args) {
      Scanner scan = new Scanner(System.in);
      String texto1 = scan.next();
      int posicionInicial = scan.nextInt();
      int posicionFinal = scan.nextInt();
      System.out.println(texto1.substring(posicionInicial, (posicionFinal + 1)));
    }
  }