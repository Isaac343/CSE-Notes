----
layout: notes
title: Modelo OSI
subject: Redes
date: 03-11-19

---

# Modelo OSI

## Capa Física

Capa mas baja del modelo OSI. Se encarga de la topología de red y de las conexiones globales de la computadora hacia la red. Hace referencia tanto al medio físico como a la forma en la que la información se transmite. 

Sus funciones principales son:

-  Definir el medio o medios físicos por el que viajara el información. 
-  Definir las caracteristicas materiales y electricas para la transmisión de datos.
-  Definir caracteristicas funcionales de la interfaz.
-  Transmitir el flujo de bits a traves del medio.
-  Manejar las señales electricas del medio de transmisión
-  Garantizar la conexión, no la fiabilidad.

## Capa de enlace de datos

Encargada del direccionamiento físico, del acceso al medio, detección de errores, distribución ordenada de tramas y control de flujo.

Es una parte esencial en la creación de protocolos básicos (MAC, IP) para regular regular la forma de la conexión entre computadoras.

El principal usuario de esta capa es el *"Switch"*, que se encarga de recibir los datos del router y enviarlos a sus respectivos destinatarios. Este es también el medio por el cual se realiza la corrección de errores, manejo de tramas, protocolización de datos.

## Capa de red

Encargada de la identificación del numero de enrutamiento entre una o mas redes.   Los datos viajan en paquetes, con protocolos de enrutamiento y protocolos enrutables.

-  Enrutables. viajan con paquetes(IP, IPX, APPLETALK)
   -  IP: Protocolo de internet, es un protocolo de comunicación de datos digitales .
   -  IPX: Antiguo protocolo de redes *NetWare* 
   -  APPLETALK: Conjunto de protocolos desarrollados por AppleInc. 
-  Enrutamiento. permiten seleccionar rutas (RIP, IGRP, EIGRP, BGP).
   -  RIP: Protocolo de Información de Encadenamiento. Es un protocolo de puerta de enlace interna, es usado por los routers para el intercambio de información. Calcula la ruta mas corta hacia el destinatario baso en el número de saltos entre nodos que deben hacer los paquetes IP.
   -  IGRP: *Interior Gateway Routing Protocol*. Protocolo de CISCO usado en conjunto con el TCP/IP. El protocolo esta basado en la tecnología vector-distancia tomando el estado del enlace. 
   -  EIGRP: (Protocolo de Enrutamiento de Puerta de Enlace Interior Mejorado). Protocolo de encadenamiento de estado de enlace. 
   -  BGP: *Border Gateway Protocol*. Protocolo para el intercambio de información entre sistemas autónomos. 

Su objetivo es hacer que los datos lleguen desde el destino hasta su destinatario. Los dispositivos que facilitan la tarea son los routers. Los *firewall* actúan sobre esta capa limitando o descartando direcciones de determinadas máquinas. También ocurre el direccionamiento lógico y la determinación de la ruta de los datos hasta el receptor final

## Capa de transporte

Es la capa encargada de transportar los paquetes de datos desde el nodo de origen hasta el nodo de destino, independizando el paquete del tipo de red física usada. 

A las unidades de información se les conoce como *Datagramas*. En conjunto con la capa de red, crean los *Sockets IP:Puerto*

## Capa de sesión

Mantiene y controla el enlace establecido entre 2 nodos que estén transmitiendo paquetes entre si. Se entiende que el servicio que presta es mantener una sesión, una vez establecida, hasta su fin permitiendo la transmisión de paquetes.

## Capa de presentación 

Se encarga de la presentación de información. Esto implica que si 2 equipos poseen distintas representaciones de caracteres, los datos lleguen de manera comprensible.

Esta capa es la primera en trabajar más **el contenido** de la 
comunicación que el cómo se establece la misma. En ella se tratan 
aspectos tales como la semántica y la sintaxis de los datos 
transmitidos, ya que distintas computadoras pueden tener diferentes 
formas de manejarlas.

Esta capa también permite cifrar los datos y comprimirlos. Por lo tanto, podría decirse que esta capa actúa como un traductor.

## Capa de aplicación

Ofrece a las aplicaciones la posibilidad de acceder a los servicios de 
las demás capas y define los protocolos que utilizan las aplicaciones 
para intercambiar datos, como correo electrónico Post Office Protocol y SMTP, gestores de bases de datos y servidor de ficheros FTP. Cabe aclarar que el usuario normalmente *no interactúa directamente*
con el nivel de aplicación. Suele interactuar con programas que a su 
vez interactúan con el nivel de aplicación pero ocultando la complejidad
subyacente.