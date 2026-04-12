#  CDIO3_Eq4_Dynamic_Beat - Dispositivo de Fisioterapia

Este repositorio contiene el código fuente, el diseño de hardware y la documentación técnica correspondiente al desarrollo del Prototipo Mínimo Viable (PMV) de nuestro dispositivo de asistencia fisioterapéutica.

## 📑 Tabla de Contenidos
- [Tecnologías Utilizadas](#-tecnologías-utilizadas)
- [Estado del Proyecto](#-estado-del-proyecto-pmv)
- [Cronograma de Ejecución](#-cronograma-de-ejecución)

## 🛠️ Tecnologías Utilizadas
- **Microcontroladores:** Red de placas ESP32
- **Sensores:** Arreglo de sensores ultrasónicos
- **Diseño de Hardware:** Desarrollo de PCB a medida y modelado de carcasa 3D
- **Validación:** Pruebas de software e interfaz de usuario

## ⚠️ Estado del Proyecto (PMV)
Actualmente contamos con un prototipo base funcional y los siguientes entregables en curso:
- **Gestión:** Lista de materiales (BOM) consolidada y elementos adquiridos.
- **Hardware:** Diseño de circuito base completado; en fase de pruebas físicas.
- **Software:** Pruebas iniciales de software e interfaz superadas.

## 📅 Cronograma de Ejecución

A continuación, se presenta la planificación del proyecto distribuida por semanas académicas y fases de desarrollo:


```mermaid id="x8m4qp"
gantt
    title Plan de Proyecto Dynamic Beat - Semestre 2026-I
    dateFormat YYYY-MM-DD
    axisFormat %d/%m

    section Fase 1 - Diseño y Prototipado
    Lista de Materiales BOM :done, des1, 2026-02-09, 7d
    Adquisición de Componentes :done, des2, after des1, 7d
    Diseño de Circuito Electrónico :done, des3, 2026-02-16, 14d
    Pruebas de Software e Interfaz :done, des4, 2026-02-23, 14d
    Prototipo Base Terminado :milestone, 2026-03-09, 1d

    section Fase 2 - Hardware
    Validación Física Sem 6 y 7 :active, dev1, 2026-03-09, 14d
    Diseño PCB Definitiva Sem 8 :dev2, after dev1, 7d
    Modelado Carcasa 3D Sem 9 :dev3, after dev2, 7d

    section Fase 3 - Integración
    Ensamble y Pruebas Sem 10 :int1, after dev3, 7d
    Validación Operativa Sem 11 :int2, after int1, 7d

    section Fase 4 - Implementación
    Evaluación con Cliente Sem 12 :crit, usr1, after int2, 21d
    Ajustes de Mejora Continua :doc1, after usr1, 7d
    Sustentación Final Sem 15 :milestone, 2026-05-11, 1d
```

