public class CuttingStick {
    public static int cortarVarilla(int tamañoVarilla, int[] listaPrecios) {
        int[] tabla = new int[tamañoVarilla + 1];

        for (int varillaActual = 1; varillaActual <= tamañoVarilla; varillaActual++) {
            int mejorValor = 0;

            for (int i = 1; i <= varillaActual; i++) {
                int recorte1=listaPrecios[i];
                int recorte2 = tabla[varillaActual - i];
                int valor=recorte1+recorte2;
                if (valor > mejorValor) {
                    mejorValor = valor;
                }
            }

            tabla[varillaActual] = mejorValor;
        }

        return tabla[tamañoVarilla];
    }

    public static void main(String[] args) {
        int[] lista = {0, 1, 5, 8, 9, 10};
        int resultado = cortarVarilla(5, lista);
        System.out.println(resultado);
    }
}