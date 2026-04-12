Hardware: Sistema de Rehabilitación 

Este apartado contiene toda la documentación técnica, diseños físicos y esquemáticos del hardware que compone el sistema de fisioterapia interactiva.


Descripción General

El hardware está diseñado como una red inalámbrica de sensores compuesta por 5 estaciones independientes (cajas) que funcionan bajo una arquitectura Maestro-Esclavo mediante el protocolo ESP-NOW:


Nodos Periféricos (4 estaciones): Cada caja actúa como un punto de interacción. Utilizan microcontroladores ESP32-C3 (versiones Supermini y con pantalla OLED integrada) conectados a sensores de ultrasonido HC-SR04 para detectar la proximidad de la extremidad del paciente.


Nodo Central (Maestro): Una unidad basada en ESP32 Wroom que centraliza la información de los periféricos y la transmite vía serial a un computador para la ejecución de la terapia (videojuego).


Gestión de Energía: Cada unidad es autónoma, alimentada por dos celdas de 3.7V en serie, reguladas mediante un módulo LM2596 para garantizar un voltaje estable de operación para los sensores y microcontroladores.


Contenido de la Carpeta

En esta rama del repositorio encontrarás la siguiente organización:


DATASHEETS

Contiene las hojas de especificaciones técnicas en formato PDF de los componentes críticos utilizados, asegurando que se conozcan los límites de operación de:
ESP32-C3 (Supermini & OLED version).
ESP32 Wroom.
Sensor HC-SR04.
Regulador LM2596.


MECHANICAL

Incluye los archivos de diseño para la fabricación de las 5 cajas del prototipo:


SOURCE

Contiene los archivos fuente originales y editables del diseño electrónico:


Esquemáticos de conexión.


Diseño de PCBs (en formatos compatibles con KiCad, Altium o Eagle según corresponda).

Diagramas de bloques del sistema de alimentación.
