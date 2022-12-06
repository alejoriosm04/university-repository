/*
Dado el siguiente código, escriba por favor cómo saldría en pantalla la impresión de list3 según la línea de código 10.
1.   int[] list1 = new int[5];
2.   int[] list2 = new int[5];
3.   for (int i = 0; i < list1.length; i++)
4.   {
5.      list1[i] = 2 * i + 1;
6.      list2[i] = 2 * i + 1;
7.   }
8.   int[] list3 = list2;
9.   list2[2]++;
10. // This is a function that prints an array of ints   
11. printIntArray(list3);
*/

public class Main {
    public static void main(String[] args) {
      int[] list1 = new int[5];
      int[] list2 = new int[5];
      for (int i = 0; i < list1.length; i++) {
        list1[i] = 2 * i + 1;
        list2[i] = 2 * i + 1;
      }
      int[] list3 = list2;
      list2[2]++;
      // This is a function that prints an array of ints   
      //printIntArray(list3);
      for (int i = 0; i < list3.length; i++) {
        System.out.println(list3[i]);
      }
    }
  }