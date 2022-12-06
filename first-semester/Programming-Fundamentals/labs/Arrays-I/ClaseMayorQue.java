import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int arr_length = scan.nextInt();
    int [] arr = new int[arr_length];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = scan.nextInt();
    }
    mayor(arr);
  }
  public static void mayor(int[] a) {
    int n = 0;
    for (int i = 1; i < a.length; i++) {
      if (a[0] < a[i]) {
        System.out.println(a[i]);
      } else {
        n++;
      }
      if (a.length-1 == n) {
        System.out.println("No hay ningun numero mayor que el primero");
      }
    }
  }
}