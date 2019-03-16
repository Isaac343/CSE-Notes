# Pruebas de uniformidad

Una de las pruebas mas importantes que debe de cumplir un conjunto de números $R_i​$ es la uniformidad. Para comprobar su acatamiento se han desarrollado pruebas estadísticas tales como $\chi^2​$ y  de *Kolmogorov-Smirnov*. En cualqueira de ambos casos para comprobar la uniformidad de los números de un conjunto $R_i​$ es necesario formular las siguientes hipótesis.
$$
H_0: r_i ~ U(V,1)
$$

$$
H_1: r_i\space no\space son\space uniformes
$$

Veamos a continuación como funciona cada una de estas pruebas. 

## Prueba $\chi^2$

La prueba $\chi^2​$ busca determinar si los números del conjunto $R_i​$ se distribuyen de manera uniforme en el intervalo  (0,1). Para llevar a acabo esta prueba es necesario dividir el intervalo (0,1) en $m​$ subintervalos, en donde $m​$ es recomendable $m = \sqrt{n}​$. Luego se clasifica cada número pseudoaleatorio del conjunto $R_i​$ en los $m​$ intervalos. A la cantidad de números $R_i​$ que se clasifican  en cada intervalo se le denomina frecuencia observada ($O_i​$) y a la cantidad de números $R_i​$ que se espera encontrar en cada intervalo se le llama frecuencia esperada ($E_i​$); Teóricamente $E = \frac{n}{m}​$. A partir de los valores de $O_i​$ y $E_i​$ se determina el estadístico $\chi_0^2​$ mediante la ecuación: 
$$
\chi_0^2 = \sum_{i=1}^m{\frac{(E_i - O_i)^2}{E_i}}
$$
Si el valor estadístico $\chi_0^2$ es menor a las tablas de $\chi_{\alpha, m-1}^2$, entonces no se puede rechazar que el conjunto de números $R_i$ sigue una distribución uniforme, en caso contrario, se rechaza que $R_i$ sigue una distribución uniforme.

Realizar la prueba $\chi^2$ a los siguientes 100 números de un conjunto $R_i$, con un nivel de confianza de 95%. 

<small>lunes 11, marzo 2019</small>
$$
m = \sqrt{n}\\ m = 10
$$

| N°   | Intervalos  | $O_i$ | $E_i = (\frac{n}{m})$ | $\chi^2$                                |
| ---- | ----------- | ----- | --------------------- | --------------------------------------- |
| 1    | 0.00 - 0.09 | 7     | 10                    | $\frac{(10-7)^2}{10} = \frac{9}{10}$    |
| 2    | 0.10 - 0.19 | 9     | 10                    | $\frac{(10-9)^2}{10} = \frac{1}{10}$    |
| 3    | 0.20 - 0.29 | 8     | 10                    | $\frac{(10-8)^2}{10} = \frac{2}{5}$     |
| 4    | 0.30 - 0.39 | 9     | 10                    | $\frac{(10 - 9)^2}{10} = \frac{1}{10}$  |
| 5    | 0.40 - 0.49 | 14    | 10                    | $\frac{(10 - 14)^2}{10} = \frac{8}{5}$  |
| 6    | 0.50 - 0.59 | 7     | 10                    | $\frac{(10 - 7)^2}{10} = \frac{9}{10}$  |
| 7    | 0.60 - 0.69 | 11    | 10                    | $\frac{(10 - 11)^2}{10} = \frac{1}{10}$ |
| 8    | 0.70 - 0.79 | 14    | 10                    | $\frac{(10 - 14)^2}{10} = \frac{8}{5}$  |
| 9    | 0.80 - 0.89 | 9     | 10                    | $\frac{(10 - 9)^2}{10} = \frac{1}{10}$  |
| 10   | 0.90 - 0.99 | 12    | 10                    | $\frac{(10 - 12)^2}{10} = \frac{2}{5}$  |
|      |             | 100   |                       | 6.2                                     |

El estadístico $6.2$ es menor al estadistico correspondiente de $\chi_{0.05, 9}^2$. En consecuencia, no se puede rechazar que los números $R_i$ siguen una distribución uniforme dado que es menor.



## Prueba Kolmogorov- Smirnov

Propuesta por Kolmogorov y Smirnov, esta es una prueba estadística que también nos sirve apara terminar si un conjunto $r_i$ cumple con la propiedad de uniformidad. Es recomendable aplicarla en conjuntos $r_i$, por ejemplo, $n < 20$. El procedimiento es el siguiente:

1. Ordenar de mayor a menor los números del conjunto $r_i = r_1\le r_2 \le r_3 \le ... \le r_n$

<small>Martes 12, marzo 2019</small>

2. Determinar los valores de $D^+ ,\ D^-\ y\ D$ con las siguientes ecuaciones:

$D^+ = \max_{1<i<n} \{\frac{i}{n}-r_i\}$
$D^- = \max_{1<i<n}\{r_i - \frac{i-1}{n}\}$
$D = \max (D^+, D^-)​$

3. Determinar el valor crítico de $D_{\alpha, n}$ de acuerdo con la tabla de Kolmogorov-Sminrnov con un grado de confianza $\alpha$ y según el tamaño de la muestra $n$.

4. Si el valor $D$ es mayor que el valor crítico $D_{\alpha, n}$, se concluye que los números del conjunto $r_i$ no siguen una distribución uniforme, por tanto se rechaza; De lo contrario se dice que no se ha detectado diferencia significativa entre las distribución de los números del conjunto $r_i$ y la distribución uniforme. 

Realizar la prueba Kolmogorow-Smirnov con un nivel de confianza del 90% al siguiente conjunto $r_i$: 
$$
r_i = \{ 0.97, 0.11, 0.65, 0.26, 0.98, 0.03, 0.013, 0.89, 0.21, 0.69 \}
$$
El nivel de confianza del 90% inplica que $\alpha$ sea igual a 10%. Ordenando los números de $r_i$. 
$$
\{0.03, 0.11, 0.13, 0.21, 0.26, 0.65, 0.69, 0.89, 0.97, 0.98\}
$$
Para determinar los valores de $D^+$ y $D^-$ es recomendable realizar una tabla

<small>Miéroles 13, marzo 2019</small>

| i                     | 1    | 2    | 3     | 4     | 5     | 6     | 7    | 8     | 9     | 10    |
| --------------------- | ---- | ---- | ----- | ----- | ----- | ----- | ---- | ----- | ----- | ----- |
| $\frac{i}{n}$         | 0.10 | 0.20 | 0.30  | 0.40  | 0.50  | 0.60  | 0.70 | 0.80  | 0.90  | 0.00  |
| $r_i$                 | 0.03 | 0.11 | 0.13  | 0.21  | 0.26  | 0.65  | 0.69 | 0.89  | 0.97  | 0.98  |
| $\frac{i-1}{n}$       | 0.00 | 0.10 | 0.20  | 0.30  | 0.40  | 0.50  | 0.60 | 0.70  | 0.80  | 0.90  |
| $\frac{i}{n} - r_i$   | 0.07 | 0.09 | 0.17  | 0.19  | 0.24  | -0.05 | 0.01 | -0.09 | -0.07 | -0.98 |
| $r_i - \frac{i-1}{n}$ | 0.03 | 0.01 | -0.07 | -0.09 | -0.14 | 0.15  | 0.09 | 0.19  | 0.17  | 0.08  |
|                       |      |      |       |       |       |       |      |       |       |       |

$D^+ = 0.24\\ D^- = 0.19\\ D = (0.24, 0.19)$
