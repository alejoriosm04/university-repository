import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int temperatura = texto.nextInt();
    if (temperatura > 27) {
      System.out.println("Comprar helado cerveza");
    }
  }
}