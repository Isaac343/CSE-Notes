---
layout: note
title: Conmutación
subject: Redes de Computadora
date: 03-25-19
---

# Conmutación de Red

Esta considerada como la acción de establecer vías o camino de un extremo a otro  entre 2 puntos, con un emisor(Tx) y un receptor (Rx), todo esto es a través de nodos de transmisión y permite la entrega de señal desde el origen hasta el destino. 

## Conmutación de paquetes

El emisor divide los datos a enviar en un número arbitrario paquetes de mismo tamaño, en ellos adjunta una cabecera y la dirección origen y destino así como  datos de control que luego serán transmitidos por diferentes medios de  conexión entre nodos temporales hasta llegar a su destino. Este método  de conmutación es el que más se utiliza en las redes de ordenadores  actuales. 

Al igual que en la conmutación de mensajes, los nodos temporales  almacenan los paquetes en colas en sus memorias que no necesitan ser  demasiado grandes.

### Modos de conmutación

-   Circuito virtual: Cada paquete se encamina por el mismo circuito virtual que los anteriores, por tanto, se controla y asegura el orden de llegada de los paquetes a destino.
-  Tipos:
   -  PVC (Permanent Virtual Circuit): Un único camino para los paquetes
   -  SVC (Switched Virtual Circuit): Nuevo camino para el siguiente envio.
-  Datagrama: En este cada paquete se encamina de forma distinta  a los demás, esto causa que la red no controle el camino que seguirán los paquetes ni su orden de llegada. 