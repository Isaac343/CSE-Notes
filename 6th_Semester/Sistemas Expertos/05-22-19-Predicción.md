---
layout: 
date:05-21-19
title: Predicción
subject: Sistemas expertos 
---

# Predicción

Infieren posibles consecuencias de situaciones dadas. Algunas veces se usan modelos de simulación para generar situaciones que puedan ocurrir. Por ejemplo predecir daños a cosechas a causa de una plaga. 



# Interpretación

Infiere la descripción de situaciones por medio de sensores de datos. Estos sistemas expertos usan datos reales con errores, con ruidos o datos incompletos, etc.

# Depuración 

Sugiere remedios o correcciones de una falla. Por ejemplo, sugerir el tipo de mantenimiento a cables dañados o las prescripciones medicas realizadas a un paciente.

# Simulación 

La simulación es una técnica que consiste en crear modelos basados en hechos, observaciones e interpretaciones sobre computadora.  A fin de estudiar el comportamiento de los mismos mediante la observación de salidas para un conjunto de entradas.  Las técnicas tradicionales de simulación requieren modelos matemáticos y lógicos que describen el comportamiento del sistema bajo estudio. 

El empleo de los sistemas expertos para la simualcion esta motivado por la principal caracteristica de los sitemas expertos, que es su capacida de simulación de un experto humano, pues es un proceso complejo. En sus aplicaciones hay que diferenciar 5 configuraciones posibles.

- Un sistema experto puede disponer de un simulador con el fin de comprobar las soluciones y rectificar el procesos que se sigue. 
- Un sistema de simulación puede contener como parte del mismo a un sistema experto, y por lo tanto el sistema experto no tiene que ser necesariamente de simulación.
- Un sistema experto puede controlar un proceso de simulación, es decir que el modelo esta en la base de conocimiento del sistema experto y su evolución es función de la base de hechos, la base de conocimientos y el motor de inferencia y no de un conjunto de ecuaciones aritmético-lógicas.
- Un sistema experto puede utilizarse como consejero del usuario y del sistema de simulación. Con el fin que el usuario reciba explicación y justificación de los procesos.
- Un sitema de instrucción realizara el seguimiento del procesos de apendizaje. El esitema detecta errores, y se adelanta a ellos, acelerando el proceso de aprendizaje.

# Recuperación de información

Los sistemas expertos con su capacidad para combinar información y reglas de actuación han sido vistos como una de las posibles soluciones al tratamiento y recuperación de información no solo documentada. En la década de 1980 fue prolija en la investigación y publicaciones sobre experimentos de este orden de interés que continua en la actualidad. Lo que diferencia a estos sistemas de recuperación de información es que estos últimos solo son capaces de recuperar lo que existe explícitamente, mientras que un sistema experto debe ser capaz de generar información no explicita, razonando con los elementos que se le dan. pero la capacidad de los sistemas expertos es en el ámbito de recuperación de información no se limita a la recuperación de información. Estos pueden utilizarse para ayudar al usuario en selección de recursos de información, infiltrado de respuestas. Un sistema experto puede actuar como un intermediario inteligente  que guía y apoya el trabajo del usuario final.

<small>05-23-19</small>

# Planificación

Es la realización de planes o secuencia de acciones y es un caso particular de la simualción, esta compuesto por un simulador y un sistema de control. El efecto final es la ordenación de un conjunto de acciones con el fin de conseguir un objetivo global. 

Los problemas que presenta la planificación mediante un sistema experto son los siguiente:

- Existen consecuencias no previsibles, de modo que hay que explorar y explicar varios planes.
- Existen muchas consideraciones que deben ser valoradas o incluirles un valor de peso.
- Suelen existir interacciones entre planes de sus objetivos por lo que deben elegirse soluciones de compromiso.
- Trabajo frecuente con incertidumbre pues la mayoría de los datos con los que se trabaja son menos probables pero no seguros. 
- Es necesario hacer uso de fuentes diversas, tales como base de datos.

La mayoría de las aplicaciones de sistemas expertos desarrolladas en el campo de la planificación y análisis financiero contemplan estos aspectos. Normalmente compuestos por 2 módulos.

- El primero realiza los cálculos por medio de la informática tradicional o cualquier tipo de herramienta de ayuda a la decisión.
- El segundo realiza los procesos de análisis de interpretación, los datos de emisión y de el informe. 

Es importante resaltar que los sistemas expertos de planificación financiera y análisis financiero son los sistemas expertos que han alcanzado un alto nivel de desarrollo contradiciendo la opinión que los sistemas expertos se refieren a dominios muy pequeños.

## Metodología para la construcción de un sistema experto

Para desarrollar sistemas expertos debemos primero identificar y analizar el problema  para saber sis este problema es solucionable a partir de una serie de reglas y experiencias. Posteriormente se debe idear algún modo de adquirir y modelar el conocimiento para por ultimo reducirlo a nivel simbólico para así poder educar a la maquina.

