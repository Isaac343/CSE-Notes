---
layout: note
tittle: Representación matricial de transformaciones tridimensionales
date: 04-12-19
subjec: Programación para ambientes virtuales
---

# Representación matricial de transformaciones tridimensionales

La representación de transformaciones bidimensionales como matrices de 3x3 tienen un equivalente para las transformaciones tridimensionales, las cuales son representadas como matrices de 4x4. Para permitir esto, el punto (x,y,z) sera representado en coordenadas homogéneas como $(w*x,\ w*y,\ w*z,\ w)$, con $w  != 0$. 

Si $w$ diferente de 1, entonces $w$ es dividido entre las primeras 3 coordenadas homogéneas para así obtener el punto cartesiano tridimensional (x, y, z).

Este tipo de sistema es el mas conveniente cuando se piensa en gráficos tridimensionales, ya que se puede dar interpretación natural de aquellos valores de $Z$ que se encuentran muy distantes del observador. Ademas, es mas lógico suponer este tipo de sistema sobre la cara de plano de visualización (display).

**Traslación:** La matriz de traslación tridimensional es una simple extensión de la bidimensional.
$$
(x', y', z', 1) = (x, y, z, 1) = 
\begin{bmatrix}
1 & 0 & 0 & x\\
0 & 1 & 0 & y\\
0 & 0 & 1 & z\\
0 & 0 & 0 & 1\\
\end{bmatrix}
$$
*En el caso de la traslación el vector de la traslación tendrá ahora tres componentes en vez de 2.*

**Escalamiento:** La matriz de escalamiento es similarmente extendida.
$$
S(S_x,\ S_y,\ S_z) = 
\begin{bmatrix}
S_x & 0 & 0 & 0\\
0 & S_y & 0 & 0\\
0 & 0 & S_Z & 0\\
0 & 0 & 0 & 1\\
\end{bmatrix}
$$
*En el caso del escalado hay que considerar 3 factores de escala ( uno por cada eje de coordenada).*



**Rotación:** La rotación bidimensional es una rotación respecto al eje Z
$$
R_z (\theta) = 
\begin{bmatrix}
\cos{\theta} & -\sin{\theta} & 0 & 0\\
\sin{\theta} & \cos{\theta} & 0 & 0\\
0 & 0 & 1 & 0\\
0 & 0 & 0 & 1\\
\end{bmatrix}
$$
*Nota:* Cuando se trata de rotar un punto (y, en general, cualquier objeto en 3D), resulta necesario especificar tanto el ángulo como el eje de rotación. A diferencia de lo que ocurría con las rotaciones 2D, que se limitaban al plano x,y. Es decir el eje de rotación era paralelo al eje Z, la cual corta el plano xy en el llamado punto de rotación. Una rotación en 3D puede usar como eje de rotación cualquier recta del espacio tridimensional lo cual puede o no ser paralela a alguno de los ejes de coordenadas; por lo que el ángulo de rotación se refiere siempre que este sea positivo, indicara rotaciones en el sentido contrario al que siguen las agujas del reloj (se supondrá que siempre se contemple el objeto desde el correspondiente, "semieje positivo"). Por el contrario, valores contrarios al ángulo de rotación indican movimientos en el sentido de las agujas del reloj.

Como resulta evidente, la expresion matricial es equivalente al siguiente sistema de ecuaciones: 
$$
X' = x\cos{\theta} - y\sin{\theta}\\ 
Y' = x\sin{\theta} - y\cos{\theta}\\
Z' = Z
$$
