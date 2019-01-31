<small>*Sistemas expertos - Jueves 24, enero 2019  
Apunte*</small>

# Redes Semánticas
Son representaciones del conocimiento mediante nodos y ramas o arcos.
Fueron propuestas por Killiam & Collins en 1968.

### Objetivo
Desarrollar una infraestructura para generar datos que las computadoras puedan entender de tal forma que puedan ser compartidos y procesados no solo por personas, sino también por herramientas automatizadas.

### Componentes
Están compuestas por **nodos** que representan objetos físicos (que se pueden ver y tocar). Se representan por objetos conceptuales, es decir hechos eventos y algunos otros conceptos. Pueden ser representados de forma descriptiva, es decri por las cualidades.  
Los **arcos** son otro componente, representan elementos con su clase, parte con su todo, causa con su síntoma y representan definiciones y características.
Un nodo es la unión por arcos los cuales indican la relación que existe entre ellos. Los arcos representan las relaciones conceptuales.

### Elementos de la representación de las redes semánticas
1. Las instancias se representan por constantes.
2. Las clases se representan por constantes.
3. Cada propiedad se representa por un predicado.
4. La constante *inicio* representa la clase inicial de la jerarquía.

### Características de las redes semánticas
- Son redes complejas y organizadas en jerarquías.
- No tienen un vocabulario prefijado de representación.
- Representación en procesamiento del lenguaje natural.
- Formalismo muy limitado para dominios mas complejos.
- Fácil comprensión gráfica.

### Ventajas de las redes semánticas
- Permite la declaración de importantes asociaciones en forma explicita.
- Debido a que los nodos relacionados están directamente conectados y no se expresan las relaciones en una gran base de datos, el tiempo que toma el proceso de búsqueda por hechos particulares puede ser significativamente reducido.

### Desventajas de las redes semánticas
- No existe una interpretación normalizada para el conocimiento expresado por la red.
- La dificultad de interpretación a menudo puede derivar en inferencias invalidas del conocimiento contenido en la red.
- Tiene poca flexibilidad.
- No existe forma de insertar reglas heurísticas para explorar la red de manera eficiente.
- La exploración de una red asociativa puede derivar en una explosión combinatoria del número de relaciones que deben ser examinadas para comprobar una relación sobre todo si la respuesta a una consulta es negativa.  

*Martes 29, enero 2019*
### Tipos de arcos
**Estructurales**. Compuestos por:
  - Instancia o ejemplar
  - Subclase
  - Tiene parte    

  *Ejemplo Estructural.*
  + Estructural -> persona
    + Ejemplar -> "Juan"
    + Subclase -> Vertebrado
    + Tiene parte -> Ojos

**Descriptivos.** Están divididos en:
- Propiedades (A es de sexo femenino, tiene 25 años, etc)
- Relaciones (Persona A es amiga de persona B)


**Ejemplo.**
- Un animal tiene vida, puede sentir y puede moverse.
- Un ave es un animal
- Un ave vuela bien, tiene plumas y pone huevos
- Un avestruz tiene patas largas y no puede volar.
- Un canario vuela muy bien.
- Un mamífero es un animal, da leche y tiene pelo.
- Una ballena tiene piel y vive en el mar.
- Un tigre come carne.

<small>*Miércoles 30, enero 2019*</small>
### Tipos de redes semánticas
**Mapas conceptuales.** Es una técnica usada para la representación grafica del conocimiento, es decir, es una red de conceptos. En la red los nodos representan los conceptos y los enlaces representan las relaciones entre conceptos.
  - Elementos.
    - Conceptos. Se entiende como concepto una regularidad en los acontecimientos o en los objetos que se designan mediante algún termino. Desde la perspectiva del individuo se pueden definir los conceptos como imágenes mentales que provocan en nosotros las palabras o signos con los que expresamos regularidades.
    - Proposición. Es la formulación verbal de una idea, es decir es un indicador acerca de la comprensión de un sujeto respecto a un fenómeno o concepto.
    - Palabras de enlace. Son las palabras que sirven para armar los conceptos y señalar el tipo de relación existente entre ambos. La palabra enlace cumple una función que es determinar la jerarquía conceptual y dar precisión a los conceptos.
  - Características. Se identifica por 3 características principales
    - Síntesis. Es el resumen que contiene lo mas importante o significativo de un mensaje , tema o texto.
    - Jerarquía. No solo se trata del tamaño de las letras sino del orden en que aparecen. Las palabras con mayor importancia aparecerán en la parte superior.
    - Impacto visual. No siempre hay que tomar como definitivo un mapa conceptual, mas bien debe ser tomado como un borrador para rehacerlo y mejorar su presentación.
  - Como construir un mapa conceptual.
    1. Seleccionar. Luego de leer un texto o seleccionar un tema concreto, es necesario seleccionar los conceptos a utilizar y nunca se deben de repetir mas de 1 concepto en una misma presentación.  
    
**Mapas de ideas**  
**Causa y efecto**  
**Telarañas**  
**Linea de tiempo**  
**Organigrama**  
**Diagrama causa - efecto**  
**Diagrama de flujo**  
**Diagrama de Benn**  
