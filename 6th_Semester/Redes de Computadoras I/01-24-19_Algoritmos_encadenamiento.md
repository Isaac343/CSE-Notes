<!-- Enrutamiento en entornos mixtos de medios de lan -->

# Algoritmos de enrutamiento

## Definición

El **enrutamiento** se puede definir como un proceso mediante el cual tratamos de encontrar un camino entre 2 puntos de una red, teniendo el nodo de origen y el nodo de destino. Cabe aclarar que para esta definición *camino*, hace referencia a varios caminos, el mejor o los mejores para llegar de 1 a N puntos.  

**Mejor ruta.**  Es aquella que cumple con las siguientes condiciones:
- Tiene el menor retraso de transito.
- Consigue mantener acotado el retardo entre paredes.
- Menor coste.

Para que un algoritmo de enrutamiento funcione correctamente, debe cumplir con las siguientes condiciones:  
## Propiedades del algoritmo de enrutamiento

**Corrección.** El paquete debe llegar al nodo que hemos indicado.  
**Simplicidad.** Soluciones sencillas. De alta importancia en redes grandes.
**Robustez.** Comportamiento correcto frente a problemas.
**Estabilidad.** El proceso debe converger antes que la red cambie de estado. Cuando esto ocurre se recalculan de nuevo las rutas, por tanto los nodos deben deben llevar a cabo acciones coherentes que conduzcan a situaciones estables.  
**Equidad o Justicia.** Todos los usuarios son tratados de la misma manera.  
**Gestionabilidad** (trazabilidad). Supone tener información de lo que ha hecho la red para que en el caso de que existan fallos u ocurran "eventos fuera de lo común".  
**Escalabilidad.** El comportamiento debe ser optimo sin importar si el número de nodos aumenta o disminuye.

## Métodos de enrutamiento

### Estructura de un Nodo
Un nodo contienen las siguientes partes:
- FIB (Foward Information Base). Tabla de enrutamiento que es consultada para hacer el reenvío de paquetes generados por usuarios.
-   Entorno local. Contiene información que el nodo ve (memoria, enlaces locales, etc.)
- PDU (Protocol Data Unit). Unidad fundamental para un intercambio de información para un nivel determinado.
- R-PDU. Paquete de control. Paquetes enviados por otros nodos con información sobre la red.
- Decisión. Lógica para determinar si la tabla  de enrutamiento debe ser cambiada o no.
- RIB (Routng Information Base). Base de información de enrutamiento que se consulta para decidir  y formar la FIB. La información de RIB se consigue mediante la interacción con el entorno local.
