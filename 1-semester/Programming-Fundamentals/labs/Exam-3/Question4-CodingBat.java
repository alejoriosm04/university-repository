class Main {
    public static void main(String[] args) {
      Main m1 = new Main();
      System.out.println(m1.cantidadDeEspacios("Edwin Duque"));
      System.out.println(m1.last2("hixxhi"));
      System.out.println(m1.FromDecimalToBinary(15));
    }
    /*
    Dado un string, retornar el número de espacios (" ") que éste contiene.
  
    cantidadDeEspacios("Edwin Duque") → 1
    cantidadDeEspacios("Hola a todos") → 2
    cantidadDeEspacios("") → 0
    */
    public int cantidadDeEspacios(String str) {
      int contador = 0;
      for (int i = 0; i < str.length(); i++) {
        String charStr = str.substring(i, i+1);
        if (charStr.equals(" ")) {
          contador++;
        }
      }
      return contador;
    }
    /*
    Dado un string, retornar la cantidad de veces que los últimos dos carácteres 
    aparecen en el string. (no incluir a los últimos dos en la cuenta) Ejemplo:
    "hixxxhi" retornaría => 1
    
    last2("hixxhi") → 1
    last2("xaxxaxaxx") → 1
    last2("axxxaaxx") → 2
    */
    public int last2(String str) {
      int contador = 0;
      for (int i = 0; i < str.length()-2; i++) {
        String last2Str = str.substring(str.length()-2);
        String twoChars = str.substring(i, i+2);
        if (twoChars.equals(last2Str)) {
          contador++;
        }
      }
      return contador;
    }
    /*
    Cree un algoritmo recursivo que permita convertir un número en sistema decimal a 
    sistema binario. El binario será retornado en forma de String y el decimal será 
    entregado a la función como entero.
    
    FromDecimalToBinary(15) → "1111"
    FromDecimalToBinary(8) → "1000"
    FromDecimalToBinary(64) → "1000000"
    */
    public String FromDecimalToBinary(int n) {
      String binary = "";
      if (n == 0) {
        return "";
      } else {
        return binary + FromDecimalToBinary(n/2) + n%2;
      }
    }
    /*
    Dada una matriz de enteros de nxn, retornar si la suma de todos sus elementos es
    múltiplo de 5. Importante mirar el hint para poder desarrollar el ejercicio.
    OperacionMatriz("{{2,2},{2,2}}") → false
    OperacionMatriz("{{1,2,3,4,5},{6,7,8,9,10},{11,12,13,14,15},{16,17,18,19,20},{21,22,23,24,25}}") → true
    OperacionMatriz("{{1,2,3},{4,5,6},{7,8,9}}") → true
    */
    public boolean OperacionMatriz(String str) {
      int sumatoriaArreglo = 0;
      int[][] arr = toArray(str);
      for (int columns = 0; columns < arr.length; columns++) {
        for(int rows = 0; rows < arr[columns].length; rows++) {
          sumatoriaArreglo+=arr[columns][rows];
        }
      }
      if (sumatoriaArreglo%5 == 0) {
        return true;
      } else {
        return false;
      }
    }
    public int[][] toArray(String s) {
      char lc = 0x7b; 
      char rc = 0x7d; 
      char bs = 0x5c; 
      char co = 0x2c;
      s = s.replaceAll("" + bs + lc,"");
      s = s.replaceAll("" + bs + rc + co,"" + bs + rc);
      String[] rows = s.split("" + bs + rc);
      int r[][] = {{},{}};
      if (rows.length == 0)
        return r;
      r = new int[rows.length][];
      for (int row = 0; row < rows.length; row++) {
        String [] cols = rows[row].split(",");
        r[row] = new int[cols.length];
        for (int col = 0; col < cols.length; col++) {
          r[row][col] = Integer.decode(cols[col]).intValue();
        }
      }
      return r;
    }
  }