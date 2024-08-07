import java.util.Scanner;
// Importamos las librerias que nos permitiran realizar la comparacion
import java.util.regex.Matcher;
import java.util.regex.Pattern;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    String htmlTexto = scan.nextLine();
// Pattern es un objeto que creamos para crear el modelo o patron a compilar
    Pattern r = Pattern.compile("<(.+)>([^<]+)</(.+)><(.+)>([^<]+)</(.+)>");
// Matcher será la cadena de texto que analizaremos, y se la entregamos al objeto de pattern
    Matcher m = r.matcher(htmlTexto);
// Creamos un ciclo para que el metodo find se encargue de buscar en la cadena teniendo en cuenta el patron a analizar
    while (m.find()) {
// Las expresiones regulares poseen grupos, especificamos que grupo buscamos imprimir
      System.out.println(m.group(2)+m.group(5));
    }
  }
}