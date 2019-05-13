---
layout: note
title: Variables aleatorias
subject: Simulación
date: 04-29-2019
---

# Definición variables aleatorias

Un modelo de simulación permite lograr una mejor entendimiento de prácticamente cualquier sistema. Para ello, resulta indispensable la mejor aproximación a la realidad, lo cual se consigue componiendo el modelo con base en variables aleatorias que interactuen entre si; pero ¿Cómo podemos determinar que tipo distribución tiene una variable aleatoria?, ¿Cómo podemos usarla en el modelo una vez que conocemos su distribución asociada?.

Podemos decir que las variables aleatorias son las que tienen un comportamiento probabilista en la realidad. Por ejemplo, el número de clientes que llegan a cada hora a un banco depende del momento del día, del día de la semana y de otros factores: por lo general la afluencia de clientes sera mayor al medio día que muy temprano por la mañana; la demanda sera mas alta el viernes que el miércoles; habrá mas clientes en un día de pago que en un día normal. Debido a estas características las variables aleatorias debe cumplir reglas de distribución de probabilidad como estas: 

-  La suma de las probabilidades asociadas a todos los valores posibles de la variable $x$ es 1.
-  La probabilidad que un solo valor de las variables $x$ se presenten siempre es mayor o igual que 0.
-  El valor esperado de la distribución de la variable aleatoria es la media de la misma, la cual a su vez estima la verdadera media de la población. 
-  Si la distribución de probabilidad asociada a una variable esta definida por mas de un parámetro, dichos parámetros pueden obtenerse mediante un estimador no sesgado. 

## Tipos de variables aleatorias

Podemos diferenciar las variables aleatorias con el tipo de valores aleatorios que representan. Por ejemplo, si habláramos del número de clientes que solicitan cierto servicio en un periodo de tiempo determinado podríamos encontrar valores tales como 0, 1, 2, ..., n, es decir, un comportamiento como el que prestan las distribuciones de probabilidad completas. Por otro lado, si habláramos del tiempo que tarada ene ser atendida una persona, nuestra investigación tal vez arrojaría resultados como 1.54 minutos, 0.028 horas, 1.37 días, es decir un comportamiento similar al de las distribuciones de probabilidad continuas. Si consideramos lo anterior podemos diferenciar entre variables aleatorias discretas y las continuas.  

### Variables aleatorias discretas

Este tipo de variables debe de cumplir con estos parámetros.


$$
P(x) = \sum_{i = 0}^{\infty} P_i = 1 \\
p(a \leq x \leq b) = \sum_{i = a}^{b} P_1 = P_a + ... + P_b
$$
algunas distribuciones discretas de probabilidad son la uniforme discreta, Bernoulli, la Hipergeometrica, Poisson, y Binominal. Podemos asociar a estas u otras distribuciones de probabilidad el comportamiento de una variable aleatoria. Por ejemplo, si nuestro propósito al analizar un muestreo de calidad consiste en decidir si a pieza bajo inspección es útil o no, estamos realizando un experimento con 2 posibles resultados: la pieza es buena o es mala. Este tipo de comportamiento esta asociado a un a distribución de Bernoulli. Por otro lado, si lo que queremos es modelar el número de usuarios que llamaran a un teléfono de atención a clientes, el tipos de comportamiento puede llegar  a parecerse a una distribución de Poisson. Incluso podría ocurrir que el comportamiento de la variable no se pareciera a otras distribuciones de probabilidad conocidas. Si este fuera el caso es perfectamente valido usar una distribución empírica que se ajuste a las condiciones reales de probabilidad. Esta distribución puede ser una ecuación o una suma de términos que cumpla con las condiciones necesarias para ser considerada una distribución de probabilidad. 

<small>Martes 30, Abril 2019</small>

## Variables aleatorias continuas 

Este tipo de variables se representan mediante una ecuación que se conoce como función de  densidad de probabilidad. Dada esta condición,cambiamos el uso de la sumatoria por la de una integral para conocer la función acumulada de la variable aleatoria. Por lo tanto, las variables aleatorias continuas deben cumplir con los siguientes parámetros.
$$
P(x) > = 0\\ 
\int_{-\infty}^{\infty}{f(x) = 1}\\
P(a \leq X \leq b) = P(a < X < b) = F(x) = \int_{a}^{b}{f(x) dx}
$$
​	Entre las distribuciones de probabilidad tenemos la *uniforme continua,* *exponencial,* *normal,* *Weibull,* *$\chi^2$,* y *Erlang*. De las misma forma que las distribuciones discretas, algunos procesos pueden ser asociados a ciertas distribuciones, por ejemplo, es posible que el tiempo entre llagas de los clientes tenga una distribución de probabilidad muy semejante a una exponencial, o que e tiempo que le toma a un operario realizar una serie de tareas se compone de manera muy similar a la dispersión que presenta una distribución normal. Sin embargo debemos hacer notar que este tipo de distribuciones tienen sus desventajas, ya que el rango de valores posibles implica que existe la posibilidad de tener tiempos entre llagada de clientes infinitos o tiempos de ensamble infinitos, situaciones lejanas a la realidad. Por fortuna esto es muy poco probable de que se presenten este tipo de eventos, aunque el analista de la simulación debe estar consiente de como pueden impactar valores como lo descritos del resultado del modelo.

