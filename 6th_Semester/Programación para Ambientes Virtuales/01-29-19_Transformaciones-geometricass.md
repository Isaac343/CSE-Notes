<small>*Programación para ambientes virtuales - Martes 29, enero 2019  
apunte*</small>  
Se tiene un punto $P=(1,1)$ y se tienen $t_x = 3$, $t_y = 4$.

$$
(x', y', 1) =
\left(\begin{array}{cc}
1 & 1 & 1 \\
\end{array}\right)
\left(\begin{array}{cc}
1 & 0 & 0\\
0 & 1 & 0\\
3 & 4 & 1
\end{array}\right)
$$
$P' = PM_1$

## Rotación
Para realizar la rotación se tiene la siguiente matriz:

$$
(x', y', 1) =
\left(\begin{array}{cc}
x & y & 1\\
\end{array}\right)
\left(\begin{array}{cc}
cos\theta & sen\theta & 0\\
-sen\theta & cos\theta & 0\\
0 & 0 & 1
\end{array}\right)
$$

$x' = xcos \theta - xsen\theta + 0$  
$y' = ysen\theta + ycos\theta + 0$  
$1 = 1$

Con los valores de $P = (3, 3)$ y $\theta = 90$

$$
(x', y', 1) =
\left(\begin{array}{cc}
3 & 3 & 1\\
\end{array}\right) *
\left(\begin{array}{cc}
cos(90) & sen(90) & 0\\
-sen(90) & cos(90) & 0\\
0 & 0 & 1
\end{array}\right)
=
\left(\begin{array}{cc}
-3 & 3 & 1\\
\end{array}\right)
$$

$x' = 0 + (-3) + 0 = -3$  
$y' = 3 + 0 + 0 = 3$  
$1 = 1$  


## Escalación

Cuando se quiere llevar a cabo una operación de escalación con matrices, se lleva  a cabo la siguiente operación:

$$
(x', y', 1) =
\left(\begin{array}{cc}
x & y & 1\\
\end{array}\right) *
\left(\begin{array}{cc}
X_y & 0 & 0\\
0 & Y_y & 0\\
0 & 0 & 1\\
\end{array}\right)
$$
$P' = P*M_s$

Con los valores de $P = (3,3)$, $S_x=3$, $S_y=5$
$$
(x', y', 1) =
\left(\begin{array}{cc}
3 & 3 & 1\\
\end{array}\right) *
\left(\begin{array}{cc}
3 & 0 & 0\\
0 & 5 & 0\\
0 & 0 & 1\\
\end{array}\right)
$$
$x' = 3(3) + 3(0) + 3(0) = 9 + 0 + 0 = 9$  
$y' = 3(0) + 3(5) + 3(0) = 0 + 15 + 0 = 15$  
$1 = 1$  
$P' = (9, 15)$
