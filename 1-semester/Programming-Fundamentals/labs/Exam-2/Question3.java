/*
Escriba aquí en texto su código de respuesta (Código completo). Utilice Arreglos para dar solución.

El dueño de un restaurante entrevista a cinco clientes de su negocio y les pide que califiquen de 1 a 10 los siguientes aspectos: (1 es pésimo y 10 es excelente o inmejorable)

1. Atención de parte de los empleados 
2. Calidad de la comida 
3. Justicia del precio (el precio que pagó le parece justo?) 
4. Ambiente (muebles cómodos?, música adecuada?, iluminación suficiente?, decoración, etc.)

Escriba un algoritmo que pida las calificaciones de los cinco clientes a cada uno de estos aspectos, y luego escriba el promedio obtenido en cada uno de ellos.

El programa debe indicar también, cuál fue en promedio, el aspecto mejor calificado y cuál fue el peor calificado
*/

import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int [] cliente1 = new int[4]; int [] cliente2 = new int[4];
    int [] cliente3 = new int[4]; int [] cliente4 = new int[4];
    int [] cliente5 = new int[4];

    System.out.print("Ingrese el nombre del restaurante que desea calificar: ");
    String nombre_restaurante = scan.nextLine();
    System.out.println("-------------------------------------------------------");
    nombre_restaurante = nombre_restaurante.toUpperCase();

    System.out.println("A continuación se van a calificar distintos aspectos");
    System.out.println("de " + nombre_restaurante + ". Por favor calificar con atención");
    System.out.println("Califique de 1 a 10 los siguientes aspectos: ");
    System.out.println("(1 es pésimo y 10 es excelente o inmejorable)");

    for (int i = 1; i < 6; i++) {
      System.out.println("Cliente " + i + "°");
      switch(i) {
        case 1:
          cliente1 = Restaurante.preguntas();
          break;
        case 2:
          cliente2 = Restaurante.preguntas();
          break;
        case 3:
          cliente3 = Restaurante.preguntas();
          break;
        case 4:
          cliente4 = Restaurante.preguntas();
          break;
        case 5:
          cliente5 = Restaurante.preguntas();
          break;
      }
    }
    float [] average_arr = {Restaurante.average(cliente1), Restaurante.average(cliente2), Restaurante.average(cliente3), Restaurante.average(cliente4), Restaurante.average(cliente5)};
    System.out.println("Promedios por cliente");
    System.out.println("Cliente 1: " + Restaurante.average(cliente1));
    System.out.println("Cliente 2: " + Restaurante.average(cliente2));
    System.out.println("Cliente 3: " + Restaurante.average(cliente3));
    System.out.println("Cliente 4: " + Restaurante.average(cliente4));
    System.out.println("Cliente 5: " + Restaurante.average(cliente5));
    System.out.println("Promedio mas alto de los clientes: ");
    Restaurante.maximum(average_arr);
    System.out.println("Promedio mas bajo de los clientes: ");
    Restaurante.minimum(average_arr);
  }
}

class Restaurante {
  public static int[] preguntas() {
    Scanner scan = new Scanner(System.in);
    int [] arr = new int[4];
    System.out.println("Pregunta 1: Atención de parte de los empleados");
    arr[0] = scan.nextInt();
    System.out.println("Pregunta 2: Calidad de la comida");
    arr[1] = scan.nextInt();
    System.out.println("Pregunta 3: Justicia del precio (el precio que pagó le parece justo?)");
    arr[2] = scan.nextInt();
    System.out.println("Pregunta 4: Ambiente (muebles cómodos?, música adecuada?, iluminación suficiente?, decoración, etc.)");
    arr[3] = scan.nextInt();
    return arr;
  }
  public static float average(int[] a) {
    float adder = 0;
    float average;
    for (int i = 0; i < a.length; i++) {
      adder = adder + a[i];
    }
    average = adder / a.length;
    return average;
  }
  public static void maximum(float[] a) {
    float biggest = a[0];
    for (int i = 1; i < a.length; i++) {
      if (a[i] > biggest) {
        biggest = a[i];
      }
    }
    System.out.println(biggest);
  }
  public static void minimum(float[] a) {
    float smallest = a[0];
    for (int i = 1; i < a.length; i++) {
      if (a[i] < smallest) {
        smallest = a[i];
      }
    }
    System.out.println(smallest);
  }
}