from flask import Flask, jsonify, request
from datetime import datetime
import uuid

# Crear la aplicación Flask
app = Flask(__name__)

# Base de datos en memoria (simulada) - Razas de gatos
razas_gatos = []

# 🐱 Ruta principal
@app.route('/', methods=['GET'])
def home():
    return jsonify({
        'mensaje': '🐱 API de Razas de Gatos del Mundo',
        'version': '1.0.0',
        'descripcion': 'Descubre las características de diferentes razas felinas',
        'endpoints': {
            'GET /razas': 'Obtener todas las razas',
            'POST /razas': 'Agregar nueva raza',
            'PUT /razas/<id>': 'Actualizar información de raza',
            'DELETE /razas/<id>': 'Eliminar raza',
            'GET /razas/populares': 'Ver razas más populares',
            'GET /razas/tamano/<tamano>': 'Filtrar por tamaño (pequeno/mediano/grande)',
            'GET /razas/origen/<pais>': 'Filtrar por país de origen',
            'GET /estadisticas': 'Estadísticas generales'
        }
    })

# 🐾 GET - Obtener todas las razas
@app.route('/razas', methods=['GET'])
def obtener_razas():
    return jsonify({
        'total_razas': len(razas_gatos),
        'razas': razas_gatos
    }), 200

