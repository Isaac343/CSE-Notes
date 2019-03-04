# Pruebas estadísticas de los números pseudoaleatorios 

Se presentaron varios algoritmos para construir un conjunto $R_i$ pero ese es solo el primer paso, ya que el conjunto resultante debe ser sometido a una serie de pruebas para determinar si los números que lo integran son aptos para usarse en un estudio de simulación. 

Se analizaran las pruebas estadísticas básicas que se empelan generalmente para determinar si un conjunto de números pseudoaleatorios entre 0 y 1 cumplen con las propiedades básicas de independencia y de uniformidad. El objetivo, en otras palabras, es validar que el resultado $R_i$ realmente esta conformado por números aleatorios.

## Prueba de medias
Una de las propiedades que deben cumplir los números del conjunto $R_I$ es que el valor esperado sea igual a $0.5$ la prueba que busca determinar lo anterior es llamada "prueba de medias", en la cual se plantean las siguientes hipótesis. 
$$
H_o:\mu_{r_i} = 0.5
$$

$$
H_1: \mu_{r_i} \neq 0.5
$$

La prueba de medias consiste en determinar el promedio de los $n$ números que contiene el conjunto $r_i$ mediante la ecuación siguiente:
$$
r= \frac{1}{n}\sum_{i = 1}^n{r_i}
$$

| 0.0449 | 0.1733 | 0.5746 | 0.049  | 0.8406 | 0.8349 | 0.92   | 0.2564 |
| ------ | ------ | ------ | ------ | ------ | ------ | ------ | ------ |
| 0.6015 | 0.6694 | 0.3972 | 0.7025 | 0.1055 | 0.1247 | 0.1977 | 0.0125 |
| 0.63   | 0.2531 | 0.8297 | 0.6483 | 0.6972 | 0.9582 | 0.9085 | 0.8524 |
| 0.5514 | 0.0316 | 0.3587 | 0.7041 | 0.5915 | 0.2523 | 0.2545 | 0.3044 |
| 0.0207 | 0.1067 | 0.3857 | 0.1746 | 0.3362 | 0.1589 | 0.3727 | 0.4145 |

$$
r = 0.432515
$$



Después se calculan los límites de aceptación superior e inferior con los siguientes ecuaciones	
$$
LI_r = \frac{1}{2}-Z_{\frac{\alpha}{2}}{[\frac{1}{\sqrt{12n}}]}
$$

$$
LS_r = \frac{1}{2}+ Z_{\frac{\alpha}{2}}[\frac{1}{\sqrt{12n}}]
$$

si el valor de $r⁻$ se encuentra dentro de los límites de aceptación concluimos que no se puede rechazar que el conjunto $r_i$ tiene un valor esperado de 0.5 con un nivel de aceptación de $1-\alpha$. 

En caso contrario se rechaza que el conjunto $r_i$ tiene un valor esperado de 0.5. 

Para el cálculo de los límites de aceptación se utiliza el estadístico $Z_{\frac{\alpha}{2}}$ el cual se determina por medio de la tabla de distribución normal estándar.

Conjunto $r = 40$ números
$n = 10$
$\alpha = 5\%$

<small>*Martes 26, febrero 2019*</small>

El conjunto es aceptado pues la hipótesis queda entre los límites. ($LS_r= 0.589461$, $LI_r = 0.410538$)

## Prueba de Varianza

Otra de las propiedades que debe satisfacer el conjunto $r_i$ es que sus números tengan una varianza de $\frac{1}{12}$. La prueba que busca determinar lo anterior es la prueba de varianza, establece las siguientes hipótesis.
$$
H_0 : \alpha^2 = \frac{1}{12}
$$

$$
H_1 : \alpha^2 \neq \frac{1}{12}
$$

La prueba de varianza consiste en determinar la varianza de los $n$ números que contiene el conjunto $R_i$ mediante la ecuación siguiente:
$$
V(r) = \frac{\sum_{i=1}^n{(r_i - \vec{r})^2}}{n-1}
$$
Después se calculan los límites inferior y superior con las siguientes ecuaciones: 
$$
LI_{v(r)} = \frac{\chi^2_{(1 - \alpha) / 2}, n -1}{12(n -1)}
$$
$$
LS_{v(r)} = \frac{\chi^2_{(\alpha/s)}, n- 1}{12(n-1)}
$$



Si el valor de $v_{(r)}$ se encuentra entre los limites de aceptación decimos que no se puede rechazar el conjunto $R_i$, tiene una varianza de $\frac{1}{12}$ con un nivel de aceptación de $1-\alpha$; de lo contrario, se rechaza el conjunto $R_i$, tiene una varianza de $\frac{1}{12}​$.

Realiza la prueba de varianza a los 40 numero $r_i$ considerando que $n= 40$, y $\alpha = 5\%​$, procede a calcular la varianza de los números, y los límites de aceptación correspondientes. 

$$V(r) = 0.086950$$

$LI_{v(r)} = \frac{\chi 1-0.05/2, 39}{12(39)} = \frac{0.975, 39}{468} = \frac{23,6543}{468} = 0.050543$

$LS_{v(r)} = \frac{\chi \space 0.05/2, 39}{12(39)} = \frac{0.025, 39}{12(39)} = \frac{44,5395}{468} = 0.093033$ 

Dado que el valor de la varianza es igual a 0.08 esta entre los limites inferior y superior por tanto no se puede rechazar el conjunto de números. 