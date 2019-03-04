<small>*Sistemas Expertos - Jueves 28, febrero 2019*</small>

# Características de un encadenamiento hacia atrás

Es un método muy útil en aplicaciones con muchos datos disponibles de los cuales solo algunos son importantes. 
Es un sistema interactivo que pregunta solamente lo necesario, a diferencia del encadenamiento hacia adelante.



## Ventajas

-  Inicia bien cuando se forma una hipótesis y se busca probarla. 
-  Se enfoca en una meta dada, la cual produce una serie de preguntas relacionadas al tema.
-  Busca en la base del conocimiento solo la información referente al programa .
-  Método para diagnosticar y describir la corrección de errores.

## Desventajas

-  Continua siendo una linea de razonamiento aun si debería cambiar a uno distinto.

## ¿Cuando utilizar un encadenamiento hacia atrás?

Algunos de los casos en donde se debería utilizar el encadenamiento hacia atrás es cuando, si primero se plante la hipótesis y luego se busca comprobarla, también cuando se necesitan datos en vez de conclusiones. Cuando se tiene mucha información 

## Proceso de un encadenamiento hacia atrás

1. Se comienza con una meta para probar
2. Se inspecciona la memoria de trabajo para ver si la meta ha sido previamente probada. 
3. En caso de no ser probado, el sistema busca en sus reglas para ver si una o mas tienen esta meta en su parte del "cuando". (*Regla Meta*).
4. El sistema ve si las premisas de las *reglas meta* están listadas en la memoria del trabajo. Las premisas no listas se tornan en nuevas metas o submetas para ser probadas.
5. Este proceso continua de manera recursiva hasta que el sistema encuentra una premisa que no es soportada por ninguna regla, llamada primitiva. Cuando una primitiva es encontrada el sistema pregunta al usuario información sobre esta primitiva, entonces el sistema usa dicha información para ayudar a probar las submetas y la meta original.