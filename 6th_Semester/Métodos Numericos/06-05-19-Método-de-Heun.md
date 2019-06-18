---
layout: note
date: 06-05-19
title: Método de Heun
---

# Método de Heun

Un método para mejorar la estimación de la pendiente empela la determinación de dos derivadas en el intervalo (una en el punto inicial y otra en el final). Las dos derivadas se promedian después con la finalidad de obtener una mejor estimación de la pendiente en todo el intervalo, se expresan como:

Predictor: $Y_{i+1}^0 = Y_i + f(X_i, Y_i)h$

Corrector:$Y_{i+1} = Y_i + \frac{f(X_i, Y_i ) + f(X_{i+1}, Y_{i+1}^0)}{2}h$

**Ejemplo:** resuelve el PVI 

$Y' = 4e^{0.8x} - 0.5y$ en $[0, 4]$, con un tamaño de paso $h=0.5$, con condiciones iniciales de $x=0$, $y=2$

| i    | $X_i$ | $Y_i$    | $f(X_i, Y_i)$ | $Y_{i+1}^0$      | $f(X_{i+1}, Y_{i+1})^0$                   | $Y_{i+1}$ |
| ---- | ----- | -------- | ------------- | ---------------- | ----------------------------------------- | --------- |
| 0    | 0     | 2        | 3             | 2 + 3 (0.5) =3.5 | $4e^{0.8 * 0.5} -0.5(3.5) = 4.217299$     |           |
| 1    | 0.5   | 3.804325 | 4.065136      | 5.836893         | $4e^{0.8*1} - 0.5(5.836893) = 5.983717$   |           |
| 2    | 1.0   | 6.316538 | 5.743895      | 9.188486         | $4e^{0.8*1.5} - 0.5(9.188486) = 8.686225$ |           |
| 3    | 1.5   | 9.924068 | 8.318434      | 14.083285        | 12.770487                                 |           |
| 4    | 2.0   |          |               |                  |                                           |           |

