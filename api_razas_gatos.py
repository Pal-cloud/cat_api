# -*- coding: utf-8 -*-
from flask import Flask, request
from datetime import datetime
import uuid
import json

# Crear la aplicación Flask
app = Flask(__name__)

# Configurar para que soporte caracteres UTF-8
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.after_request
def after_request(response):
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response

# Función personalizada para jsonify con UTF-8
def jsonify_utf8(data, status_code=200):
    response = app.response_class(
        response=json.dumps(data, ensure_ascii=False, indent=2),
        status=status_code,
        mimetype='application/json; charset=utf-8'
    )
    return response

# Base de datos en memoria (simulada) - Razas de gatos
razas_gatos = []

# Función para convertir nombres a IDs válidos para URLs
def nombre_to_id(nombre):
    """Convierte el nombre de la raza a un ID válido para URLs"""
    import re
    # Remover caracteres especiales y convertir a minúsculas
    id_raza = re.sub(r'[^\w\s-]', '', nombre.lower())
    # Reemplazar espacios y guiones múltiples por guiones simples
    id_raza = re.sub(r'[\s_-]+', '-', id_raza)
    # Remover guiones al inicio y final
    return id_raza.strip('-')

# Función para encontrar raza por nombre o ID
def encontrar_raza(identificador):
    """Encuentra una raza por su nombre original o ID generado"""
    identificador_lower = identificador.lower()
    for raza in razas_gatos:
        # Buscar por ID directo
        if raza['id'].lower() == identificador_lower:
            return raza
        # Buscar por nombre exacto
        if raza['nombre'].lower() == identificador_lower:
            return raza
        # Buscar por ID generado del nombre
        if nombre_to_id(raza['nombre']) == identificador_lower:
            return raza
    return None

# 🐱 Ruta principal
@app.route('/', methods=['GET'])
def home():
    return jsonify_utf8({
        'mensaje': '🐱 API de Razas de Gatos del Mundo',
        'version': '1.0.0',
        'descripción': 'Descubre las características de diferentes razas felinas',
        'endpoints': {
            'GET /razas': 'Obtener todas las razas',
            'POST /razas': 'Agregar nueva raza',
            'GET /razas/<nombre>': 'Obtener raza por nombre',
            'PUT /razas/<nombre>': 'Actualizar raza por nombre',
            'DELETE /razas/<nombre>': 'Eliminar raza por nombre',
            'GET /razas/populares': 'Ver razas más populares',
            'GET /razas/tamano/<tamano>': 'Filtrar por tamaño (pequeño/mediano/grande)',
            'GET /razas/origen/<país>': 'Filtrar por país de origen',
            'GET /estadísticas': 'Estadísticas generales'
        }
    })

# 🐾 GET - Obtener todas las razas
@app.route('/razas', methods=['GET'])
def obtener_razas():
    return jsonify_utf8({
        'total_razas': len(razas_gatos),
        'razas': razas_gatos
    }), 200

# 🌟 GET - Razas más populares (DEBE IR ANTES DE LA RUTA DINÁMICA)
@app.route('/razas/populares', methods=['GET'])
def razas_populares():
    populares = sorted([r for r in razas_gatos if r['popularidad'] >= 7], 
                      key=lambda x: x['popularidad'], reverse=True)
    return jsonify_utf8({
        'total_populares': len(populares),
        'razas': populares
    }), 200

# � GET - Razas por tamaño (DEBE IR ANTES DE LA RUTA DINÁMICA)
@app.route('/razas/tamano/<tamano>', methods=['GET'])
def razas_por_tamano(tamano):
    if tamano not in ['pequeno', 'mediano', 'grande']:
        return jsonify_utf8({'error': 'Tamaño debe ser: pequeno, mediano o grande'}), 400
    
    # Mapear nombres URL a nombres reales
    tamano_map = {'pequeno': 'pequeño', 'mediano': 'mediano', 'grande': 'grande'}
    tamano_real = tamano_map.get(tamano, tamano)
    
    filtradas = [r for r in razas_gatos if r['tamaño'] == tamano_real]
    return jsonify_utf8({
        'tamano_buscado': tamano_real,
        'total_encontradas': len(filtradas),
        'razas': filtradas
    }), 200

