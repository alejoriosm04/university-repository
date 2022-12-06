import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int tipo = texto.nextInt();
    int cantidad = texto.nextInt();
    int compras;
    switch (tipo) {
      case 1:
        compras = cantidad * 5;
        System.out.println(compras);
        break;
      case 2:
        compras = cantidad * 10;
        System.out.println(compras);
        break;
      case 3:
        compras = cantidad * 15;
        System.out.println(compras);
        break;
    }
  }
}