# GIF Compressor Pro Python 🚀

Herramienta de ingeniería de software para la compresión masiva e inteligente de archivos GIF animados. Diseñada específicamente para reducir drásticamente el peso de los archivos manteniendo la nitidez en elementos vectoriales y texto (ideal para firmas de correo electrónico y banners web).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Gifsicle](https://img.shields.io/badge/Dependency-Gifsicle-orange)

## 📋 Características

* **Compresión Inteligente:** Utiliza la técnica *"Explode & Merge"* para evitar errores de sintaxis en sistemas UNIX/Mac.
* **Reducción Temporal:** Elimina el 50% de los frames (redundancia temporal) para reducir el peso a la mitad.
* **Optimización de Paleta:** Fuerza una paleta global de 256 colores para evitar el peso extra de paletas locales por frame.
* **Corrección de Fluidez:** Ajusta el *delay* entre frames para compensar la eliminación de imágenes y mantener una animación suave.
* **Interfaz Profesional:** Utiliza la librería `rich` para mostrar barras de progreso, spinners de carga y tablas de resultados coloreadas.
* **Auto-Diagnóstico:** El script verifica automáticamente si tienes las dependencias instaladas y te dice cómo corregirlo si falta algo.
* **Modo Seguro:** No sobrescribe tus archivos originales; genera copias con el sufijo `_compressed`.

## 🛠️ Requisitos del Sistema

Para ejecutar esta herramienta necesitas:

1.  **Python 3.x** instalado.
2.  **Gifsicle** (Motor de procesamiento de imágenes).
3.  **Librería Rich** (Para la interfaz gráfica en terminal).

### Instalación de Dependencias

**1. Instalar Gifsicle:**

* **MacOS:** `brew install gifsicle`
* **Ubuntu/Debian:** `sudo apt install gifsicle`
* **Windows:** Descargar instalador de [lcdf.org/gifsicle](https://www.lcdf.org/gifsicle/) y agregar al PATH.

**2. Instalar Librería de Python:**

```bash
pip install rich

🚀 Modo de Uso

    Descarga el archivo gif_compressor.py.

    Abre tu terminal en la carpeta donde está el script.

    Ejecuta el siguiente comando:

Bash

python gif_compressor.py

    Sigue las instrucciones en pantalla:

        Arrastra la carpeta que contiene tus GIFs.

        Escribe el peso objetivo (ejemplo: 500kb o 1mb).

El sistema procesará todos los GIFs de la carpeta y generará una tabla con los resultados finales.
⚙️ Configuración Avanzada

Puedes modificar las constantes al inicio del script para ajustar la agresividad de la compresión:
Python

LOSSY_LEVEL = 120  # Nivel de pérdida visual (Mayor = menos peso, más ruido)
DELAY_TIME = 8     # Velocidad de animación (8 = 80ms por frame)

🤝 Créditos

Desarrollado con ❤️ y lógica pura.

    Autor: EGherarld

    Co-Autor: Gemini AI (Google)

📄 Licencia

Este proyecto está bajo la Licencia MIT. Eres libre de usarlo, modificarlo y distribuirlo, siempre y cuando mantengas la atribución al autor original.


---

### 3. El Tipo de Licencia

Para este tipo de herramientas, la mejor licencia es la **MIT License**.

**¿Por qué?**
* Es la más popular y "amigable" en el mundo del código abierto.
* Permite que cualquiera use tu script (incluso para fines comerciales en su empresa).
* La única condición es que **deben mantener tu nombre (EGherarld)** en el archivo de licencia o en el código.
* Te protege a ti: Dice explícitamente que el software se entrega "tal cual" y no eres responsable si alguien borra sus archivos por error (aunque tu script ya protege contra eso).

Aquí tienes el texto para poner en un archivo llamado `LICENSE`:

```text
MIT License

Copyright (c) 2025 EGherarld

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
