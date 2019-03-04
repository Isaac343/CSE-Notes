<small>*Métodos numericos - Viernes 22, febrero 2019*</small>

# Método de Gauss - Seidel

Conforme un nuevo valor de $x$ se calcula, este se usa inmediatamente en la siguiente ecuación para determinar el otro valor de $x$. De esta forma, si la solución es convergente, se empleara la mejor aproximación disponible.

![](/home/isaac/Documentos/CSE-Notes/6th_Semester/Métodos Numericos/resources/Gauss_Seidel.jpg)

<span style="color:#23f453"> Ejemplo.</span>
$$
15c_1 - 3c_2 - c_3 = 3300
$$

$$
-3c_1 + 18c_2 -6c_3 = 1200
$$

$$
-4c_1 - c_2 + 12c_3 = 2400
$$

Despejando: 
$$
c_1 = \frac{3300 + 3c_2 + c_3}{15}
$$

$$
c_2 = \frac{1200 + 3c_1 + 6c_3}{18}
$$

$$
c_3 = \frac{2400 + 4c_1 + c_2}{12}
$$

| $i$  | $C_1$      | $C_2$      | $C_3$      | $\epsilon_a C_1(\%)$ |
| ---- | ---------- | ---------- | ---------- | -------------------- |
| 0    | 0          | 0          | 0          | -                    |
| 1    | 220        | 103.333333 | 281.944444 | 100                  |
| 2    | 259.462962 | 203.891975 | 303.478652 | 15.20                |
| 3    | 281.010305 | 214.661268 | 311.558541 | 2.22                 |
| 4    | 283.702823 | 217.803318 | 312.717884 | 0.95                 |
| 5    | 284.408523 | 218.307382 | 312.995123 | 0.2                  |



![](/home/isaac/Documentos/CSE-Notes/6th_Semester/Métodos Numericos/resources/Gauss_Seidel_Exercise.jpg)

<small>Lunes 25, febrero 2019</small>

https://docs.google.com/spreadsheets/d/1NfFXnyah1tTMkC2kdGf5kdm6FiiP04M-iub4Fxgvojg/edit#gid=1597546790

## Relajación

Es una ligera modificación al método de Gauss-Seidel para mejorar la convergencia. Después de que se calcula cada nuevo valor de $x$, ese valor se modifica mediante un promedio ponderado de los resultados de las iteraciones anterior y actual: 
$$
X_i^{nuevo} = \lambda X_i^{nuevo} + (1 - \lambda) X_i^{anterior}
$$
Donde $\lambda$ es un factor ponderado con un valor entre 0 y 2.

Si a $\lambda$ se le asigna un valor entre 0 y 1 el resultado es un promedio ponderado de los resultados actuales y anteriores. Esta modificación se conoce como *sub-relajación*. Se emplea comúnmente para hacer que un sistema no convergente, converja o apresure la convergencia al amortiguar sus oscilaciones.

Para valores $\lambda​$ de 1 a 2, se le da una ponderación extra al valor actual. Con esto se pretende mejorar la aproximación al llevarla mas cerca de la solución verdadera. A esta modificación se le llama *sobre-relajación*, y permite acelerar la convergencia de un sistema que ya es convergente.

La elección de un valor adecuado de $\lambda$ es especificado por el problema y se determina en forma empírica.

![](/home/isaac/Documentos/CSE-Notes/6th_Semester/Métodos Numericos/resources/Gauss_Seidel_Exercise_Rel.jpg)

| N°   | $X_1$ | $X_2$ | $X_3$ | $\epsilon_a$ |      |
| ---- | ----- | ----- | ----- | ------------ | ---- |
| 0    | 0     | 0     | 0     | -            |      |





<small>*Miércoles 27, febrero 2019*</small>

<span style='color:#23f453;'>Ejercicio 6.</span>

Use el método de Gauss-Seidel para

a) sin relajación 

b) con relajación($\lambda = 1.2$)

para resolver el siguiente sistema para una tolerancia de $\epsilon_a = 5\%$. Si es necesario, reacomode las ecuaciones para lograr convergencia.
$$
2x_1 - 6x_2 - x_3 = - 38
$$

$$
-3x_1 -x_2 + 7x_3 = -34
$$

$$
-8x_1 + x_2 - 2x_3 = -20
$$

Reacomodando las ecuaciones:
$$
-8x_1 + x_2 - 2x_3 = -20
$$

$$
2x_1 - 6x_2 - x_3 = - 38
$$

$$
-3x_1 -x_2 + 7x_3 = -34
$$

Tras despejar las ecuaciones: 
$$
X_1 = \frac{-20 - X_2 + 2X_3}{-8}
$$

$$
X_2 = \frac{-38 -2X_1 + X_3}{-6}
$$

$$
X_3 = \frac{-34 + 3X_1 + X_2}{7}
$$

Aplicando sobre - relajación

| N°   | $X_1$    | $X_1$ R  | $X_2$    | $X_2$ R  | $X_3$     | $X_3$ R    | $\epsilon_a$ |
| ---- | -------- | -------- | -------- | -------- | --------- | ---------- | ------------ |
| 0    | 0        | 0        | 0        | 0        | 0         | 0          | -            |
| 1    | 2.5      | 3        | 7.333333 | 8.80     | -2.314286 | -2.777193  | 100          |
| 2    | 4.294286 | 4.553143 | 8.313905 | 8.216686 | -1.731984 | -1.5222952 | 43.11        |
| 3    | 3.907824 | 3.778760 | 7.846745 | 7.772757 | -2.127281 | -2.248146  | 20.49        |
| 4    | 4.033631 | 4.084605 | 8.069560 | 8.128920 | -1.945323 | -1.884759  | 7.48         |
| 5    | 3.987305 | 3.967845 | 7.970075 | 7.938396 | -2.022594 | -2.050161  | 2.94         |

Sin relajación

| N°   | $X_1$    | $X_2$    | $X_3$     | $\epsilon_a$ |
| ---- | -------- | -------- | --------- | ------------ |
| 0    | 0        | 0        | 0         | -            |
| 1    | 2.5      | 7.166667 | -2.761905 | 100          |
| 2    | 4.086310 | 8.155754 | -1.940760 | 38           |
| 3    | 4.004659 | 7.991680 | -1.999192 | 2.03         |
| 4    | 3.998758 | 7.999451 | -2.000611 | 0.14         |
| 5    | 4.000084 | 8.000130 | -1.999945 | 0.033        |

