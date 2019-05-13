---
layout: note
title: Protocolos
date: 05-06-19
subject: Redes de computadora I
---

# Protocolos

## MTP - Media Transfer Protocol 

Se trata de un conjunto de extensiones a protocolo de transferencia de imágenes creado por Microsoft. 

Los dispositivos que usan MTP funcionan a través del conector físico USB. 

Su propósito principal es la transferencia de archivos informáticos multimedia y sus metadatos  a/desde dispositivos, con la posibilidad de controlar remotamente el  dispositivo, leyendo o estableciendo algunos de sus parámetros como por  ejemplo los relacionados con la gestión de derechos digitales (DRM). El dispositivo también puede usar MTP para enviar eventos al ordenador al que está conectado. 

La razón fundamental para usar MTP frente a los medios de almacenamiento USB (Clase de dispositivo de almacenamiento masivo USB, *USB Mass Storage* o USB MSC) es que permite a los dispositivos tener un sistema de archivo propio, mientras que los que funcionan con USB MSC casi siempre usan FAT.  Cuando un periférico que usa FAT se conecta a una computadora, esta "se  apropia" del sistema de archivos y por lo tanto el dispositivo no puede  por sí solo añadir, eliminar, ejecutar o renombrar ficheros durante el  tiempo que está conectado sin arriesgarse a corromper el sistema de  archivos. MTP (o PTP) no impone este bloqueo. Además gestiona cuando un  dispositivo se desconecta en medio de una transferencia, situación en la  que un sistema de archivos FAT se corrompería. 

## FTP - File Transfer Protocol

Protocolo de red establecido para la transferencia de archivos entre sistemas conectados a una red TCP, con base en la arquitectura cliente-servidor. Desde un equipo cliente se puede conectar a un servidor para descargar archivos desde él o para enviarle archivos, independientemente del sistema operativo utilizado en cada equipo.

El servicio FTP es ofrecido por la capa de aplicación del modelo de capas de red TCP/IP al usuario, utilizando normalmente el puerto de red 20 y el 21. Un problema básico de FTP es que está pensado para ofrecer la máxima velocidad en la conexión, pero no la máxima seguridad, ya que todo el intercambio de información, desde el login y password del usuario en el servidor hasta la transferencia de cualquier archivo, se realiza en texto plano sin ningún tipo de cifrado, con lo que un posible atacante puede capturar este tráfico, acceder al servidor y/o apropiarse de los archivos transferidos.

## HTTP - Hypertext Transfer Protocol 

Protocolo que permite la transferencia de información a traves de la World Wide Web. Es un protocolo orientado a transacciones y sigue el esquema petición-respuesta entre un cliente y un servidor. El cliente (se le suele llamar "agente de usuario", en inglés *user agent*) realiza una petición enviando un mensaje, con cierto formato al servidor. El servidor (se le suele llamar un servidor web) le envía un mensaje de respuesta. Ejemplos de cliente son los navegadores web y las arañas web (también conocidas por su término inglés, *webcrawlers*).

Posee distintos métodos de petición, algunos de ellos son: 

-  **GET -** Solicita una representación del curso especificado, dichas peticiones  solo deben recuperar datos y no deben tener ningún otro efecto.
-  **HEAD -** Pide una respuesta idéntica a la de la petición GET, sin embargo en la respuesta no se devuelve el cuerpo. Permite recuperar solamente los metadatos de los encabezados.
-  **POST -** envia datos a un recurso especificado par auqe sean procesados, dichos datos son incluidos en el cuerpo de la petición. Cómo resultado se obtiene la creación de un nuevo recurso, la actualización de recursos existentes o ambas cosas. 
-  **PUT -** Realiza una "carga" de un recurso especificado. Permite escribir en una conexión socket del servidor un archivo. Sin embargo esto no es posible usarlo en servidores de alojamiento compartido.
-  **DELETE _** Borra el recurso especificado.
-  **TRACE -** Principalmente usado con fines de depuración y diagnostico ya que el cliente puede ver lo que llega al servidor. El método en si, solicita que el servidor introduzca en la respuesta todos los datos recibidos en el mensaje de petición.
-  **OPTIONS -** Devuelve los métodos HTTP que el servidor soporta para un URL especifico. 
-  **CONECT -** Permite saber si se tiene acceso a un host. La petición no necesariamente llega a un servidor, entre otras cosas permite saber si un proxy da acceso a un host bajo condiciones especiales.

## NFS - Network File System 

Es un protocolo de nivel de aplicación según el modelo OSI. Se utiliza para sistemas de archivos distribuidos entorno a una LAN. Posibilita que distintos  sistemas conectados a una misma red accedan a ficheros remotos como si se  tratara de locales.

### Características

-  El sistema NFS  está dividido al menos en dos partes principales: un servidor y uno o más clientes. Los clientes acceden de forma remota a los datos que se encuentran almacenados en el servidor.

-  Las estaciones de trabajo locales utilizan menos espacio de  disco debido a que los datos se encuentran centralizados en un único  lugar pero pueden ser accedidos y modificados por varios usuarios, de  tal forma que no es necesario replicar la información.

-  Los usuarios no necesitan disponer de un directorio “home” en  cada una de las máquinas de la organización. Los directorios “home”  pueden crearse en el servidor de NFS para posteriormente poder acceder a  ellos desde cualquier máquina a través de la infraestructura de red.

-  También se pueden compartir a través de la red dispositivos de almacenamiento como disqueteras, CD-ROM y unidades ZIP. Esto puede reducir la inversión en dichos dispositivos y mejorar el aprovechamiento del hardware existente en la organización.

## DDS - Data Distribution Service 

aSe trata de un middleware de tipo publish/subscribe en computación distribuida

DDS ha sido creado en respuesta a la necesidad por parte de la industria de estandarizar sistemas centrados en datos.

La especificación DDS describe dos niveles de interfaces: 

-  Una **DCPS** (**D**ata-**C**entric **P**ublish-**S**ubscribe)  a nivel inferior que tiene por objeto hacer un reparto de la  información de forma eficiente a los receptores apropiados.
-  Una capa superior opcional **DLRL** (**D**ata **L**ocal **R**econstruction **L**ayer) que permite una integración simple de DDS en la capa de aplicaciones.

