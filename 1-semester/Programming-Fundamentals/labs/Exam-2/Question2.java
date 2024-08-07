/* Hay un algoritmo que tiene como propósito, imprimir el nombre Gangsta (una especie de pseudónimo) de una persona, de acuerdo a las siguientes reglas y orden:

1. La inicial del nombre (y concatenar el carácter punto (.))
2. Adicionar Eafit
3. Apellido (TODO EN MAYUSCULA)
4. Primer Nombre
5. Concatenar al anterior punto la terminación -tense
 
Ejemplo: Si al solicitar al usuario ingresar su nombre, éste escribe: "Edwin Duque"
el software debe imprimirlo así: E. Eafit DUQUE Edwin-tense
 
Un programador, realiza el siguiente algoritmo pero éste, tiene un problema; desde punto de vista lógico según lo solicitado, las líneas de código no están ubicadas en el orden correcto. Te han contratado para reorganizar las líneas de código de manera que el software cumpla con su propósito. Como lo arreglarías?
 
import java.util.*;
public class GangstaName
{
       public static void main(String[] args)
       {
            Scanner console = new Scanner(System.in);
            String name = console.nextLine();
            System.out.print("Digite su nombre: ");

            String last = name.substring(name.indexOf(" ") + 1);
            last = last.toUpperCase();
            String fInitial = first.substring(0, 1);
            String first = name.substring(0, name.indexOf(" "));
            
           System.out.println("Your gangsta name is \"" + fInitial + ". Eafit" + last + " " + first + "-tense\"");
           }
 */

import java.util.Scanner;
public class GangstaName {
  public static void main(String[] args) {
    Scanner console = new Scanner(System.in);
    System.out.print("Digite su nombre: ");
    String name = console.nextLine();
    
    String last = name.substring(name.indexOf(" ") + 1);
    last = last.toUpperCase();
    String first = name.substring(0, name.indexOf(" "));
    String fInitial = first.substring(0, 1);
            
    System.out.println("Your gangsta name is \"" + fInitial + ". Eafit " + last + " " + first + "-tense\"");
  }
}