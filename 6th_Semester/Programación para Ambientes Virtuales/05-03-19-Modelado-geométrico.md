---
layout: note
title: Modelado geométrico
date: 05-03-19
subject: Programación para ambientes virtuales
---

# Modelado geométrico

## Modelos geométricos

Son una representación geométrica generada por la computadora debido a que; los componentes de un sistema se representan con entidades geométricas (lineas, polígonos o circunferencias). Las formas en las que se puede representar un modelo geométrico son: distribución espacial y forma de los componentes y otros componentes que afectan a la apariencia de los componentes.

## Modelado de superficie

Es la estimación de los valores de una superficie en cualquiera de sus puntos, partiendo de un conjunto de datos de muestreo (x, y, z) denominados puntos de control.

Aplicaciones: 

-  Geología
-  Geofísica 
-  Meteorología
-  Ingeniería ambiental
-  Economía
-  Medicina

Este modelo nos permite utilizar representaciones de los sólidos basadas en el almacenamiento de la frontera que es una entidad bidimensional. Para que el solido sea representable se suele imponer una condición adicional de suavidad en su frontera, mas concretamente se suele exigir que la frontera sea algebraica (o al menos analítica). Esto es, que debe ser representable por un polinomio de grado finito. 

## Modelado de sólido

Es una rama del modelado geométrico que hace énfasis en la aplicabilidad general de los modelos, en la creación de representaciones completas de objetos físicos sólidos, que son adecuadas para la respuesta de preguntas geométricas arbitrarias de manera algorítmica.

El modelado de sólidos es el conjunto de teorías, técnicas, y sistemas orientados a la representación "completa en cuanto información" de sólidos. Dicha representación debe permitir (al menos en principio) calcular automáticamente cualquier prioridad bien conocida en cualquier solido almacenado.

Con los sólidos representados necesitaremos, ademas de visualizarlos y editarlo, calcular su propiedades físicas (por ejemplo su peso o su centro de gravedad) y simular sobre ellos procesos físicos (como la transmisión de calor en su interior).

## Procesos generativos 

Se refiere a ala imagen que se genera, compone o construye, una manera algorítmica a través del uso de sistemas definidos por un proceso. 

Se  mencionan las siguientes etapas: 

1. Obtención del diseño 3D adecuado
2. Asignación de materiales
3. Elaboración de escenas mediante luces y vistas 3D
4. Modelado 

# Proyecciones

La proyección es la representación gráfica de un objeto sobre una superficie plana, obtenida al unir las intersecciones sobre dicho plano de las lineas proyectantes de todos los puntos del objeto desde el vértice.

En términos generales las proyecciones transforman puntos en un sistema de coordenadas de dimensión "n" a puntos en un sistema de coordenadas de dimensión menor que "n".

De hecho durante mucho tiempo se ha hecho la gratificación por computadora para estudiar objetos "n-dimensionales" por medio de su proyección sobre 2 dimensiones. La proyección de objetos tridimensionales es definida por rayos de proyección, llamados proyectores, que emanan de un centro de proyección,pasan por cada punto del objeto e intersectan un plano de proyección para formar la proyección. Por lo general, el centro de proyección se encuentra a una distancia finita del plano de proyección. Sin embargo, en algunos tipos de proyecciones es conveniente pensar en función de un centro de proyección que tienda a estar infinitamente lejos.