# 🌍 GET - Razas por origen (DEBE IR ANTES DE LA RUTA DINÁMICA)  
@app.route('/razas/origen/<pais>', methods=['GET'])
def razas_por_origen(pais):
    filtradas = [r for r in razas_gatos if pais.lower() in r['origen'].lower()]
    return jsonify_utf8({
        'pais_buscado': pais,
        'total_encontradas': len(filtradas),
        'razas': filtradas
    }), 200

# �🔍 GET - Obtener una raza específica por nombre/ID (RUTA DINÁMICA AL FINAL)
@app.route('/razas/<raza_id>', methods=['GET'])
def obtener_raza(raza_id):
    raza = encontrar_raza(raza_id)
    if not raza:
        return jsonify_utf8({'error': 'Raza no encontrada'}), 404
    
    return jsonify_utf8(raza), 200

# ➕ POST - Agregar nueva raza
@app.route('/razas', methods=['POST'])
def crear_raza():
    datos = request.get_json()
    
    # Validación básica
    if not datos or 'nombre' not in datos:
        return jsonify_utf8({'error': 'El nombre de la raza es obligatorio'}), 400
    
    nueva_raza = {
        'id': nombre_to_id(datos['nombre']),
        'nombre': datos['nombre'],
        'origen': datos.get('origen', 'Desconocido'),
        'descripcion': datos.get('descripcion', ''),
        'temperamento': datos.get('temperamento', []),
        'tamaño': datos.get('tamaño', 'mediano'),  # pequeño, mediano, grande
        'peso_promedio': datos.get('peso_promedio', '3-5 kg'),
        'esperanza_vida': datos.get('esperanza_vida', '12-15 años'),
        'popularidad': datos.get('popularidad', 5),  # 1-10
        'colores_comunes': datos.get('colores_comunes', []),
        'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    
    razas_gatos.append(nueva_raza)
    return jsonify_utf8({
        'mensaje': '✅ Raza de gato agregada exitosamente',
        'raza': nueva_raza
    }), 201

# ✏️ PUT - Actualizar información de raza
@app.route('/razas/<raza_id>', methods=['PUT'])
def actualizar_raza(raza_id):
    datos = request.get_json()
    
    # Buscar la raza usando la nueva función
    raza = encontrar_raza(raza_id)
    if not raza:
        return jsonify_utf8({'error': 'Raza no encontrada'}), 404
    
    # Actualizar campos
    if 'nombre' in datos:
        raza['nombre'] = datos['nombre']
        # Actualizar también el ID si cambió el nombre
        raza['id'] = nombre_to_id(datos['nombre'])
    raza['origen'] = datos.get('origen', raza['origen'])
    raza['descripcion'] = datos.get('descripcion', raza['descripcion'])
    raza['temperamento'] = datos.get('temperamento', raza['temperamento'])
    raza['tamaño'] = datos.get('tamaño', raza['tamaño'])
    raza['peso_promedio'] = datos.get('peso_promedio', raza['peso_promedio'])
    raza['esperanza_vida'] = datos.get('esperanza_vida', raza['esperanza_vida'])
    raza['popularidad'] = datos.get('popularidad', raza['popularidad'])
    raza['colores_comunes'] = datos.get('colores_comunes', raza['colores_comunes'])
    
    return jsonify_utf8({
        'mensaje': '📝 Información de raza actualizada',
        'raza': raza
    }), 200

# 🗑️ DELETE - Eliminar raza
@app.route('/razas/<raza_id>', methods=['DELETE'])
def eliminar_raza(raza_id):
    global razas_gatos
    
    # Buscar la raza usando la nueva función
    raza = encontrar_raza(raza_id)
    if not raza:
        return jsonify_utf8({'error': 'Raza no encontrada'}), 404
    
    # Eliminar la raza
    razas_gatos = [r for r in razas_gatos if r['id'] != raza['id']]
    
    return jsonify_utf8({
        'mensaje': '🗑️ Raza eliminada',
        'raza_eliminada': raza
    }), 200

# 📊 GET - Estadísticas generales
@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    total = len(razas_gatos)
    
    if total == 0:
        return jsonify_utf8({
            'mensaje': 'No hay razas registradas aún',
            'total_razas': 0
        }), 200
    
    # Estadísticas por tamaño
    tamaños = {}
    for tamaño in ['pequeño', 'mediano', 'grande']:
        tamaños[tamaño] = len([r for r in razas_gatos if r['tamaño'] == tamaño])
    
    # Top países de origen
    paises = {}
    for raza in razas_gatos:
        pais = raza['origen']
        paises[pais] = paises.get(pais, 0) + 1
    
    # Popularidad promedio
    popularidad_promedio = sum(r['popularidad'] for r in razas_gatos) / total
    
    return jsonify_utf8({
        'resumen': {
            'total_razas': total,
            'popularidad_promedio': round(popularidad_promedio, 1),
            'razas_muy_populares': len([r for r in razas_gatos if r['popularidad'] >= 8])
        },
        'por_tamaño': tamaños,
        'top_paises_origen': dict(sorted(paises.items(), key=lambda x: x[1], reverse=True)[:5])
    }), 200

if __name__ == '__main__':
    # Agregar 4 razas de gatos de ejemplo
    razas_gatos.extend([
        {
            'id': 'calico',
            'nombre': 'Gato Calicó (Tricolor)',
            'origen': 'Mundial',
            'descripcion': 'Gato caracterizado por su pelaje de tres colores: negro, naranja y blanco. Casi siempre son hembras debido a la genética ligada al cromosoma X.',
            'temperamento': ['independiente', 'cariñoso', 'inteligente', 'juguetón'],
            'tamaño': 'mediano',
            'peso_promedio': '3-5 kg',
            'esperanza_vida': '13-16 años',
            'popularidad': 8,
            'colores_comunes': ['tricolor', 'negro-naranja-blanco', 'calicó diluido'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': 'snowshoe',
            'nombre': 'Gato Snowshoe',
            'origen': 'Estados Unidos',
            'descripcion': 'Raza híbrida entre Siamés y Americano de Pelo Corto. Conocido por sus distintivas "botas" blancas en las patas.',
            'temperamento': ['dulce', 'vocal', 'sociable', 'activo'],
            'tamaño': 'mediano',
            'peso_promedio': '3.5-5.5 kg',
            'esperanza_vida': '14-19 años',
            'popularidad': 7,
            'colores_comunes': ['seal point', 'blue point', 'con marcas blancas'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': 'vaca',
            'nombre': 'Gato Vaca (Bicolor Negro y Blanco)',
            'origen': 'Mundial',
            'descripcion': 'Gato con patrón bicolor distintivo de manchas negras y blancas que recuerda a las vacas Holstein. Muy común en gatos domésticos.',
            'temperamento': ['amigable', 'tranquilo', 'adaptable', 'cariñoso'],
            'tamaño': 'mediano',
            'peso_promedio': '3.5-6 kg',
            'esperanza_vida': '13-17 años',
            'popularidad': 9,
            'colores_comunes': ['negro y blanco', 'bicolor', 'tuxedo'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': 'atigrado',
            'nombre': 'Gato Común Atigrado y Blanco',
            'origen': 'Mundial',
            'descripcion': 'El gato doméstico más común, con rayas atigradas (tabby) y marcas blancas. Excelente cazador y muy adaptable.',
            'temperamento': ['independiente', 'cazador', 'adaptable', 'inteligente'],
            'tamaño': 'mediano',
            'peso_promedio': '3.5-5.5 kg',
            'esperanza_vida': '12-18 años',
            'popularidad': 10,
            'colores_comunes': ['tabby marrón', 'atigrado gris', 'tabby con blanco'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    ])
    
    print("🐱 Iniciando API de Razas de Gatos...")
    print("📍 Disponible en: http://127.0.0.1:5000")
    print("🌟 Razas precargadas:", len(razas_gatos))
    app.run(debug=True, host='0.0.0.0', port=5000)
