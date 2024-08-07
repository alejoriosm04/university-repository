// PRUEBA DE ESCRITORIO NO HACE PARTE DE LA SOLUCION
class Main {
    public static void main(String[] args) {
      Orco orco1 = new Orco("Drew", 20, "Rabioso");
      orco1.imprimirNombre();
      orco1.moverse();
      Monstruo m1 = new Monstruo("Monstruo1", 50);
      m1.moverse();
      Juego j1 = new Juego();
      j1.moverMonstruos();
    }
  }