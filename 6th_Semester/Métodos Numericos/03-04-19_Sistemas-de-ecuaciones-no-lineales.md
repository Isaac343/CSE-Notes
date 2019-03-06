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
