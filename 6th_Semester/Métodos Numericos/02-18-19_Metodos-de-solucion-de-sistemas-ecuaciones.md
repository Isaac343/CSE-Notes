---
layout: note
title : Método de solución de sistemas de ecuaciones
---
# Unidad 2
<small>*Lunes 18, febrero 2019  
Apunte*</small>

# Método de solución de sistemas de ecuaciones

## Método de Jacobi
Sea un sistema de ecuaciones:
$$ \{A\}\{X\} = \{B\} $$
Si los elementos de la diagonal no son todos cero, se resuelven las ecuaciones como sigue:

<span style="color:#02c3a0; font-weight:bold;"> Para un sistema 3x3</span>  
$a_{11}X_1 + a_{12}X_2 + a_{13}X_3 = b_1$  
$a_{21}X_1 + a_{22}X_2 + a_{23}X_3 = b_2$  
$a_{31}X_1 + a_{32}X_2 + a_{33}X_3 = b_3$  

<span style="color:#02c3a0; font-weight:bold;"> la primera ecuación para $X_1$</span>  
$X_1 = \frac{b_1 - a_{12}X_2 - a_{13}X_3}{a_{11}}$  
<span style="color:#02c3a0; font-weight:bold;"> la segunda ecuación para $X_2$</span>  
$X_2 = \frac{b_2 - a_{21}X_1 - a_{23}X_3}{a_{22}}$  
<span style="color:#02c3a0; font-weight:bold;"> la tercer ecuación para $X_3$</span>  
$X_3 = \frac{b_3 - a_{31}X_1 - a_{33}X_2}{a-{33}}$

Se eligen valores iniciales para las X. Lo mas simple es suponer que todas las X son cero.  
Se calculan las nuevas $x$ y se sustituyen en la siguiente iteración.

### Criterio de paro
$$|\epsilon_{a,i}| = |\frac{X^i_k - X^{i-1}_k}{X^i_k}|* 100 \% < \epsilon_s $$
para todas las $k$ donde $i$ e $i-1$ son las iteraciones actuales y previas respectivamente.  
<span style="color:#02c3a0; font-weight:bold;"> Ejemplo. </span> Resuelve el sistema por el método de Jacobi, hasta que el error relativo porcentual este por debajo de 5%.  
$$ 10X_1 + 2X_2 - X_3 = 27 $$  
$$ -3X_1 - 6X_2 + 2X_3 = -61.5 $$  
$$ X_1 + X_2 + 5X_3 = -21.5 $$  
Despejando  
$$ X_1 = (27 - 2X_2 + X_3) / 10 $$  
$$ X_2 = (-61.5 + 3X_1 - 2X_3) / (-6) $$  
$$ X_3 = (-21.5 - X_1 - X_2) / 5 $$  

| N° | $X_1$ | $X_2$ | $X_3$ | $\epsilon_a$ |
| :- | :- | :- | :- | :- |
| 00 | 0 | 0 | 0 | - |
| 01 | 2.7 | 10.25 | -4.3 | 100 |
| 02 | 0.22 | 7.466666 | -6.89 | 1127.27 |
| 03 | 0.517667 | 7.843333 | -5.837333 | 135.3031 |
| 04 | 0.547600 | 8.045389 | -5.9722 | 5.4621 |
| 05 | 0.493702 | 7.985467 | -6.018597 | 10.91 |
| 06 | 0.501046 | 7.996950 | -5.995834 | 1.4657 |
| 07 | 0.501027 | 8.000865 | -5.999599 | 0.003792 |  
