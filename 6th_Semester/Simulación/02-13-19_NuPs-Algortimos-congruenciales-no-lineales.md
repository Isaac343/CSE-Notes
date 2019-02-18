<small>*Miércoles 13, febrero 2019  
Apunte* </small>
# Algoritmos congrueniasles no lineales
## Algoritmo conguruencial cuadrático
Este algoritmo posee la siguiente formula
$$ X_{i+1} = (a{X^2}_i + bX_i + c)mod(m) $$
$$ i = 0, 1, 2, 3, ..., N $$
En este caso los numeors $m = 2^g$ pueden ser generados con la ecuación
$$ r_i = \frac{X_i}{m-1} $$
De acuerdo con *L'Ecuyer* las condiciones deben cumplir los parámetros m, a, c, g para alcanzar un periodo máximo de $N = m$, dichos parámetros son:
$m = 2^g$  
$a$ debe ser un número par  
$c$ debe ser un número impar  
$g$ debe ser entero  
$(b - 1)mod4 = 1$  
De esta manera se logra un periodo de vida máximo $N = m$.

Generar, a partir del algoritmo congruencial cuadrático, suficientes números enteros hasta alcázar el periodo de vida máximo del algoritmo, para esto considere los parámetros $X_13$, $m = 8$, $a = 26$, $b = 27$ y $c = 27$.

| N° | $X_{i+1} = (a{X^2}_i + bX_i + c)mod(m)$| $r_i = \frac{X_i}{m-1} |
| :- | :- | :- |
| 01 | $X_1 = ((26 * 13^2)+(27*13)+27)mod(8)*8 = 4$ | $r_1 = \frac{4}{7} = 0.5714$ |
| 02 | $X_2 = ((26 * 4^2)+(27*4)+27)mod(8)*8 = 7$ | $r_2 = \frac{7}{7} = 1$ |
| 03 | $X_3 = ((26 * 7^2)+(27*7)+27)mod(8)*8 = 2$ | $r_3 = \frac{2}{7} = 0.2857$ |
| 04 | $X_4 = ((26 * 2^2)+(27*2)+27)mod(8)*8 = 1$ | $r_4 = \frac{1}{7} = 0.1428$ |
| 05 | $X_5 = ((26 * 1^2)+(27*1)+27)mod(8)*8 = 0$ | $r_5 = \frac{0}{7} = 0$ |
| 06 | $X_6 = ((26 * 0^2)+ 27*0)+27)mod(8)*8 = 3$ | $r_6 = \frac{3}{7} = 0.4285$ |
| 07 | $X_7 = ((26 * 3^2)+ 27*3)+27)mod(8)*8 = 6$ | $r_7 = \frac{6}{7} = 0.8571$ |
| 08 | $X_8 = ((26 * 6^2)+ 27*6)+27)mod(8)*8 = 5$ | $r_8 = \frac{5}{7} = 0.7142$ |
| 09 | $X_9 = ((26 * 5^2)+ 27*5)+27)mod(8)*8 = 4$ | $r_9 = \frac{4}{7} = 0.5714$ |

## Algoritmo de Blum, Blum y Shub
Si en el algoritmo conguruencial cuadrático $a = 1$, $b = 0$ y $c = 0$ entonces se construye una nueva ecuación recursiva:
$$
X_{i+1} = ({X^2}_i)mod(m)
$$
$$
i = 0, 1, 2, 3, ..., n
$$
Esta ecuación fue propuesta por *Blum, Blum y Shub* como un nuevo método para generar números que no tienen un comportamiento predecible.
 
