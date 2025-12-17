# GIF Compressor Pro Python 🚀

> **Ingeniería de software aplicada a la optimización de assets digitales.**

Herramienta de línea de comandos (CLI) diseñada para la compresión masiva e inteligente de archivos GIF animados. Su algoritmo reduce drásticamente el peso de los archivos (hasta un 60-70%) manteniendo la nitidez crítica en elementos vectoriales y texto. Ideal para firmas de correo electrónico corporativas, banners web y assets de marketing.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Win%20|%20Mac%20|%20Linux-lightgrey?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Gifsicle](https://img.shields.io/badge/Core-Gifsicle-orange?style=for-the-badge)

---

## 📋 Características Principales

Esta herramienta no es un simple script; es una solución de ingeniería robusta:

* **🧩 Compresión "Explode & Merge":** Utiliza una técnica de descomposición de frames para evitar errores de sintaxis y conflictos de argumentos en sistemas UNIX/Mac.
* **⏱️ Reducción Temporal (Frame Drop):** Elimina inteligentemente el 50% de la redundancia temporal (frames pares) reduciendo el peso a la mitad sin perder la esencia de la animación.
* **🎨 Optimización de Paleta Global:** Fuerza una paleta unificada de 256 colores, eliminando el peso muerto de las paletas locales por frame.
* **🌊 Corrección de Fluidez:** Recalcula y ajusta el *delay* (tiempo de exposición) entre frames para compensar la eliminación de imágenes, garantizando una animación suave.
* **📊 Interfaz Profesional:** Implementación de `rich` para visualización de datos en tiempo real (barras de progreso, spinners y tablas de reporte).
* **🛡️ Modo Seguro:** Integridad de datos garantizada. Nunca sobrescribe los originales; genera versiones con el sufijo `_compressed`.
* **🔧 Auto-Diagnóstico:** El sistema verifica sus propias dependencias al inicio y sugiere comandos de reparación si faltan librerías.

---

## 🛠️ Requisitos del Sistema

Para asegurar el funcionamiento correcto, el entorno debe cumplir con:

1.  **Python 3.x** instalado.
2.  **Gifsicle** (Motor de procesamiento de imágenes).
3.  **Librería Rich** (Interfaz gráfica en terminal).

### 📦 Instalación de Dependencias

#### 1. Instalar Gifsicle (Motor Core)

Dependiendo de tu sistema operativo, ejecuta en tu terminal:

* **🍏 MacOS:**
    ```bash
    brew install gifsicle
    ```
* **🐧 Ubuntu/Debian:**
    ```bash
    sudo apt install gifsicle
    ```
* **🪟 Windows:**
    Descargar el instalador desde [lcdf.org/gifsicle](https://www.lcdf.org/gifsicle/) y asegurar que esté agregado a las variables de entorno (PATH).

#### 2. Instalar Dependencias de Python

```bash
pip install rich
```

## 🚀 Modo de Uso

La herramienta está diseñada para ser "Drag & Drop" (arrastrar y soltar) en la terminal.

    Descarga el archivo gif_compressor.py.

    Abre tu terminal en la carpeta donde guardaste el script.

    Ejecuta el comando maestro:

```Bash

python gif_compressor.py
```

    Sigue el asistente interactivo:

        📂 Paso 1: El sistema te pedirá la ruta. Arrastra la carpeta que contiene tus GIFs a la terminal.

        ⚖️ Paso 2: Escribe el peso objetivo (ejemplos válidos: 500kb, 1mb, 200000b).

    Resultado: El sistema procesará el lote completo y mostrará una tabla de ingeniería con el análisis de reducción (Peso Original vs. Peso Final).

## ⚙️ Configuración Avanzada

Si eres desarrollador, puedes ajustar las constantes al inicio del script (gif_compressor.py) para modificar la agresividad del algoritmo:
Python

```bash
# Nivel de compresión con pérdida (invisible en textos)
# Rango recomendado: 80 - 140. Mayor número = Menos peso, más ruido visual.
LOSSY_LEVEL = 120  

# Corrección de tiempo (en centésimas de segundo)
# 8 = 80ms. Aumentar si la animación se siente muy rápida.
DELAY_TIME = 8
```

Con cariño EGherarld
