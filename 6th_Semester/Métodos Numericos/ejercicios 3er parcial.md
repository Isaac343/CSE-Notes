---
layout: notes
title: Ejercicios tercer parcial métodos numéricos
date: 14-12-19
subject: Métodos numéricos
---



# Integración - Distribución normal de probabilidad  12/04

```python
import math

miu, sigma, odds, pairs = 0, 1, 0, 0

intervalos = int(input('Número de intervalos para Simpson 1/3: '))
sup_lim = float(input('limite superior: '))
inf_lim = -3.4 #float(input('limite inferior: '))

intervalos_array, functions_array = [], []

h = (sup_lim - inf_lim)/(intervalos)
round(h, 6)
print(h)
b = 0
intervalos_array.append(inf_lim)
for a in range(0, intervalos-1):
    b = b + h
    data = inf_lim + b
    intervalos_array.append(data)
intervalos_array.append(sup_lim)

for z in range (0, intervalos+1):
    fun_value = ((1)/(sigma * (math.sqrt(2 * math.pi)))) * (math.e ** (-(intervalos_array[z]-miu)**2 / (2 * (sigma**2))) )
    functions_array.append(fun_value)

for d in range(1, intervalos):
    if d%2 != 0:
        odds = odds + functions_array[d]
    elif d%2 == 0:
        pairs =pairs + functions_array[d]

result = (sup_lim - inf_lim)*((functions_array[0] + (4*odds) + (2*pairs) + functions_array[intervalos])/(3*intervalos))
for h in range(intervalos+1):
    print("%i | %.6f | %.6f" % (h, intervalos_array[h], functions_array[h]))
print("%.6f" % (result))
complemento =  1 - result
print("%.6f" % (complemento))
```

# Distribución Chi cuadrada

```python
import math

v = int(input('Valor de "v": '))# grados de libertad (n-1)
x, odds, pairs = 0, 0, 0

intervalos =int(input('Número de intervalos para Simpson 1/3: '))
sup_lim = float(input('Límite superior: '))
inf_lim = float(input('Limite inferior: '))

intervalos_array, functions_array = [], []

h = (sup_lim - inf_lim) / intervalos
round(h, 6)
print(h)
b = 0
intervalos_array.append(inf_lim)
for a in range(0, intervalos-1):
    b = b + h
    data = inf_lim + b
    intervalos_array.append(data)
intervalos_array.append(sup_lim)

for c in range(0, intervalos+1):
    fun_value = ((1) / (2**(v/2) * math.gamma(v/2))) * (intervalos_array[c]**((v/2)-1)) * (math.e**(-intervalos_array[c]/2))
    functions_array.append(fun_value)

for d in range(1, intervalos):
    if d%2 != 0:
        odds = odds + functions_array[d]
    elif d%2 == 0:
        pairs =pairs + functions_array[d]

result = (sup_lim - inf_lim)*((functions_array[0] + (4*odds) + (2*pairs) + functions_array[intervalos])/ (3*intervalos))

for h in range(intervalos+1):
    print("%i | %.6f | %.6f" % (h, intervalos_array[h], functions_array[h]))
print("%.6f" % (result))

```



# Series de Taylor diferenciación numérica I

 Ejercicio.

Calcule la aproximación de la primera derivada de la función en el punto indicado.

$ f(x) = x\cos{x} - x^2 \sin{x}$ en $x = 3$

| i    | $x_i$ | $f(x_i)$  |
| ---- | ----- | --------- |
| 1    | 2.8   | -5.264530 |
| 2    | 2.9   | -4.827866 |
| 3    | 3     | -4.240058 |
| 4    | 3.1   | -3.496909 |
| 5    | 3.2   | -2.596792 |
|      |       |           |

**Diferencias hacia adelante** $f'(x_i) = \frac{x_{i+1} - x_i}{h}$
$$
f'(3) = \frac{-3.496909 - (-4.240058)}{0.1} = 7.431490
$$
**Diferencias hacia atrás** $f'(x_i) = \frac{x_{i-1} - x_i}{h}$
$$
f'(3) = \frac{-4.230058 - (-4.827866)}{0.1} = 5.878080
$$
**Diferencias centradas** $f'(x_i) = \frac{x_{i+1} - x_{i-1}}{h}$
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

# Series de Taylor diferenciación numérica II

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



-  **Diferencias hacia adelante** $f'(x_i) = \frac{-f(x_{i+2}) + 4f(x_{i+1}) - 3f x_i}{2h}$
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

