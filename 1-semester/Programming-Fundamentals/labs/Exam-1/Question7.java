// parOimpar
/* Dado un número entero n, retornar si es par o impar
parOimpar(1) → "impar"
parOimpar(2) → "par"
parOimpar(3) → "impar" */

/* SOLUCION
public String parOimpar(int n) {
  if (n % 2 == 0) {
    return "par";
  } else {
    return "impar";
  }
}
*/

// sumaMultiplosTresCinco
/* Encuentre la suma de todos los múltiplos de 3 o de 5 que sean menores o
iguales al número natural N.
sumaMultiplosTresCinco(1) → 0
sumaMultiplosTresCinco(2) → 0
sumaMultiplosTresCinco(3) → 3
*/

/* SOLUCION
public int sumaMultiplosTresCinco(int n) {
  int acumulador = 0;
  for (int i = 3; i <= n; i++) {
    if (i % 5 == 0) {
      acumulador = acumulador + i;
    } else if (i % 3 == 0) {
      acumulador = acumulador + i;
    }
  }
  return acumulador;
}
*/

// CalificacionFinal
/* Un curso se evalúa de la siguiente forma: se toma 5 prácticas
calificadas (p1,p2,p3,p4,p5). Se determina el promedio y se le da al
estudiante una categoría que puede ser A, B, C, o D; según si: Su promedio
es entre 4 a 5 => A; Su promedio es mayor o igual a 3 pero menor 4 => B; Su
promedio es mayor o igual a 2 pero menor a 3 => C; De lo contrario, si no
está en ninguna de las categorías anteriores => D;
CalificacionFinal(1, 2, 3, 4, 5) → "B"
CalificacionFinal(5, 5, 5, 5, 5) → "A"
CalificacionFinal(4, 4, 4, 5, 5) → "A"
*/

/* SOLUCION
public String CalificacionFinal(double p1,double p2,double p3,double p4,double p5) {
  if ((p1+p2+p3+p4+p5)/5 >= 4 && (p1+p2+p3+p4+p5)/5 <=5) {
    return "A";
  } else if ((p1+p2+p3+p4+p5)/5 >= 3 && (p1+p2+p3+p4+p5)/5 < 4) {
    return "B";
  } else if ((p1+p2+p3+p4+p5)/5 >= 2 && (p1+p2+p3+p4+p5)/5 < 3) {
    return "C";
  } else {
    return "D";
  }
}
*/

// esNumeroPerfecto
/* 
Crea un algoritmo que permita saber si un número n*2 (n multiplicado por dos), es perfecto o no
esNumeroPerfecto(1) → false
esNumeroPerfecto(2) → false
esNumeroPerfecto(3) → true
*/

/* SOLUCION
public boolean esNumeroPerfecto(int n) {
  int perfecto = n * 2;
  int acumulador = 0;
  for (int i = 1; i < perfecto; i++) {
    if (perfecto % i == 0) {
      acumulador = acumulador + i;
    }
  }
  if (acumulador == perfecto) {
    return true;
  } else {
    return false;
  }
}
*/

// multiploMasPequeno
/* 
¿Cuál es el número positivo más pequeño que es uniformemente divisible por todos los números del
1 al n? n, es número entero positivo (menor o igual a 15, por temas de consumo de cómputo)
multiploMasPequeno(3) → 6
multiploMasPequeno(5) → 60
multiploMasPequeno(7) → 420
*/

/* SOLUCION
.......I dont know bro
*/