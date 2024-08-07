import java.util.Scanner;
public class Main {
  public static void main(String[] args) {
    Scanner scan = new Scanner(System.in);
    int i;
    SensorActuador sa1 = new SensorActuador(5, 1, 10);
    for (int j = 0; j < 4; j++) {
      i = scan.nextInt();
      if (j < 2) {
        sa1.disminuirTemp(i);
      } else {
        sa1.aumentarTemp(i);
      }
    }
    System.out.println(sa1.getTemperatura());
  }
}

class SensorActuador {
  private int temperatura;
  private int minTemp;
  private int maxTemp;
  public SensorActuador(int temp, int min, int max) {
    this.temperatura = temp;
    this.minTemp = min;
    this.maxTemp = max;
  }
  public int getTemperatura() {
    return this.temperatura;
  }
  public void disminuirTemp(int i) {
    if (this.temperatura - i > this.minTemp) {
      this.temperatura = this.temperatura - i;
    }
  }
  public void aumentarTemp(int i) {
    if (this.temperatura + i < this.maxTemp) {
      this.temperatura = this.temperatura + i;
    }
  }
}