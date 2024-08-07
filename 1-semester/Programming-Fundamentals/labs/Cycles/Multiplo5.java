import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int num = texto.nextInt();
    int i = 5;
    int j = 2;
    while (i <= num) {
      System.out.println(i);
      i = 5;
      i = i * j;
      j++;
    }
  }
}