### Equipo de deasrrollo de un sistema experto

Los participantes en el desarrollo de un sistema experto desempeñan 3 papeles distintos:

1. **Experto**. Pone a disposición del sistema experto sus conocimientos.
2. **Ingeniero de conocimiento.** Plantea las preguntas al experto, estructura sus conocimientos y los integra a ala base del conocimiento.
3. **Usuario.** Aporta su deseo e ideas determinado el escenario en el que debe aplicarse el sistema experto.

### Fases de la metodologia de un sistema experto

- Saber si el problema es abarcable por un sistem experto, es decir que cumpla con: 

  - información declarativa (el verdadero desafío al programar un sistema experto es la manera para capturar dicho conocimiento usado por expertos, es decir la forma de ir educando a las máquinas. Para ello se hace inevitable la necesitada de considerar el conocimiento como modular, de este modo si un S.E. en desarrollo falla, es lógico pensar a que esto se debe de alguna manera a que falta algun conocimiento o experiencia en el progrma. Esta condicion que el conocimiento debe se modular, impide la solución de problemas en que intervenga el sentido conocimiento 
  - Ventajas de la interfaz. Como las conclusiones de un sistema experto son similares a las hechas a los seres humanos el comportamiento de un sistema experto es naturalmente amigable y los usuarios generalmente pueden mantener el sistema.
  - El conocimiento faltante en un a base de hechos puede ser obtenida de forma natural.
  - El S.E. debe ser capaz de explicar sus conclusiones.

  La importancia de este proceso no solo es que de esta forma se pueda verificar fácilmente algún razonamiento de la máquina o tal vez llegar a un conocimiento importante sino que de esta forma la maquina es capaz de enseñar a los humanos a partir de sus experiencias.

  - **Elección de la herramienra aopropiada**

Puede ser una ya existente a la realización del sistem experto. Se ha establecido algunos principios escenciales concerneintes a elecciń de una. Uno de los principios es que la herramienta debía psoer el graod de genaralidad necesario para reflera el software de partida, 

- La herramienta deberia peseer las caracterisitacs siguientes:
  - El lenguaje debera ser lo mas simpe y universal posible 
  - un medio de acceso a los mecanismos de control si la generalidad es mas importante que la eficacia o a la inversa.
  - Un control muy limitado si se busaca un aprendizage una automodificaicon o exlicaciones alradas
  - Capadidades de dialogo desarrolladas si el tiempo es critico
  - Es neceario utilizar un hermmaienta que ya haya servido.

Para la realización de un sistema experto tambien se debe considear la tecnca de solucín del problema adecaudo a  este caso y la solucion en determinación. 

La determinacion de estos se obtiene luego de haber efectuado la adquisición y el modelado de la informaicion para llevarlo en leguaje a nivel simbolico y poder implementarlo como un sistema.

- Transferencia de xperianda,  se efectua del experto al sistema experto ayudado por el expero. La disciplina que interfiere con la trasferencia de experiencia se denomina . ---  <este proceso se escompone en 4 fases o etapas. 
  - análisis
  - adquisición de conocimiento y conceptualización.
  - formalizan  y representativo del conocmiento.
  - validación

### Fase 1 análisi del problema

consiste en elaborar los probemas que deen soporte al sistema. ene sta primera fase es de vital importancia determianr correctamente el ambito de trabajo. para la acepación al exito es primordial en cuenta los deseos y las ideas de los usarión

### Fase 2 adquisiscón de conocimiento y conpcetualización

Objetivo: identificar todos los momentos que intervienen en la solución del sistema (información escrita, dialogo con el experto, datos empiricos, graficos, etc.)

A mediad que se va obteniendo el conocimiento es neceario depurarlo, seleccionado los conceptos básicos que haran posble el funcionamiento del sistema.

### Fase 3 Normalización y presentación del conocimineto. 

La activiad del ingeniero del conocimiento se concreta en las siguientes tareas:

- Formaliso de la representación  del conomció
- Reeleccion del concoimeinto que con los ambitos que intervien en la solción del problema
- Creacción de la base del conocieminto utilizando el formalismo y la arquitectura eleda.
- Diseño de la interfaz de un sistema experto con el usuario y con el diseño del apartado lógico. En esta fase se determiann las regllas y se incorporan a a la base de hechos.

Durante la inferencia se pude verificar o deducir los daos en la veridicacion de un hecho el proceos esta dirigid por los objetivos mientras que los ------- los datos. 

La conclusión de una regla puede constituire en condición de la premsia necesaria para otra regla y seguir así sucesivamente y llegar al final de la inferen.

### Fase 4. Validación

En el desarrollo de un sistema experto no se considera que este acabado una vez que funciona, sino que se continua desarrollando y tanto el conocimiento del sistema como los métodos de procesamiento quedando reflejados lo progresos o cambios en el.