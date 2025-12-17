"""
GIF Compressor Pro - Batch Processing Tool
------------------------------------------
Herramienta profesional para compresión de GIFs con auto-diagnóstico de dependencias.

@author  EGherarld
@co-author Gemini AI
@version 1.1.0 (Robust Check)
@license MIT
"""

import os
import sys
import shutil
import subprocess
import glob
import re
import time
import platform

# --- 1. VERIFICACIÓN DE DEPENDENCIAS (Antes de cualquier cosa) ---
def check_system_health():
    """
    Verifica que las herramientas necesarias estén instaladas.
    Si falta alguna, genera las instrucciones exactas y detiene el script.
    """
    missing_tools = []
    install_instructions = []
    
    # A. Verificar Gifsicle (Herramienta del sistema)
    if shutil.which("gifsicle") is None:
        missing_tools.append("Gifsicle (Motor de compresión)")
        
        # Detectar sistema para sugerir comando
        system_os = platform.system().lower()
        if "darwin" in system_os: # Mac
            install_instructions.append("brew install gifsicle")
        elif "linux" in system_os:
            install_instructions.append("sudo apt install gifsicle")
        else: # Windows
            install_instructions.append("Descarga el instalador de: https://www.lcdf.org/gifsicle/")

    # B. Verificar Rich (Librería visual de Python)
    try:
        import rich
    except ImportError:
        missing_tools.append("Rich (Interfaz gráfica en terminal)")
        install_instructions.append(f"{sys.executable} -m pip install rich")

    # Si falta algo, imprimimos el reporte y salimos
    if missing_tools:
        print("\n" + "="*60)
        print("🛑  ¡ALTO AHÍ! FALTAN HERRAMIENTAS")
        print("="*60)
        print("Para que este script funcione correctamente, necesitas instalar:")
        
        for tool in missing_tools:
            print(f" - {tool}")
            
        print("\n💡  SOLUCIÓN RÁPIDA:")
        print("Copia y pega los siguientes comandos en tu terminal:\n")
        
        for cmd in install_instructions:
            print(f"   {cmd}")
            
        print("\n" + "="*60)
        sys.exit(1)

# Ejecutamos el chequeo antes de importar librerías externas
check_system_health()

# --- AHORA SÍ, IMPORTAMOS LO BONITO ---
from rich.console import Console
from rich.table import Table
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn, TimeElapsedColumn
from rich.panel import Panel
from rich.text import Text
from rich import box

# Inicializamos consola
console = Console()

# --- CONSTANTES ---
LOSSY_LEVEL = 120
DELAY_TIME = 8 

def print_banner():
    """Muestra el banner informativo con créditos."""
    title = Text("GIF COMPRESSOR PRO", style="bold white on blue", justify="center")
    
    info_text = """
    [bold yellow]Descripción:[/bold yellow]
    Herramienta de ingeniería para compresión masiva de GIFs.
    Utiliza algoritmos de descomposición (Explode), filtrado de redundancia temporal
    (Frame Drop) y reconstrucción optimizada (Merge + Global Palette).
    
    [bold cyan]Instrucciones:[/bold cyan]
    1. Ingresa la ruta de la carpeta con tus GIFs.
    2. Define el peso máximo deseado (ej. 500kb).
    3. El sistema creará versiones '_compressed' sin tocar los originales.
    
    [bold green]By EGherarld[/bold green] (ft. Gemini AI)
    """
    
    panel = Panel(
        info_text,
        title=title,
        border_style="blue",
        box=box.ROUNDED,
        padding=(1, 2)
    )
    console.print(panel)
    console.print("\n")

def parse_size_to_kb(size_str: str) -> int:
    """Convierte '500kb', '2mb' a enteros KB."""
    size_str = size_str.lower().strip()
    match = re.match(r"(\d+)\s*(mb|kb|b)?", size_str)
    
    if not match: return 500

    value = int(match.group(1))
    unit = match.group(2)

    if unit == "mb": return value * 1024
    elif unit == "b": return value // 1024
    else: return value

def get_file_size_kb(filepath: str) -> int:
    if not os.path.exists(filepath): return 0
    return os.path.getsize(filepath) // 1024

