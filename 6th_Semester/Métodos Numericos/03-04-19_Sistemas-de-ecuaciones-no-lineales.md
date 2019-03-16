---
layout: note
title: Sistema de ecuaciones no lineales
subject: Ḿétodos numericos
---
<small>*Métodos Numéricos - Lunes 04, febrero 2019*</small>

# Sistemas de ecuaciones no lineales

Un sistema de ecuaciones no lineales tiene la forma:
$$
f_1 (x_1, x_2, ..., x_n) = 0
$$

$$
f_2 (x_1, x_2, ..., x_n) = 0
$$

$$
f_n (x_1, x_2, ..., x_n) = 0
$$

Donde podemos considerar a toda función $f_i$ como un mapeo del vector

 $X = (x_1, x_2, ..., x_n)$ del espacio *n-dimensional* $\R^n$ en la recta real $\R$.

Este sistema de $n$ ecuaciones no lineales con $n$ incógnitas puede representarse también mediante la definición de la función $F$, mapeando $\R^n$ en $\R^n$ por medio de: $F:\R^n -> \R^n$
$$
F (x_1, x_2, ..., x_n) = (f_1(x_1, x_2, ..., x_n),\space f_2(x_1, x_2, ..., x_n), ..., f_n(x_1, x_2, ..., x_n))
$$
En notación vectorial esto es:
$$
F(x) = 0
$$
Las funciones $f_1, f_2, ..., f_n$ son las funciones coordenadas de $F$.

Por ejemplo, el sistema
$$
5x_1^2 - x_1^2 = 0
$$

$$
x_2 - 0.25(\sin{x-1} + \cos{x_2}) = 0
$$

*Nota, se trata de un sistema de 2 x 2*.Este sistema puede expresarse como:
$$
f_1 (x_1, x_2)= 5x_1^2 - x_2^2 = 0
$$

$$
f_2(x_1, x_2) = x_2 - 0.25(\sin{x_1} + \cos{x_2} = 0)
$$

$$
F(x_1, x_2) = [5x_1^2 - x_2^2, x_2 - 0.25(\sin{x_1} + \cos_{x_2})]
$$



## Puntos fijos para funciones de varias variables

Dado un sistema no lineal de $n$ ecuaciones con $n$ incógnitas $F(x) = 0$, el método de punto fijo para este sistema consiste en transformar dicho sistema en otro equivalente del tipo $x = G(x)$.

<span style='color:#02c3a0; font-weight:bold'>Ejemplo</span>

Se resuelve la primera ecuación para una variable, despejando una incógnita ($x_1$).
$$
5x_1^2 - x_2^2 = 0
\space
\space
\space
x_1 = \sqrt{\frac{x_2^2}{5}} = \frac{1}{\sqrt{5}}x_2
$$
Se procede con la siguiente ecuación
$$
x_2 - 0.25(\sin{x_1} + \cos{x_2} = 0)
\space
\space
\space
x_2 =  0.25(\sin{x_1} + \cos{x_2})
$$

| N°   | $x_1$    | $x_2$    | $\epsilon_a x_1 (\%)$ |
| ---- | -------- | -------- | --------------------- |
| 0    | 0.1      | 0.1      | -                     |
| 1    | 0.044712 | 0.273709 | 123.60                |
| 2    | 0.122407 | 0.251870 | 62.47                 |
| 3    | 0.112640 | 0.272637 | 8.67                  |
| 4    | 0.121927 | 0.268867 | 7.61                  |
| 5    | 0.120241 | 0.271424 | 1.40                  |
| 6    | 0.121385 | 0.270835 | 0.94                  |

Una forma de acelerar la convergencia consiste en usar las estimaciones mas recientes, igual que en el método de Gauss-Seidel para los sistemas lineales.

<span style="color:#23f453; font-weight:bold;">Ejercicio 9.</span> Resolver el sistema anterior por medio de Gauss-Seidel.

| N°   | $x_1$    | $x_2$    | $\epsilon_a x_1 (\%)$ |
| ---- | -------- | -------- | --------------------- |
| 0    | 0.1      | 0.1      | -                     |
| 1    | 0.044721 | 0.259928 | 123.60                |
| 2    | 0.116243 | 0.270598 | 61.52                 |
| 3    | 0.121015 | 0.271083 | 3.94                  |
| 4    | 0.121232 | 0.271104 | 0.1789                |

<small>Lunes 11, marzo 2019</small>

<span style="color:#23f453; font-weight:bold;">Ejercicio 10.</span> Resuelva el sistema de ecuaciones no lineales.
$$
3X_1 - \cos{x_2 x_3} - \frac{1}{2} = 0
$$

