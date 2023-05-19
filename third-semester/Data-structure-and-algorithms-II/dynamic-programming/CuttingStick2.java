import java.util.ArrayList;
import java.util.List;

public class CuttingStick {
    public static int cortarVarilla(int tamañoVarilla, int[] listaPrecios) {
        int[] tabla = new int[tamañoVarilla + 1];
        int[] cortes = new int[tamañoVarilla + 1];

        for (int varillaActual = 1; varillaActual <= tamañoVarilla; varillaActual++) {
            int mejorValor = 0;

            for (int i = 1; i <= varillaActual; i++) {
                int recorte1 = listaPrecios[i];
                int recorte2 = tabla[varillaActual - i];
                int valor = recorte1 + recorte2;

                if (valor > mejorValor) {
                    mejorValor = valor;
                    cortes[varillaActual] = i; // Guardar el corte óptimo
                }
            }

            tabla[varillaActual] = mejorValor;
        }

        // Obtener la secuencia de cortes
        List<Integer> secuenciaCortes = new ArrayList<>();
        int varillaActual = tamañoVarilla;

        while (varillaActual > 0) {
            int mejorCorte = cortes[varillaActual];
            secuenciaCortes.add(mejorCorte);
            varillaActual -= mejorCorte;
        }

        // Imprimir la secuencia de cortes
        System.out.println("Secuencia de cortes: " + secuenciaCortes);

        return tabla[tamañoVarilla];
    }

    public static void main(String[] args) {
        int[] lista = {0, 1, 5, 8, 9, 10, 12, 13, 15, 18};
        int resultado = cortarVarilla(9, lista);
        System.out.println("Mejor valor obtenido: " + resultado);
    }
}
