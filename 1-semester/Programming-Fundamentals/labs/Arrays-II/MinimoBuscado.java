public class Main{
    // Ignorar el metodo main. Es una simple prueba de escritorio, no hace parte de la solucion
    public static void main(String[] args) {
      int [][] numeros = new int[3][3];
      numeros[0][0] = 1;
      numeros[0][1] = 2;
      numeros[0][2] = 3;
      numeros[1][0] = 4;
      numeros[1][1] = 5;
      numeros[1][2] = 6;
      numeros[2][0] = 7;
      numeros[2][1] = 8;
      numeros[2][2] = 9;
      System.out.println(minimoBuscado(numeros));
    }
    public static int minimoBuscado(int[][] arr) {
      int menor = arr[0][0];
      for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr[i].length; j++) {
          if (arr[i][j] <= menor) {
            menor = arr[i][j];
          }
        }
      }
      return menor;
    }
  }
  
  /*
  // SOLUCION CON RECURSION
  // Codigo para encontrar el numero minimo en un
  // arreglo de arreglos en Java (estoy usando la 10)
  
  // Autor: Luis M. Torres-Villegas
  
  class Main {  
    public static void main(String args[]) {
      // Pruebas
      // int[][] arr = {{1,2,3}, {4,5,6}, {7,8,9}};
      // int[][] arr = {{67,68,69}, {5,4,76}, {20,3,16}};
      int[][] arr = {{100,102,103}, {99,95,76}, {85,77,92}};
      int result = Array.minimoBuscado(arr, 0);
      System.out.println(result);
    } 
  }
  
  class Array {
    public static int minimoBuscado(int[][] arr, int i) {
      if (i == arr.length-1) {
        return minimoBuscado(arr[i], 0);
      } else {
        return Math.min(minimoBuscado(arr[i], i), minimoBuscado(arr, i+1)); 
      }
    }
    
    public static int minimoBuscado(int[] arr, int i) {
      if (i == arr.length-1) {
        return arr[i];
      } else {
        return Math.min(arr[i], minimoBuscado(arr, i+1));
      }
    }
  } */