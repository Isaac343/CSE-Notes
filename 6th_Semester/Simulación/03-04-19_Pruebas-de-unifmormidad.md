# Pruebas de uniformidad

Una de las pruebas mas importantes que debe de cumplir un conjunto de números $R_i$ es la uniformidad. Para comprobar su acatamiento se han desarrollado pruebas estadísticas tales como $\chi^2$ y  de *Kolmogorov-Smirnov*. En cualqueira de ambos casos para comprobar la uniformidad de los números de un conjunto $R_i$ es necesario formular las siguientes hipótesis.
$$
H_0: r_i ~ U(V,1)  
$$

$$
H_1: r_i\space no\space son\space uniformes
$$

Veamos a continuación como funciona cada una de estas pruebas. 

## Prueba $\chi^2$

La prueba $\chi^2$ busca determinar si los números del conjunto $R_i$ se distribuyen de manera uniforme en el intervalo  (0,1). Para llevar a acabo esta prueba es necesario dividir el intervalo (0,1) en $m$ subintervalos, en donde $m$ es recomendable $m = \sqrt{n}$. Luego se clasifica cada número pseudoaleatorio del conjunto $R_i$ en los $m$ intervalos. A la cantidad de números $R_i$ que se clasifican  en cada intervalo se le denomina frecuencia observada ($O_i$) y a la cantidad de números $R_i$ que se espera encontrar en cada intervalo se le llama frecuencia esperada ($E_i$); Teóricamente $E = \frac{n}{m}$. A partir de los valores de $O_i$ y $E_i$ se determina el estadístico $\chi_0^2$ mediante la ecuación: 
$$
\chi_0^2 = \sum_{i=1}^m{\frac{(E_i - O_i)^2}{E_i}}
$$
Si el valor estadístico $\chi_0^2$ es menor a las tablas de $\chi_{\alpha, m-1}^2$, entonces no se puede rechazar que el conjunto de números $R_i$ sigue una distribución uniforme, en caso contrario, se rechaza que $R_i$ sigue una distribución uniforme.

Realizar la prueba $\chi^2$ a los siguientes 100 números de un conjunto $R_i$, con un nivel de confianza de 95%. 



