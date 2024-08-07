import java.util.Scanner;
// Forma compleja de hacerlo pero aplicando lo que se ha visto
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String base = scan.next();
    String eliminar = scan.next();
    int n = base.indexOf(eliminar);
    String nuevaBase;
    if (base.indexOf(eliminar) != -1) {
      nuevaBase = base.substring(0, n) + base.substring((n+eliminar.length()), base.length());
      if (nuevaBase.indexOf(eliminar) != -1) {
      nuevaBase = nuevaBase.substring(0, nuevaBase.indexOf(eliminar)) + nuevaBase.substring((nuevaBase.indexOf(eliminar)+eliminar.length()), nuevaBase.length()); 
      }
      System.out.println(nuevaBase);
    } else {
      System.out.println(base);
    }
  }
}

// Forma facil y practica de hacerlo, con el metodo replace()
/* public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String base = scan.next();
    String eliminar = scan.next();
    System.out.println(base.replace(eliminar, ""));
  }
} */