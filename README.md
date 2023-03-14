# analizador_de_rimas
Algoritmo capaz de identificar rimas en un texto 

Bibliotecas requeridas:
 - colorama (Visualizacion)
 - unicode (Para normalizar el texto, acentos y codificacion utf-8)

Flujo de trabajo:
  -Recibe un archivo de texto con la información estructurada en formato RAP 4X4
  - Es procesada para obtener una lista con todos los versos palabra por palabra
  - La lista es analizada para obtener solo las sílabas de las palabras almacenadas
  - Luego compara si las últimas palabras(Solo las silabas) en cada verso con el resto 
  - Reconoce hasta 3 niveles en rimas (Conteo de sílabas)

**** Para cambiar el archivo, solo modifiqué la variable "archivo" por el nombre de un archivo dentro de "/letras" (solo el nombre del archivo)

![Captura](https://user-images.githubusercontent.com/96961824/225124004-d5476f0f-1eb0-4190-8181-031bb8b41dfe.PNG)
