
# Direcciones Estáticas y Dinámicas
El enrutamiento  ruteo es el proceso por el cual un router decide a donde enviar un paquete de datos.
## Direcciones estáticas (rutas estáticas)
Son aquellas direcciones o rutas puestas a mano o que vienen por defecto, no tienen ninguna reacción ante nuevas rutas o caídas de tramos de red. Se pueden encontrar habitualmente en sistemas cliente o en redes donde solo se sale a Internet.
Las rutas estáticas por defecto especifican una puerta de enlace (gateway) de último recurso a la que el router debe enviar un paquete destinado a una red que no aparece en su tabla de enrutamiento.

Son usadas principalmente en erutadores desde una red hasta una red de conexión única, pues solo existe una ruta de entrada y una de salida en una red de conexión única. Las rutas estáticas pueden ser configuradas para conseguir conectividad entre un enlace  de datos y el router, sin que el enlace este directamente conectado al router.
Si se desea una conexión de extremo a extremo, es necesario configurar la ruta estática en ambas direcciones. Al hacerlo se esta construyendo una tabla de enrutamento de forma manual.

El comando **ip route** permite configurar una ruta estática, siendo los parámetros del comando los que la definen. Mientras la ruta se encuentre activa, las rutas también lo estarán; pero también se les puede asignar un valor de *permanent*.



## Rutas Dinámicas
Estas pueden darse cuando el router usado posee encadenamiento dinámico. Gracias a esto es posible que la propia red agregue nuevos nodos o en caso de fallo de un enlace, es capz de poner o quitar la ruta del nodo en cuestión de la tabla de enrutamiento o buscar un camino optimo para esta ruta.