# ➕ POST - Agregar nueva raza
@app.route('/razas', methods=['POST'])
def crear_raza():
    datos = request.get_json()
    
    # Validación básica
    if not datos or 'nombre' not in datos:
        return jsonify({'error': 'El nombre de la raza es obligatorio'}), 400
    
    nueva_raza = {
        'id': str(uuid.uuid4()),
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
    return jsonify({
        'mensaje': '✅ Raza de gato agregada exitosamente',
        'raza': nueva_raza
    }), 201

# ✏️ PUT - Actualizar información de raza
@app.route('/razas/<raza_id>', methods=['PUT'])
def actualizar_raza(raza_id):
    datos = request.get_json()
    
    # Buscar la raza
    raza = next((r for r in razas_gatos if r['id'] == raza_id), None)
    if not raza:
        return jsonify({'error': 'Raza no encontrada'}), 404
    
    # Actualizar campos
    raza['nombre'] = datos.get('nombre', raza['nombre'])
    raza['origen'] = datos.get('origen', raza['origen'])
    raza['descripcion'] = datos.get('descripcion', raza['descripcion'])
    raza['temperamento'] = datos.get('temperamento', raza['temperamento'])
    raza['tamaño'] = datos.get('tamaño', raza['tamaño'])
    raza['peso_promedio'] = datos.get('peso_promedio', raza['peso_promedio'])
    raza['esperanza_vida'] = datos.get('esperanza_vida', raza['esperanza_vida'])
    raza['popularidad'] = datos.get('popularidad', raza['popularidad'])
    raza['colores_comunes'] = datos.get('colores_comunes', raza['colores_comunes'])
    
    return jsonify({
        'mensaje': '📝 Información de raza actualizada',
        'raza': raza
    }), 200

# 🗑️ DELETE - Eliminar raza
@app.route('/razas/<raza_id>', methods=['DELETE'])
def eliminar_raza(raza_id):
    global razas_gatos
    
    # Buscar y eliminar la raza
    raza = next((r for r in razas_gatos if r['id'] == raza_id), None)
    if not raza:
        return jsonify({'error': 'Raza no encontrada'}), 404
    
    razas_gatos = [r for r in razas_gatos if r['id'] != raza_id]
    
    return jsonify({
        'mensaje': '🗑️ Raza eliminada',
        'raza_eliminada': raza
    }), 200

# 🌟 GET - Razas más populares
@app.route('/razas/populares', methods=['GET'])
def razas_populares():
    populares = sorted([r for r in razas_gatos if r['popularidad'] >= 7], 
                      key=lambda x: x['popularidad'], reverse=True)
    return jsonify({
        'total_populares': len(populares),
        'razas': populares
    }), 200

# 📏 GET - Razas por tamaño
@app.route('/razas/tamano/<tamano>', methods=['GET'])
def razas_por_tamano(tamano):
    if tamano not in ['pequeno', 'mediano', 'grande']:
        return jsonify({'error': 'Tamaño debe ser: pequeno, mediano o grande'}), 400
    
    # Mapear nombres URL a nombres reales
    tamano_map = {'pequeno': 'pequeño', 'mediano': 'mediano', 'grande': 'grande'}
    tamano_real = tamano_map.get(tamano, tamano)
    
    filtradas = [r for r in razas_gatos if r['tamaño'] == tamano_real]
    return jsonify({
        f'razas_tamano_{tamano}': len(filtradas),
        'razas': filtradas
    }), 200

# 🌍 GET - Razas por país de origen
@app.route('/razas/origen/<pais>', methods=['GET'])
def razas_por_origen(pais):
    filtradas = [r for r in razas_gatos if r['origen'].lower() == pais.lower()]
    return jsonify({
        f'razas_de_{pais}': len(filtradas),
        'razas': filtradas
    }), 200

# 📊 GET - Estadísticas generales
@app.route('/estadisticas', methods=['GET'])
def estadisticas():
    total = len(razas_gatos)
    
    if total == 0:
        return jsonify({
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
    
    return jsonify({
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
            'id': str(uuid.uuid4()),
            'nombre': 'Persa',
            'origen': 'Irán',
            'descripcion': 'Gato de pelo largo, conocido por su cara achatada y temperamento tranquilo. Una de las razas más antiguas y elegantes.',
            'temperamento': ['tranquilo', 'dulce', 'independiente'],
            'tamaño': 'mediano',
            'peso_promedio': '3.5-5.5 kg',
            'esperanza_vida': '12-17 años',
            'popularidad': 9,
            'colores_comunes': ['blanco', 'negro', 'crema', 'gris', 'chinchilla'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': str(uuid.uuid4()),
            'nombre': 'Maine Coon',
            'origen': 'Estados Unidos',
            'descripcion': 'Conocido como el "gigante gentil", es una de las razas más grandes. Excelente cazador y muy sociable.',
            'temperamento': ['amigable', 'inteligente', 'juguetón', 'sociable'],
            'tamaño': 'grande',
            'peso_promedio': '5.5-8.2 kg',
            'esperanza_vida': '13-14 años',
            'popularidad': 8,
            'colores_comunes': ['marrón tabby', 'negro', 'blanco', 'plata'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': str(uuid.uuid4()),
            'nombre': 'Siamés',
            'origen': 'Tailandia',
            'descripcion': 'Gato elegante y vocal, conocido por sus ojos azules intensos y patrones de color únicos.',
            'temperamento': ['vocal', 'inteligente', 'activo', 'cariñoso'],
            'tamaño': 'mediano',
            'peso_promedio': '2.5-4.5 kg',
            'esperanza_vida': '15-18 años',
            'popularidad': 7,
            'colores_comunes': ['seal point', 'chocolate point', 'blue point', 'lilac point'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        },
        {
            'id': str(uuid.uuid4()),
            'nombre': 'Ragdoll',
            'origen': 'Estados Unidos',
            'descripcion': 'Conocido por su naturaleza relajada y tendencia a "desmayarse" cuando se le carga.',
            'temperamento': ['relajado', 'dulce', 'dócil', 'tranquilo'],
            'tamaño': 'grande',
            'peso_promedio': '4.5-9 kg',
            'esperanza_vida': '13-18 años',
            'popularidad': 8,
            'colores_comunes': ['colorpoint', 'mitted', 'bicolor'],
            'fecha_agregada': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
    ])
    
    print("🐱 Iniciando API de Razas de Gatos...")
    print("📍 Disponible en: http://127.0.0.1:5000")
    print("🌟 Razas precargadas:", len(razas_gatos))
    app.run(debug=True, host='0.0.0.0', port=5000)
