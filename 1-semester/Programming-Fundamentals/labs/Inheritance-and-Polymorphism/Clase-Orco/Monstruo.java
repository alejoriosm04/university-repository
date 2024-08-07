// NO ES NECESARIO IMPLEMENTAR ESTA CLASE PARA SOLUCIONAR EL EJERCICIO
public class Monstruo {
    private String nombre;
    private int sangre;
    public Monstruo(String nombre, int sangre) {
      this.nombre = nombre;
      this.sangre = sangre;
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