#### Sistemas Expertos
#### Enero 22, 2019  
#### Apunte

# REGLAS DE PRODUCCION
Se trata de un método procidemental de representación del conocimiento, que pone enfasis en representar y soportar las relaciones inferenciales en contraposisicon a los metodos.

Las reglas de produccion son de tipo "si entonces" si se cumplen las condiciones se ejecutan las acciones. Por ejemplo: El paciente tose, tiene fiebre y dolor muscular -> gripa.

La inferencia en los sistemas basados en reglas se realiza mediante emparejamiento: existen 2 tipos:
- **Sistema de emparejamiento hacia adelante.** Una regla es activada si los antecedentes emparejan con algunos hechos.
- **Sistemas de emparejamiento hacia atras.** Una regla es activada si los consecuentes emparejan con algunos hechos.

## Caracterisiticas de las reglas de produccion:<br>
- **Modulardidad.** Cantidades de conocimiento relativamente independiente.<br>
- **Incrementabilidad.** Hace posible añadir o cambiar reglas con relativa independencia.<br>
- **Naturalidad y transparencia.** Representación del conocimeinto proxima y comprensible por las personas.<br>
- **Capacidad de generar explicaciones.**<br>

## Arquitectrua de los sistemas basados en reglas
- Base del conocimeinto.
- Memoria activada. Contiene los hechos que representan el estado actual del problema y las reglas.
- Motor de inferencia. Decide que reglas se ejecuaran.  

## Reglas
Una regla es definida como una representación estratégica o tecnica la cual es apropiada cuando el conocimeinto con el que deseamos trabajar proviene de la experiencia o intución por lo tanto carece de una demostración física o matemática.

## Tipos de reglas y proposiciones
Las proposiciones se pueden clasificar en los siquientes grupos:
- **Proposiciones cualificadas.** Introducen un atributo para cualificar la proposicion que forma una regla. El atributo corresponde al grdao que determina la regla es decir, grado de suceso (probable o poco probable).
- **Proposiciones cuantificadas.** Indica cantidades difusas en las reglas.

Los tipos de reglas son:
- **Con exepciones.** Del tipo *"si la temperatura es alta, tendre calor, exepto que tenga aire acondicionado"*.
- **Graduales.**  Del tipo *"Entre mas partidos se ganenen mas fácil se ganra una liga"*.
- **Conflictivas.** Son reglas que dentro de un mismo sistema de información contienen información contradictoria, la cual puede acarrear muchos problemas, tales como malos resultados o generar porblemas. Este tipo de regla, son aquellas que para un mismo antecedente tienen consecuentes distintos. Por ejemplo *"Si tengo hambre, entonce como. Pero si tengo hambre no he comido"*.
