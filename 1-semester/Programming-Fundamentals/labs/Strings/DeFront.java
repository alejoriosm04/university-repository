import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String text = scan.next();
    text = text.toLowerCase();
    char a = text.charAt(0);
    char b = text.charAt(1);
    if (a != 'a' && b != 'b') {
      System.out.println(text.substring(2, text.length()));
    } else if (a != 'a') {
      System.out.println(text.substring(1, text.length()));
    } else if (b != 'b') {
      System.out.println(text.substring(0, 1) + text.substring(2, text.length()));
    } else {
      System.out.println(text);
    }
  }
}