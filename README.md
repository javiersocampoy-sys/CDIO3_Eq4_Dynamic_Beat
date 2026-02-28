# CDIO3_Eq[4]_[Dynamic Beat]
En este repositorio se tendrá toda la documentación con respecto al proyecto correspondiente a la asignatura de CDIO3. 

Proyecto_CDIOIII_DYNAMIC_BEAT
DYNAMIC BEAT: Sistema interactivo para terapias de rehabilitación

DYNAMIC BEAT es una plataforma de rehabilitación basada en sistemas embebidos que digitaliza la terapia física mediante el juego. El sistema utiliza una arquitectura distribuida de sensores de ultrasonido para capturar la cinemática del paciente en tiempo real, proporcionando una métrica objetiva del progreso y transformando ejercicios repetitivos en desafíos dinámicos que aumentan la adherencia al tratamiento.

Objetivo del Proyecto
Desarrollar un prototipo didáctico de bajo costo para la Fundación Covida, enfocado en pacientes con movilidad reducida para medir y mejorar:

Precisión del Movimiento: Validación de la ejecución correcta de ejercicios mediante detección de proximidad.

Tiempo de Reacción: Medición de la velocidad de respuesta ante estímulos visuales/auditivos.

Engagement del Paciente: Gamificación de la terapia mediante una interfaz gráfica interactiva.

Seguimiento Clínico: Generación de registros de cada sesión para el análisis del terapeuta.

🛠️ Hardware y Arquitectura
El sistema opera bajo una arquitectura Hub-and-Spoke (Nodo Central y Periféricos) utilizando el protocolo ESP-NOW para una comunicación de baja latencia sin necesidad de infraestructura WiFi externa.

Lista de Componentes (BOM)

MCU Central: ESP32 WROOM 32 (Gestión de lógica y comunicación PC).

MCU Nodos (x4): XIAO ESP32C3 / Super Mini (Sensores inalámbricos remotos).

Sensores: HC-SR04 (Ultrasonido para interacción sin contacto).

Interfaz Visual: Interfaz gráfica desarrollada en Python (Pygame).

Energía: Baterías Li-ion 3.7V (2500mAh) + Regulador LM2596 + BMS para protección.

Diagrama de Bloques
[Nodos HC-SR04] --(ESP-NOW)--> [Hub ESP32] --(Serial/USB)--> [PC / Interfaz Python]

Funcionalidades Clave
1. Interacción Sin Contacto
A diferencia de los pulsadores físicos que pueden ser difíciles de accionar para pacientes con movilidad limitada, Dynamic Beat utiliza filtros de promedio móvil en los sensores ultrasonido para detectar gestos en el aire, facilitando la terapia.

2. Red Inalámbrica Propietaria
Implementa ESP-NOW, lo que permite que los objetivos de entrenamiento (nodos) se ubiquen en cualquier lugar de la sala de terapias sin cables estorbosos, manteniendo una sincronización de milisegundos con el software central.


Instalación y Uso
Firmware (ESP32/C3)

Clonar el repositorio de la lógica de sensores.

Abrir con Arduino IDE o Python.

Instalar librerías: WiFi.h, esp_now.h, NewPing (para HC-SR04).

Cargar el código de Master en el ESP32 WROOM y Slave en los nodos C3.

Software de Interfaz (PC)

Instalar Python.

Ejecutar pip install pygame pyserial.

Conectar el Hub USB y lanzar juegocdio.py.
