<small>*Simulación - Miércoles 30, enero 2019  
Apunte*</small>

# Algoritmos congurenciales

## Algoritmo lineal
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

<small>*Miércoles 6, febrero 2019*</small>
Bajo dichas condiciones se obtiene un periodo de vida máximo $N = m = 2^g$.
Generar suficientes números entre 0 y 1 con los parametro $X_0 =$ 6, $ K =$ 3, $g =$ 3, y $C =$ 7.
$a = 1 + 4(k)$ y $m = 2^3$  
$a = 1 + 4(3) = 13$ y $m = 2^3 = 8$   
$X_0 = 6$  
$X_1 = (13 * 6 + 7)mod(8)$

| N° | $X_{i+1} = (aX_n + C)mod(m)$ | $X_n = aX_n * m$ | $r_n = \frac{X_n}{C}$ |
| :- | :---- | :---- | :---- |
| 01 | $X_1 = ((13) * (6) + 7)mod(8) = 0.625$ | $X_1 = 0.635*8 = 5$ | $r_1 = \frac{5}{7} = 0.7142$ |
| 02 | $X_2 = ((13) * (5) + 7)mod(8) = 0.000$ | $X_2 = 0.000*8 = 0$ | $r_2 = \frac{0}{7} = 0.0000$ |
| 03 | $X_3 = ((13) * (0) + 7)mod(8) = 0.875$ | $X_3 = 0.875*8 = 7$ | $r_3 = \frac{7}{7} = 1.000$ |
| 04 | $X_4 = ((13) * (7) + 7)mod(8) = 0.250$ | $X_4 = 0.250*8 = 2$ | $r_4 = \frac{2}{7}= 0.2857$ |
| 05 | $X_5 = ((13) * (2) + 7)mod(8) = 0.125$ | $X_5 = 0.125*8 = 1$ | $r_5 = \frac{1}{7} = 0.1428$ |
| 06 | $X_6 = ((13) * (1) + 7)mod(8) = 0.500$ | $X_6 = 0.500*8 = 4$ | $r_6 = \frac{4}{7} = 0.5714$ |
| 07 | $X_7 = ((13) * (4) + 7)mod(8) = 0.375$ | $X_7 = 0.375*8 = 3$ | $r_7 = \frac{3}{7} = 0.4285$ |
| 08 | $X_8 = ((13) * (3) + 7)mod(8) = 0.750$ | $X_8 = 0.750*8 = 6$ | $r_8 = \frac{6}{7} = 0.8571$ |


Es importante mencionar que el número generado en $X_8 =$ 6 es exactamente igual a la semilla $X_0$, y si continuáramos generando mas números, estos se repetirían. Ademas, sabemos que el algoritmo congruencial lineal genera una secuencia de números enteros.
Consideremos de nuevo el ejemplo anterior
$X_0 =$ 6, $a =$ 12 como valor arbitrario.
$X_1 = (12 * 6 + 7)mod(8) = 0.975 * 8 = 7$, por tanto $r_i = \frac{7}{7} = 1$  
$X_2 = (12 * 7 + 4)mod(8) = 0.372 * 8 = 3$, por tanto $r_i = \frac{3}{7} = 0.428$  
$X_3 = (12 * 3 + 7)mod(8) = 0.375 * 8 = 3$, por tanto $r_i = \frac{3}{7} = 0.428$  
El periodo de vida ene ste caso es $N =$ 2, de manera que, como se puede observar no se logra el periodo de vida máximo. Como conclusión tenemos que si no se cumple alguna de las condiciones, el periodo de vida máximo $N=m$ no se garantiza, por lo que el periódo de vida sero manor que $m$.

## Algoritmo congruencial multiplicativo
El algoritmo congruencial multiplicativo surge del algoritmo congruencial lineal cuando $C =$ 0. Entonces la ecuación lineal recursiva es
$$X_{i+1} = (aX_i)mod(m)$$  
$$ i = (0 , 1, 2, 3, ..., n)$$

En comparación con el algoritmo congruencial lineal, la ventaja del algoritmo multiplicativo es que implica una operación menos a realizar. Los parámetros de arranque de este algoritmo son $X_0$, $a$ y $m$.
Para transformar los números $X_i$ en el intervalo (0, 1), se usa la ecuación:
$$ r_i =\frac{X_i}{m-1}$$

De acuerdo con *Banks, Carson, Nelson y Nicol*, las condiciones que deben cumplir los parámetros para este algoritmo congruencial multiplicativo alcance su máximo periodo $M$.

$m = 2^3$  
$a = 3 + 8 k$ ó $a = 5 + 8 k$  
$k = 0, 1, 2, 3, ...$  
$X_0 =$ número impar  
$g$ debe ser entero  
A partir de estas condiciones se logra un algorimto $N = \frac{k}{4} = 2^{g-2}$.

Generar suficientes números entre 0 y 1 con los siguientes parámetros: $X_0 = 17$, $K = 2$, $g = 5$, $a = 5 + 8(2) = 21$, $m = 32$ hasta $X_8$. Determinar cual es el periodo mimo de vida.

| N° | $X_n = a * X_{n-1}mod(m)$ | |  |
| :- | :---- | :---- | :---- |
| 01 |  |  |  |
| 02 |  |  |  |
| 03 |  |  |  |
| 04 |  |  |  |
| 05 |  |  |  |
| 06 |  |  |  |
| 07 |  |  |  |
| 08 |  |  |  |

<small>*Martes 12, febrero 2019*</small>
## Algoritmo congruencial aditivo
Este algoritmo requiere una secuencia previa de $n$ números enteros $x_1, x_2, x_3, ..., x_n$ para generar una secuencia de números enteros  que empieza en $x_{n+1}, x_{n+2}, x_{n+3}$. Su ecuación recursiva es:
$$X_i = (X_{i+1} + X_{i-n}) mod(m)$$
$$ i = n+1, n+2, n+3, ..., N$$
Los numeros $r_i$ son generados con la siguiente formula
$$ r_i = \frac{X_i}{m-1} $$

Generar 7 números pseudoaleatorios entre 0 y 1, a partir de la siguiente secuencia de números enteros: $x_1 = 65, x_2 = 89, x_3 = 98, x_4 = 03, x_5 = 69;$ m=100. para generar $R_1, a R_7$ antes es necesario generar $r_1$ hasta $r_12$
| N° | $X_i = (X_{i-1}+X_{i-n})mod(m)$ | $r_i = \frac{X_i}{m-1}$ |
| :- | :---- | :---- |
| 01 | $X_6 = (69 + 65)mod(100) = 0.34$ | $\frac{34}{99} = 0.3434$ |
| 02 | $X_7 = (34 + 89)mod(100) = 0.23$ | $\frac{23}{99} = 0.2323$ |
| 03 | $X_8 = (23 + 98)mod(100) = 0.21$ | $\frac{21}{99} = 0.2121$ |
| 04 | $X_9 = (21 + 03)mod(100) = 0.24$ | $\frac{24}{99} = 0.2424$ |
| 05 | $X_10 = (24 + 69)mod(100) = 0.93$ | $\frac{93}{99} = 0.9393$ |
| 06 | $X_11 = (93 + 34)mod(100) = 0.27$ | $\frac{27}{99} = 0.2727$ |
| 07 | $X_12 = (27 + 23)mod(100) = 0.50$ | $\frac{50}{99} = 0.5050$ |
| 08 | $X_13 = (50 + 21)mod(100) = 0.71$ | $\frac{71}{99} = 0.7171$ |
