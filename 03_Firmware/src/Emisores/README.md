 Firmware - Nodos Esclavos (Emisores)
 
  DescripciónEste firmware se carga en los 4 ESP32 Mini independientes. 
Su función principal es leer la distancia detectada por el sensor ultrasónico y transmitirla de forma inalámbrica al 
Nodo Maestro utilizando el protocolo ESP-NOW.Cada nodo es autónomo, cuenta con su propia fuente de alimentación y se 
identifica mediante un NODE_ID único para que el juego pueda distinguir qué sensor está siendo activado por el paciente.

  Especificaciones TécnicasProtocolo: 
 ESP-NOW (Modo Broadcast para emparejamiento automático).
 Canal WiFi: 6.
 Frecuencia de Envío: 1 Hz (ajustable según la necesidad del juego).
 ID de Nodo: Configurable manualmente en el código (#define NODE_ID).
 
  Configuración de Identificación (¡Importante!)Para que el sistema funcione, antes de subir el código a cada ESP32 Mini, 
  se debe modificar la línea 5 del archivo .ino:
  Sensor 1: #define NODE_ID 1
  Sensor 2: #define NODE_ID 2
  Sensor 3: #define NODE_ID 3
  Sensor 4: #define NODE_ID 4
  
   Diagrama de Conexión (Propuesto)Aunque el código actual usa valores aleatorios para pruebas, 
   el hardware final debe conectarse de la siguiente forma:
ComponentePin ESP32 MiniFunciónHC-SR04 (Trig)
GPIO XDisparo del pulsoHC-SR04 (Echo)
GPIO YRecepción del ecoLED Indicador
GPIO ZFeedback visual de detecciónBatería LiPoVCC / GNDAlimentación (vía regulador)

   
  Lógica de FuncionamientoInicialización: 
El nodo configura el WiFi en modo estación y prepara el canal 6.
Registro de Peer: Se añade la dirección de BROADCAST para que cualquier receptor en el mismo canal escuche el mensaje.
Bucle Principal:Se captura la lectura del sensor (actualmente simulada con random).
Se empaqueta el ID y el valor en la estructura mensaje_t.Se envía el paquete y se confirma por el monitor serial.

