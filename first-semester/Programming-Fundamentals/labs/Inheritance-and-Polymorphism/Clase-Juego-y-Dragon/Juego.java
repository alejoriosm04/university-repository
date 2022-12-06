public class Juego {
    private Monstruo[] monstruo;
    public Juego() {
      Orco o1 = new Orco("Garnag", 10, "grrr");
      Dragon d1 = new Dragon("Brenton", 20, "metal");
      Orco o2 = new Orco("Rogthun", 5, "purr");
      Dragon d2 = new Dragon("Shenlong", 40, "cuero");
      this.monstruo = new Monstruo[4];
      monstruo[0] = o1;
      monstruo[1] = d1;
      monstruo[2] = o2;
      monstruo[3] = d2;
    }
    public void moverMonstruos() {
      for (Monstruo item: monstruo)
        item.moverse();
    }
  }