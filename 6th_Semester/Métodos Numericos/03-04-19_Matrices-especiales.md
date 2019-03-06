---
layout: note
title: Matrices especiales
subject: Ḿétodos numericos
---
# Matrices especiales

una matriz a bandas en la que todos sus elementos son 0 con excepción de una banda centrada sobre la diagonal principal.

Las dimensiones de un sistema a bandas se cuantifica mediante 2 parámetros: el ancho de banda (*BW*) y el ancho de media banda(*HBW*). Estos 2 valores se relacionan mediante

$$
\left(\begin{array}{cc}
BW & HBW & 0\\
HBW & BW & HBW\\
0 & HBW & BW\\
\end{array}\right)
$$

<span style="color:#23f453; font-weight:bold;">Ejemplo.</span>

$$
\left(\begin{array}{cc}
8 & -2 & -1 & 0 & 0\\
-2 & 9 & -4 & -1 & 0\\
-1 & -3 & 7 & -1 & -2\\
0 & -4 & -2 & 12 & -5\\
0 & 0 & -7 & -3 & 15\\
\end{array}\right)
\left(\begin{array}{cc}
x_1\\ x_2\\ x_3\\ x_4\\ x_5\\
\end{array}\right)
=
\left(\begin{array}{cc}
5\\ 2\\ 1\\ 1\\ 5\\
\end{array}\right)
$$

<span style="color:#23f453; font-weight:bold;">Ejercicio 7.</span> Resolver el sistema anterior con una tolerancia $\epsilon = 3\%$

$X_1 = \frac{5+ 2X_2 + X_3}{8}$, $X_2 = \frac{2 + 2X_1 + 4X_3 + X_4}{9}$, $X_3 = \frac{1+X_1 + 3X_2 + X_4 + 2X_5}{7}$, $X_4 = \frac{1 + 4X_2 + 2X_3 + 5X_5}{12}$, $X_5 = \frac{5 + 7X_3 +3X_4}{15}$

| N°   | $X_1$    | $X_2$    | $X_3$    | $X_4$    | $X_5$    | $\epsilon_a X_1$ |
| ---- | -------- | -------- | -------- | -------- | -------- | ---------------- |
| 0    | 0        | 0        | 0        | 0        | 0        | -                |
| 1    | 0.62500  | 0.361111 | 0.386905 | 0.268188 | 0.567526 | 100              |
| 2    | 0.763641 | 0.593677 | 0.706844 | 0.635502 | 0.790295 | 18.16            |
| 3    | 0.861775 | 0.798492 | 0.924763 | 0.832914 | 0.931472 | 11.39            |
| 4    | 0.940218 | 0.934712 | 1.062887 | 0.960165 | 0.931472 | 5.18             |
| 5    | 0.991539 | 1.021644 | 1.151342 | 1.041347 | 1.078896 | 3.20             |
| 6    | 1.024329 | 1.077264 | 1.207894 | 1.093277 | 1.115673 | 3.20             |
| 7    | 1.045303 | 1.112829 | 1.244059 | 1.126483 | 1.139191 | 2.01             |
