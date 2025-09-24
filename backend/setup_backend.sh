#!/bin/bash

# Ruta al entorno virtual
VENV_DIR="env"

# Verificar si existe el entorno virtual
if [ ! -d "$VENV_DIR" ]; then
  echo "Creando entorno virtual en $VENV_DIR ..."
  python3 -m venv "$VENV_DIR"
else
  echo "Entorno virtual ya existe en $VENV_DIR"
fi

# Activar el entorno virtual
source "$VENV_DIR/bin/activate"

# Actualizar pip
echo "Actualizando pip..."
pip install --upgrade pip

# Instalar dependencias
echo "Instalando dependencias usando requirements.txt..."
pip install -r requirements.txt

# Ejecutar migraciones
echo "Aplicando migraciones..."
python manage.py makemigrations core
python manage.py migrate

echo "¡Configuración completada!"