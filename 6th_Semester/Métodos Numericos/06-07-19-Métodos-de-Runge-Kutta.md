---
layout: note
date: 06-07-19
title: Métodos de Runge Kutta
subject: Métodos numericos 
---

# Métodos de Runge Kutta

Los métodos de *Runge Kutta (RK)* logran la exactitud del procedimiento de la serie de Taylor sin necesitar el cálculo de derivadas de orden superior. Existen muchas variantes, pero todas tiene la forma generalizada de la ecuación:
$$
Y_{i+1} = Y_i + \phi (X_i, Y_i, h)h
$$
Done $\phi (X_i, Y_i, h)$ se conoce como función incremento y se escribe en forma general como: 
$$
\phi = a_1K_1 + a_2K_2 + ... + a_nK_n
$$
Donde las $a$ son constantes  y las $K$ son:
$$
K_1 = f(X_i, Y_i)\\
K_2 = f(X_i + p_1h, Y_i + q_{11}K_1h)\\
K_3 = f(X_i + P_2h, Y_i + q_{22}K_2h)\\
...\\
K_n = f(X_i + P_{n-1}h, Y_i + q_{n-1,1}K_lh+ ... + q_{n-1, n-1}K_{n-1}h)
$$

### Ejemplo -  Runge-Kutta de segundo orden

$$
Y_{i+1} = Y_i + (a_1K_1 + a_2K_2)h
$$

donde: 
$$
K_1 = f(X_i, Y_i)\\
K_2 = f(x_i + p_ih, Y_1+q_{11}K_1h)
$$
Los valores de $a_1, a_2, p_1$ y $p_2$ se evalúan al igualar la ecuación con la expansión en la serie de Taylor el término de segundo orden. 
$$
a_1 +a_2 = 1\\ a_2 p_1 = \frac{1}{2}\\ a_2q_{11} = \frac{1}{2}
$$

por tanto
$$
a_1 = 1-a_2
p_1 = \frac{1}{2a_2}
q_{11} = \frac{1}{2a_2}
$$
Si $a_2 = \frac{1}{2}$ entonces
$$
Y_{i+1} = Y_1 + (\frac{1}{2}K_1 + \frac{1}{2}K_2)h
$$

donde:
$$
K_1 = f(X_i, Y_i)\\
K_2 = f(X_{i+h}, Y_{i+k}, h)
$$

### Ejemplo - Método de Runge-Kutta de cuarto grado(RK4)

$$
Y_{i+1} = Y_i+ \frac{1}{6}(k-1 + 2K_2 + 2K_3 + K_4)h
$$

donde: 
$$
K_1 = f(X_i, Y_i)\\
K_2 = f(X_i + \frac{1}{2}h, Y_i + \frac{1}{2}K_1h)\\
K_3 = f(X_i + \frac{1}{2}h, Y_i + \frac{1}{2}K_2h)\\
K_4 = f(x_i + h, Y_i+K_3h)
$$

Resuelve el problema de valor inicial $\frac{dy}{dx} = 4e^{0.8x} - 0.5y$ en $[0,4]$ con valores iniciales para $x = 0$ y $y = 2$, con un tamaño de paso $h = 1$ 

| i    | X    | Y        | $K_1 = f(X_i, Y_i)$ | $K_2$     | $K_3$    | $k_4$    |      |
| ---- | ---- | -------- | ------------------- | --------- | -------- | -------- | ---- |
| 0    | 0    | 2        | 3                   | 4.217299  | 3.912974 | 5.945677 |      |
| 1    | 1    | 6.201037 | 5.801645            | 23.210417 |          |          |      |
|      |      |          |                     |           |          |          |      |
|      |      |          |                     |           |          |          |      |
|      |      |          |                     |           |          |          |      |
|      |      |          |                     |           |          |          |      |
|      |      |          |                     |           |          |          |      |

$Y_{0+1}= 2 + \frac{1}{6} (3 +2(4.127299) + 2(3.912974) + 5.945677)(1) = 6.201037$

Operaciones

| Operaciones para primer "intervalo"                          | Resultado de K |
| ------------------------------------------------------------ | -------------- |
| $K_1 = f(0,2) = 4e^{0.8(0)} - 0.5(2) = $                     | 3              |
| $K_2 = f(0 + \frac{1}{2}(1), 2+\frac{1}{2}(3)(1) ) = f(0.5, 3.5) = 4e^{0.8(0.5)}-0.5(3.5) = $ | 4.217299       |
| $K_3 = f(0 + \frac{1}{2}(1), 2+\frac{1}{2}(4.217299)(1)) = f(0.5, 4.103650) = 4e^{0.8(0.5)}-0.5(4.183650) = $ | 3.912974       |
| $K_4 = f(0 + 1, 2 + 3.912974(1)) = f(1, 5.912974) = 4e^{0.8(1)}-0.5(5.912974) = $ | 5.945677       |
|                                                              |                |
|                                                              |                |
|                                                              |                |

## Ejemplo. 

Si la resistencia del aire es proporcional al cuadrado de la velocidad instantánea, entonces la velocidad $v$ de una masa $m$ que se deja caer desde cierta altura se determina por:
$$
m \frac{dv}{dt} = mg - kv^2,\ \ \ k>0
$$
Sea $v(0) = 0$, $k = 0.125$, $m = 5 slugs$ y $g = 32$ pies/$s^2$. Use el método de RK4 con $h = 1$ para aproximar la velocidad $v$(5).
$$
5 \frac{dv}{dt} = 5(32) - 0.125v^2\\
\frac{dv}{dt} = \frac{5(32) - 0.125v^2}{5}\\
\frac{dv}{dt} = 32 - 0.025v^2\\
f(t) = 32 - 0.025v^2
$$

| $i$  | $X_i$ | $Y_i$       | $K_1$     | $K_2$     | $K_3$     | $K_4$     |
| ---- | ----- | ----------- | --------- | --------- | --------- | --------- |
| 0    | 0     | 0           | 32.000000 | 25.600000 | 27.904000 | 12.534170 |
| 1    | 1     | 25.25702827 | 16.052063 | 4.305948  | 13.217294 | -5.006837 |
| 2    | 2     | 32.93898006 | 4.875590  | 0.712095  | 4.286029  | -2.642532 |
| 3    | 3     | 34.97719755 | 1.414891  | 0.165156  | 1.270303  | -0.847033 |
| 4    | 4     | 35.55032704 | 0.404356  | 0.043959  | 0.365275  | -0.248261 |
| 5    | 5     | 35.71275425 | 0.114980  | 0.012241  | 0.104050  | -0.071086 |
| 6    | 6     | 35.7588334  | 0.032646  | 0.003455  | 0.029557  | -0.020223 |
| 7    | 7     | 35.77190794 | 0.009265  | 0.000979  | 0.008390  | -0.005743 |
| 8    | 8     | 35.77561787 | 0.002629  | 0.000278  | 0.002381  | -0.001630 |

**Solución analítica**
$$
\frac{dv}{dt} + \frac{1}{40}v^2 = 32\\
L \{ \frac{dv}{dt} + \frac{1}{40}v^2\} = L \{32\}\\
SV(s) - v(0) + \frac{1}{40} V^2(s) = \frac{32}{S}\\
SV(s) - 0 + \frac{1}{40}V(s) = \frac{32}{S}\\
V(s)(\frac{1}{40}V(s)+S)  = \frac{32}{S}
$$

