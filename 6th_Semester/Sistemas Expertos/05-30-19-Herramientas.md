---
layout: note
date: 05-30-19
title: Herramientas
subject: Sistemas expertos
---

# Herramientas

## Framework y tecnologías disponibles para la construcción de un sistema experto

### Prolo

Es un lenguaje de programación lógica con propósito general asociado con la IA y lingüística comunicacional este es un lenguaje declarativo basado en reglas su nombre deriva de Anna Gram programación lógica la sintaxis del lenguaje se basa en lo siguiente: declarar hechos sobre objetos y sus relaciones , hacer preguntas sobre objetos y sus relaciones y definir reglas de objetos y sus relaciones. 

### Clips 

A mediados de los años 80 la Nasa requería de sistemas expertos para el desarrollo de proyectos por lo tanto una serie de prototipos surgen pero sus resultados no fueron lo suficientemente buenos para cumplir con los requerimientos internos en consecuencia se desarrollo un prototipo de un sistema experto denominado clips cuya principal característica era su capacidad para funcionar con otros sistemas existentes posteriores mejoras y ampliaciones han convertido clips en un mundo de referencias para el desarrollo de otros sistemas expertos 

### Yes 

El motor de reglas Yes es un proyecto que tuvo su origen en clips pero que fue escrito enteramente en java este se desarrollo durante la década de los 90 en los sandia national laboratories que comparte con clips varios conceptos de diseño y similitudes con respecto a la sintaxis así mismo implementa la especificación de referencia JPCB94 



### Drolls

Al igual que en el caso de los clips y Yes Drolls es la implementación y ampliación del algoritmo redit diseñado por el doctor Charles Forje en la universidad Carnech Melu. Básicamente su algoritmo consiste en una red de nodos conectados con diferentes características que evalúan las entradas mediante la propagación de los resultados del siguiente nodo cuando hay coincidencias Drolls Ofrece herramientas de integración con Java con la capacidad de escalabilidad y una división clara entre los datos y la lógica del dominio 

### Llena 

Framework desarrollado en tencnología java que incluye un motor de inferencia basado en normas una API ontológica y un motor de búsqueda. 

### Y-UPS 

Añade encarnamiento hacia adelante las normas de producción del primer orden con el fin de facilitar el desarrollo de los sistemas expertos mediante programación declarativa

### Open Zip

Es la versión de código abierto de la tecnología zip mas completa base de conocimientos generales y motor de razonamiento de sentido común.

## Encadenamiento hacia atrás

EL encadenamiento hacia atrás es una estrategia de búsqueda orientada a objetivos comienza con el objetivo y trabaja hacia atrás con las condiciones iniciales el proceso comienza con la hipótesis después se inicia una búsqueda para encontrar y verificar los datos de respaldo necesarios y el proceso finaliza con la aceptación o rechazo de la hipótesis 

## Características del encadenamiento hacia atrás 

Algunas de las características de los sistemas de encadenamiento hacia atrás son las siguientes

1. Es un método muy útil en aplicaciones con muchos datos disponibles de partido los cuales solo una pequeña parte son relevantes
2. Es un sistema interactivo lo cual pregunta lo necesario a diferencia del encadenamiento hacia adelante que no pregunta nada 

## Ventajas del encadenamiento hacia atras

El encadenamiento hacia atrás posee las siguientes ventajas trabaja bien cuando el problema comienza formando la hipótesis y luego busca probarla se enfoca en una meta dada lo cual produce una serie de preguntas relacionadas al tema otra ventaja es que buscan en la base del conocimiento solo información referente al problema este es excelente para el diagnostico prescripción y corrección de errores  

## Desventajas del encadenamiento hacia atras 

Podrían decirse que la principal desventaja que posee es que continua siendo una linea de razonamiento aun si deberá cambiar a uno distinto

## Cuando usar un encadenamiento hacia atrás

Algunos de los casos en los que se debería usar es cuando si primero se plantea la hipótesis y luego se busca probarla si se necesitan mas datos que conclusiones o bien cuando se tiene mucha información disponible 

## Proceso de desarrollo

El proceso de desarrollo de un encadenamiento hacia atrás esta dado de la siguiente manera 

1. Se comienza con una meta para probar

2. Posteriormente se inspecciona la memoria de trabajo para ver si la meta a sido brevemente probada
3. En caso de que no haya sido probado el sistema busca en sus reglas para ver si una o mas tienen esa meta en su parte del DEM (entonces) y a este tipo de reglas se le llama reglamento 
4. EL sistema hace las premisas de las reglas meta están listadas en la memoria de trabajo y en las premisas no listadas se tornan nuevas metas o submetas al ser probadas
5. Este proceso continua de manera recursiva hasta que el sistema busca una premisa que no es soportada por ninguna regla llamada primitiva

Cuando una primitiva es encontrada el sistema pregunta al usuario acerca de esta primitiva entonces el sistema usa esta información para ayudar a probar las submetas y la meta original.

## Ejemplo de encademaniento hacia atras. 

Decisión de inversión se encuentra las siguientes variables involucradas variable 

A que tiene 10,000

B es menor de 30

C Tiene educación de nivel universitario

D tiene ingreso anual de al menos 40,000

E Debe invertir en valores 

F Debe invertir en acciones de crecimiento

G invertir en acciones de IBM

Cada una de estas variables puede ser verdadera o falsa los echos son los siguientes supongamos que un inversor tiene 10,000 y tiene 25 años y este le gustaría recibir consejos sobre la inversión IBM  entonces esto sabe que 

A es verdadero y B es verdadero

1. Supongamos que nuestra base de conocimiento, si una persona tiene 10,000 y tiene u titulo universitario entonces debería invertir en valores,

2. SI el ingreso anual de una persona es de al menos 40,000 y tiene un titulo universitario entonces debería invertir en acciones de crecimiento 

3. SI una persona es menor de 30 años y esta invirtiendo en valores entonces debería de invertir en acciones de crecimiento

4. SI una persona es menor de 30 años entonces tiene un titulo universitario
5. SI una persona quiere invertir en acciones de crecimiento entonces debería invertir en acciones de IBM 

Entonces estas reglas se pueden escribir de esta manera

1. Si A entonces C luego E 

2. Si D y C luego F
3. Si B y E entonces F
4. Si B entonces C
5. Si F entonces G