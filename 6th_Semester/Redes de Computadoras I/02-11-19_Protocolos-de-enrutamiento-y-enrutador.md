<small>*Redes de computadora I - Lunes 11, febrero 2019  
Investigación*</small>

# Protocolos de enrutamiento
Los enrutadores(routers) son los encargados de aprender rutas por las cuales pueden alcanzar otras redes, haciendo posible así el envío de paquetes de datos entre nodos de la red. Para lograr esto el enrutador genera rutas de forma automática (aunque también existen rutas estáticas asignadas por un usuario.  
Para generar las rutas automáticamente (rutas dinámicas), se hace uso de un **"Protocolo de enrutamiento dinámico"**.
Existen multiples tipos de enrutamiento dinámico como los son:
- RIP
- IGRP
- EIGRP
- OSPF
- IS-IS
- BGP
Estos protocolos cumplen con la definición básica de protocolo: *"Un estándar compuesto de reglas, procedimientos y formatos que definir cómo lograr algo"*.
- Protocolo de enrutamiento. Le indica al enrutador como enrutar. Otorga o establece una configuración que permite al enrutador "aprender" cuales son las mejores rutas disponibles y enrute los paquetes a traves de estas.
- Protocolo de enrutado. Este protocolo es enrutado por el protocolo de enrutamiento. este se encarga de establecer cómo se preparan los datos antes de ser enrutados. (ejemplo protocolo IP, determina comó se dividen los datos en paquetes). Depende de la red que se este usando.
