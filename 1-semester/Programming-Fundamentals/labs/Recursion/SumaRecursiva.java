import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int num = scan.nextInt();
    System.out.println(sumaRecursiva(num));
  }
  public static int sumaRecursiva(int n) {
    if (n == 1) {
      return 1;
    } else {
      return n + sumaRecursiva(n-1);
    }
  }
}