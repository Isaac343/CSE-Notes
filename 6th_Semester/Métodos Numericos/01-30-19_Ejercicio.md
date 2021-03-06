---
layout: note
title: Métodos numéricos - ejercicio
subject: Ḿétodos numericos
---
# Ejercicio
La velocidad de un paracaidista que cae está dada por
$$
V = (gm/c)(1 - e ^{(c/m)t})
$$
donde $g = 9.8 m/s^2​$. Para un paracaidista con coeficiente de arrastre de c = 15 kg/s , calcule la masa $m​$ de modo que la velocidad sea $v = 35 m/s​$ en $t = 9s​$. Utilice el método de la falsa posisición parra determinar $m​$ a un nivel de $E_a = 0.1​$%.

$g = 9.8 m/s^2$, $c = 15 kg/s$, $v=35 m/s$, $t = 9s$, $E_s = 0.1\%$  
$$
 f(x) = \frac{9.8}{15} m (1-e^{-\frac{135}{m}})-35 = 0
$$
*No existe intervalo dado por el problema, tras graficar se determinaron los intervalos 59 y 60.*  

| i  | $X_l$| $X_u$ | $X_r$ | $f(x_l)$ | $f(x_u)$ | $f(x_r)$ | $E_a$ |
| :- | :- | :- | :- | :- | :- | :- | :- |
| 01 | 59 | 60 | 59.841947| -0.364102 | 0.068350 | 0.003888 | - |
| 02 | 59 | 59.841947 | 59.833051| -0.364102 | 0.003888 | -0.003441 | 0.014867 |

Use regla de la falsa posición para determinar el coeficiente de arrastre necesario para que un paracaidista de **80kg** tenga una velocidad de **36m/s** después de **4s** de caída libre. Itere hasta que el error relativo aproximado caída por debajo de **0.01%**.

Aplicada la gratificación a la formula:
$$ (gm/c)(1 - e ^{(c/m)t})-V = 0 ​$$  
Se determinan los valores $X_l =​$ 3.4 y $X_u =​$ 3.5.

$g = 9.8 m/s^2​$, $m = 80 kg​$, $v=36​$ m/s, $t = 4s​$,  $E_s = 0.1\%​$
$$
f(x) = \frac{784}{c}(1-e^{(-\frac{c}{80}) * 4})-36 = 0
$$


| i  | $X_l$| $X_u$ | $X_r$ | $f(x_l)$ | $f(x_u)$ | $f(x_r)$ | $E_a$ |
| :- | :-- | :---  | :- | :- | :- | :- | :- |
| 01 | 3.4 | 3.5 | 3.456109 | 0.049054 | -0.038372 | -0.000035 | - |
| 02 | 3.4 | 3.456109 | 3.456068 | 0.049054 | -0.000035 | -0.0000002 | -0.0011866 |