def compress_single_gif(input_path, output_path, target_kb, progress, task_id):
    """Lógica principal de compresión."""
    input_abs = os.path.abspath(input_path)
    output_abs = os.path.abspath(output_path)
    temp_dir = os.path.join(os.path.dirname(output_abs), f"temp_{int(time.time())}_{os.path.basename(input_path)}")
    
    if os.path.exists(temp_dir): shutil.rmtree(temp_dir)
    os.makedirs(temp_dir)

    try:
        progress.update(task_id, description=f"[cyan]Explosionando frames...[/cyan]")
        
        # 1. Explode
        shutil.copy(input_abs, os.path.join(temp_dir, "base.gif"))
        subprocess.run(["gifsicle", "--explode", "base.gif"], cwd=temp_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        progress.update(task_id, description=f"[magenta]Filtrando frames...[/magenta]", advance=30)
        
        # 2. Filter (Drop odd frames)
        frames = sorted(glob.glob(os.path.join(temp_dir, "base.gif.*")))
        preserved_frames = []
        for i, frame in enumerate(frames):
            if i % 2 == 0: preserved_frames.append(frame)
            else: os.remove(frame)

        progress.update(task_id, description=f"[green]Optimizando paleta...[/green]", advance=30)

        # 3. Merge (Global Palette + Lossy)
        cmd_merge = [
            "gifsicle", "--merge", "-O3", 
            f"--lossy={LOSSY_LEVEL}", "--colors=256", f"--delay={DELAY_TIME}"
        ]
        
        frame_names = [os.path.basename(f) for f in preserved_frames]
        cmd_merge.extend(frame_names)
        cmd_merge.extend(["-o", output_abs])

        subprocess.run(cmd_merge, cwd=temp_dir, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        progress.update(task_id, advance=40)
        
        final_size = get_file_size_kb(output_abs)
        
        if final_size <= target_kb: return "SUCCESS", final_size
        else: return "WARN", final_size

    except Exception:
        return "ERROR", 0
    finally:
        if os.path.exists(temp_dir): shutil.rmtree(temp_dir)

def main():
    print_banner()

    # --- INPUT ---
    console.print("[bold white]Configuración:[/bold white]")
    folder_path = console.input("[yellow]📂 Arrastra carpeta de GIFs aquí: [/yellow]").strip().strip("'").strip('"')
    
    if not os.path.isdir(folder_path):
        console.print(f"[bold red]❌ Ruta inválida.[/bold red]")
        return

    size_input = console.input("[yellow]⚖️  Tamaño objetivo (ej. 500kb): [/yellow]").strip()
    target_kb = parse_size_to_kb(size_input)
    
    console.print(f"\n[dim]Meta: {target_kb} KB[/dim]\n")

    gif_files = glob.glob(os.path.join(folder_path, "*.gif"))
    gif_files = [f for f in gif_files if "_compressed" not in f]

    if not gif_files:
        console.print("[bold red]⚠️  No hay GIFs en esta carpeta.[/bold red]")
        return

    # --- PROCESO ---
    results_data = []
    
    with Progress(
        SpinnerColumn("dots"),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TimeElapsedColumn(),
        console=console
    ) as progress:
        
        main_task = progress.add_task("[bold white]Total...[/bold white]", total=len(gif_files))

        for idx, gif_path in enumerate(gif_files, 1):
            filename = os.path.basename(gif_path)
            orig_size = get_file_size_kb(gif_path)
            
            name_p, ext_p = os.path.splitext(filename)
            output_path = os.path.join(folder_path, f"{name_p}_compressed{ext_p}")
            
            file_task = progress.add_task(f"Comprimiendo {filename}...", total=100)
            status, final_size = compress_single_gif(gif_path, output_path, target_kb, progress, file_task)
            
            results_data.append({
                "id": idx, "file": filename, "orig": orig_size, 
                "final": final_size, "status": status
            })
            
            progress.remove_task(file_task)
            progress.advance(main_task)

    # --- TABLA FINAL ---
    console.print("\n")
    table = Table(title="📊 Reporte de Ingeniería", box=box.SIMPLE_HEAD)
    table.add_column("#", justify="right", style="dim")
    table.add_column("Archivo", style="bold white")
    table.add_column("Original", justify="right", style="cyan")
    table.add_column("Final", justify="right", style="magenta")
    table.add_column("Estado", justify="center")

    for row in results_data:
        if row["status"] == "SUCCESS":
            status_str = "[bold green]✅ OPTIMIZADO[/bold green]"
            final_fmt = f"[green]{row['final']} KB[/green]"
        elif row["status"] == "WARN":
            status_str = "[bold orange1]⚠️  CERCA[/bold orange1]"
            final_fmt = f"[yellow]{row['final']} KB[/yellow]"
        else:
            status_str = "[bold red]❌ FALLÓ[/bold red]"
            final_fmt = "[red]0 KB[/red]"

        table.add_row(str(row["id"]), row["file"], f"{row['orig']} KB", final_fmt, status_str)

    console.print(table)
    console.print(f"\n[italic blue]Archivos guardados en: {folder_path}[/italic blue]")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold red]🛑 Cancelado por el usuario.[/bold red]")
        sys.exit(0)