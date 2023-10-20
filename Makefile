VENV_NAME = venv

.PHONY: env install_dependencies activate_env

# Crea el entorno virtual
venv:
    python3 -m venv $(VENV_NAME)

# Activa el entorno virtual
activate_env:
    source $(VENV_NAME)/bin/activate

# Instala las dependencias en el entorno virtual
install_dependencies: activate_env
    pip install -r requirements.txt

