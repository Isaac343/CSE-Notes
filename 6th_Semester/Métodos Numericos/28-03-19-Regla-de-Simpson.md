---
layout: note
title: Regla de Simpson
date: 28-03-19
subject: Métodos numéricos 	
---

# Regla de Simpson

La regla de Simpson o también llamada regla de Kepler es un método de integración numérica que se utiliza para obtener la aproximación de la integral:
$$
\int^{b}_a f(x) dx = \frac{b-a}{6} \left[ f(a) + 4f(\frac{a+b}{2}) +f(b)\right]
$$

En integración numérica, una forma de aproximar una integral definida en un intervalo [*a*,*b*] es mediante la regla del trapecio, es decir, que sobre cada subintervalo en el que se divide [*a*,*b*] se aproxima *f* por un polinomio de *primer grado*,
para luego calcular la integral como suma de las áreas de los trapecios
formados en esos subintervalos . El método utilizado para la regla de 
Simpson sigue la misma filosofía, pero aproximando los subintervalos de *f* mediante polinomios de segundo grado.

Regla de Simpson 1/3 de aplicación múltiple
$$
I \sim (b-a)\frac{f(x_0) + 4 \sum^{n-1}_{i=1,3,5}f(x_1) + 2\sum^{n-2}_{j=2,4,6}f(x_j)+ f(x_b)}{3n}
$$


## Derivación

$$
\int^{b}_a f(x)dx \sim \frac{b-a}{6}[f(a) + 4f(m + f(b))]
$$

## Regla 3/8

$$
I = (b-a)\frac{f(x_0) + 3(f(x_1)) + 3(f(x_2)) + f(x_4)}{8}
$$


$$
I = \int^b_a f(x)dx \sim \int^b_aP_3 (x)dx \sim 
\frac{3h}{8} \left[ f(x_0) + 3f(x_1) + 3f(x_2) + f(x_3)\right] =
\frac{3h}{8} \left[ f(a) + 3f(\frac{2a+b}{3}) + 3f(\frac{a+2b}{3}) + f(b) \right]
$$

Error
$$
E(f) = \frac{3}{80}h^5 f^{(4)} (\zeta)
$$





<small>04-05-19</small>

La velocidad con la que cae un objeto se calcula con:
$$
v(t) = \sqrt{\frac{gm}{c_d}} \tan{h}(\sqrt{\frac{gC_d}{m}}t)
$$
donde $C_d =$ coeficiente de arrastre de segundo de orden.

Si $g = 9.8 \ ^m/s^{2}$, $m = 68.1$kg, y $C_d = 0.25 \ ^{kg}/m$, determine que tan lejos cae el objeto en 10 segundos: 

​	a) con la regla del trapecio de aplicación múltiple

​	b) con la regla del trapecio de aplicación múltiple 
$$
v(t) = \sqrt{\frac{(9.81)(68.1)}{0.25}} \tan{h(\sqrt{\frac{(9.81)(0.25)}{68.1}}t)}\\
v(t) = 51.693752 \tanh{(0.189771t)}\\
d = \int^{10}_0{51.693752\tanh{(0.189771t)}dt} = 
$$
