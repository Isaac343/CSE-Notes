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

## Algoritmos no congruenciales
### Algoritmo de cuadrados medios.
Propuesto en la década de los 40 del siglo XX por Von Neumann y metrópolis, este algoritmo requiere un número entero, llamado semilla, con **D** dígitos, este es elevado al cuadrado para seleccionar del resultado los **D** dígitos del centro; el primer número $r_i$ se determina simplemente anteponiendo el "0" a esos dígitos. Para obtener el segundo $r_i$ se sigue el mismo procedimiento, solo que ahora se eleva al cuadrado los D dígitos del centro este método se repite hasta obtener **n** números ri.  

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
Serie de números aleatorios con semilla 317, D = 3.
| N° | $Y_n$ | $X_n$ | $R_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (317)^2 = 0,100,489$ | $x_0 = 004$ | $r_1 = 0.004$ |
| 02 | $Y_1 = (4)^2 = 00,016$ | $x_1 = 001$ | $r_2 = 0.001$ |
| 03 | $Y_2 = (1)^2 = 00,001$ | $x_2 = 000$ | $r_3 = 0.000$ |
| 04 | $Y_3 = (0)^2 = 0$ | $x_3 = 0$ | $r_4 = 0.000$ |
| 05 | $Y_4 = (0)^2 = 0$ | $x_4 = 0$ | $r_5 = 0.000$ |



Martes 29, enero 2019

### Algoritmo de productos medios
La mecánica de generación de números pseudoaleatorios de este algoritmo no congruencial es similar a la del algoritmo de cuadrados medios.
La diferencia entre ambos radica en que el algoritmo de productos medios requiere de 2 semillas ambas con $D$ dígitos, ademas, en lugar de elevarlas al cuadrado, las semillas se multiplican y del producto se seleccionan los $D$ dígitos de centro. A continuación se presentan con mas detalle los pasos del método para generar números.
1. Seleccionar una semilla con $D$ dígitos mayor a 3.
2. Seleccionar una semilla con $D$ dígitos mayor a 3.
3. $Y_0 = X_0 + X_1$; Sea $X_2$ = los $D$ dígitos del cetro, y sea $r_i$  = 0.$D$ dígitos del centro.  
<small> *Miércoles 30, enero 2019*</small>
4. Sea $Y_i$ = $X_i * X_{i+1}$ y sea $X_{i+2} =$ los $D$ dígitos del centro. y sea $r_{i+2} = 0.D$ dígitos del centro.
5. Repetir el paso 4 hasta obtener los $n$ números $r_i$ deseados.  
*Nota: Si no es posible obtener los $D$ dígitos del centro, agregue 0s a la izquierda del número $r_i$.*

Generar los primeros 5 números $r_i$ a partir de las semillas $X_0 = 5015$ y $X_1 = 5734$, siendo $D = 4$.

| N° | $Y_n$ | $X_n$ | $r_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (5015)*(5734) = 28,756,010$ | $X_2 = 7560$ | $r_1 = 0.7560$ |
| 02 | $Y_1 = (5734)*(7560) = 43,349,049$ | $X_3 = 3490$ | $r_2 = 0.3490$ |
| 03 | $Y_2 = (7560)*(3490) = 26,384,400$ | $X_4 = 3844$ | $r_3 = 0.3844$ |
| 04 | $Y_3 = (3490)*(3844) = 13,425,560$ | $X_5 = 4255$ | $r_4 = 0.4255$ |
| 05 | $Y_4 = (3844)*(4255) = 16,356,200$ | $X_6 = 3562$ | $r_5 = 0.3562$ |

Ejercicio. Generar los primeros 5 números $R_i$ a partir de las semillas $X_0 = 36$ y $X_1 = 97$, con $D = 2$.

| N° | $Y_n$ | $X_n$ | $r_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (36)*(97) = 3,492$ | $X_2 = 49$ | $r_1 = 0.49$ |
| 02 | $Y_1 = (97)*(49) = 4,753$ | $X_3 = 75$ | $r_2 = 0.75$ |
| 03 | $Y_2 = (49)*(75) = 3675$ | $X_4 = 67$ | $r_3 = 0.67$ |
| 04 | $Y_3 = (75)*(67) = 5025$ | $X_5 = 02$ | $r_4 = 0.02$ |
| 05 | $Y_4 = (67)*(02) = 0,134$ | $X_6 = 13$ | $r_5 = 0.13$ |


### Algoritmo de multiplicador constante
Este algoritmo no congruencial es similar al algoritmo de productos medios. Los siguientes son los pasos necesarios para generar números pseudoaleatorios con el algoritmo multiplicador constante.  
1. Seleccionar una semilla $X_0$ con $D$ dígitos donde $D > 3$.
2. Seleccionar una constante $(a)$ con $D$ dígitos donde $D > 3$.
3. $Y_0 = a * X_0$, sea $X_1 =$ los $D$ dígitos del centro, $r_i = 0.D$ dígitos del centro.
4. Sea $Y_i = a * X_i$; sea $X_{i+1} = $ los $D$ dígitos del centro, donde $i = 1, 2, 3, ..., n$.
5. Repetir el paso 4 hasta obtener los $n$ números $r_i$ deseados.

