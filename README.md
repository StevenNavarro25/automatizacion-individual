# Automatización de Formularios Web

Este proyecto permite automatizar el llenado de formularios web utilizando Python y Selenium, tomando los datos desde un archivo CSV.

## Requisitos
- Python 3.8 o superior
- Google Chrome
- ChromeDriver compatible con tu versión de Chrome
- Las dependencias listadas en `requirements.txt`

## Instalación
1. Clona o descarga este repositorio.
2. Instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   ```
3. Asegúrate de tener el archivo `datos.csv` en la raíz del proyecto con la estructura adecuada.

## Uso
1. Activa el entorno virtual si lo tienes:
   ```bash
   source .venv/Scripts/activate
   ```
2. Ejecuta el script principal:
   ```bash
   python formulario.py
   ```

## Personalización
- **Ruta del archivo CSV:**
  Si tu archivo de datos no se llama `datos.csv` o está en otra ubicación, modifica la ruta en el script `formulario.py` donde se carga el CSV.
- **Carga de archivos:**
  Si el formulario requiere cargar archivos, asegúrate de que las rutas sean absolutas y válidas en tu sistema. Modifica las rutas en el script si es necesario.
- **URLs y Selectores:**
  Si el formulario web cambia de URL o estructura, actualiza las URLs y selectores en el script `formulario.py`.