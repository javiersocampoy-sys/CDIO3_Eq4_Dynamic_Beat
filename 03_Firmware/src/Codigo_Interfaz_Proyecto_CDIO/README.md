
Esta carpeta contiene el **código principal del sistema interactivo**, desarrollado en Python utilizando **Pygame**, el cual se comunica con un **ESP32** mediante puerto serial.
El juego está diseñado para ser utilizado en sesiones de fisioterapia, donde el usuario interactúa con sensores físicos que envían señales al sistema.

### 🔹 main.py

Contiene:

* Lógica completa del juego
* Lectura del puerto serial (ESP32)
* Renderizado de la interfaz gráfica
* Control de puntuación, animaciones y flujo del juego

### 🔹 assets/

Contiene todos los recursos gráficos utilizados:

* Imágenes (botones, fondos, flechas, personajes)
* Tipografías personalizadas (.ttf)

⚠️ IMPORTANTE:
El código actualmente usa una **ruta absoluta**, por lo que debe modificarse para que funcione en otros equipos.

Ejemplo actual:

```python
ruta_imagenes = "C:\\Users\\Javier S Ocampo\\Documents\\Juego CDIO\\Imagenes"
```

Se recomienda cambiarlo a ruta relativa:

```python
ruta_imagenes = os.path.join(os.path.dirname(__file__), "assets")
```

---

##  Requisitos para ejecutar el sistema

Antes de ejecutar el código, asegúrese de tener instalado:

* Python 3.x
* Librerías necesarias:

```bash
pip install pygame pyserial
```

---

##  Configuración del puerto serial (MUY IMPORTANTE)

El sistema se comunica con un **ESP32**, por lo tanto es necesario configurar correctamente el puerto serial.

###  Línea a modificar en el código:

```python
puerto_serial = serial.Serial('COM4', 115200, timeout=0.01)
```

###  ¿Qué debe hacer el usuario?

* En Windows:

  1. Abrir el **Administrador de dispositivos**
  2. Buscar el ESP32 en "Puertos (COM y LPT)"
  3. Identificar el puerto asignado (ej: COM3, COM5, etc.)
  4. Reemplazar `'COM4'` por el puerto correspondiente

* En Linux/Mac:
  Puede ser algo como:

  ```bash
  /dev/ttyUSB0
  /dev/ttyACM0
  ```

---

##  Cómo ejecutar el juego

1. Conectar el ESP32 al computador
2. Verificar el puerto serial
3. Ajustar la ruta de imágenes (si es necesario)
4. Ejecutar:

```bash
python main.py
```

---

##  Funcionamiento del sistema

El ESP32 envía datos por serial en el siguiente formato:

```
SensorX -> Letra
```

Ejemplo:

```
Sensor1 -> B
```

El sistema interpreta estas letras como direcciones:

| Letra | Acción        |
| ----- | ------------- |
| B     | Arriba (↑)    |
| A     | Abajo (↓)     |
| C     | Izquierda (←) |
| D     | Derecha (→)   |

---

## ⚠️ Consideraciones importantes

* Si el juego no responde:

  * Verificar conexión serial
  * Verificar puerto correcto
* Si no cargan imágenes:

  * Revisar rutas en `assets`
* Si hay errores:

  * Revisar instalación de librerías