*Nota. Si no es posible obtener los $D$ dígitos del centro del número $Y_i$, agregue $0s$ a la izquierda del número $Y_i$.*

Ejemplo. $X_0 = 5340$, $a = 2010$, $D=4$

| N° | $Y_n = a * X_n$ | $X_n$ | $r_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (2010)*(5340) = 10,733,400$ | $X_2 = 7334$ | $r_1 = 0.7334$ |
| 02 | $Y_1 = (2010)*(7334) = 14,741,340$ | $X_3 = 7413$ | $r_2 = 0.7413$ |
| 03 | $Y_2 = (2010)*(7413) = 14,900,130$ | $X_4 = 9001$ | $r_3 = 0.9001$ |
| 04 | $Y_3 = (2010)*(9001) = 18,092,010$ | $X_5 = 0920$ | $r_4 = 0.0920$ |
| 05 | $Y_4 = (2010)*(920) = 01,849,200$ | $X_6 = 8492$ | $r_5 = 0.8492$ |

Ejercicio. Sea la semilla $X_0 = 9803$ y la constante $a = 6965$, considerando $D = 4$ dígitos.
| N° | $Y_n = a * X_n$ | $X_n$ | $r_n$ |
| :- | :---- | :---- | :---- |
| 01 | $Y_0 = (6965)*(9830) = 68,465,950$ | $X_2 = 4659 $ | $r_1 = 0.4659$ |
| 02 | $Y_1 = (6965)*(4659) = 32,449,935$ | $X_3 = 4499 $ | $r_2 = 0.4499$ |
| 03 | $Y_2 = (6965)*(4499) =31,335,535$ | $X_4 = 3355 $ | $r_3 = 0.3355$ |
| 04 | $Y_3 = (6965)*(3355) = 23,367,575$ | $X_5 = 3675 $ | $r_4 = 0.3675$ |
| 05 | $Y_4 = (6965)*(3675) = 25,596,375$ | $X_6 = 5963$ | $r_5 = 0.5963$ |

## Algoritmos congurenciales

### Algoritmo lineal
Este algoritmo congruencial fue propuesto por D.H. Lehmer en 1951. Según Law y Kelton, este algoritmo ha sido el mas usado. El algoritmo congruencial lineal genera una secuencia de números enteros por medio de la siguiente ecuación:
$$
X_{i+1} = (aX_i + C)  mod (M)
$$
donde; $X_0$ es la semilla, $X_0 > 0$ y debe ser entero. $a =$ constante multiplicativa, $a>0$ y debe ser entero.

<small>*Martes 5, febrero 2019*</small>  
La operación $"mod(M)"$ significa multiplicar $X_i * a$, sumar C, y dividir el resultado entre N para obtener el residuo de $X_{i+1}$. Es importante señalar que la ecuación recursiva del algoritmo congruencial lineal genera un secuencia de números enteros $S = \{0, 1, 2, 3, ..., m-1\}$, y que paa obtener números pseudoaleatorios en el intervalo (0, 1) se requiere la siguiente ecuación:
$$ r_i = \frac{x}{m-1} $$
$$ i = 0, 1, 2, 3, ..., n $$

**Ejercicio.** Generar 5 numeros aleatorias con los siquientes parametros, $X_o =$ 37, $a =$ 19, $C =$ 33, y $m =$ 100.  


| N° | $X_{i+1} = aX_n + C$ | $X_n = \frac{aX_n +c}{100}$ | $r_n = \frac{Mod X_n * 100}{99}$ |
| :- | :---- | :---- | :---- |
| 01 | $X_1 = (19) * (37) + 33 = 736$ | $X_1 = \frac{736}{100} = 7.36$ | $r_1 = \frac{36}{99} = 0.3636$ |
| 02 | $X_2 = (19) * (36) + 33 = 717$ | $X_2 = \frac{717}{100} = 7.17$ | $r_2 = \frac{17}{99} = 0.1717$ |
| 03 | $X_3 = (19) * (17) +33 = 356$ | $X_3 = \frac{356}{100}= 3.56$ | $r_3 = \frac{56}{99}= 0.5656$ |
| 04 | $X_4 = (19) * (56) + 33 = 1097$ | $X_4 = \frac{1097}{100} = 10.97$ | $r_4 = \frac{97}{99}= 0.9797$ |
| 05 | $X_5 = (19) * (97) +33 = 1876$ | $X_5 = \frac{1876}{100} = 18.76$ | $r_5 = \frac{76}{99} = 0.7676$ |

En el ejemplo anterior se vieron de manera arbitraria cada uno de los parámetros requeridos: $X_0, a, c, m$. Sin embargo para que el algoritmo sea capaz el máximo periodo de vida $N$, es preciso que dichos parámetros cumplan ciertas condiciones. *Banks, Carson, Nelson y Nicol*  sugieren lo siguiente:
$m = 2^g$  
$a = 1+4k$  
$K$ debe ser entero  
$c$ relativamente primo a $m$  
$g$ debe ser entero$
