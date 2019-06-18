---
layot: note
date: 06-03-19
title: Solución de ecuaciones diferenciales
subject: Métodos Numéricos
---

# Solución de ecuaciones diferenciales

## Métodos de Runge-Kutta

Solucionar ecuaciones con diferenciales ordinarias de la forma 
$$
\frac{dy}{dx} = f(x,y)
$$
La forma general para dar solución a estas ecuaciones es: Nuevo valor = valor anterior + pendiente * tamaño de paso
$$
Y_{i+1} = Y_i + \phi h
$$
La pendiente estimada $\phi$ se usa para extrapolar desde un valor anterior $Y_i$ a un nuevo valor $Y_{i+1}$ en una distancia $h$. Esta formula se aplica paso a paso para calcular un valor posterior y, por lo tanto, parra trazar la trayectoria de la solución.

**add image**

## Método de Euler

La primera derivada ofrece una estimación directa de la pendiente en $X_i$: 

$\phi = f(x_i, y_i)$ donde $f(x_i, y_i)$ es la ecuación diferencial evaluada en $x_i$ y $y_i$. 

Al sustituir se tiene $Y_{i+1}$

Esta formula se conoce como *Método de Euler*, de Euler-Caochy o de punto pendiente. Se predice un nuevo calor de Y usando la pendiente (igual a la primera derivada en el valor original de x), Para extrapolar linealmente sobre el tamaño de paso h.

**Ejemplo.** Resuelve la ecuación diferencial:
$$
\frac{dy}{dx} = 2x^3 + 12x^2 - 20x +18.5
$$
desde $x = 0$ hasta $x=4$ con $h=0.5$

La condición inicial en $x=0$ es $y=1$

| i    | $X_i$ | $Y_i$                             | $f(X_i, Y_i)$                         |
| ---- | ----- | --------------------------------- | ------------------------------------- |
| 0    | 0     | 1                                 | $f(x_i.y_i) = f(0, 1)= 8.5$           |
| 1    | 0.5   | $Y_1 = 1 +8.5 * 0.5 = 5.25$       | $f(x_i, y_i) = f(0.5, 5.25) = 1.25$   |
| 2    | 1     | $Y_2 = 5.25 + 1.25 * 0.5 = 5.875$ | $f(x_i, y_i) = f(1, 5.875) = -1.5$    |
| 3    | 1.5   | $Y_3 = 5.875 - 1.5 * 0.5 = 5.125$ | $f(x_i, y_i) = f(1.5, 5.129) = $-1.25 |
| 4    | 2     | $Y_4 = 5.125 -1.25 * 0.5 = 4.5$   | $f(x_i, Y_i) = f(2, 4.5)$ = 0.5       |



**Ejercicio** Considere el problema con valores iniciales $y' = 0.1\sqrt{y} + 0.4x^2$ y  $y(2) = (4)$. Utilice el método de Euler para obtener una aproximación de $y(2.5)$ usando primero $h = 0.1$ y después $h=0.05$.

| i    | $X_i$ | $Y_i$ | $f(x_i, Y_i)$ |
| ---- | ----- | ----- | ------------- |
| 0    | 2     |       |               |
| 1    |       |       |               |
| 2    |       |       |               |
| 3    |       |       |               |
| 4    |       |       |               |
| 5    |       |       |               |
| 6    |       |       |               |
| 7    |       |       |               |
| 8    |       |       |               |
| 9    |       |       |               |

