/* ESTA ES LA SOLUCION QUE EL EJERCICIO PIDE */
/* public class Main {
  public int factorial(int num) {
    int factorial = 1;
    for (int i = 1; i <= num; i++) {
      factorial = factorial * i;
    }
    return factor;
  }
} */

/* EJERCICIO PARA VERIFICAR COMO SERIA EL FUNCIONAMIENTO EN CONSOLA */
/* IGNORAR */
/* EL PROGRAMA ENTREGA TODOS LOS VALORES QUE SE VAN PRODUCIENDO A MEDIDA QUE SE VA REALIZANDO EL FACTORIAL, EN FORMA DE CADENA. FINALIZA CON EL VALOR QUE DA EL FACTORIAL DEL NUMERO QUE EL USUARIO INGRESO */

import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int num = scan.nextInt();
    int factor = 1;
    for (int i = 1; i <= num; i++) {
      factor = factor * i;
      System.out.print(factor);
    }
  }
}