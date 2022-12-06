import java.util.Scanner;
public class Main {
  public static void main (String[] args) {
    Scanner scan = new Scanner(System.in);
    int stars = scan.nextInt(); /* WE DECLARE THE QUALIFICATION VARIABLE THAT THE USER GIVES */
    int zero = 0; /* THE COUNTER FOR ALL THE POSSIBLE QUALIFICATIONS */
    int one = 0;
    int two = 0;
    int three = 0;
    int four = 0;
    int five = 0;
    int accumulator = 0; /* THE VARIABLE THAT SAVES THE NUMBER OF QUALIFICATIONS */
    while (stars >= 0 && stars < 6) {
      accumulator++; /* ADD EVERYTIME THAT A QUALIFICATION IS GIVEN ACCORDING TO THE POSSIBLE RESULTS  */
        switch (stars) { /* MODIFY EACH COUNTER OF EACH QUALIFICATION EVERYTIME THE EVENT OCCURS */
        case 0:
          zero++;
          break;
        case 1:
          one++;
          break;
        case 2:
          two++;
          break;
        case 3:
          three++;
          break;
        case 4:
          four++;
          break;
        case 5:
          five++;
          break;
        }
      stars = scan.nextInt(); /* RESTART THE VARIABLE TO ASK FOR A NEW QUALIFICATION AGAIN */
    }
    System.out.println("0("+zero+") "+"*("+one+") "+"**("+two+") "+"***("+three+") "+"****("+four+") "+"*****("+five+")");
    System.out.println("Total: " + accumulator);
  }
}