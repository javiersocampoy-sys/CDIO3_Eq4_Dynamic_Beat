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

  Pinout (Mapa de Conexiones)

| Pin ESP32 | Componente | Función | Notas |
| :--- | :--- | :--- | :--- |
| **5V / VIN** | LM2596 (Out) | Alimentación | Entrada regulada |
| **GND** | Sistema | Tierra Común | Unión de todas las tierras |
| **GPIO 4** | HC-SR04 | Trig | Sensor Ultrasonido |
| **GPIO 5** | HC-SR04 | Echo | Sensor Ultrasonido |
| **GPIO 8** | OLED (SDA) | Datos I2C | Pantalla |
| **GPIO 9** | OLED (SCL) | Reloj I2C | Pantalla |


 Lógica del Sistema (Arquitectura)
El dispositivo no utiliza un bucle lineal; emplea una Máquina de Estados para gestionar las fases de la terapia y la seguridad del paciente.

Diagrama de Flujo de Estados

```mermaid
stateDiagram-v2
    [*] --> INIT
    INIT --> IDLE : Comunicación Serial OK
    
    IDLE --> GAME_START : Señal desde Maestro/PC
    
    state GAME_START {
        [*] --> SCANNING : Sensor Activo
        SCANNING --> DETECTION : Distancia < Umbral
        
        DETECTION --> FEEDBACK : Encender Luces
        FEEDBACK --> SEND_DATA : Enviar ID al Maestro
        
        SEND_DATA --> COOLDOWN : Debounce (Evitar doble golpe)
        COOLDOWN --> SCANNING : Reset de detección
    }
    
    GAME_START --> GAME_OVER : Fin de rutina (PC)
    GAME_OVER --> IDLE : Mostrar resultados
    
    ERROR --> IDLE : Reset Manual
