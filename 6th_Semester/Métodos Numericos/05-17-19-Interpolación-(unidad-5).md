---
layout: note
date: 05-17-19
title: Interpolación
subject: Métodos numéricos
---

# Unidad 5

# Interpolación

Estimar valores intermedios con valores asociados con datos.

## Interpolación polinomial 

Polinomio de n-esímo grado: $f(x) = a_0 + a_1x + a_2x²+ ... + a_nx^n$.

Dados n + 1 puntos asociados con datos, hay uno y solo un polinomio de grado **n** que pasa a través de todos lo puntos.

## Interpolación lineal

Unir dos puntos asociados con datos con una linea recta:
$$
\frac{f(x)-f(x_0)}{x-x_0} = \frac{f(x_1) - f(x_0)}{x_1 - x_0}\\
f(x) = f(x_0) + \frac{f(x_1) - f(x_0)}{x_1 -x_0}(x - x_0)\\
$$

## Interpolación cuadrática 

Si se tienen 3 puntos asociados con datos, éstos pueden ajustarse en un polinomio de segundo grado. 

Una forma conveniente es:
$$
f_2(x) = b_0 + b_1(x - x_0) + b_2(x - x_0)(x - x_1)\\
= b_0 + b_1x - b_1x_0 + b_2(x2 - x_1x - x_0x + x_0x_1)\\ 
= b_0 + b_1x - b_1x_0 + b_2x2 - b_2x_1x - b_2x_0x + b_2 + b_2x_0x_1\\
=(b_0 - b_1x_0 + b_2x_0x_1) + (b_1 - b_2x_0 - b_2x_1)x + b_2x2
$$
donde
$$
a = b_0 - b_1x_0 + b_2x_0x_1\\
a_1 = b_1 - b_2x_0 - b_2x_1\\
a_2 = b_2
$$
Si $x = x_0$ tenemos $b_0 = f(x_0)$
Si $x = x_1$ tenemos:
$$
f(x_1) = b_1+ b_1(x_1 - x_0)\\
b_1 = \frac{f(x_1)-b_0}{x_1 - x_0}\\
b_1 = \frac{f(x_1) - f(x_0)}{x_1 - x_0}
$$
Si $x = x_2$ tenemos:
$$
f(x_2) = b_0 + b_1(x_2 - x_0) + b_2(x_2-x_0)(x_2-x_1)\\
b_2 = \frac{\frac{f(x_2) - f(x_1)}{x_2 - x_1} \frac{f(x_1 - f(x_0))}{x_1 - x_0}}{x_2 - x_0}
$$


## Ejemplo

Ajuste polinomios de primer y segundo grado a los puntos: 

| N°   | $X_n$ | $f(x_n)$            |
| ---- | ----- | ------------------- |
| 1    | 1     | $f(x_0) = 0$        |
| 2    | 4     | $f(x_1) = 1.386294$ |
| 3    | 5     | $f(x_2) = 1.609438$ |
| 4    | 6     | $f(x_3) = 1.791759$ |

Evalúe ambos en x = 2
$$
f_1(x) = 0 + \frac{1.386294 - 0}{4 - 1}(x-1)\\
f_1(x) = 0.462098(x-1)\\
f_1(x) = 0.46209 (2-1) = 0.462098
$$
Para el polinomio de segundo grado:
$$
b = 0\\
b_1 = \frac{1.386294 - 0}{4-1} = 0.462098\\
b_2 = \frac{\frac{1.386294 - 1.386394}{25 - 4} - \frac{1.386294 - 0}{4 - 1}}{5-1}
$$

$$
f_2(x) = 0 + 0.462098(x_1) + (-0.059739) (x-1)(x-4)\\
f_2(x) = 0.462098(x_1) - 0.059730(x-1)(x-4)\\
f_2(x) = 0.462098(2_1) - 0.059739(2-1)(2-4) = 0.581576
$$



## Interpolación de Newton

| i    | $x_i$ | $f(x_i)$ | Primer                                        | Segundo                                          | Tercer                                   |
| ---- | ----- | -------- | --------------------------------------------- | ------------------------------------------------ | ---------------------------------------- |
| 0    | 1     | 0        | $\frac{1.386244 - 0}{4-1} = 0.462098$         |                                                  |                                          |
| 1    | 4     | 1.386244 | $\frac{1.609438 - 1.386244}{5-4} = 0.223144$  | $\frac{0.223144 - 0.462098}{5 - 4} = -0.238954 $ |                                          |
| 2    | 5     | 1.609438 | $\frac{1.791759 - 1.1609438}{6-5} = 0.182321$ | $\frac{0.182332 - 0.223144}{6-5} = -0.040812$    | $\frac{1.791759-1.609438}{6-5}=0.182321$ |
| 3    | 6     | 1.791759 |                                               |                                                  |                                          |





<small>Viernes 24, mayo 2019</small>

## Ejemplo 2

| N°   | Tiempo | f(T) | PRIMERO       | SEGUNDO       | TERCERO          | CUARTO           | QUINTO            |
| ---- | ------ | ---- | ------------- | ------------- | ---------------- | ---------------- | ----------------- |
| 1    | 10     | 5    |               |               |                  |                  |                   |
|      |        |      | 3             |               |                  |                  |                   |
| 2    | 15     | 20   |               | -0.34         |                  |                  |                   |
|      |        |      | -0.4          |               | 0.05466666667    |                  |                   |
| 3    | 20     | 18   |               | 0.48          |                  | -0.002786666667  |                   |
|      |        |      | 4.4           |               | -0.02893333333   |                  | -0.00009857142857 |
| 4    | 25     | 40   |               | -0.2433333333 |                  | 0.001156190476   |                   |
|      |        |      | -0.4666666667 |               | 0.01153333333    |                  | 0.00003784126984  |
| 5    | 40     | 33   |               | 0.1026666667  |                  | -0.0003574603175 |                   |
|      |        |      | 2.1           |               | -0.0009777777778 |                  | 0.00001155555556  |
| 6    | 50     | 54   |               | 0.07333333333 |                  | -0.0008196825397 |                   |
|      |        |      | 3.2           |               | -0.02966666667   |                  |                   |
| 7    | 55     | 70   |               | -0.52         |                  |                  |                   |
|      |        |      | -2            |               |                  |                  |                   |
| 8    | 60     | 60   |               |               |                  |                  |                   |



Diferencias haca adelante
$$
E_2 (t) = 18 + 4.4(t-20)-0.2433333(t-20)(t-25) = 50.36\\
$$
Diferencias hacia atrás
$$
E_2 (t) = 33 - 0.466667(t-40) - 0.243333(t-40)(t-25) = 50.36
$$
