import pygame
import random
import sys
import os
import serial

# --- INICIO DE CONEXIÓN SERIAL ---
try:
    # Ajustado a 115200 baudios como configuraste en el ESP32
    puerto_serial = serial.Serial('COM4', 115200, timeout=0.01) 
    print("ESP32 conectado correctamente.")
except serial.SerialException:
    print("Error: No se pudo conectar al puerto serial. Verifica el COM.")
    puerto_serial = None

# Inicializar Pygame
pygame.init()

# Configuración de pantalla
ANCHO, ALTO = 800, 700
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Dynamic Beat - Versión Profesional")

# Colores
AZUL = (0, 120, 255)
VERDE = (0, 255, 150)
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
MARRON = (101, 67, 33)
NARANJA = (255, 203, 61)

# --- RUTAS E IMÁGENES ---
ruta_imagenes = "C:\\Users\\Javier S Ocampo\\Documents\\Juego CDIO\\Imagenes"

# Fuentes de sistema
pygame.font.init()
FUENTE = pygame.font.Font(os.path.join(ruta_imagenes, "KGPerfectPenmanship.ttf"), 30)
FUENTE_TITULO_GRANDE = pygame.font.Font(os.path.join(ruta_imagenes, "Astromeda PERSONAL USE ONLY!.ttf"), 115)
FUENTE_CUSTOM_INSTR = pygame.font.Font(os.path.join(ruta_imagenes, "KGPerfectPenmanship.ttf"), 38)
FUENTE_CUSTOM_INSTR.set_bold(False)
FUENTE_PUNTAJE = pygame.font.Font(os.path.join(ruta_imagenes, "Super Chips.ttf"), 33)

# Carga de imágenes generales (Optimizadas para cargarse 1 sola vez)
IMAGENES_FLECHAS = {
    '↑': pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "BotonVerde.png")), (250, 130)),
    '↓': pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "BotonAzul.png")), (250, 130)),
    '←': pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "BotonRojo.png")), (250, 130)),
    '→': pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "BotonAmarillo.png")), (250, 130)),
}
STICKMAN_ACIERTO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "StickmanAcierto.png")), (190, 200))
STICKMAN_ACIERTO_2 = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "StickmanAcierto2.png")), (190, 200))
STICKMAN_FALLO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "StickmanFallo.png")), (190, 200))
FONDO_IMG = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Fondo5.png")), (800, 700))
FONDO_CUADRO_BASE = pygame.image.load(os.path.join(ruta_imagenes, "CuadroInstrucciones.png"))

# Imágenes UI de pantallas (Movidas aquí para no cargarlas en bucles)
IMG_PANEL_PUNTAJE = pygame.transform.smoothscale(pygame.image.load(os.path.join(ruta_imagenes, "Puntaje.png")), (560, 555))
IMG_BOTON_REINICIAR = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Reiniciar.png")), (220, 110))
IMG_BOTON_SALIR = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Salir2.png")), (190, 90))
IMG_ESTRELLITA = pygame.transform.smoothscale(pygame.image.load(os.path.join(ruta_imagenes, "Estrella.png")), (131, 131))
IMG_ESTRELLA = pygame.transform.smoothscale(pygame.image.load(os.path.join(ruta_imagenes, "Estrella.png")), (169, 169))
IMG_INSTRUCCIONES_TITULO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Instrucciones.png")), (600, 110))
IMG_MODO_TITULO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Seleccionmodo.png")), (735, 125))
IMG_BOTON_NOVATO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Facil.png")), (214, 98))
IMG_BOTON_MEDIO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Medio.png")), (219, 102))
IMG_BOTON_DIFICIL = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Dificil.png")), (240, 124))
IMG_BOTON_JUGAR = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Jugar.png")), (214, 130))
IMG_BOTON_SALIR_INICIO = pygame.transform.scale(pygame.image.load(os.path.join(ruta_imagenes, "Salir1.png")), (205, 104))

# Carga de las imágenes para la zona de juego
IMG_ZONA_1 = pygame.image.load(os.path.join(ruta_imagenes, "PulVerde.png"))
IMG_ZONA_2 = pygame.image.load(os.path.join(ruta_imagenes, "PulAzul.png"))
IMG_ZONA_3 = pygame.image.load(os.path.join(ruta_imagenes, "PulRojo.png"))
IMG_ZONA_4 = pygame.image.load(os.path.join(ruta_imagenes, "PulAmarillo.png"))

