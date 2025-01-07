@echo off
REM Ruta al entorno virtual
SET VENV_PATH=env

REM Activar el entorno virtual
CALL %VENV_PATH%\Scripts\activate.bat

REM Ejecutar el script Python
python main.py

REM Desactivar el entorno virtual
CALL %VENV_PATH%\Scripts\deactivate.bat

REM Pausa para que puedas leer la salida antes de que la ventana se cierre
PAUSE
