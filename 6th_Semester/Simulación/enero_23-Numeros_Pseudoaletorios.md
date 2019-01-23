
# **Unidad II -Número pseudoaleatorios**

Un número pseudoaleatorio es un número generado en un proceso que parece producir números al azar pero no es así realmente.
Las secuencias de números pseudoaleatorios no muestran ningún patrón o irregularidad aparente desde un punto de vista estadístico, a pesar de haber sido generados por un algoritmo completamente determinista, en el que las mismas condiciones iniciales producen siempre el mismo resultado.:
Los mecanismos de generación de números aleatorios que se utilizan en la mayoría de los sistemas informáticos son en realidad procesos pseudoaleatorios.  
Una de las utilidades principales de los números pseudoaleatorios se lleva a cabo en el llamado *Metodo de MonteCarlo*, con múltiples utilidades, por ejemplo para hallar áreas, volúmenes encerrados en un gráfica y cuyas integrales son muy difíciles de hallar o irresolubles; mediante la generación de puntos basados en estos números, podemos hacer una buena aproximación de la superficie, volumen total, encerrándolo en un cuadrado, cubo, aunque no los suficientemente buena.
Así mismo también destacan en el campo de la criptografía. Por ello se sigue investigando en la generación de dichos números empleando por ejemplo medidores de ruido blanco o analizadores atmosféricos, ya que experimentalmente se ha comprobado que tienen una aleatoriedad bastante alta.  

# Métodos de generacion de números pseudoaleatorios
Existen un gran número de metodos para generar los números aleatorios entre 0 y 1.
El método a utilizar, en si mismo no tiene importancia; la importancia radica en los números que genera, ya que estos números deben cumplir ciertas características para que sean validos. Dichas características son:
1. Uniformememnte distribuidos
2. Estadisticamente independientes
3. Su media debe ser estadisticamente igual a 1/2.
4. Su varianza debe ser estadisticamente igual a 1/2.
5. Su periodo o ciclo de vida debe ser largo