$$
x_1^2 - 81 (x_2+ 0.1)^2 + \sin{x_3} + 1.06 = 0
$$

$$
e^{-x_1 x_2} +20x_3+ \frac{10 \pi - 3}{3} = 0
$$

Use el vector inicial $x = (0.1, 0.1, -0.1)$ con 5 iteraciones (Jacobi). Repita el ejercicio usando convergencia acelerada (Gauss-Seidel).
$$
x_1 = \frac{\frac{1}{2} + \cos{x_2 x_3}}{3}
$$

$$
x_2 =\sqrt{\frac{-x_1^2 - \sin{x_3} - 1.06}{-81}} - 0.1
$$

$$
x_3 = \frac{-e^{-x_1 x_2} - \frac{10 \pi - 3}{3}}{20}
$$



Método de Jacobi

| N°   | $X_1$    | $X_2$    | $X_3$     | $\epsilon_a\space de\space X_1$ |
| ---- | -------- | -------- | --------- | ------------------------------- |
| 0    | 0.1      | 0.1      | -0.1      | -                               |
| 1    | 0.499983 | 0.009441 | -0.523101 | 79.99                           |
| 2    | 0.499996 | 0.000026 | -0.523363 | 0.002                           |
| 3    | 0.5      | 0.000012 | -0.523598 | 0.0008                          |
| 4    | 0.5      | 0.000000 | -0.523598 | 0.000000                        |
| 5    | 0.5      | 0.000000 | -0.523599 | 0.000000                        |

Método de Gauss-Seidel

| N°   | $X_1$    | $X_2$    | $X_3$     | $\epsilon_a\space de\space X_1$ |
| ---- | -------- | -------- | --------- | ------------------------------- |
| 0    | 0.1      | 0.1      | -0.1      | -                               |
| 1    | 0.499983 | 0.022230 | -0.523046 | 79.99                           |
| 2    | 0.499999 | 0.022231 | -0.523046 | 0.003235                        |
| 3    | 0.499977 | 0.000028 | -0.523598 | 0.004307                        |
| 4    | 0.5      | 0.000000 | -0.523599 | 0.004600                        |
| 5    | 0.5      | 0.000000 | -0.523599 | 0.000000                        |


## Método de Newton

Se define la matriz *Jacobiana* $J(x)$ como 
$$
J(x) = 
\left(\begin{array}{cc}
\frac{\part{f_1}}{\part{x_1}}(x) & \frac{\part{f_1}}{\part{x_2}}(x) & \frac{\part{f_1}}{\part{x_3}}(x) \\
\frac{\part{f_2}}{\part{x_1}}(x) & \frac{\part{f_2}}{\part{x_2}}(x) & \frac{\part{f_2}}{\part{x_3}}(x) \\
\frac{\part{f_3}}{\part{x_1}}(x) & \frac{\part{f_3}}{\part{x_2}}(x) & \frac{\part{f_3}}{\part{x_3}}(x)
\end{array}\right)
$$
Por ejemplo, para el sistema anterior se tiene:
$$
f_1 = 3x_1 - cos(x_2 x_1) - \frac{1}{2} \\ 
f_2 = x_1^2 - 81(x_2 + 0.1)^2 + \sin{x_3} + 1.06 \\
f_3 = e^{-x_1 x_2} + 20x_3 + \frac{10\pi + 3}{3}
$$

$$
\frac{\part{f_1}}{\part{x_1}} = 3 \space\space\space \frac{\part{f_1}}{\part{x_2}} = x_3\sin{x_2 x_3} \space\space\space \frac{\part{f_1}}{\part{x_3}} = x_2\sin{x_2 x_3}\\
\frac{\part{f_2}}{\part{x_1}} = 2x_1 \space\space\space \frac{\part{f_2}}{\part{x_2}} = -162(x_2 + 0.1) \space\space\space \frac{\part{f_2}}{\part{x_3}} = \cos{x_3}\\
\frac{\part{f_3}}{\part{x_1}} = -x_2 e^{-x_1x_2} \space\space\space \frac{\part{f_3}}{\part{x_2}} = -x_1 e^{-x_1x_2} \space\space\space \frac{\part{f_3}}{\part{x_3}} = 20
$$

Obtenemos
$$
J = 
\left(\begin{array}{cc}
3 & x_3\sin{x_2x_3} & x_2\sin{x_2x_3}\\
2x_1 & -162(x_2 + 0.1) & \cos{x_3}\\
-x_2e^{-x_1x_2} & -x_1e^{-x_1x_2} & 20 
\end{array}\right)
$$


