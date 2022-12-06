public class Orco extends Monstruo {
    private String grunyido;
    public Orco (String nombre, int sangre, String grunyido) {
      super(nombre, sangre);
      this.grunyido = grunyido;
    }
    public String getGrunyido() {
      return this.grunyido;
    }
    public void setGrunyido(String g) {
      this.grunyido = g;
    }
    public void imprimirNombre() {
      System.out.println(this.getNombre());
    }
  }