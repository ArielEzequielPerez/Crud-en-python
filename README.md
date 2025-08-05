
# Proyecto Django - CRUD

Este proyecto es una aplicación Django con base de datos SQLite.

---

## 🚀 Levantar el proyecto localmente (sin Docker)

### 1. Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
# .\venv\Scripts\activate  # Windows
```

2. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe requirements.txt, podés generarlo con:

pip freeze > requirements.txt

3. Aplicar migraciones

```bash
python3 sistema/manage.py migrate
```

4. Crear superusuario (opcional)

```bash
python3 sistema/manage.py createsuperuser
```
5. Ejecutar el servidor

```bash
python3 sistema/manage.py runserver
```

Accedé a: http://localhost:8000


# 🐳 Levantar el proyecto con Docker y Docker Compose
1. Construir la imagen

```bash
docker compose build
```
2. Levantar los servicios

```bash
docker compose up
```
Accedé a: http://localhost:8000

3. Ejecutar migraciones (dentro del contenedor)

```bash
docker compose exec web python3 sistema/manage.py migrate
```
4. Crear superusuario (opcional)

```bash
docker compose exec web python3 sistema/manage.py createsuperuser
```
5. Debe crear un usuario admin

Para loguearse como admin debe ingresar aqui http://localhost:8000/admin/logout/

La base de datos db.sqlite3 se persiste automáticamente gracias al volumen configurado en compose.yml.
- 🛠 Requisitos

    Python 3.10+

    Docker + Docker Compose (solo para la opción Docker)