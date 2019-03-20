

# Pruebas de independencia

Recuerde que las do propiedades mas importantes que deben satisfacer los números de un conjunto $r_i$ son uniformidad e independencia. En la sección anterior conectamos las pruebas que buscan determinar si los números del conjunto $r_i$ son uniformes. A continuación se trataran de las pruebas estadísticas que tratan de corroborar si los números en intervalo 0,1 son independientes o, en otras palabras si parecen pseudoaleatorios. 

Para probar la independencia de los números de un conjunto $r_i$, es preciso formar las siguientes hipótesis:

$H_0:$ Los números del conjunto $r_i$ **SON** independientes
$H_1:$ Los números del conjunto $r_i$ **NO** son independientes

## Prueba de corridas arriba y abajo

El procedimiento de esta prueba consiste en determinar una secuencia de números ($S$) que solo contiene unos y ceros, de acuerdo con una comparación entre $r_i$ y $r_{i-1}$. Después se determina el número de corridas $C_0$ (Una corrida se identifica como la cantidad de unos o ceros consecutivos). Luego se calcula el valor esperado, la varianza del número de corridas y el estadístico $z_0$, mediante las siguientes ecuaciones.
$$
\mu_{C_0} = \frac{2_{n}-1}{3}\\ \sigma^2_{C_0} = \frac{16n - 29}{90}\\ Z_0 = |\frac{C_0 -\mu_{C_0}}{\sigma_{C_0}}|
$$
Si el estadístico $Z_0​$ es mayor que el valor crítico $Z_{\alpha / 2}​$ se concluye que los números $r_i​$ no son independientes. De lo contrario no se pude rechazar que el conjunto de $r_i​$ sea independiente. 

Considere el siguiente conjunto:
$$
r_i = (0.9, 0.26, 0.01, 0.98, 0.13, 0.12, 0.69, 0.11, 0.05, 0.065, 0.21, 0.03, 0.11, 0.07, 0.97, 0.27, 0.12, 0.95, 0.02, 0.06)
$$


La secuencia de ceros se construye de la siguiente manera: 
Se coloca un 0 si el el número $r_i$ es menor que o menor o igual que el número $r_i$ anterior, en caso de ser mayor o igual que el número $r_i$ anterior se coloca un 1.

Si se toma en cuenta la serie de 21 número $r_i​$ anterior, la secuencia de ceros y unos es: 
$$
S = \{0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1\}
$$
Recuerda que una corrida se forma con unos consecutivos o ceros consecutivos. Por ejemplo los primeros 2 ceros forman la primera corrida la cual se dice que tiene una longitud de 2; el tercer número de la secuencia, 1 forma la segunda corrida con longitud de 1; siguen 2 ceros, los cuales forman a tercera corrida con longitud de 2; el siguiente es un 1, el cual forma la siguiente corrida con longitud de 1, etc. Siguiendo el proceso anterior se determina que el número de corridas de la secuencia es $C_0 = 14$.

<small>Martes 19, marzo 2019</small> 

Como el estadístico $Z_0$ es menor que el valor crítico de $Z(1.96)$ se concluye que no se puede rechazar que los números del conjunto $r_i$ son independientes, es decir, de acuerdo con esta prueba los números son aptos para usarse en simulación.

## Prueba de corridas arriba y abajo de la media 

## Prueba de Poker

## Prueba de series



