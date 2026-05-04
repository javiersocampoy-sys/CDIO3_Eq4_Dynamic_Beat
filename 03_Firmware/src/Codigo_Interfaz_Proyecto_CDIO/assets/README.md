# Assets – Recursos del Juego

## Descripción general

Esta carpeta contiene todos los **recursos gráficos y tipográficos** utilizados en el juego **Dynamic Beat**.
Aquí se almacenan los elementos visuales necesarios para la interfaz, animaciones y retroalimentación del usuario durante la experiencia interactiva.

##  Tipos de recursos incluidos

### 🔹 Imágenes

Se utilizan para:

* Circuilos direccionales (Rojo, Azul, Verde, Amarillo)
* Zonas de activación (sensores visuales)
* Fondos del juego
* Botones (jugar, salir, reiniciar)
* Indicadores visuales (estrellas, puntaje)
* Personaje (animaciones de acierto/fallo)

Formatos comunes:

* `.png` (preferido por transparencia)
* `.jpg` (fondos)


###  Fuentes

Archivos `.ttf` utilizados para:

* Títulos
* Instrucciones
* Puntaje

Ejemplos en el proyecto:

* KGPerfectPenmanship.ttf
* Super Chips.ttf
* Astromeda PERSONAL USE ONLY!.ttf


## Uso dentro del código

Los recursos se cargan desde Python utilizando rutas definidas en el archivo principal (`main.py`).

Ejemplo:

```python id="uso1"
pygame.image.load(os.path.join(ruta_imagenes, "BotonVerde.png"))
```

## ⚠️ Configuración importante (RUTAS)

Actualmente, el proyecto puede usar rutas absolutas como:

```python id="uso2"
ruta_imagenes = "C:\\Users\\Usuario\\...\\Imagenes"
```
Estas rutas **NO funcionan en otros computadores**


### ✅ Solución recomendada:

Usar rutas relativas:

```python id="uso3"
ruta_imagenes = os.path.join(os.path.dirname(__file__), "assets")
```

Esto permite que el proyecto funcione en cualquier equipo sin modificar el código.

## 📌 Recomendaciones de uso

* No cambiar nombres de archivos sin actualizar el código
* Mantener formatos consistentes (.png preferiblemente)
* Usar nombres claros (ej: `BotonVerde.png`, `Fondo1.png`)
* Evitar espacios o caracteres especiales en nombres
* Organizar por carpetas según tipo de recurso

## 🚫 Errores comunes

* ❌ Imágenes no encontradas → rutas incorrectas
* ❌ Juego no inicia → falta de recursos en la carpeta
* ❌ Fuentes no cargan → archivo `.ttf` faltante

