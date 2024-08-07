1. El programa comienza ejecutando el método "main" de la clase "Main".

2. En el método "main", se crea una instancia de la clase "KMP", que es la clase que contiene la implementación del algoritmo.

3. A continuación, se llama al método "matcher" de la instancia de la clase "KMP" creada en el paso anterior, pasando dos cadenas de texto como argumentos. La primera cadena de texto es la cadena en la que se buscará la subcadena, y la segunda cadena de texto es la subcadena que se desea buscar en la primera cadena.

4. El método "matcher" comienza calculando la función de prefijo de la subcadena, utilizando el método "computePrefixFunction". Esta función de prefijo es un arreglo de enteros que contiene información sobre los prefijos más largos de la subcadena que son también sufijos. La función de prefijo se utiliza para evitar la comparación de caracteres innecesarios en la cadena principal.

5. Luego, se inicializa una variable "j" en cero. Esta variable se utilizará para mantener el índice actual de la subcadena que se está buscando en la cadena principal.

6. A continuación, se itera sobre todos los caracteres de la cadena principal utilizando un ciclo "for". En cada iteración, se verifica si el caracter actual de la cadena principal coincide con el caracter de la subcadena en la posición "j".

7. Si los caracteres coinciden, se incrementa el valor de "j" en uno. Si "j" es igual a la longitud de la subcadena, se ha encontrado la subcadena en la cadena principal, y se imprime la posición en la que se encontró.

8. Si los caracteres no coinciden, se utiliza la función de prefijo para mover el índice "j" hacia atrás. La función de prefijo devuelve la longitud del prefijo más largo de la subcadena que coincide con un sufijo propio de la subcadena hasta la posición actual. Este valor se utiliza para mover el índice "j" hacia atrás para continuar la búsqueda de la subcadena.

9. La función "computePrefixFunction" utiliza un enfoque eficiente para calcular la función de prefijo. Utiliza un índice "j" para iterar sobre los caracteres de la subcadena, y otro índice "i" para indicar la posición en la que se está calculando la función de prefijo. En cada iteración, se verifica si los caracteres en las posiciones "i" y "j" coinciden. Si coinciden, se incrementa el valor de "j". Si no coinciden, se utiliza el valor de la función de prefijo en la posición "j-1" para mover el índice "j" hacia atrás. La función de prefijo en la posición "i" se establece en el valor actual de "j".

10. La función "computePrefixFunctionInefficient" también calcula la función de prefijo, pero utiliza un enfoque ineficiente. En cada iteración, se genera una nueva subcadena que va desde el inicio de la subcadena original hasta la posición actual, y se compara con todas las subcadenas que son prefijos y sufijos de esa subcadena. El valor de la función de prefijo en la posición actual se establece en
