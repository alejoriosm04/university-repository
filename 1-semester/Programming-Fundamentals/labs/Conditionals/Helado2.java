import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int temperatura = texto.nextInt();
    int edad = texto.nextInt();
    if (temperatura > 27 && edad >= 18) {
      System.out.println("Comprar helado cerveza");
    }
    else {
      System.out.println("Lo sentimos juventud");
    }
  }
}