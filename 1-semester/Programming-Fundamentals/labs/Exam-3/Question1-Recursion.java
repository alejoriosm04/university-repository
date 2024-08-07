class Main {
    public static void main(String[] args) {
      System.out.println("Suma de los primeros n numeros");
      Main m1 = new Main();
      System.out.println(m1.sum(5));
    }
    public int sum (int n) {
      if (n == 0) {
        return 0;
      } else {
        return n + sum(n-1);
      }
    }
  }