// EJERCICIOS EN CODINGBAT

// -------------------------------------------
// myString1
// -------------------------------------------

/*
Dado un string, retornar un nuevo string que contenga la letra inicial en mayúscula y el resto de letras reemplazado por puntos. Si el string está vacío, retornar un string con un punto (.)


myString1("") → "."
myString1("edwin") → "E...."
myString1("esternocleidomastoideo") → "E....................."
*/

// SOLUCION

public String myString1(String str) {
    String newString = "";
    if (str.length() == 0) {
      newString = ".";
    } else {
      String fLetter = str.substring(0, 1);
      String fLetterUpper = fLetter.toUpperCase();
      newString = newString + fLetterUpper;
      for (int i = 1; i < str.length(); i++) {
        newString = newString + ".";
      }
    }
    return newString;
  }
  
  // -------------------------------------------
  // SwappingArrays
  // -------------------------------------------
  
  /*
  Dado un arreglo de enteros, retornar uno nuevo pero haciendole swapping a sus elmentos; es decir, si un arreglo es {1,2,3} debe retornar un nuevo arreglo {3,2,1}. Se espera que el arreglo tenga al menos un elemento.
  
  
  SwappingArrays([1, 2, 3]) → [3, 2, 1]
  SwappingArrays([1]) → [1]
  SwappingArrays([1, 2]) → [2, 1]
  */
  
  // SOLUCION
  
  public int [] SwappingArrays(int[] numbers) {
    int memory;
    int j = numbers.length - 1;
    for (int i = 0; i < (numbers.length)/2; i++) {
      memory = numbers[j];
      numbers[j] = numbers[i];
      numbers[i] = memory;
      j--;
    }
    return numbers;
  }
  
  // -------------------------------------------
  // sumandoPosicionesPares
  // -------------------------------------------
  
  /*
  Dado un arreglo de enteros, sumar los valores que se encuentren en las posiciones pares y retornarlo. Si el arreglo solo tiene un elemento, retornar cero. El arreglo debe tener al menos un elemento.
  
  
  sumandoPosicionesPares([1, 7, 3, 4, 5, 9]) → 20
  sumandoPosicionesPares([1, 2, 3, 4, 5, 6]) → 12
  sumandoPosicionesPares([1]) → 0
  */
  
  // SOLUCION
  
  public int sumandoPosicionesPares(int[] nums) {
    int contador = 0;
    if (nums.length == 1) {
      contador = 0;
    } else {
      for (int i = 1; i < nums.length; i = i + 2) {
        contador = contador + nums[i];
      }
    }
    return contador;
  }