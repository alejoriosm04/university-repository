import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    int dia = texto.nextInt();
    double salario = texto.nextDouble();
    switch (dia) {
      case 1:
        salario = salario * 1.455;
        System.out.println(String.format("%.2f", salario));
        break;
      case 2:
      case 3:
        System.out.println(String.format("%.2f", salario));
        break;
      case 4:
        salario = salario * 1.1;
        System.out.println(String.format("%.2f", salario));
        break;
      case 5:
        salario = salario * 1.295;
        System.out.println(String.format("%.2f", salario));
        break;
      case 6:
      case 7:
        salario = salario * 1.75;
        System.out.println(String.format("%.2f", salario));
    }
  }
}