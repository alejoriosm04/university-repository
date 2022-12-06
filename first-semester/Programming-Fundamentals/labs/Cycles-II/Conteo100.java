import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int num;
    int contador = 0;
    while (true) {
      num = scan.nextInt();
      if (num > 100) {
        contador++;
      } else if (num == 0) {
        System.out.println(contador);
        break;
      }
    }
  }
}