import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    double num = 0.0; /* VARIABLE THAT COMPARES WITH THE FIRST INPUT AND THEN IS ASIGNED TO THE NAME OF THE OTHER VARIABLE */
    int counter = 0; /* COUNTER THAT CONTROLS THE ADDITION OR THE SUBSTRACTION */
    String counter_2 = ""; /* THE STRING OF TEXT THAT PRINT THE TIMES THE COUNTER ADD OR SUBSTRACT */
    double user_num; /* THE VARIABLE THAT THE USER MODIFIES */
    while (true) { /* A CYCLE THAT EXECUTES ALWAYS THAT ALL THE THINGS ARE CORRECT INSIDE THIS */
      user_num = scan.nextDouble(); /* ASK THE USER TO MAKE THE INPUT */
      if (user_num == 0) { /* THE CONDITIONAL THAT CONTROLLS THE CYCLE. IF THE CONDITIONAL IS TRUE, THE CYCLE FINISHES INMEDIATLY AND ALSO PRINTS THE OUTPUT WITH THE TOTAL VALUE OF THE COUNTER */
        counter_2 += "Contador: " + counter;
        break;
      }
      if (user_num >= num) { /* IF THE INPUT IS HIGHER THAT THE LAST NUMBER OR THE ORIGINAL VALUE OF #NUM THE COUNTER ADDS +1 AND ALSO THE STRING ADDS +1 */
        counter++;
        counter_2 += "+1\n";
      } else if (user_num < num) { /* IF THE INPUT IS LESS THAT THE LAST NUMBER OR THE ORIGINAL VALUE OF #NUM THE COUNTER SUBSTRACTS -1 AND ALSO THE STRING ADDS -1 */
        counter -= 1;
        counter_2 += "-1\n";
      }
      num = user_num; /* ASSIGN THE INPUT TO THE VARIABLE NUM TO MAKE THE COMPARATIVE IN THE NEXT CYCLE BETWEEN THIS VARIABLES */
    }
    System.out.println(counter_2); /* PRINT THE FINAL RESULT OF THE COUNTER AND THE STRING */
  }
}