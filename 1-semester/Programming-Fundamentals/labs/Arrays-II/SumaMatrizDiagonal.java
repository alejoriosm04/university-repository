public class Main{
    // Ignorar el metodo main. Es una simple prueba de escritorio, no hace parte de la solucion
    public static void main(String[] args) {
      int [][] numeros = new int[4][4];
      numeros[0][0] = 00; numeros[0][1] = 01; numeros[0][2] = 02; numeros[0][3] = 03;
      numeros[1][0] = 10; numeros[1][1] = 11; numeros[1][2] = 12; numeros[1][3] = 13;
      numeros[2][0] = 20; numeros[2][1] = 21; numeros[2][2] = 22; numeros[2][3] = 23;
      numeros[3][0] = 30; numeros[3][1] = 31; numeros[3][2] = 32; numeros[3][3] = 33;
      System.out.println(sumaDiagonal(numeros));
    }
    public static int sumaDiagonal(int[][] arr) {
      int sumador = 0;
      for (int i = 0; i < arr.length; i++) {
        for (int j = 0; j < arr[i].length; j++) {
          if (i == j) {
            sumador = sumador + arr[i][j];
          }
        }
      }
      return sumador;
    }
  }