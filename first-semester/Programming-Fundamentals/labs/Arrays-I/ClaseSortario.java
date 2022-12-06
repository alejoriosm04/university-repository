import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int arr_length = scan.nextInt();
    int [] arr = new int[arr_length];
    for (int i = 0; i < arr.length; i++) {
      arr[i] = scan.nextInt();
    }
    System.out.println(detectorDeMalaSuerte(arr));
  }
  public static boolean detectorDeMalaSuerte(int[] a) {
    boolean detector;
    int n = 0;
    for (int i = 0; i < a.length; i++) {
      if (a[i] == 1) {
        n++;
      } else if (a[i] == 3) {
        n++;
      } else if (a[i] == 13) {
        n++;
      }
    }
    if (n != 0) {
      detector = true;
    } else {
      detector = false;
    }
    return detector;
  }
}