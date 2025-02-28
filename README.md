# 📌 API de Agendamiento de Citas  

## 🚀 Instalación  

### 1️⃣ Clonar el repositorio  
```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_PROYECTO>
```

### 2️⃣ Crear un entorno virtual (opcional pero recomendado)  
```bash
# En Linux/macOS
python3 -m venv venv  
source venv/bin/activate  

# En Windows
python -m venv venv  
venv\Scripts\activate
```

### 3️⃣ Instalar dependencias  
Ejecuta el siguiente comando para instalar las librerías necesarias:  
```bash
pip install -r requirements.txt
```
Si aún no has creado `requirements.txt`, guárdalo con este contenido:  
```
alembic==1.14.1
blinker==1.9.0
click==8.1.8
colorama==0.4.6
Flask==3.1.0
Flask-Migrate==4.1.0
Flask-MySQLdb==2.0.0
Flask-SQLAlchemy==3.1.1
greenlet==3.1.1
itsdangerous==2.2.0
Jinja2==3.1.5
Mako==1.3.9
MarkupSafe==3.0.2
mysqlclient==2.2.7
python-dotenv==1.0.1
SQLAlchemy==2.0.38
typing_extensions==4.12.2
Werkzeug==3.1.3
```


## 🔧 Configuración  

Crea un archivo `.env` en la raíz del proyecto y define las variables de conexión a la base de datos:  
```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=
MYSQL_DB=api_agendamiento_citas
```


## ▶️ Ejecución  

Para iniciar la API, usa:  
```bash
python app.py
```
Por defecto, se ejecutará en **http://127.0.0.1:5000**.  


## 📌 Funcionalidades implementadas  
✅ Configuración del entorno con Flask y MySQL.  
✅ Registro de pacientes, incluyendo sus datos personales y credenciales de usuario.  
✅ Registro, actualización y eliminación de citas médicas.  
✅ Registro de médicos con su especialidad y datos personales.  
✅ Ruta principal con un formulario de inicio de sesión.  


## 📍 Rutas disponibles  

### 🔹 **Pacientes**  

#### ➕ **Registrar un paciente**  
Registra un paciente junto con sus credenciales.  

- **URL**: `/paciente`  
- **Método**: `POST`  
- **Formato de solicitud (JSON)**:  
```json
{
  "nombre": "Carlos",
  "apellido": "Gómez",
  "numero_documento": "987654321",
  "correo": "carlos@mail.com",
  "clave": "123456"
}
```
- **Respuesta exitosa**:  
```json
{
  "mensaje": "Paciente registrado exitosamente.",
  "exito": true
}
```

---

### 🔹 **Médicos**  

#### ➕ **Registrar un médico**  
Registra un nuevo médico en la base de datos.  

- **URL**: `/medico`  
- **Método**: `POST`  
- **Formato de solicitud (JSON)**:  
```json
{
  "nombre": "Juan",
  "apellido": "Pérez",
  "numero_documento": "123456789",
  "celular": "3112345678",
  "cod_tipo_documento": 1,
  "cod_especialidad": 2
}
```
- **Respuesta exitosa**:  
```json
{
  "mensaje": "Medico registrado exitosamente.",
  "exito": true
}
```
- **Respuesta en caso de error**:  
```json
{
  "mensaje": "Error en el registro: <detalle_del_error>",
  "exito": false
}
```

---

### 🔹 **Citas**  

#### 📋 **Listar todas las citas**  
- **URL**: `/citas`  
- **Método**: `GET`  
- **Respuesta exitosa**:  
```json
{
  "citas": [
    {
      "codigo": 1,
      "nombre": "Consulta General",
      "creditos": 3
    }
  ],
  "mensaje": "Citas listadas.",
  "exito": true
}
```

#### 🔍 **Obtener una cita específica**  
- **URL**: `/citas/<codigo>`  
- **Método**: `GET`  
- **Ejemplo de respuesta**:  
```json
{
  "curso": {
    "codigo": 1,
    "nombre": "Consulta General",
    "creditos": 3
  },
  "mensaje": "Cita encontrada.",
  "exito": true
}
```

#### ➕ **Registrar una nueva cita**  
- **URL**: `/cita`  
- **Método**: `POST`  
- **Formato de solicitud (JSON)**:  
```json
{
  "inicio": "2024-02-28 08:00:00",
  "fin": "2024-02-28 08:30:00",
  "cod_paciente": 1,
  "cod_medico": 2,
  "cod_tipo_cita": 3,
  "cod_estado": 1
}
```
- **Respuesta exitosa**:  
```json
{
  "mensaje": "Cita registrada exitosamente.",
  "exito": true
}
```

#### ✏️ **Actualizar una cita**  
- **URL**: `/cita/<codigo>`  
- **Método**: `PUT`  
- **Ejemplo de solicitud (JSON)**:  
```json
{
  "inicio": "2024-02-28 09:00:00",
  "fin": "2024-02-28 09:30:00",
  "cod_paciente": 1,
  "cod_medico": 2,
  "cod_tipo_cita": 3,
  "cod_estado": 2
}
```
- **Respuesta exitosa**:  
```json
{
  "mensaje": "Cita actualizada exitosamente.",
  "exito": true
}
```

#### ❌ **Eliminar una cita**  
- **URL**: `/cita/<codigo>`  
- **Método**: `DELETE`  
- **Respuesta exitosa**:  
```json
{
  "mensaje": "Cita eliminada exitosamente.",
  "exito": true
}
```
