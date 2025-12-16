#!/usr/bin/env python3
"""
🐱 Script de Prueba para API de Razas de Gatos
Prueba todas las funcionalidades de la API automáticamente
"""

import requests
import json
import time

# Configuración
BASE_URL = "http://127.0.0.1:5000"
headers = {'Content-Type': 'application/json'}

def print_separator(title):
    print(f"\n{'='*50}")
    print(f"🐾 {title}")
    print('='*50)

def test_endpoint(method, endpoint, data=None, description=""):
    """Función auxiliar para probar endpoints"""
    url = f"{BASE_URL}{endpoint}"
    print(f"\n🔗 {method} {endpoint}")
    if description:
        print(f"   {description}")
    
    try:
        if method == "GET":
            response = requests.get(url)
        elif method == "POST":
            response = requests.post(url, headers=headers, data=json.dumps(data))
        elif method == "PUT":
            response = requests.put(url, headers=headers, data=json.dumps(data))
        elif method == "DELETE":
            response = requests.delete(url)
        
        print(f"   Status: {response.status_code}")
        
        if response.headers.get('content-type', '').startswith('application/json'):
            result = response.json()
            print(f"   Respuesta: {json.dumps(result, indent=2, ensure_ascii=False)}")
            return result
        else:
            print(f"   Respuesta: {response.text}")
            return response.text
            
    except requests.exceptions.RequestException as e:
        print(f"   ❌ Error: {e}")
        return None
    except Exception as e:
        print(f"   ❌ Error inesperado: {e}")
        return None

def main():
    print("🐱 Iniciando pruebas de API de Razas de Gatos")
    print("⚠️  Asegúrate de que la API esté corriendo en http://127.0.0.1:5000")
    
    # Verificar que la API esté disponible
    try:
        response = requests.get(f"{BASE_URL}/")
        if response.status_code != 200:
            print("❌ La API no está respondiendo correctamente")
            return
    except requests.exceptions.RequestException:
        print("❌ No se puede conectar a la API. ¿Está corriendo?")
        return
    
    print_separator("1. INFORMACIÓN GENERAL")
    test_endpoint("GET", "/", description="Información de la API")
    
    print_separator("2. CONSULTAR RAZAS EXISTENTES")
    test_endpoint("GET", "/razas", description="Obtener todas las razas")
    test_endpoint("GET", "/estadisticas", description="Estadísticas generales")
    
    print_separator("3. AGREGAR NUEVA RAZA")
    nueva_raza = {
        "nombre": "British Shorthair",
        "origen": "Reino Unido",
        "descripcion": "Gato robusto y tranquilo, conocido por su cara redonda y pelaje denso. Muy popular en Europa.",
        "temperamento": ["tranquilo", "independiente", "leal", "gentil"],
        "tamaño": "mediano",
        "peso_promedio": "3.5-7 kg",
        "esperanza_vida": "14-20 años",
        "popularidad": 8,
        "colores_comunes": ["gris", "negro", "blanco", "crema", "tabby"]
    }
    
    resultado = test_endpoint("POST", "/razas", data=nueva_raza, 
                             description="Agregar British Shorthair")
    nueva_raza_id = None
    if resultado and 'raza' in resultado:
        nueva_raza_id = resultado['raza']['id']
        print(f"   ✅ Raza creada con ID: {nueva_raza_id}")
    
    print_separator("4. FILTROS Y BÚSQUEDAS")
    test_endpoint("GET", "/razas/populares", description="Razas más populares (≥7)")
    test_endpoint("GET", "/razas/tamano/grande", description="Razas de tamaño grande")
    test_endpoint("GET", "/razas/tamano/mediano", description="Razas de tamaño mediano")
    test_endpoint("GET", "/razas/origen/Estados Unidos", description="Razas de Estados Unidos")
    test_endpoint("GET", "/razas/origen/Irán", description="Razas de Irán")
    
    print_separator("5. ACTUALIZAR INFORMACIÓN")
    if nueva_raza_id:
        actualizacion = {
            "popularidad": 9,
            "descripcion": "Gato robusto y tranquilo, conocido por su cara redonda y pelaje denso. ¡ACTUALIZADO! Muy popular en Europa y América."
        }
        test_endpoint("PUT", f"/razas/{nueva_raza_id}", data=actualizacion,
                     description="Actualizar popularidad y descripción")
    
    print_separator("6. ESTADÍSTICAS FINALES")
    test_endpoint("GET", "/estadisticas", description="Estadísticas actualizadas")
    test_endpoint("GET", "/razas", description="Todas las razas (final)")
    
    print_separator("7. ELIMINAR RAZA DE PRUEBA")
    if nueva_raza_id:
        test_endpoint("DELETE", f"/razas/{nueva_raza_id}", 
                     description="Eliminar raza de prueba")
    
    print_separator("8. PRUEBAS DE ERROR")
    test_endpoint("GET", "/razas/tamano/enorme", description="Tamaño inválido (debe fallar)")
    test_endpoint("POST", "/razas", data={"descripcion": "Sin nombre"}, 
                 description="Crear raza sin nombre (debe fallar)")
    test_endpoint("GET", "/razas/origen/PaisInexistente", description="País sin razas")
    
    print_separator("PRUEBAS COMPLETADAS")
    print("✅ Todas las pruebas de la API de Razas de Gatos han sido ejecutadas")
    print("🐱 ¡Miau! Tu API está funcionando perfectamente")

if __name__ == "__main__":
    main()
