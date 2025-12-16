# 🐱 Cat API - API REST de Razas de Gatos

<div align="center">

<img src="https://raw.githubusercontent.com/Pal-cloud/cat_api/main/public/api_cats.png" alt="Banner API Cats" width="400" height="150" style="object-fit: cover;">

**Una API REST completa y personalizada para explorar las razas de gatos más populares del mundo** 🌍

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com/)
[![API](https://img.shields.io/badge/API-REST-orange.svg)](https://restfulapi.net/)
[![Cats](https://img.shields.io/badge/🐱-Cat_API-purple.svg)](#-razas-incluidas)

</div>

---

## 🚀 **Inicio Rápido**

### ⚡ **1 minuto para empezar:**

```bash
# 1. Clona o descarga el proyecto
git clone https://github.com/Pal-cloud/cat_api.git

# 2. Instala dependencias
pip install flask requests

# 3. ¡Inicia tu API!
python api_razas_gatos.py
```

### 🌐 **Enlaces directos (una vez iniciada):**
| 🔗 Endpoint | 📝 Descripción | 🌍 URL |
|-------------|----------------|---------|
| **🏠 Principal** | Información de la API | http://127.0.0.1:5000/ |
| **🐾 Todas las razas** | Ver las 4 razas completas | http://127.0.0.1:5000/razas |
| **📊 Estadísticas** | Datos y métricas | http://127.0.0.1:5000/estadisticas |
| **⭐ Populares** | Razas más queridas | http://127.0.0.1:5000/razas/populares |

---

## 🐱 **Razas Incluidas**

Tu API viene **precargada** con 4 razas fascinantes:

| 🐾 Raza | 🌍 Origen | ⭐ Popularidad | 📏 Tamaño | 🎨 Temperamento |
|---------|-----------|----------------|-----------|-----------------|
| **Persa** | 🇮🇷 Irán | 9/10 | Mediano | Tranquilo, Dulce |
| **Maine Coon** | 🇺🇸 Estados Unidos | 8/10 | Grande | Amigable, Sociable |
| **Siamés** | 🇹🇭 Tailandia | 7/10 | Mediano | Vocal, Inteligente |
| **Ragdoll** | 🇺🇸 Estados Unidos | 8/10 | Grande | Relajado, Dócil |

---

## 🛠️ **Características de la API**

### ✨ **Funcionalidades completas:**
- 🔍 **CRUD Completo** - Crear, Leer, Actualizar, Eliminar razas
- 📊 **Filtros Avanzados** - Por tamaño, origen, popularidad
- 📈 **Estadísticas** - Métricas automáticas y análisis
- 🎯 **Búsquedas** - Por país de origen y características
- ✅ **Validación** - Datos consistentes y seguros

### 🔗 **Endpoints Disponibles:**

```http
GET    /                           # Información de la API
GET    /razas                      # Todas las razas
POST   /razas                      # Agregar nueva raza
PUT    /razas/{id}                 # Actualizar raza
DELETE /razas/{id}                 # Eliminar raza
GET    /razas/populares            # Razas populares (≥7)
GET    /razas/tamano/{tamaño}      # Filtrar por tamaño
GET    /razas/origen/{país}        # Filtrar por origen
GET    /estadisticas               # Métricas generales
```

---

## 📚 **Archivos del Proyecto**

| 📁 Archivo | 📝 Descripción |
|------------|----------------|
| **`api_razas_gatos.py`** | 🚀 API principal con todas las funciones |
| **`test_api_razas_gatos.py`** | 🧪 Script de pruebas automáticas |
| **`inicio_rapido.py`** | ⚡ Iniciador rápido con navegador |
| **`requirements.txt`** | � Dependencias del proyecto |
| **`public/api_cats.png`** | 🖼️ Banner e imagen del proyecto |

---

## 🎯 **Ejemplos de Uso**

### **Ver todas las razas:**
```bash
curl http://127.0.0.1:5000/razas
```

### **Agregar una nueva raza:**
```bash
curl -X POST http://127.0.0.1:5000/razas \
  -H "Content-Type: application/json" \
  -d '{
    "nombre": "British Shorthair",
    "origen": "Reino Unido",
    "popularidad": 8,
    "tamaño": "mediano"
  }'
```

### **Ver estadísticas:**
```bash
curl http://127.0.0.1:5000/estadisticas
```

---

## 🎨 **Personalización Avanzada**

¿Quieres llevar tu API al siguiente nivel? Aquí tienes ideas geniales:

### 🔧 **Agregar más campos a las razas:**
```python
# En api_razas_gatos.py, función crear_raza():
'energia': datos.get('energia', 5),          # 1-10
'sociabilidad': datos.get('sociabilidad', 5),
'nivel_ruido': datos.get('nivel_ruido', 5),
'facilidad_cuidado': datos.get('facilidad_cuidado', 5),
'imagen_url': datos.get('imagen_url', '')
```

### 🎯 **Nuevos endpoints especializados:**
```python
# Razas perfectas para apartamentos
@app.route('/razas/apartamento', methods=['GET'])
def razas_apartamento():
    return [r for r in razas_gatos 
            if r['tamaño'] in ['pequeño', 'mediano'] 
            and 'tranquilo' in r['temperamento']]

# Razas ideales para familias con niños  
@app.route('/razas/familia', methods=['GET'])
def razas_familia():
    return [r for r in razas_gatos 
            if 'amigable' in r['temperamento'] 
            or 'sociable' in r['temperamento']]
```

### 🌍 **Cambiar el tema completamente:**
- **🌿 API de Plantas** - Especies, cuidados, estaciones
- **📚 API de Libros** - Tu biblioteca personal
- **🍳 API de Recetas** - Ingredientes, dificultad, tiempo
- **🏋️ API de Ejercicios** - Rutinas y seguimiento

### 🗄️ **Upgrade a base de datos:**
```python
# Instalar: pip install sqlite3
import sqlite3

def crear_tabla():
    conn = sqlite3.connect('razas_gatos.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE razas (
            id TEXT PRIMARY KEY,
            nombre TEXT NOT NULL,
            origen TEXT,
            descripcion TEXT,
            popularidad INTEGER
        )
    ''')
    conn.commit()
    conn.close()
```

---

## 🎨 **Personalización**

¿Quieres adaptar la API a tu gusto? ¡Perfecto!

- 🔧 **Agregar campos:** Edad, peso, cuidados específicos
- 🌍 **Cambiar datos:** Otras mascotas, plantas, libros, etc.
- 🎯 **Nuevas funciones:** Filtros, búsquedas, imágenes

---

## 🧪 **Pruebas**

### **Pruebas automáticas:**
```bash
python test_api_razas_gatos.py
```

### **Inicio con navegador:**
```bash
python inicio_rapido.py
```

---

## ¿Qué es una API?

✔ Definición

Una API (Application Programming Interface) es un conjunto de reglas que permite que dos aplicaciones se comuniquen entre sí.

Ejemplos:

    • Una app del clima consultando un servidor de meteorología.

    • Un frontend web pidiéndole datos a un backend.

## ¿Qué es una API REST?

✔ Definición API Web / API REST

Cuando hablamos de API REST generalmente nos referimos a APIs que funcionan sobre HTTP siguiendo ciertos principios:

📌 Principios REST

    • Cliente - Servidor: Frontend y backend separados.

    • Sin estado (stateless): Cada petición contiene toda la información necesaria.

    • Recursos: Todo se modela como recursos (usuarios, productos, posts…).

    • Métodos HTTP: GET, POST, PUT, DELETE para operaciones.

    • Representaciones: JSON, XML para transferir datos.

## ¿Qué es CRUD?

✔ Definición CRUD

CRUD es un acrónimo para las operaciones básicas en bases de datos:

    • Create (Crear): Agregar nuevos datos.

    • Read (Leer): Obtener/consultar datos existentes.

    • Update (Actualizar): Modificar datos existentes.

    • Delete (Eliminar): Borrar datos.

📌 Mapeo CRUD a HTTP

    • CREATE → POST /recursos

    • READ → GET /recursos o GET /recursos/id

    • UPDATE → PUT /recursos/id

    • DELETE → DELETE /recursos/id

---

## 🛠️ Configuración del Proyecto

### Requisitos
- Python 3.7+
- Flask 2.0+

### Instalación
```bash
pip install flask requests
```

### Estructura del Proyecto
```
📁 pildora_api_rest_crud/
├── 🐱 api_razas_gatos.py     # API principal
├── 🧪 test_api_razas_gatos.py # Pruebas
├── ⚡ inicio_rapido.py        # Inicio rápido
├── � requirements.txt       # Dependencias
├── 🖼️ public/api_cats.png     # Banner
└── 📝 README.md              # Este archivo
```

---

## 🤝 **Contribuir**

¡Las contribuciones son bienvenidas!

1. 🍴 Fork el proyecto
2. 🌟 Crea una feature branch
3. 💻 Realiza tus cambios
4. 🧪 Ejecuta las pruebas
5. 📤 Envía un pull request

---

## 📄 **Licencia**

Este proyecto es de uso educativo y está disponible bajo la licencia MIT.

---

## 🎉 **¡Disfruta explorando el mundo felino con tu API!**

<div align="center">

Made with ❤️ and 🐱

**⭐ ¡Dale una estrella a cat_api si te gusta el proyecto! ⭐**

</div>
# cat_api
