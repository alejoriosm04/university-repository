import java.util.Scanner;
public class Main {
  public static void main(String [] args) {
    Scanner scan = new Scanner(System.in);
    String name = scan.next();
    int num;
    while (true) {
      num = scan.nextInt();
      if (num > 500) {
        System.out.println(name + " eres mi angel");
        break;
      } else {
        System.out.println(name + " me decepcionas");
      }
    }
  }
}