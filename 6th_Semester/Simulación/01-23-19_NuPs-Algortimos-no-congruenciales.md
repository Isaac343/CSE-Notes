<small>*Simulación - Miércoles 23, enero 2019  
Apunte*</small>

# Algoritmos no congruenciales
## Algoritmo de cuadrados medios.
Propuesto en la década de los 40 del siglo XX por Von Neumann y metrópolis, este algoritmo requiere un número entero, llamado semilla, con **D** dígitos, este es elevado al cuadrado para seleccionar del resultado los **D** dígitos del centro; el primer número $r_i$ se determina simplemente anteponiendo el "0" a esos dígitos. Para obtener el segundo $r_i$ se sigue el mismo procedimiento, solo que ahora se eleva al cuadrado los D dígitos del centro este método se repite hasta obtener **n** números ri.  

### Pasos para generar números con el algoritmo de pasos medios
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



<small>*Martes 29, enero 2019*</small>

## Algoritmo de productos medios
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


## Algoritmo de multiplicador constante
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
