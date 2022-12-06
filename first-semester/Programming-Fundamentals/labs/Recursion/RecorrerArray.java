public class Main {
    // PRUEBA DE ESCRITORIO, NO HACE PARTE DE LA SOLUCION FINAL. IGNORAR
    public static void main(String[] args) {
      int[] array = {0, 1, 2, 3, 4, 5};
      int indice = 0;
      recorrerArray(array, indice);
    }
    public static void recorrerArray(int[] array, int indice) {
      System.out.println(array[indice]);
      if (indice < array.length-1) {
        recorrerArray(array, indice+1);
      }
    }
  }