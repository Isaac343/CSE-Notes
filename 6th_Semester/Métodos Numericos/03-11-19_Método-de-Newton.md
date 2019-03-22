---
layout: note
title : Método de Newton-Rapson E. no lineales
subject: Ḿétodos numericos
---

<small>Lunes 11, marzo 2019</small>

## Método de Newton-Rapson para sistemas de ecuaciones no lineales

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
f_2 = x^2_1 - 81(x_2 + 0.1)^2 + \sin{x_3} + 1.06\\
f_3 = e^{-x_1x_2} + 20x_3 + \frac{10 \pi - 3}{3}
$$

$$
\frac{\part{f_1}}{\part{x_1}} = 3 \ \ \ \frac{\part{f_1}}{\part{x_2}} = x_3\sin{x_2x_3} \ \ \ \frac{\part{f_1}}{\part{x_3}} = x_2 \sin{x_2x_3} \\
\frac{\part{f_2}}{\part{x_1}} = 2x_1 \ \ \ \frac{\part{f_2}}{\part{x_2}} = -162(x_2 + 0.1) \ \ \ \frac{\part{f_2}}{\part{x_3}} = \cos{x_3} \\
\frac{\part{f_3}}{\part{x_1}} = -x_2 e^{-x_1x_2} \ \ \ \frac{\part{f_3}}{\part{x_2}} = -x_1 e^{-x_1x_2} \ \ \ \frac{\part{f_3}}{\part{x_3}} = 20
$$

Obtenemos
$$
J =
\left(\begin{array}{cc}
3 & x_3\sin{x_2x_3} & x_2\sin{x_2x_3}\\
2x_1 & -162(x_2+0.1) & \cos{x_3}\\
-x_2e^{-x_1x_2} & -x_1e^{-x_1x_2} & 20\\
\end{array}\right)
$$
Se obtiene el sistema:
$$
[J(x) \ Y(x)] = -F(x)
$$
<span style="color:#23f453; font-weight:bold;">Ejercicio 11.</span>

Para obtener el vector Y se debe despejar, siendo así que $J(x)$ pasa a ser su matriz inversa. (*Si la matriz Jacobiana tiene inversa o el determinante es distinto de 0, entonces el sistema SI tiene solución*).
$$
\begin{bmatrix}
3 & x_3\sin{x_2x_3} & x_2\sin{x_2x_3}\\
2x_1 & -162(x_2+0.1) & \cos{x_3}\\
-x_2e^{-x_1x_2} & -x_1e^{-x_1x_2} & 20\\
\end{bmatrix}
\begin{bmatrix}
Y_1\\ Y_2 \\ Y_3
\end{bmatrix}
=
\begin{bmatrix}
3x_1 - cos(x_2 x_1) - \frac{1}{2} \\
x^2_1 - 81(x_2 + 0.1)^2 + \sin{x_3} + 1.06\\
e^{-x_1x_2} + 20x_3 + \frac{10 \pi - 3}{3}\\
\end{bmatrix}
$$


Se hace uso del vector incial $X = [\ 0.1, 0.1, -0.1\ ]​$

Primera iteración:
$$
\begin{bmatrix}
3 & 0.001 & 0.001\\
0.2 & -32.4 & 0. 995004\\
-0.099005 & -0.099005 & 20\\
\end{bmatrix}
\begin{bmatrix}
Y_1\\ Y_2 \\ Y_3
\end{bmatrix}
=
\begin{bmatrix}
1.199950\\ 2.269833\\ -8.462025
\end{bmatrix}
$$
Se obtienen los valores 1.199950, 2.269833, -8.462025 como los resultados de la primer iteración. Al solucionar el sistema se obtiene que $Y_1 = 0.39987$, $Y_2 = -0.08053$, $Y_3 = -0.42152$. Se procede a actualizar los valores de $X$

$X_1 = X_1 + Y_1 \ \rightarrow \ 0.1 + 0.39987 = 0.49987\\ X_2 = X_2 + Y_2 \ \rightarrow 0.1 + -0.08054 = 0.019467 \\ X_3 = X_3+ Y_3 \ \rightarrow -0.1 + -0.42152 = -0.52152​$

*El proceso puede resumirse en despeje, sustitución del vector en la matriz, creación del sistema, actualización de vector.*

 <small>Viernes 25, marzo 2019</small>

<span style="color:#23f453; font-weight:bold;">Ejercicio 12.</span>

Resolver el sistema de ecuaciones no lineales:
$$
[x_1 + \cos{x_1x_2x_3} - 1]^{1/2} = 0\\
(1-x_1)^{1/4} + x_2 + x_3 (0.05x_3 - 0.15) = 1 \\
1 + x_1^2 + 0.1 x_2^2 - 0.01x_2 - x_3 = 1
$$
