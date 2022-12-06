public class Main {
    // Ignorar el metodo main. Es una simple prueba de escritorio, no hace parte de la solucion
    public static void main(String[] args) {
      int [][] numeros = new int[3][2];
      numeros[0][0] = 1; numeros[0][1] = 2;
      numeros[1][0] = 3; numeros[1][1] = 4;
      numeros[2][0] = 5; numeros[2][1] = 6;
      transpuesta(numeros);
    }
    public static void transpuesta(int[][] arr) {
      int [][] arr2 = new int[arr[0].length][arr.length];
      for (int i = 0; i < arr[0].length; i++) {
        for (int j = 0; j < arr.length; j++) {
          arr2[i][j] = arr[j][i];
        }
      }
      
      // Imprimir por pantalla matriz original **No hace parte de la solucion**
      /* for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr[i].length; j++) {
          System.out.print(arr[i][j]);
        }
        System.out.println("\n");
      } */
      
      for (int i = 0; i < arr2.length; i++) {
        for (int j = 0; j < arr2[i].length; j++) {
          System.out.print(arr2[i][j]);
        }
        System.out.println("\n");
      }
    }
  }