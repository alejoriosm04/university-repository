public class Dragon extends Monstruo {
    private String escamas;
    public Dragon (String nombre, int sangre, String escamas) {
      super(nombre, sangre);
      this.escamas = escamas;
    }
    public void imprimirNombre() {
      System.out.println(this.getNombre());
    }
    public void moverse() {
      System.out.println("Soy un dragon, estoy volando " + this.getNombre());
    }
  }