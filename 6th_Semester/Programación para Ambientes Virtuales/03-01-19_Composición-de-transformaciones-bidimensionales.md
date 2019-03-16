---
title: Composición de transformaciones bidimensionales
date: 03-01-19
subject: Programacíon para Ambientes Virtuales
---


# Traslaciones, rotaciones y escalaciones

## Composición de transformaciones bidimensionales

Si 2 vectores de traslación sucesivos 
$$
(t_{1x}, t_{1y}) y (t_{2x}, t_{2y})
$$
Son aplicados a un posición de coordenadas $P$, y se obtiene $P'$, y es igual a la traslación de 

$P' = T(t_{2x}, t_{2y}) * T(t_{x1}, t_{1y}) * P$

$P' = T(t_{2x}, t_{2y}) * T(t_{1x}, t_{1y}) * P$

 Donde $P$ y $P'$ son representadas como columnas de coordenadas homogéneas de 3 elementos. Este resultado se puede verificar calculando la matriz producto para los 2 grupos asociativos. Ademas la matriz de transformación compuesta para esta secuencia de traslación es:
$$
\left(\begin{array}{cc}
1 & 0 & t_{2x}\\
0 & 1 & t_{2y}\\
0 & 0 & 1\\
\end{array}\right)
* 
\left(\begin{array}{cc}
1 & 0 & t_{1x}\\
0 & 1 & t_{2x}\\
0 & 0 & 1\\
\end{array}\right)
=
\left(\begin{array}{cc}
1 & 0 & t_{1x} + t_{2x}\\
0 & 1 & t_{1y} + t_{2y}\\
0 & 0 & 1\\
\end{array}\right)
$$

o bien, pude representarse como:
$$
T(t_{2x}, t_{2y}) * T(1_{1x}, t_{1y}) = T(t_{1x} + t_{2x}, t_{1y} + t_{2y})
$$

## Composición de rotación bidimensional

Dos sucesiones sucesivas aplicadas a un punto $P$, producen la rotación transformada como:
$$
P' = R(\theta_2)* \{R(\theta_1)*P\}
$$
Al multiplicar las 2 matrices de rotación se puede verificar que las 2 rotaciones sucesivas son aditivas. 

Dado que son aditivas, para que las coordenadas rotales finales de un punto puedan ser calculadas con la matriz de rotación compuesta, como:
$$
P' = R(\theta_1 + \theta_2) * P
$$

## Composición de escalación bidimensional

La concatenación de matrices para 2 transformaciones de escalación sucesivas produce las siguiente matriz de escalación compuesta:
$$
\left(\begin{array}{cc}
S_{2x} & 0 & 0\\
0 & S_{2y} & 0\\
0 & 0 & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
S_{1x} & 0 & 0\\
0 & S_{1y} & 0\\
0 & 0 & 1\\
\end{array}\right)
= 
\left(\begin{array}{cc}
S_{2x}*S_{1x} & 0 & 0\\
0 & S_{2y} * S_{1y} & 0\\
0 & 0 & 1\\
\end{array}\right)
$$
La resultante de esta matriz muestra que las matrices de escala sucesiva son multiplicativas. 



## Rotación de punto de pivote general 

Para aplicar la rotación aun objeto que se encuentra fuera de origen, es necesario primero que el objeto sea trasladado al origen, después se aplica rotación y se regresa el objeto al punto pivote.

La operación matricial es la siguiente:
$$
\left(\begin{array}{cc}
1 & 0 & X_1\\
0 & 1 & X_2\\
0 & 0 & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
\cos{\theta} & -\sin{\theta} & 0\\
\sin{\theta} & \cos{\theta} & 0\\
0 & 0 & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
1 & 0 & -X_1\\
0 & 1 & -X_2\\
0 & 0 & 1\\
\end{array}\right)
$$

$$
= 
\left(\begin{array}{cc}
\cos{\theta} & -\sin{\theta} & -X_1\cos{\theta} + Y_1\sin{\theta} + X_1\\
\sin{\theta} & \cos{\theta} & -X_1\sin{\theta} - Y_1\cos{\theta} + Y_1\\
0 & 0 & 1\\
\end{array}\right)
$$

<small>Martes 5, febrero 2019</small>
$$
\left(\begin{array}{cc}
1 & 0 & x\\
0 & 1 & y\\
0 & 0 & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
S_x & 0 & 0\\
0 & S_y & 0\\
0 & 0 & 1\\
\end{array}\right)
*
\left(\begin{array}{cc}
1 & 0 & -x\\
0 & 1 & -y\\
0 & 0 & 1\\
\end{array}\right)
=
\left(\begin{array}{cc}
S_x & 0 & x(1-S_x)\\
0 & S_y & y(1-S_y)\\
0 & 0 & 1
\end{array}\right)
$$

$$
T(x, y) * S(S_x, S_y) * T(-x, -y) = S(x, y, S_x, S_y)
$$

### Propiedades de concatenación

La multiplicación de  matrices es asociativa. Para tres matrices cualesquiera A, B, C, el producto matricial $(A*B*C)$ se puede llevar a cabo al multiplicar $A*B$ y $A(B*C)$ Por lo tanto podemos evaluar los productos matriciales al usar una agrupación asociativa ya sea de izquierda a derecha o de derecha a izquierda.

Por otro lado, los productos de la transformación tal vez no sean conmutativos en general, el producto matricial $A*B$ no es igual que $B*A$. Esto significa que si queremos trasladar y girar un objeto, debemos ter cuidado del sentido en que se evalúa la matriz compuesta. Para algunos casos especiales, cómo una secuencia de transformaciones, todas de la misma clase, la multiplicación de las matrices de transformación es conmutativa por ejemplo: "*Se podrían realizar dos rotaciones sucesivas en cualquier sentido y la posición final sería la misma*". Esta propiedad conmutativa se aplica también para 2 traslaciones sucesivas o 2 escalaciones sucesivas. Otro par conmutativo de operaciones es la escalación y rotación uniforme.