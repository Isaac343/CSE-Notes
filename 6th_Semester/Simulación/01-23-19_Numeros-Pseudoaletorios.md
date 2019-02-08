<small>*Simulación - Miércoles 23, enero 2019  
Apunte*</small>

# **Unidad II -Número pseudoaleatorios**

Un número pseudoaleatorio es un número generado en un proceso que parece producir números al azar pero no es así realmente.
Las secuencias de números pseudoaleatorios no muestran ningún patrón o irregularidad aparente desde un punto de vista estadístico, a pesar de haber sido generados por un algoritmo completamente determinista, en el que las mismas condiciones iniciales producen siempre el mismo resultado.:
Los mecanismos de generación de números aleatorios que se utilizan en la mayoría de los sistemas informáticos son en realidad procesos pseudoaleatorios.  
Una de las utilidades principales de los números pseudoaleatorios se lleva a cabo en el llamado *Metodo de MonteCarlo*, con múltiples utilidades, por ejemplo para hallar áreas, volúmenes encerrados en un gráfica y cuyas integrales son muy difíciles de hallar o irresolubles; mediante la generación de puntos basados en estos números, podemos hacer una buena aproximación de la superficie, volumen total, encerrándolo en un cuadrado, cubo, aunque no los suficientemente buena.
Así mismo también destacan en el campo de la criptografía. Por ello se sigue investigando en la generación de dichos números empleando por ejemplo medidores de ruido blanco o analizadores atmosféricos, ya que experimentalmente se ha comprobado que tienen una aleatoriedad bastante alta.  

# Métodos de generación de números pseudoaleatorios
Existen un gran número de métodos para generar los números aleatorios entre 0 y 1.
El método a utilizar, en si mismo no tiene importancia; la importancia radica en los números que genera, ya que estos números deben cumplir ciertas características para que sean validos. Dichas características son:
1. Uniformemente distribuidos
2. Estadisticamente independientes
3. Su media debe ser estadisticamente igual a 1/2.
4. Su varianza debe ser estadisticamente igual a 1/2.
5. Su periodo o ciclo de vida debe ser largo


## ¿Para que sirven?
se usan como una fuente confiable de variabilidad dentro de los modelos de simulación, fundamentalmente por que las sucesiones de números pseudoaleatorios son mas rápidas de generar que las de los números aleatorios. La simulación es el proceso de diseñar un modelo de un sistema real, que servirá para dirigir experimentos con el propósito de entender, explicar, analizar o mejorar el comportamiento del sistema.  
Para simular el comportamiento de una o mas variables aleatorias es necesario contar con un conjunto suficientemente grande de números aleatorias, pero por desgracia generar una sucesión de números que sean completamente aleatorios resulta muy complicado ya que tendríamos que generar una sucesión infinita de valores que nos permitiera comprobar la inexistencia de correlaciones entre ellos lo que resultaría costoso y tardado lo que volvería impráctica la simulación; por ello es necesario usar los números pseudoaleatorios, de los cuales podemos asegurar con u nivel alto de confiabilidad que se comportan de manera similar a un conjunto de números aleatorios.
La experimentación directa sobre la realidad genera ciertos problemas: costo muy algo, gran lentitud, en ocasiones las pruebas son destructivas, pueden no ser éticas(sobre todo si están involucrado seres vivos), pueden resultar imposibles (por ejemplo para producir sucesos futuros).

## ¿Como se generan los números aleatorios entre 0 y 1?
Los números pseudoaleatorios se generan mediante algoritmos deterministicos, es decir aquellos en que se obtiene el mismo resultado bajo las mismas condiciones iniciales, por lo cual requieren parámetros de arranque.  
Sea una secuencia $r_i = (r_1, r_2, r_3, ..., r_n)$ con **n** valores distintos, se le conoce como el conjunto necesario de números entre 0 y 1 para realizar una simulación, siendo **n** el periodo o ciclo de vida.  
Esta secuencia forma la parte principal de la simulación de procesos estocásticos (basados en probabilidades) y son usados para generar la conducta de variables aleatorias, continuas o discretas. Estos números se consideran pseudoaleatorios por que es imposible el generar núeros realmente aleatorios.  
Es preciso contar con un conjunto **ri** grande esto con la finalidad de simular el comportamiento de una  mas variables aleatorias, ademas el periodo de vida debe ser amplio debido a que es conveniente realizar varias replicas de simulación, corriendo cada una con números pseudoaleatorios distintos. Es importante señalar que **ri** se considera satisfactorio si pasa sin problema las pruebas de uniformidad e independencia, solo así podrá ser usado en la simulación.  
Los algoritmos determínisticos para generar números pseudoaleatorios se dividen en *no congurenciales* y *congurenciales*, estos a su vez se dividen en *lineales* y *no lineales*.
