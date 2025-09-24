# Proyecto Sorteo San Valentín CTS

Aplicación Full Stack para gestionar un sorteo de San Valentín.  
El premio consiste en una estadía de 2 noches todo pagado para una pareja en un hotel.

---

## Descripción general

El sistema permite:

- Registro de usuarios con validación de correo.
- Creación de contraseña para activar la cuenta.
- Confirmación automática de participación en el sorteo.
- Gestión de concursantes por parte del administrador.
- Selección aleatoria de un ganador.
- Notificación automática por correo al ganador.

---

## Tecnologías usadas

### Backend
- Python 3.x
- Django
- Django REST Framework
- Celery + Redis (tareas asíncronas, envío de correos)

### Frontend
- Vue.js (con Vite)

### Base de datos
- SQLite (entorno de desarrollo, opción de migrar a PostgreSQL o MySQL)

---

## Flujo de la aplicación

1. **Inscripción**: El usuario se registra con sus datos.  
2. **Validación de correo**: No se permiten registros duplicados.  
3. **Verificación**: Se envía un correo con un enlace de activación.  
4. **Creación de contraseña**: Tras verificar, el usuario activa su cuenta.  
5. **Confirmación**: El sistema confirma la participación en el sorteo.  
6. **Selección del ganador**: El admin selecciona al azar un ganador válido.  
7. **Notificación**: Se envía correo automático al ganador.  

---

## Estructura del proyecto

```
frontend/       # Código fuente Vue.js
backend/        # Código fuente Django
prueba_cts/     # Configuración principal del proyecto Django
db.sqlite3      # Base de datos (desarrollo)
manage.py
requirements.txt
```

---

## Instrucciones de instalación y ejecución

### Frontend

```bash
cd frontend
npm install     # Instalar dependencias
npm run dev     # Iniciar servidor de desarrollo
```

Disponible en: [http://localhost:3000](http://localhost:3000)  

### Backend

Para configurar el backend, solo debes ejecutar el script setup_backend.sh que se encuentra dentro del directorio backend. Este script se encargará de:

Crear el entorno virtual (si no existe)
Activarlo
Actualizar pip
Instalar las dependencias desde requirements.txt
Ejecutar las migraciones necesarias

Pasos para ejecutar el script de configuración
En la terminal, navega a la carpeta backend:

1. Activar entorno virtual:  
   ```bash
   cd backend
   ```

2. Dale permiso de ejecución al script (solo la primera vez):
   ```bash
   chmod +x setup_backend.sh
   ```

3. Ejecuta el script:
   ```bash
   ./setup_backend.sh
   ```

#### Iniciar servidor y celery
Luego de que el script haya terminado puedes iniciar el servidor Django y celery con:

```bash
   python manage.py runserver 8000
```
```bash
celery -A prueba_cts worker --loglevel=info
```
---

## Eliminación de usuarios en Django

### Eliminar **todos los usuarios**

```bash
python manage.py shell
```

```python
from core.models import Usuario
Usuario.objects.all().delete()
```

### Eliminar solo **usuarios no verificados**

```python
Usuario.objects.filter(verificado=False).delete()
```

**Advertencia:** La eliminación es irreversible. Haz respaldo si es necesario.  

---

## Endpoints principales

| Método | Endpoint                  | Descripción |
|--------|---------------------------|-------------|
| POST   | `/api/registro/`          | Registro de usuario |
| POST   | `/api/verificar-correo/`  | Verificación de correo |
| POST   | `/api/generar-ganador/`   | Selección de ganador (admin) |
| POST   | `/api/login/`             | Login de administrador |

---

## Ejemplos con cURL

### Registro
```bash
curl --location 'http://localhost:8000/api/registro/' --header 'Content-Type: application/json' --data-raw '{"username": "usuario1","email": "usuario1@ejemplo.com","telefono": "123456789","password":"random"}'
```

### Verificación de correo
```bash
curl --location 'http://localhost:8000/api/verificar-correo/' --header 'Content-Type: application/json' --data '{"id": "13"}'
```

### Generar ganador (admin)
```bash
curl --location --request POST 'http://localhost:8000/api/generar-ganador/' --header 'Content-Type: application/json'
```

### Login admin
```bash
curl --location 'http://localhost:8000/api/login/' --header 'Content-Type: application/json' --data '{"username": "admin", "password": "adminpass"}'
```

---

## Configuración SMTP en Django

En `settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'tu_correo@gmail.com'
EMAIL_HOST_PASSWORD = 'tu_contraseña_app'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
```

### 🔹 Pasos para Gmail
1. Activa **verificación en dos pasos (2FA)**.  
2. Genera una **contraseña de aplicación** en [Google Security](https://myaccount.google.com/security).  
3. Usa esa clave en `EMAIL_HOST_PASSWORD`.  

Si usas otro proveedor SMTP, ajusta host y puerto según corresponda.  

---

## Notas finales

- Este proyecto está en **modo desarrollo** con SQLite.  
- Se recomienda migrar a **PostgreSQL** o **MySQL** en producción.  
- Configura **celery + redis** correctamente para un entorno real.  

---

Desarrollado para **CTS - Sorteo San Valentín** 
