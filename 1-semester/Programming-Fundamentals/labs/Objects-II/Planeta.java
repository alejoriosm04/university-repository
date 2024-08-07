class Planeta {
    private String nombre;
    private double masa;
    public static int contador = 0;
    public Planeta() {
      this("Tierra", 5.972);
      Planeta.contador++;
    }
    public Planeta(String n, double m) {
      this.nombre = n;
      this.masa = m;
    }
    public Planeta(Planeta p) {
      this.nombre = getNombre();
      this.masa = getMasa();
    }
    public String getNombre() {
      return this.nombre;
    }
    public double getMasa() {
      return this.masa;
    }
    public void setNombre(String n) {
      this.nombre = n;
    }
    public void setMasa(double m) {
      this.masa = m;
    }
    public static Planeta planetaMedio(Planeta p) {
      Planeta p1 = new Planeta();
      p1.setNombre(p.getNombre());
      p1.setMasa(p.getMasa()/2);
      return p1;
    }
  }