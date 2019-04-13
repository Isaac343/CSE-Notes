---
layout: note
tittle: Transformaciones de la composición general y de eficiencia computacional
date: 04-05-19
---

# Transformaciones de la composición general y de eficiencia computacional

Una imagen digital es una representación rasterizada de una imagen en 2D definida como un arreglo de puntos (pixeles). 

## AWD 

-  Una imagen es representada por la clase *image*.
-  Se utiliza el modelo de empuje para imágenes.
-  AWD utiliza 2 objetos: productor y consumidor(*imageProducer* e *imageConsumer*). Un productor actúa como el origen de una imagen y un consumidor la recibe para presentarlas en un dispositivo rasteriazdor.

## Java 2D

-  Una imagen es representada por la clase *BufferImage*.
-  Se utiliza el modelo inmediato
-  Un *BufferImage* contiene un raster y un *color mode*

Carga de imágenes en Java 2D:

-  Para leer una imagen de un archivo: BufferedImage bi=ImageO.reade(file);
-  Una imagen pude ser manipulada utilizando operaciones de procesamiento de imágenes. Para las siguientes operaciones: $f(xy)$ representa un pixel de la imagen original, y $g(xy)$ representa el pixel de la imagen resultante