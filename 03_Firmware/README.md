 Firmware Dynamic Beat 
 
Este repositorio contiene el código fuente en C++ para el sistema de control del dispositivo de fisioterapia. El firmware gestiona la lectura de sensores ultrasónicos, el control de actuadores y la interfaz de usuario, operando bajo una arquitectura de Máquina de Estados Finitos (FSM) para garantizar la precisión en las rutinas de terapia.

 Entorno de Desarrollo
Platform: PlatformIO (Recomendado) o Arduino IDE.

Framework: Arduino.

Board: esp32-c3-devkitm-1 / esp32dev (Ajustar según el módulo específico usado, como el C3 Supermini o Wroom).

Dependencias (Librerías)
Para compilar este proyecto, es necesario instalar las siguientes librerías:

NewPing (Optimización de sensores HC-SR04).

Adafruit SSD1306 (Controlador de la pantalla OLED).

Adafruit GFX (Gráficos para la interfaz).

WiFi.h (Gestión de conectividad si se usa el Wroom para telemetría).

 Pinout (Mapa de Conexiones - Borrador)
Configuración de pines sugerida (puedes ajustarla según tu config.h real):
