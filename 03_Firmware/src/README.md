#  Códigos del Sistema

Esta carpeta contiene todo el código fuente necesario para el funcionamiento de la red de sensores y la visualización de datos. La arquitectura del software está dividida en tres componentes principales: el firmware para los nodos de adquisición, el firmware del nodo central y el software de escritorio.

##  Estructura del Directorio

*   **`EMISORES`**: Contiene el firmware desarrollado para los microcontroladores ESP32 que actúan como nodos periféricos. Estos dispositivos se encargan de la lectura de los sensores (como los sensores ultrasónicos) y de transmitir la información de forma inalámbrica hacia el nodo central, utilizando el protocolo de comunicación ESP-NOW para garantizar una baja latencia.
*   **`RECEPTOR`**: Contiene el firmware para el ESP32 que actúa como nodo central o *gateway*. Este dispositivo recibe los paquetes de datos de todos los emisores de la red a través de ESP-NOW y los retransmite hacia la computadora mediante comunicación serial.
*   **`Codigo_Interfaz_Proyecto_CDIO`**: Contiene los scripts en Python que conforman la interfaz gráfica y el sistema de procesamiento. Esta aplicación lee los datos del puerto serie, los procesa y proporciona retroalimentación visual en tiempo real. 

## ⚙️ Notas de Implementación

1.  **Firmware (ESP32):** Antes de cargar los códigos, asegúrate de configurar correctamente las direcciones MAC en los archivos para que la red ESP-NOW entre los emisores y el receptor se establezca exitosamente.
2.  **Software (Python):** Verifica tener instaladas las dependencias necesarias (`pygame`, `pyserial`, etc.) antes de ejecutar el script principal de la interfaz. Puedes instalarlas ejecutando `pip install -r requirements.txt` (si aplica).
