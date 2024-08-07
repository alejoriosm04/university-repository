import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int arr_length = scan.nextInt();
    int[] arr = new int[arr_length];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = scan.nextInt();
    }
    System.out.println(balancear(arr));
  }
  public static boolean balancear(int[] a) {
    boolean balanced;
    int accumulator_left = 0;
    int accumulator_right = 0;
    for (int i = 0; i < ((a.length-1)/2); i++) {
      accumulator_left = accumulator_left + a[i];
    }
    for (int i = a.length-1; i > ((a.length-1)/2); i--) {
      accumulator_right = accumulator_right + a[i];
    }
    if (accumulator_left == accumulator_right) {
      balanced = true;
    } else {
      balanced = false;
    }
    return balanced;
  }
}