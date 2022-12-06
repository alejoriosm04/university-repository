import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int temperatura = texto.nextInt();
    int edad = texto.nextInt();
    if (temperatura > 27 && edad >= 18) {
      int dinero = texto.nextInt();
      if (dinero > 5000) {
        System.out.println("Comprar helado cerveza");
      }
      else {
        System.out.println("De que me hablas viejo");
      }
    }
    else {
      System.out.print("Lo sentimos juventud");
    }
  }
}