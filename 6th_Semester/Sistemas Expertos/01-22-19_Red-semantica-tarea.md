<small>*Sistemas Expertos - Martes 22, enero 2019   
Tarea*</small>

# RED SEMÁNTICA
Una red semántica o esquema de representación en *red* es una representación del conocimiento lingüístico en la que los conceptos y sus interrelaciones se representan mediante un grafo. En caso de que no existan ciclos, estas redes pueden ser visualizadas como árboles. Las redes semánticas son usadas, entre otras cosas, para representar mapas conceptuales y mentales. En un grafo o red semántica los elementos semánticos se representan por nodos. Dos elementos semánticos entre los que se admite se da la relación semántica que representa la red, estarán unidos mediante una línea, flecha o enlace o arista. Cierto tipo de relaciones no simétricas requieren grafos dirigidos que usan flechas en lugar de líneas.

Note que el concepto de Web semántica es diferente de Red semántica. En inglés la Web Semántica es referida como "Semantic Web", mientras que una Red semántica se denominaría "Semantic Network".

## Definición
Existen diversos tipos de relaciones semánticas como la hiponimia, hiperonimia, la meronimia, etc. Dado un conjunto de conceptos, elementos semánticos o términos relacionados semánticamente mediante alguna relación semántica, una red semántica representa estas relaciones en forma de grafo. Explícitamente, dado un conjunto de términos $(t_1, t_2,..., t_n)$ y cierta relación semántica simétrica entre ellos se construye un grafo $G = (V,A)$ cumpliendo las siguientes condiciones:
- El conjunto $V$ es el conjunto de vértices o nodos del grafo. Este conjunto estará formado por $n$ elementos (tantos vértices como términos relacionables). A cada uno de los vértices del grafo representará uno de los términos, por tanto los vértices del grafo se llamarán: $t_1$, $t_2$,..., $t_n$.
- El conjunto A es el conjunto de aristas o líneas del grafo. Dados dos vértices (términos) del grafo $t_i$ y $t_j$ existirá una línea aij que une los vértices $t_i$ y $t_j$ si y solo si los términos de $p$ en $t_i$ y $t_j$ están relacionados.

Si la relación no es simétrica, entonces se usan grafos dirigidos para representar la relación.
