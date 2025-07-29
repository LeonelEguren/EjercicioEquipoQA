Proyecto de Automatización de Pruebas con Playwright (Python) para ejercicio tecnico de testing
Este repositorio contiene un conjunto de pruebas automatizadas usando Playwright con Python y pytest.



**Instalación**
Clonar el repositorio:

git clone https://github.com/LeonelEguren/EjercicioEquipoQA.git

  **Crear un entorno virtual:**

python -m venv venv
source venv/bin/activate     # En Linux/macOS
venv\Scripts\activate        # En Windows
 **Instalar las dependencias:**


pip install 

 **Instalar Playwright y sus navegadores:**

playwright install 

**Configuracion**
Crea un archivo .env para manejar credenciales o variables sensibles:

env

Este archivo está ignorado en .gitignore por seguridad.



**Evidencia**
Las capturas de pantalla de los pasos de prueba se guardan en la carpeta:

/evidencia/

 **Estructura del proyecto**
bash
Copiar
Editar
.
├── tests/
│   └── test_login.py
├── evidencia/
├── .env
├── .gitignore
└── README.md


