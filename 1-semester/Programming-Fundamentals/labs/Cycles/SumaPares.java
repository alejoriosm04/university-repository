import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int n = texto.nextInt();
    int acumulador = 0;
    for (int i = 0; i < n; i++) {
      int n1 = texto.nextInt();
      if (n1 % 2 == 0) {
        acumulador = acumulador + n1;
      }
    }
    System.out.println(acumulador);
  }
}