import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int num = texto.nextInt();
    int evaluate = num % 2;
    if (evaluate == 0) {
      System.out.println("Es par");
    } else {
      System.out.println("Es impar");
    }
  }
}