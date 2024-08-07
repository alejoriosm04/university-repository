/*
CREAR UNA BASE DE DATOS PARA UNIVERSIDAD QUE DESEA REALIZAR REGISTRO DE SUS
ESTUDIANTES Y GENERAR CIERTOS REPORTES SOBRE EL SEXO, EL TIPO DE CLASE
TIPO DE MAJOR Y SUS FECHAS DE CUMPLEAÑOS
*/
import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    Estudiante sa1 = new Estudiante();
    System.out.println("Ingrese su sexo: ");
    String s = scan.next();
    sa1.tipoSexo(s);
    System.out.println("Ingrese su clase: ");
    String c = scan.next();
    sa1.tipoClase(c);
    System.out.println("Si esta en un major escriba la palabra major, de lo contrario, omita: ");
    String m = scan.next();
    sa1.setMajor(m);
    System.out.println("Ingrese su fecha de nacimiento en formato dia y mes: ");
    String f = scan.next();
    System.out.println("El numero de estudiante hombres y mujeres respectivamente es: " + sa1.getSexo());
    System.out.println("El numero de estudiante junior, senior y graduate respectivamente es: " + sa1.getClase());
    System.out.println("El numero de estudiante major es: " + sa1.getSMajor());
  }
}

class Estudiante {
  private String sexo;
  private int hombres;
  private int mujeres;
  private String clase;
  private int junior;
  private int senior;
  private int graduate;
  private String major;
  private int s_major;
  private String fechaNacimiento;
  public int getSexo() {
    return this.hombres;
    return this.mujeres;
  }
  public void tipoSexo(String s) {
    int contadorHombre = 0;
    int contadorMujer = 0;
    if (s.equals("hombre")) {
      contadorHombre++;
    } else if (s.equals("mujer")) {
      contadorMujer++;
    }
    this.hombres = contadorHombre;
    this.mujeres = contadorMujer;
  }
  public int getClase() {
    return this.junior;
    return this.senior;
    return this.graduate;
  }
  public void tipoClase(String c) {
    int contadorJunior = 0;
    int contadorSenior = 0;
    int contadorGraduate = 0;
    if (c.equals("junior")) {
      contadorJunior++;
    } else if (c.equals("senior")) {
      contadorSenior++;
    } else if (c.equals("graduate")) {
      contadorGraduate++;
    }
    this.junior = contadorJunior;
    this.senior = contadorSenior;
    this.graduate = contadorGraduate;
  }
  public int getSMajor() {
    return s_major;
  }
  public void setMajor(String m) {
    int contadorMajor = 0;
    if (m.equals("major")) {
      contadorMajor++;
    }
    this.s_major = contadorMajor;
  }
}