---
layout: note
title: Prueba de Poker
subject: Simulación
date: 03-25-2019
---

# Prueba de poker

Esta prueba consiste en visualizar el numero $r_i$ con 5 decimales (cómo si fuera una mano del juego de poker con 5 cartas) y clarificarlos como: todos diferentes (TD), exactamente un par (1P), dos pares (2P), 1 tercia (T), un par y una tercia (TP), poker(P) y quintilla(Q). Por ejemplo, si $r_iv= 0.69651$, se le clasifica como par pues hay 2 números "6"

En caso de qu $r_i = 0.34341​$ debe clasificarse como 2 pares (dos número 3 y dos número 4).

Finalmente $r_i = 0.98898$, el cual esta clasificado como una tercia y un par, pues hay tres números 8 y dos números 9. La prueba poker se puede realizar a números $r_i$ a 3,4 y 5 decimales. Para $r_i$ con 3 decimales solo existen 3 categorías de clasificación: todos diferentes (TD), un par (1P), una tercia (T). Cuando se cuenta con $r_i$ con 4 decimales, se cuenta con 5 categorías para clasificar los números: todos diferentes(TD), un par(1P), dos pares(2P), una tercia(T) y poker (P). 

La prueba poker requiere el estadístico de la distribución "*chi-cuadrada*"($\chi^2_{\alpha, 6}$) para números con 5 decimales, $\chi^2_{\alpha, 4}$ para números con 4 decimales, $\chi^2_{\alpha, 2}$. $\chi^2_{\alpha, 6}​$ tiene 6 grados de libertad debido a que los números se clasifican en 7 categorías  o clases: todos diferentes, exactamente un par, dos pares, una tercia, una tercia y un par, poker, quintilla.

El procedimiento de la prueba consiste en:

1. determinar la categoría de cada número del conjunto $r_i$
   2. contabilizar los números $r_i$ de la misma categoría o clase para obtener la frecuencia observada $O_i$.
2. Calcular el estadístico de la prueba $\chi^2 = \sum^m_{i=1}{\frac{(E_i - O_i)^2}{E_i}}$. Donde $E_i$ es la frecuencia esperada de números $r_i$ en cada categoría, y $m$ representa la cantidad de categorías o clases en las que se clasificaron los números $r_i$, siendo $m = 7,\ m=5\ y \ m=3$. Los números de categorías para la prueba pocker con signo 4, respectivamente. 
3. Comparar el estadístico de C contra $\chi^2_{\alpha, m-1}$.



| 0.06141 | 0.72484 | 0.94107 | 0.56766 | 0.14411 | 0.87648 |
| ------- | ------- | ------- | ------- | ------- | ------- |
| 0.81792 | 0.48999 | 0.18590 | 0.06060 | 0.11223 | 0.64794 |
| 0.52953 | 0.50502 | 0.30444 | 0.70688 | 0.25357 | 0.31555 |
| 0.04127 | 0.67347 | 0.28103 | 0.99367 | 0.44598 | 0.73997 |
| 0.27813 | 0.62182 | 0.82578 | 0.85623 | 0.51483 | 0.09099 |

TD = 8, 1P = 12, 2P = 3, T = 3, TP = 4, P = 0, Q = 0

Formula para obtener combinaciones sin repetición
$$
\frac{n!}{r! (n!-r!)}
$$


Para las manos de poker se tiene que:

 

|         Mano          |                           Ecuacion                           | Propabilidad |
| :-------------------: | :----------------------------------------------------------: | :----------: |
| Todas Diferentes (TD) |                  $\frac{10*9*8*7*6}{10^5}$                   |    0.3024    |
|      1 Par (1P)       |       $\frac{10*1*9*8*7}{10^5} * \frac{5!}{2!(5-2)!}$        |    0.5040    |
|     2 Pares (2P)      | $\frac{1}{2} * \frac{10*1*9*1*8}{10^5} * \frac{5!}{2!(5-2)!} * \frac{3!}{2!(3-2)!}$ |    0.1080    |
|      Tercia (T)       |       $\frac{10*1*1*9*8}{10^5} * \frac{5!}{3!(5-3)!}$        |    0.0720    |
| Tercia y un par (TP)  | $\frac{10*1*1*9*1}{10^5}* \frac{5!}{3!(5-3)!} * \frac{2!}{2!(2-2)!}$ |    0.0090    |
|       Poker (P)       |       $\frac{10*1*1*1*9}{10^5} * \frac{5!}{4!(5-4)!}$        |    0.0045    |
|     Quintilla (Q)     |       $\frac{10*1*1*1*1}{10^5} * \frac{5!}{5!(5-5)!}$        |    0.0001    |



| N°   | $O_i$ | $E_I$ Frecuencia esperada | $(\frac{E_i - O_i}{E_i})^2$ |
| ---- | ----- | :------------------------ | --------------------------: |
| TD   | 8     | 0.3024(30) = 9.07220      |                    0.126718 |
| 1P   | 12    | 0.5040(30) = 15.12        |                    0.643810 |
| 2P   | 3     | 0.1080(30) = 3.24         |                    0.017778 |
| T    | 4     | 0.0720(30) = 2.16         |                    1.567407 |
| TP   | 3     | 0.0090(30) = 0.27         |                   27.603333 |
| P    | 0     | 0.0045(30) = 0.135        |                    0.135000 |
| Q    | 0     | 0.0001(30) = 0.0030       |                    0.003000 |
|      |       | $\chi^2$                  |                   30.097046 |

El valor para $\chi^2$ para $\alpha = 0.05$ y 6 es: 12.5916. Dado que $30.0970046 > 12.5916$ el conjunto de números $r_i$ es aceptado 