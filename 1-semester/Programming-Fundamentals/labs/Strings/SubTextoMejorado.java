import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String texto1 = scan.next();
    int posicionInicial = scan.nextInt();
    int posicionFinal = scan.nextInt();
    if (posicionFinal > texto1.length()) {
      System.out.println("Error");
    } else if (posicionInicial > posicionFinal) {
      System.out.println("Error2");
    } else {
      System.out.println(texto1.substring(posicionInicial, (posicionFinal + 1)));
    }
  }
}