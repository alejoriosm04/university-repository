<h1 align = "center">Parcial I - Estructura Datos y Algoritmos 2</h1>

Programa creado en Python para la simulación de la congestión de los sistemas de urgencia para una ciudad intermedia con dos centros de urgencia.

Se busca analizar los intervalos de tiempo entre cada uno de los estados que un paciente necesita enfrentar en un centro de salud. A partir de estos, mejorar el flujo de atención y tener un criterio claro de ordenamiento.


## ¿Qué realiza?

Cumple con cada una de las funcionalides descritas en el documento de **Parcial I - EDA2** enviado.

- Generación de datos dummy que indican la información de un paciente en el flujo de atención explicado.

<div align="center">
  <img src='https://i.imgur.com/xcst6n5.png' height='380px'/>
</div>

- Clasificación particular a partir de el estado actual de cada paciente.
- Distribución del estado de cada paciente en los diferentes servicios para realizar un análisis de datos.

<div align="center">
  <img src='https://i.imgur.com/ZWFAGFx.png' height='380px'/>
</div>

- Análisis de datos a través de `matplotlib` para graficar la evolución de los servicios.

<div align="center">
  <img src='https://i.imgur.com/R4yAheI.png' height='380px'/>
</div>

- Ordenamiento de pacientes y servicios con **QuickSort** a partir de los tiempos encontrados y calculados.
- Simulación de datos a través de una red neuronal, creada con `Keras` y `Tensorflow`, entrenada para la toma de decisiones y el efectivo uso de la información.

<div align="center">
  <img src='https://i.imgur.com/q7hjtwd.png' height='380px'/>
</div>

- Retroalimentación a partir de las predicciones de la red neuronal.

<div align="center">
  <img src='https://i.imgur.com/3vKcNp8.png' height='380px'/>
</div>

## ¿Cómo funciona?

A continuación se explica el funcionamiento del programa creado, con el objetivo de establecer claramente como se analizó el ejercicio y porqué se codificó esta solución.

### Dummy data

- Se encontrarón dos objetos principales en la historia de usuario (Paciente y Servicio). Ambos objetos fueron modelados para poder crear a partir de esta modelación los datos de simulación.

- Paciente, es un objeto que posee como atributos: **nombre, edad, enfermedad, estado, cada uno de los tiempos de cada estado y el tiempo total**. Los datos simulados fueron obtenidos de una base de datos con múltiples combinaciones para darle la aleatoridad buscada.

- Servicio, es un objeto que posee como atributos: **nombre, lista de pacientes activos, tiempo total de pacientes activos y tiempo promedio de atención**. Los datos son calculados a partir de los pacientes anteriormente generados.

- Cada una de las funciones `built-in` de comparación de Python, fueron modificadas para cada objeto. Con el objetivo de mejorar eficiencia y legibilidad en el código.

### Ordenamiento

- Al momento de tener todos los datos creados y organizados en cada uno de los servicios de atención, se procede a realizar el ordenamiento y el análisis de datos.

- En cada servicio, los pacientes fueron ordenados por tiempo de espera, de menor a mayor. Para de este modo, liberar más rápidamente pacientes. De igual forma, se ordenaron cada uno de los servicios por tiempo promedio de espera, con el objetivo de conocer, cual es el servicio menos eficiente y más saturado. A partir de este ordenamiento de datos, es de donde nace el análisis de datos posterior.

### Data Analysis

- Se hizo uso de `matplotlib` para tener un resultado visual de lo que está ocurriendo y tener una idea más clara de la evolución del servicio. Por consola, también se imprimen los datos de personas y de servicio.

- Como parte fundamental del análisis de datos buscado, se creó y entrenó una red neuronal que analiza el tiempo total de espera, número de pacientes atendidos y tiempo promedio de espera. Para poder hacer una predicción de estos datos a futuro y saber que decisiones tomar.

- El Dataset de entrenamiento de datos se elaboró de forma manual. Ver [Para tener en cuenta](#para-tener-en-cuenta).

- Se creó una red neuronal de clasificación binaria. Con el objetivo de obtener una salida que nos representa la probabilidad de que un servicio esta en correcto estado o en crítico estado, de acuerdo a determinados valores númericos.

- Las funciones matemáticas y el análisis estadístico realizado partió de ejemplos anteriores realizados en clase.

- El modelo de entrenamiento de la red neuronal fue guardado para evitar que la red neuronal necesite entrenarse una y otra vez, al momento de usar el programa. Se graficó de igual forma, la evolución del modelo con `matplotlib`. Si el modelo esta correctamente guardado, en futuras ejecuciones del programa, el modelo será importado a través de funciones de `Tensorflow`.

- Finalmente, a partir del output que se obtenga de clasificación binaria, se harán determinadas recomendaciones para la evolución correcta y mejora del servicio.

## Para tener en cuenta

- El parcial desde un principio tuvo un enfoque muy abierto y subjetivo en su interpretación. Sin embargo, se mantuvo un enfoque en el Data Analysis.

- El Dataset de entrenamiento presenta una cantidad reducida de datos para entrenar correctamente el modelo de la red neuronal. Su creación se hizo de forma manual y considerando casos muy especificos. En consecuencia, el modelo no es el mas optimo en sus predicciones y sus resultados no son los mejores.

- A pesar de las carencias presentes en el modelo de la red neuronal, el objetivo principal fue modelar y diseñar una posible solución a una problemática del mundo real. En un futuro, tanto el autor como otro colaboradores podrán darle una aplicabilidad más real a esta idea de proyecto.

- Si vas a usar conocimiento intelectual de este proyecto, tomate el tiempo de agradecerle al autor :).

- No se provee ninguna guía de instalación para testing o uso.

## Author

[Alejandro Ríos](https://github.com/alejoriosm04) desarrolló completamente este parcial.

Copyright (c) 2022, Alejandro Ríos-Muñoz.