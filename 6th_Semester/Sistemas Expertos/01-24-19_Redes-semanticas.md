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
