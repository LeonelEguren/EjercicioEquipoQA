from playwright.sync_api import Playwright, sync_playwright, expect
import os
from dotenv import load_dotenv
from datetime import datetime   

load_dotenv()

def guardar_screenshot(page, test_name):
    # Guarda una captura de pantalla en la carpeta 'evidencia' con el nombre del caso de prueba y la fecha.

    evidencia_dir = "evidencia"
    # Generar el nombre del archivo con la fecha actual
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    nombre_archivo = f"{evidencia_dir}/{test_name}_{fecha_actual}.png"

    # Guardar la captura de pantalla
    page.screenshot(path=nombre_archivo)
