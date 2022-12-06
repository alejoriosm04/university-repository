import java.util.Scanner;
class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Ingrese el número de columnas y filas, en formato nxn");
    System.out.println("-----------------------------------------------------");
    int columnasFilas = scan.nextInt();
    Animal[][] arr = new Animal[columnasFilas][columnasFilas];
    System.out.println("A continuación, se llenará la matriz de Gatos");
    System.out.println("-----------------------------------------------------");
    llenarMatrizGatos(arr);
    System.out.println("Estado actual de la matriz:");
    System.out.println("-----------------------------------------------------");
    mostrarMatriz(arr);
    llenarMatrizPatos(arr, columnasFilas);
    System.out.println("Estado actual de la matriz:");
    System.out.println("-----------------------------------------------------");
    mostrarMatriz(arr);
    System.out.println("A continuación, se verificará si la matriz tiene triki");
    System.out.println("Para que una matriz tenga triki, debe tener:");
    System.out.println("- Una diagonal completa, una fila completa o una columna completa");
    System.out.println("-----------------------------------------------------");
    trikiDiagonal(arr, columnasFilas);
  }
  public static void mostrarMatriz(Animal[][] arr) {
    for (int columna = 0; columna < arr.length; columna++) {
      for (int fila = 0; fila < arr[columna].length; fila++) {
        arr[columna][fila].animalito();
      }
      System.out.println("");
    }
  }
  public static Animal[][] llenarMatrizGatos(Animal[][] arr) {
    for (int columna = 0; columna < arr.length; columna++) {
      for (int fila = 0; fila < arr[columna].length; fila++) {
        arr[columna][fila] = new Gato();
      }
    }
    return arr;
  }
  public static Animal[][] llenarMatrizPatos(Animal[][] arr, int columnasFilas) {
    Scanner scan = new Scanner(System.in);
    System.out.println("Ingrese las coordenadas donde desea crear un pato");
    System.out.println("Usar el formato columna x fila. Ambas comienzan en la posicion 0");
    System.out.println("-----------------------------------------------------");
    for (int i = 1; i <= columnasFilas; i++) {
      System.out.println("Ingrese la columna");
      int columna = scan.nextInt();
      System.out.println("Ingrese la fila");
      int fila = scan.nextInt();
      arr[columna][fila] = new Pato();
    }
    return arr;
  }
  public static void trikiDiagonal(Animal[][] arr, int columnasFilas) {
    Animal memory = arr[0][0];
    int contadorDiagonal1 = 0;
    for (int columna = 0; columna < arr.length; columna++) {
      for (int fila = 0; fila < arr[columna].length; fila++) {
        if (columna == fila) {
          if (arr[columna][fila].getClass().equals(memory.getClass())) {
            contadorDiagonal1++;
            memory = arr[columna][fila];
          }
        }
      }
    }
    if (contadorDiagonal1 == columnasFilas) {
      System.out.println("-- Existe un triki diagonal de izquierda a derecha");
    }
  }
}