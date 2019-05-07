---
layout: note
title: Diferenciación numérica 
date: 05-06-19
subject: Métodos numéricos
---

# Diferenciación Numérica 

## Serie de Taylor 

$$
V(t_{i+1}) = v(t_i) + v'(t_i)(t_{i+1} - t_i) + \frac{v''(t_i)}{2!}(t_{i+1-t_i})^2 + ... + R_n
$$

Tras truncar: 
$$
v(t_{i+1}) = v(t_i) + v'(t_i)(t_{i+1}-t_i)+R_i
$$
Al despejar el término deseado: 
$$
v'(t_i) = \frac{v(t_{i+1}-v(t_i))}{t_{i+1}-t_i}- \frac{R_i}{t_{i+1}-t_i}
$$
$v'(t_i)$ = aproximación del primer valor - error de truncamiento 

*Diferencias divididas finitas*

### Diferencias divididas

$$
f'(x_i) = \frac{f(x_{i+1} - f(x_i))}{x_{i+1}-x_i} + O(x_{i+1}-x_i)
$$

La notación $O$ permite conocer el orden del error que se obtiene. A mayor potencia en el error, mas pequeño se vuelve este.
$$
f'(x_i) = \frac{\Delta f_i}{h} + O(h)
$$

## Ejercicio.

Calcule la aproximación de la primera derivada de la función en el punto indicado.

$ f(x) = x\cos{x} - x^2 \sin{x}​$ en $x = 3​$

| i    | $x_i$ | $f(x_i)$  |
| ---- | ----- | --------- |
| 1    | 2.8   | -5.264530 |
| 2    | 2.9   | -4.827866 |
| 3    | 3     | -4.240058 |
| 4    | 3.1   | -3.496909 |
| 5    | 3.2   | -2.596792 |
|      |       |           |

**Diferencias hacia adelante** $f'(x_i) = \frac{x_{i+1} - x_i}{h}​$
$$
f'(3) = \frac{-3.496909 - (-4.240058)}{0.1} = 7.431490
$$
**Diferencias hacia atrás** $f'(x_i) = \frac{x_{i-1} - x_i}{h}​$
$$
f'(3) = \frac{-4.230058 - (-4.827866)}{0.1} = 5.878080
$$
**Diferencias centradas** $f'(x_i) = \frac{x_{i+1} - x_{i-1}}{h}​$
$$
f'(3) = \frac{-3.496909 - (-4.827866)}{0.1} = 6.654785
$$
**Derivada exacta**
$$
f'(x) = -x\sin{x}+\cos{x}-(x^2\cos{x} + 2\sin{x})\\
= -x \sin{x} + \cos{x} - x^2 \cos{x} - 2x\sin{x}\\
= \cos{x} - 3x\sin{x}-x^2 \cos{x}\\
f'(3) = 6.649860
$$


## Ejercicio. 

$f(x) = (\cos{3x})^2 -e^{2x}$ en $x= -2.3$ con h= 0.1

| i    | $x_i$ | $f(x_i)$ |
| ---- | ----- | -------- |
| 1    | -2.1  | 0.984722 |
| 2    | -2.2  | 0.890665 |
| 3    | -2.3  | 0.655356 |
| 4    | -2.4  | 0.361862 |
| 5    | -2.5  | 0.113418 |
|      |       |          |



-  **Diferencias hacia adelante** $f'(x_i) = \frac{-f(x_{i+2}) + 4f(x_{i+1}) - 3f x_i}{2h}​$
   $$
   f(-2.3) = \frac{-(0.984722) + 4(0.890665) - 3(0.655356)}{2(0.1)} = 3.059350
   $$
   

-  **Diferencias hacia atrás** $f'(x_i) = \frac{3f(x_i) - 4f(x_{i-1}) + f(x_{i-2})}{2h}$
   $$
   f(-2.3) = \frac{3(0.655356) - 4(0.361862) + (0.113418)}{2(0.1)} = 3.160190
   $$
   

-  **Diferencias centralizadas** $f'(x_i) = \frac{-f(x_{i+2}) + 8(x_{i+1}) - 8(x_{i-1}) + f(x_{i-2})}{12h}$
   $$
   f(-2.3) = \frac{-(0.984722) + 8(0.890665) - 8(0.361862) + (0.113418)}{12(0.1)} =2.799267
   $$
   

-  **Derivada exacta**
   $$
   f'(x) = 2\cos{3x} (-3\sin{3x}) -2e^{2x}\\
   = -6 \cos{3x} \sin{3x} - 2e^{2x}\\
   f'(-2.3) = 2.810983
   $$
   