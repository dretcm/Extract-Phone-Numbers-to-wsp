@echo off
REM Nombre del entorno virtual
SET VENV_NAME=env
REM Nombre del archivo de dependencias
SET REQUIREMENTS_FILE=requirements.txt

REM Crear el entorno virtual
echo Creando entorno virtual...
python -m venv %VENV_NAME%

REM Activar el entorno virtual
echo Activando entorno virtual...
CALL %VENV_NAME%\Scripts\activate.bat

REM Verificar si el archivo requirements.txt existe
if not exist %REQUIREMENTS_FILE% (
    echo El archivo %REQUIREMENTS_FILE% no existe. Creando uno por defecto...
    echo regex> %REQUIREMENTS_FILE%
    echo selenium>> %REQUIREMENTS_FILE%
    echo pandas>> %REQUIREMENTS_FILE%
    echo openpyxl>> %REQUIREMENTS_FILE%
)

REM Instalar dependencias desde requirements.txt
echo Instalando dependencias desde %REQUIREMENTS_FILE%...
pip install --upgrade pip
pip install -r %REQUIREMENTS_FILE%

REM Desactivar el entorno virtual
echo Desactivando entorno virtual...
CALL %VENV_NAME%\Scripts\deactivate.bat

REM Confirmación final
echo.
echo Todo listo. El entorno virtual y las dependencias han sido configurados correctamente.
PAUSE