size_img = (250, 130)
img_z1 = pygame.transform.scale(IMG_ZONA_1, size_img)
img_z2 = pygame.transform.scale(IMG_ZONA_2, size_img)
img_z3 = pygame.transform.scale(IMG_ZONA_3, size_img)
img_z4 = pygame.transform.scale(IMG_ZONA_4, size_img)

pos_z1 = (ANCHO // 2 - 250, 525)
pos_z2 = (ANCHO // 2 - 404, 525)
pos_z3 = (ANCHO // 2 + 15, 525)
pos_z4 = (ANCHO // 2 + 154, 525)

# Configuración de flechas
DIRECCIONES = ['↑', '↓', '←', '→']
# B = Verde (Arriba), A = Azul (Abajo), C = Rojo (Izquierda), D = Amarillo (Derecha)
LETRAS_SERIAL = {'B': '↑', 'A': '↓', 'C': '←', 'D': '→'}
POSICIONES_FLECHAS = {'↑': ANCHO // 2 - 200, '↓': ANCHO // 2 - 355, '←': ANCHO // 2 + 61, '→': ANCHO // 2 + 202}
ZONA_ACTIVACION_Y = 590
ALTURA_ZONA = 150
VELOCIDAD_FLECHA = 2
TOTAL_RONDAS = 20

# --- OPTIMIZACIÓN: PRECALCULAR EL RESPLANDOR (GLOW) ---
glow_ancho, glow_alto = ANCHO - 100, ALTURA_ZONA
SUPERFICIE_GLOW = pygame.Surface((glow_ancho + 60, glow_alto + 60), pygame.SRCALPHA)
for i in range(1, 26):
    intensidad = int(8 + 247 * (1 - (i / 25))**1.5)
    color = (0, 255, 255, intensidad)
    pygame.draw.rect(SUPERFICIE_GLOW, color, (30 - i, 30 - i, glow_ancho + i * 2, glow_alto + i * 2), width=2, border_radius=10)
pygame.draw.rect(SUPERFICIE_GLOW, (255, 255, 255, 255), (30, 30, glow_ancho, glow_alto), width=2, border_radius=10)


class Flecha:
    def __init__(self, direccion):
        self.direccion = direccion
        self.x = POSICIONES_FLECHAS[direccion]
        self.y = -50
        self.activa = True
        self.imagen = IMAGENES_FLECHAS[direccion]
    def mover(self):
        self.y += VELOCIDAD_FLECHA
        if self.y > ALTO + 50: self.activa = False
    def dibujar(self, ventana):
        ventana.blit(self.imagen, (self.x - 50, self.y - 50))

class Muñeco:
    def __init__(self):
        self.x = 370
        self.y = ALTO - 210
        self.estado = "fallo"
        self.timer_acierto = 0
        self.frame_actual = 1  # <--- NUEVO: Controla qué animación mostrar

    def cambiar_estado(self, estado):
        if estado == "acierto":
            self.estado = "acierto"
            self.timer_acierto = pygame.time.get_ticks()
            
            # ---  Alternar entre la imagen 1 y la 2 ---
            if self.frame_actual == 1:
                self.frame_actual = 2
            else:
                self.frame_actual = 1
        else: 
            self.estado = "fallo"

    def dibujar(self, ventana):
        tiempo_actual = pygame.time.get_ticks()
        if self.estado == "acierto" and tiempo_actual - self.timer_acierto > 500: 
            self.estado = "fallo"
            
        if self.estado == "acierto":
            if self.frame_actual == 1:
                imagen = STICKMAN_ACIERTO
            else:
                imagen = STICKMAN_ACIERTO_2
        else:
            imagen = STICKMAN_FALLO
            
        ventana.blit(imagen, (self.x - 60, self.y))

def dibujar_fondo():
    VENTANA.blit(FONDO_IMG, (0, 0))

def dibujar_zona_activacion():
    x, y = (ANCHO - glow_ancho) // 2, ZONA_ACTIVACION_Y - ALTURA_ZONA // 2
    VENTANA.blit(SUPERFICIE_GLOW, (x - 30, y - 30))

def render_texto_con_borde(texto, fuente, color_texto, color_borde):
    base = fuente.render(texto, True, color_texto)
    superficie = pygame.Surface((base.get_width() + 2, base.get_height() + 2), pygame.SRCALPHA)
    for dx in range(-1, 2):
        for dy in range(-1, 2):
            if dx != 0 or dy != 0:
                superficie.blit(fuente.render(texto, True, color_borde), (dx + 1, dy + 1))
    superficie.blit(base, (1, 1))
    return superficie


# --- PANTALLAS DEL JUEGO ---
def pantalla_instrucciones():
    esperando = True
    progreso = 0
    velocidad_escritura = 0.5
    reloj = pygame.time.Clock()

    lineas = [
        "Pase la mano o la pierna por encima  ",
        "del  sensor  del   mismo   color   que    ",
        "el   indicador   de   su   extremidad,  ",
        "únicamente  cuando  los  círculos se ",
        "encuentren dentro del recuadro ",
        "blanco", "",
        "Presiona CUALQUIER TECLA", "para continuar..."
    ]
    total_caracteres = sum(len(l) for l in lineas)

    ancho_caja, alto_caja = 750, 525
    x_caja = (ANCHO // 2) - (ancho_caja // 2)
    y_caja = 140
    cuadro_inst = pygame.transform.scale(FONDO_CUADRO_BASE, (ancho_caja, alto_caja))

    while esperando:
        reloj.tick(60)
        dibujar_fondo()
        VENTANA.blit(cuadro_inst, (x_caja, y_caja))
        VENTANA.blit(IMG_INSTRUCCIONES_TITULO, (ANCHO // 2 - IMG_INSTRUCCIONES_TITULO.get_width() // 2, 60))

        texto_x, texto_y = 90, 200
        caracteres_acumulados = 0
        for i, linea in enumerate(lineas):
            if int(progreso) > caracteres_acumulados:
                limite_linea = int(progreso) - caracteres_acumulados
                texto_parcial = linea[:limite_linea]
                if "Presiona" in linea or "continuar" in linea:
                    texto_render = FUENTE_CUSTOM_INSTR.render(texto_parcial, True, NEGRO)
                else:
                    texto_render = render_texto_con_borde(texto_parcial, FUENTE_CUSTOM_INSTR, BLANCO, NEGRO)
                VENTANA.blit(texto_render, (texto_x, texto_y + i * 45))
            caracteres_acumulados += len(linea)

        if progreso < total_caracteres: progreso += velocidad_escritura
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                if progreso < total_caracteres: progreso = total_caracteres
                else: esperando = False

def pantalla_instrucciones_2():
    esperando = True
    progreso = 0
    velocidad_escritura = 0.5
    reloj = pygame.time.Clock()

    lineas = [
        "En caso de no pasar por encima del ",
        "sensor, no se obtendrán puntos   ",
        "negativos; sin embargo, si se pasa  ",
        "por encima de un sensor incorrecto, ",
        "se sumará un punto negativo.",
        "Todas las rondas son de 20 puntos.", "",
        "Presiona CUALQUIER TECLA ", "para continuar..."
    ]
    total_caracteres = sum(len(l) for l in lineas)

    ancho_caja, alto_caja = 750, 525
    x_caja = (ANCHO // 2) - (ancho_caja // 2)
    y_caja = 140
    cuadro_inst = pygame.transform.scale(FONDO_CUADRO_BASE, (ancho_caja, alto_caja))

    while esperando:
        reloj.tick(60)
        dibujar_fondo()
        VENTANA.blit(cuadro_inst, (x_caja, y_caja))
        VENTANA.blit(IMG_INSTRUCCIONES_TITULO, (ANCHO // 2 - IMG_INSTRUCCIONES_TITULO.get_width() // 2, 60))

        texto_x, texto_y = 90, 200
        caracteres_acumulados = 0
        for i, linea in enumerate(lineas):
            if int(progreso) > caracteres_acumulados:
                limite_linea = int(progreso) - caracteres_acumulados
                texto_parcial = linea[:limite_linea]
                if "Presiona" in linea or "continuar" in linea:
                    texto_render = FUENTE_CUSTOM_INSTR.render(texto_parcial, True, NEGRO)
                else:
                    texto_render = render_texto_con_borde(texto_parcial, FUENTE_CUSTOM_INSTR, BLANCO, NEGRO)
                VENTANA.blit(texto_render, (texto_x, texto_y + i * 45))
            caracteres_acumulados += len(linea)

        if progreso < total_caracteres: progreso += velocidad_escritura
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN or evento.type == pygame.MOUSEBUTTONDOWN:
                if progreso < total_caracteres: progreso = total_caracteres
                else: esperando = False

def choose_difficulty():
    selecting = True
    rect1 = IMG_BOTON_NOVATO.get_rect(topleft=(ANCHO // 2 - IMG_BOTON_NOVATO.get_width() // 2, 280))
    rect2 = IMG_BOTON_MEDIO.get_rect(topleft=(ANCHO // 2 - IMG_BOTON_MEDIO.get_width() // 2, 370))
    rect3 = IMG_BOTON_DIFICIL.get_rect(topleft=(ANCHO // 2 - IMG_BOTON_DIFICIL.get_width() // 2, 448))

    while selecting:
        dibujar_fondo()
        VENTANA.blit(IMG_MODO_TITULO, (ANCHO // 2 - IMG_MODO_TITULO.get_width() // 2, 130))
        VENTANA.blit(IMG_BOTON_NOVATO, rect1.topleft)
        VENTANA.blit(IMG_BOTON_MEDIO, rect2.topleft)
        VENTANA.blit(IMG_BOTON_DIFICIL, rect3.topleft)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT: pygame.quit(); sys.exit()
            
            # --- AQUÍ CONFIGURAS VELOCIDAD Y RAPIDEZ ---
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if rect1.collidepoint(event.pos): return 1, 240 # facil
                    if rect2.collidepoint(event.pos): return 1, 230 # Medio
                    if rect3.collidepoint(event.pos): return 2, 220 # Difícil

def pantalla_inicio():
    corriendo = True
    titulo_surface = render_texto_con_borde("DYNAMIC BEAT", FUENTE_TITULO_GRANDE, NARANJA, NEGRO)
    rect_jugar = IMG_BOTON_JUGAR.get_rect(topleft=(ANCHO//2 - IMG_BOTON_JUGAR.get_width()//2, 320))
    rect_salir = IMG_BOTON_SALIR_INICIO.get_rect(topleft=(ANCHO//2 - IMG_BOTON_SALIR_INICIO.get_width()//2, 440))

    while corriendo:
        dibujar_fondo()
        VENTANA.blit(titulo_surface, (ANCHO//2 - titulo_surface.get_width()//2, 150))
        VENTANA.blit(IMG_BOTON_JUGAR, rect_jugar.topleft)
        VENTANA.blit(IMG_BOTON_SALIR_INICIO, rect_salir.topleft)
        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if rect_jugar.collidepoint(evento.pos): corriendo = False
                    if rect_salir.collidepoint(evento.pos): pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE: corriendo = False
                if evento.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()

def pantalla_final(aciertos, fallos):
    corriendo = True
    rect_panel = IMG_PANEL_PUNTAJE.get_rect(center=(ANCHO // 2, 310)) # Panel arriba
    rect_reiniciar = IMG_BOTON_REINICIAR.get_rect(center=(ANCHO // 2 - 100, 560)) # Botón izq
    rect_salir = IMG_BOTON_SALIR.get_rect(center=(ANCHO // 2 + 100, 560)) # Botón der
    if aciertos >=1 and aciertos <= 5:
         num_estrellas = 1
    elif aciertos >=6 and aciertos <= 14:
        num_estrellas = 2
    elif aciertos >=15:
        num_estrellas = 3
    else:
        num_estrellas = 0
    while corriendo:
        dibujar_fondo()
        VENTANA.blit(IMG_PANEL_PUNTAJE, rect_panel.topleft)
        #posicion de las estrellas
        pos_estrella_izq = (241, 281)
        pos_estrella_centro = (316, 229)
        pos_estrella_der = (430, 279)

        # Se dibujan según la cantidad ganada
        if num_estrellas >= 1:
            VENTANA.blit(IMG_ESTRELLITA, pos_estrella_izq)
        if num_estrellas >= 2:
            VENTANA.blit(IMG_ESTRELLITA, pos_estrella_der)
        if num_estrellas == 3:
            VENTANA.blit(IMG_ESTRELLA, pos_estrella_centro)
        texto_puntaje = render_texto_con_borde(str(aciertos), FUENTE_PUNTAJE, BLANCO, MARRON)
        VENTANA.blit(texto_puntaje, (420, 410)) 
        VENTANA.blit(IMG_BOTON_REINICIAR, rect_reiniciar.topleft)
        VENTANA.blit(IMG_BOTON_SALIR, rect_salir.topleft)
        
        pygame.display.update()
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()
            if evento.type == pygame.MOUSEBUTTONDOWN:
                if evento.button == 1:
                    if rect_reiniciar.collidepoint(evento.pos):
                        main() # Reinicia el juego
                    if rect_salir.collidepoint(evento.pos):
                        pygame.quit(); sys.exit() # Sale del juego

            # Mantenemos las teclas por si acaso
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_r: main()
                if evento.key == pygame.K_ESCAPE: pygame.quit(); sys.exit()


def main():
    global VELOCIDAD_FLECHA
    pantalla_inicio()
    pantalla_instrucciones()      
    pantalla_instrucciones_2()    
    VELOCIDAD_FLECHA, intervalo = choose_difficulty()
   
    flechas, contador, aciertos, fallos = [], 0, 0, 0
    reloj, muñeco = pygame.time.Clock(), Muñeco()

    flechas, contador, aciertos, fallos = [], 0, 0, 0
    reloj, muñeco = pygame.time.Clock(), Muñeco()
    
    # --- NUEVO: Control de antirrebote ---
    tiempo_ultimo_comando = {'B': 0, 'A': 0, 'C': 0, 'D': 0}
    TIEMPO_COOLDOWN = 400  # Milisegundos que el sistema ignorará esa misma letra
   
    while True:
        reloj.tick(60)
        dibujar_fondo()
        if contador % intervalo == 0 and len(flechas) < TOTAL_RONDAS:
            flechas.append(Flecha(random.choice(DIRECCIONES)))
        contador += 1

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT: pygame.quit(); sys.exit()

        # --- NUEVA LÓGICA DE DETECCIÓN SENSORIAL (CORREGIDA PARA FRASES) ---
        if puerto_serial is not None and puerto_serial.in_waiting > 0:
            try:
                # 1. Leemos la LÍNEA COMPLETA (readline) en lugar de un byte
                linea_entrada = puerto_serial.readline().decode('utf-8').strip().upper()
                tiempo_actual = pygame.time.get_ticks()
                
                # 2. Filtramos: Solo nos importan las líneas que contengan la flecha "->"
                if "->" in linea_entrada:
                    
                    # 3. Cortamos el texto por la flecha y nos quedamos con lo de la derecha ([-1])
                    dato_entrada = linea_entrada.split("->")[-1].strip()
                    
                    if dato_entrada in LETRAS_SERIAL:
                        
                        # Antirrebote
                        if tiempo_actual - tiempo_ultimo_comando[dato_entrada] > TIEMPO_COOLDOWN:
                            tiempo_ultimo_comando[dato_entrada] = tiempo_actual 
                            
                            dir_pres = LETRAS_SERIAL[dato_entrada]
                            acerto = False
                            
                            for f in flechas:
                                if f.activa and f.direccion == dir_pres and abs(f.y - ZONA_ACTIVACION_Y) < ALTURA_ZONA:
                                    aciertos += 1; f.activa = False; muñeco.cambiar_estado("acierto"); acerto = True; break
                            
                            if not acerto: 
                                fallos += 1; muñeco.cambiar_estado("fallo")
                            
                            puerto_serial.reset_input_buffer()
            except Exception as e:
                pass # Evita que el juego se cierre si hay ruido en el puerto serial

        dibujar_zona_activacion()
        VENTANA.blit(img_z1, pos_z1)
        VENTANA.blit(img_z2, pos_z2)
        VENTANA.blit(img_z3, pos_z3)
        VENTANA.blit(img_z4, pos_z4)

        for f in flechas:
            f.mover()
            if f.activa: f.dibujar(VENTANA)
       
        flechas = [f for f in flechas if f.activa]
        muñeco.dibujar(VENTANA)

        # Renderizado del HUD
        texto_stats = render_texto_con_borde(f"Puntos: {aciertos}  Fallos: {fallos}", FUENTE, BLANCO, NEGRO)
        ancho_cuadro_hud = texto_stats.get_width() + 40
        alto_cuadro_hud = texto_stats.get_height() + 20
        cuadro_hud = pygame.transform.scale(FONDO_CUADRO_BASE, (ancho_cuadro_hud, alto_cuadro_hud))
       
        VENTANA.blit(cuadro_hud, (10, 10))
        VENTANA.blit(texto_stats, (30, 20))
       
        pygame.display.update()
        if aciertos + fallos >= TOTAL_RONDAS:
            pygame.time.wait(1000); pantalla_final(aciertos, fallos)

main()
