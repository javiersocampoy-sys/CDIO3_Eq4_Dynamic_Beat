Firmware - Nodo Maestro (Receptor)
Descripción
Este código se encarga de gestionar la recepción inalámbrica de datos en el ESP32 Principal. 
Su función es centralizar las señales provenientes de los 4 nodos esclavos (sensores ultrasónicos) y 
enviarlas a través del puerto Serial hacia el ordenador donde se ejecuta el videojuego de fisioterapia.

Especificaciones Técnicas
Protocolo de Comunicación: ESP-NOW (Seleccionado por su baja latencia, ideal para aplicaciones en tiempo real).

Frecuencia/Canal: Canal 6 (WiFi).

Gestión de Nodos: Registro automático mediante std::vector y callbacks de nuevos peers.

Velocidad Serial: 115200 baudios

Estructura del Paquete de Datos
Para garantizar la integridad de la comunicación, tanto el Maestro como los Esclavos deben compartir la misma estructura de datos:
typedef struct {
  uint8_t id;    // Identificador único del sensor (1-4)
  float valor;   // Distancia en cm captada por el ultrasonido
} mensaje_t;

Conexiones
Este nodo actúa como puente USB-Serial, por lo cual su conexión es mínima:

Alimentación: Vía cable Micro-USB/USB-C conectado al PC.

Salida de Datos: Puerto Serial (UART).

Instrucciones de Instalación y Uso
Entorno: Abrir en Arduino IDE o VS Code (PlatformIO).

Dependencias: Asegurarse de tener instalado el core de ESP32 (versión 3.0 o superior recomendada para la librería ESP32_NOW.h).

Configuración: Verificar que el #define CHANNEL 6 coincida con el código de los emisores.

Monitoreo: Al abrir el Monitor Serial, el sistema mostrará el mensaje "Receptor listo". Cuando un esclavo se encienda, aparecerá "Nuevo nodo registrado".
