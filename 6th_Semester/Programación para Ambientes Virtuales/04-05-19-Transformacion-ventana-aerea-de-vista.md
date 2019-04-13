---
layout: note
title: Transformación ventana aérea de vista
subject: Programación para ambientes virtuales
---

# Transformación ventana aérea de vista

Dadas las primitivas de salida especificadas en coordenadas del mundo, debe especificarse como llevar dichas coordenadas a coordenadas de pantalla para que puedan ser mostradas. Se debe especificar una región rectangular (ventana) en coordenadas del mundo y una correspondiente región rectángula en coordenadas de la pantalla (viewport), en el cual se efectuara el mapeo de la ventana del mundo. (*La ventana es una fracción del plano "mundo". Tanto el mundo como la pantalla tienen coordenadas, pero estas no coinciden entre si.*).

La ventana en coordenadas del mundo y el viewport en coordenadas de pantalla determinan el mapeo que es aplicado en coordenadas del mundo.

Dados: 

-  La ventana(en coordenadas de mundo).
-  El viewport

La matriz de transformación que mapea la ventana en coordenadas de pantalla puede ser desarrollada mediante la composición de tres transformaciones simples. sugeridas en la figura siguiente. 

Pasos para transformar una ventana en coordenadas de mundo al viewport en coordenadas de pantalla:

1. Como se puede apreciar en lo anterior, la ventana, especificada por su esquina inferior izquierda y su esquina superior derecha es primero trasladada al origen de las coordenadas del mundo. 
2. La ventana es escalada para coincidir con las dimensiones del viewport.
3. Se utiliza una traslación para posicionar el viewport. La matriz que corresponde a estas transformaciones es:

$$
M_{wv} = T(U_{min}, V_{min}) * S
\left[ \frac{U_{max} * V_{mix}}{X_{max}-X_{min}} * \frac{V_{max}*V_{min}}{Y_{max}-Y_{min}}\right]
* T(-X_{min} - Y_{min})\\
= 
\begin{bmatrix}
1 & 0  & U_{min}\\
0 & 1 & V_{min}\\
0 & 0 & 1
\end{bmatrix} 
* 
\begin{bmatrix}
\frac{U_{max}-U_{min}}{X_{max}-X_{min}} & 0 & 0\\
0 & \frac{V_{max}-V_{min}}{Y_{max}-Y_{min}} & 0\\
0 & 0 & 1
\end{bmatrix}
*
\begin{bmatrix}
1 & 0 & -X_{min}\\
0 & 1 & -Y_{min}\\
0 & 0 & 1
\end{bmatrix}
$$

La transformación ventana - viewport también puede combinarse con rutinas de recorte en relación con el tamaño de la ventana (clipping). 

Las primitivas de salida en coordenadas del mundo son recortadas en relación al marco de la ventana.