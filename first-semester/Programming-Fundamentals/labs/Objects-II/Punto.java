class Punto {
    private double X;
    private double Y;
    public Punto() {
      this.X = X;
      this.Y = Y;
    }
    public Punto(double x, double y) {
      this.X = x;
      this.Y = y;
    }
    public double getX() {
      return this.X;
    }
    public double getY() {
      return this.Y;
    }
    public void setX(double x) {
      this.X = x;
    }
    public void setY(double y) {
      this.Y = y;
    }
    public static double distancia(Punto p1, Punto p2) {
      double dist = Math.sqrt(Math.pow(p1.getX()-p2.getX(), 2) + Math.pow(p1.getY()-p2.getY(), 2));
      return dist;
    }
  }