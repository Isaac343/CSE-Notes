---
layout: note
title : Propiedades de los números pseudoaleatorios entre 0 y 1
---
<small>*Simulación - Miércoles 13, febrero 2019  
Apunte*</small>

# Propiedades de los números pseudoaleatorios entre 0 y 1
¿De que manera se puede garantizar que tales números son realmente aleatorios entre 0 y 1?, ¿Cuales son las características que los identifican?, ¿Cuales son sus parámetros?.
La respuestas son muy importantes dado que los números aleatorios serán utilizados en la simulación para generar los valores de cualquier variable aleatoria.

En gran medida, conocer las propiedades que deben tener estos números aleatorios garantiza una buena simulación, por ello, se enumeran a continuación:
1. **Media de los aleatorios entre 0 y 1.**  En vista que estos números deben tener la misma probabilidad de presentarse, es preciso que su comportamiento muestre una distribución de probabilidad uniforme continua, con el límite inferior 0 y el límite superior 1. La función densidad de un distribución uniforme es la siguiente:
$$ f(x) = \frac{1}{b-a} $$
a < x < b, en este caso $a = 0$, y $$b = 1$$ .  
Para tener la media dela distribución se multiplica la función de densidad por $x$, y se integra en todo el rango de la misma distribución de la siguiente manera.
$$
E(x) = \int_a^b f(x)dx = \int_a^b \frac{x}{b-a} = \frac{x^2}{2(b-a)} |^a_b
$$
$$
E(x) = \int_0^1 f(x)dx =\int \frac{x}{1-0}dx = \frac{x²}{2(1-0)} |^1_0
$$

por lo tanto el valor esperado, es decir la media de valores =

2. **Varianza.** Si se parte de la misma distribución uniforme continua se obtiene  la varianza de la distribución:
$$ V(x) = \alpha^2 = E(x^2) - M^2 $$
$$ E(x^2) = \int_a^b \frac{1}{b-a}(x^2) dx = \frac{x^3}{3(a-b)}|^b_a = \frac{(b -a)^3}{3(b -a)} = \frac{(b-a)^2}{3} = \frac{(1-0)^2}{3} = \frac{1}{3} = 0.3333 $$
