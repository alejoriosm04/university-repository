import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner texto = new Scanner(System.in);
    double salario = texto.nextDouble();
    String contrato = texto.next();
    if (contrato.equals("publico") && salario > 10000000) {
      double impuesto = salario * 0.15;
      System.out.println(String.format("%.2f", impuesto));
    } else {
      System.out.println("No debes aportar");
    }
  }
}