import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int num;
    while (true) {
      num = scan.nextInt();
      if (num != 0) {
        num = num * 3;
        System.out.println(num);
      } else {
        break;
      }
    }
  }
}