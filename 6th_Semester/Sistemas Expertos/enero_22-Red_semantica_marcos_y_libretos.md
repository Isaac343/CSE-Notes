#### Sistemas Expertos  
#### Enero 22, 2019  
#### Tarea

# RED SEMANTICA
Una red semantica o esquema de representacion en *red* es una representación del conocimeinto lingüistico en la que los conceptos y sus interrelaciones se representan mediante un grafo. En caso de que no existan ciclos, estas redes pueden ser visualizadas como árboles. Las redes semánticas son usadas, entre otras cosas, para representar mapas conceptuales y mentales. En un grafo o red semántica los elementos semánticos se representan por nodos. Dos elementos semánticos entre los que se admite se da la relación semántica que representa la red, estarán unidos mediante una línea, flecha o enlace o arista. Cierto tipo de relaciones no simétricas requieren grafos dirigidos que usan flechas en lugar de líneas.

Note que el concepto de Web semántica es diferente de Red semántica. En inglés la Web Semántica es referida como "Semantic Web", mientras que una Red semántica se denominaría "Semantic Network".

## Definición
Existen diversos tipos de relaciones semánticas como la hiponimia, hiperonimia, la meronimia, etc. Dado un conjunto de conceptos, elementos semánticos o términos relacionados semánticamente mediante alguna relación semántica, una red semántica representa estas relaciones en forma de grafo. Explícitamente, dado un conjunto de términos {t1, t2,..., tn} y cierta relación semántica simétrica entre ellos se construye un grafo G = (V,A) cumpliendo las siguientes condiciones:
- El conjunto V es el conjunto de vértices o nodos del grafo. Este conjunto estará formado por n elementos (tantos vértices como términos relacionables). A cada uno de los vértices del grafo representará uno de los términos, por tanto los vértices del grafo se llamarán: t1, t2,..., tn.
- El conjunto A es el conjunto de aristas o líneas del grafo. Dados dos vértices (términos) del grafo ti y tj existirá una línea aij que une los vértices ti y tj si y solo si los términos de pona ti y tj están relacionados.

Si la relación no es simétrica, entonces se usan grafos dirigidos para representar la relación. 
