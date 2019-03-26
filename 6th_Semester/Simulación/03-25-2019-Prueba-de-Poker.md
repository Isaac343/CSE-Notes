---
layout: note
title: Prueba de Poker
subject: Simulación
date: 03-25-2019
---



# Prueba de poker

Esta prueba consiste en visualizar el numero $r_i$ con 5 decimales (cómo si fuera una mano del juego de poker con 5 cartas) y clarificarlos como: todos diferentes (TD), exactamente un par (1P), dos pares (2P), 1 tercia (T), un par y una tercia (TP), poker(P) y quintilla(Q). Por ejemplo, si $r_iv= 0.69651​$, se le clasifica como par pues hay 2 números "6"

En caso de qu $r_i = 0.34341​$ debe clasificarse como 2 pares (dos número 3 y dos número 4).

Finalmente $r_i = 0.98898$, el cual esta clasificado como una tercia y un par, pues hay tres números 8 y dos números 9. La prueba poker se puede realizar a números $r_i$ a 3,4 y 5 decimales. Para $r_i$ con 3 decimales solo existen 3 categorías de clasificación: todos diferentes (TD), un par (1P), una tercia (T). Cuando se cuenta con $r_i$ con 4 decimales, se cuenta con 5 categorías para clasificar los números: todos diferentes(TD), un par(1P), dos pares(2P), una tercia(T) y poker (P). 

La prueba poker requiere el estadístico de la distribución "*chi-cuadrada*"($\chi^2_{\alpha, 6}$) para números con 5 decimales, $\chi^2_{\alpha, 4}$ para números con 4 decimales, $\chi^2_{\alpha, 2}$. $\chi^2_{\alpha, 6}​$ tiene 6 grados de libertad debido a que los números se clasifican en 7 categorías  o clases: todos diferentes, exactamente un par, dos pares, una tercia, una tercia y un par, poker, quintilla.

El procedimiento de la prueba consiste en:

1. determinar la categoría de cada número del conjunto $r_i$
2. contabilizar los números $r_i$ de la misma categoría o clase para obtener la frecuencia observada $O_i$.
3. Calcular el estadístico de la prueba $\chi^2 = \sum^m_{i=1}{\frac{(E_i - O_i)^2}{E_i}}$. Donde $E_i$ es la frecuencia esperada de números $r_i$ en cada categoría, y $m$ representa la cantidad de categorías o clases en las que se clasificaron los números $r_i$, siendo $m = 7,\ m=5\ y \ m=3$. Los números de categorías para la prueba pocker con signo 4, respectivamente. 
4. Comparar el estadístico de C contra $\chi^2_{\alpha, m-1}$.



