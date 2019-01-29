Miércoles 23, enero 2019
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

## Algoritmos no congruenciales
**Algoritmo de cuadrados medios.** Propuesto en la década de los 40 del siglo XX por Von Neumann y metrópolis, este algoritmo requiere un número entero, llamado semilla, con **D** dígitos, este es elevado al cuadrado para seleccionar del resultado los **D** dígitos del centro; el primer número $r_i$ se determina simplemente anteponiendo el "0" a esos dígitos. Para obtener el segundo $r_i$ se sigue el mismo procedimiento, solo que ahora se eleva al cuadrado los D dígitos del centro este método se repite hasta obtener **n** números ri.  

#### Pasos para generar números con el algoritmo de pasos medios
1. Seleccionar semilla $(X_0)(D>3)$.
2. Sea $X_0$ = Resultado de elevar ${X_0}^2$; sea $X_1$ = D dígitos del centro, y sean $R_i$ = D dígitos.
3. Sea $R_i$ resultado de $(X_i)^2$; sea $X_{i+1} = D$ dígitos centrales, y sea $R_i = 0$ D dígitos del centro para toda $i = 1,2,3,...,n$
4. Repetir el paso 3 hasta obtener los $n$ números $R_i$ deseados.

*Nota: si no es posible obtener los D dígitos del centro del número Y<sub>i</sub> agregue 0s a la izquierda del número Y<sub>i</sub>.*

**Ejemplo.** Generar los primeros 5 números r<sub>i</sub>, a partir de una semilla X<sub>0</sub> = 5735, de donde se puede observar que D = 4 dígitos.  
| N° | $Y_n$ | $X_n$ | $R_n$ |
| :- | :-----| :-----| :---- |
| 01 | $Y_0 = (5735)^2 = 32,890,225$ | $x_0 = 8902$ | $r_1 = 0.8902$ |
| 02 | $Y_1 = (8902)^2 = 79,245,694$ | $x_1 = 2456$ | $r_2 = 0.2456$ |
| 03 | $Y_2 = (2456)^2 = 06,031,936$ | $x_2 = 0319$ | $r_3 = 0.0319$ |
| 04 | $Y_3 = (0319)^2 = 101,761$    | $x_3 = 1176$ | $r_4 = 0.1176$ |
| 05 | $Y_4 = (1176)^2 = 1,382,976$  | $x_4 = 3829$ | $r_5 = 0.3829$ |    

*Nota. Generalmente este algoritmo es incapaz de generar una secuencia de $R_i$ con periodo de vida $n$ grande. En ocasiones solo es capaz de generar un número, por ejemplo si $X_0 = 1000$ entonces $X_1 = 0000$; $r_i = 0.0000$ y se se dice que el algoritmo se degenera con la semilla de $X_0 = 1000$.*  


#### Tarea.
Serie de números aleatorios con semilla 317, D = 4.
| N° | $Y_n$ | $X_n$ | $R_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (317)^2 = 100,489$ | $x_0 = 0049$ | $r_1 = 0.0049$ |
| 02 | $Y_1 = (49)^2 = 2,401$ | $x_1 = 0240$ | $r_2 = 0.0240$ |
| 03 | $Y_2 = (240)^2 = 57,600$ | $x_2 = 0576$ | $r_3 = 0.0576$ |
| 04 | $Y_3 = (576)^2 = 331,776$ | $x_3 = 3177$ | $r_4 = 0.3177$ |
| 05 | $Y_4 = (3177)^2 = 10,093,329$ | $x_4 = 0933$ | $r_5 = 0.0933$ |
