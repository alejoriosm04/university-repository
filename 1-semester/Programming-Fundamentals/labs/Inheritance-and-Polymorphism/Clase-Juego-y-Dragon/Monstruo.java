// NO HACE PARTE DE LA SOLUCION
public class Monstruo {
    private String nombre;
    private int sangre;
    public Monstruo(String nombre, int sangre) {
      this.nombre = nombre;
      this.sangre = sangre;
    }
    public void moverse() {
      System.out.println("Soy un monstruo que se mueve lento " + this.nombre);
    }
    public String getNombre() {
      return this.nombre;
    }
    public void setNombre(String n) {
      this.nombre = n;
    }
    public int getSangre() {
      return this.sangre;
    }
    public void setSangre(int s) {
      this.sangre = s;
    }
  }