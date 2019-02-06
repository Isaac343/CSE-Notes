<small>*Programación para ambientes virtuales - Martes 5, febrero 2019  
Apunte*</small>
# Composición de transformaciones bidimensionales
Para aplicar varias transformaciones a un conjunto de puntos basta con combinar las matrices de transformación en una sola mediante multiplicación matricial.
$$
[M_1][M_2][M_3]...[M_n] = [M_r]  
$$
$$
P' = P * [M_r]
$$

**Ejercicio.**  
Aplicar al punto $P$(4, 5), la traslación $t_x =$ 2, $t_y =$ 3; la escalación $S_x =$ 4, $S_y =$ 4; y la rotación de $\theta =$ 90°.

$$
(M_r) =
\left(\begin{array}{cc}
1 & 0 & d_x\\
0 & 1 & d_y\\
0 & 0 & 1\\
\end{array}\right)
\left(\begin{array}{cc}
cos\theta & sen\theta & 0\\
-sen\theta & cos\theta & 0\\
0 & 0 & 1
\end{array}\right)
\left(\begin{array}{cc}
S_x & 0 & 0\\
0 & S_y & 0\\
0 & 0 & 1\\
\end{array}\right)
$$
aplicación con valores:
$$
\left(\begin{array}{cc}
1 & 0 & 2\\
0 & 1 & 3\\
0 & 0 & 1\\
\end{array}\right)
\left(\begin{array}{cc}
4 & 0 & 0\\
0 & 4 & 0\\
0 & 0 & 1
\end{array}\right)
=
\left(\begin{array}{cc}
4+0+0 & 0+4+0 & 0+0+1\\
0+0+0 & 0+4+0 & 0+0+3\\
0+0+0 & 0+0+0 & 0+0+1\\
\end{array}\right)
=
\left(\begin{array}{cc}
4 & 4 & 1\\
0 & 4 & 3\\
0 & 0 & 1\\
\end{array}\right)
$$

$$
M_r =
\left(\begin{array}{cc}
4 & 4 & 1\\
0 & 4 & 3\\
0 & 0 & 1\\
\end{array}\right)
\left(\begin{array}{cc}
0 & 1 & 0\\
-1 & 0 & 0\\
0 & 0 & 1\\
\end{array}\right)
=
\left(\begin{array}{cc}
-4 & 4 & 1\\
-4 & 0 & 3\\
0 & 0 & 1\\
\end{array}\right)
$$

$$
P' = (4,5) * M_r
$$

$$
P' =
\left(\begin{array}{cc}
4 & 5 & 1\\
\end{array}\right)
\left(\begin{array}{cc}
-4 & 4 & 1\\
-4 & 0 & 3\\
0 & 0 & 1\\
\end{array}\right)
=
\left(\begin{array}{cc}
(-16 + -20 + 0) & (16+0+0) & (4+15+1)\\
\end{array}\right)
$$
$$
P' = \left(\begin{array}{cc}
-36 & 16 & 20\\
\end{array}\right)
$$

## Traslaciones sucesivas

**Ejemplo**  
$P'= P * T_1(t_{x1}, t_{y1})$  
$P'' = P'* T_2(t_{x2}, t_{y2})$  
$P'' = P' * T_2 = P*T_1*T_2$  

$$
T =
\left(\begin{array}{cc}
1 & 0 & 0\\
0 & 1 & 0\\
t_{x1} & t_{y1} & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
1 & 4 & 1\\
0 & 1 & 3\\
t_{x2} & t_{y2} 1\\
\end{array}\right)
=
\left(\begin{array}{cc}
1 & 0 & 0\\
0 & 1 & 0\\
t_{x1}+t_{x2} & t_{y1}+t_{y2} & 1\\
\end{array}\right)
$$
