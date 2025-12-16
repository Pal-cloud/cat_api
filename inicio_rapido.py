#!/usr/bin/env python3
"""
🐱 INICIO RÁPIDO - API de Razas de Gatos

¡Tu API personalizada está lista para usar!

🚀 Para empezar:
1. Ejecuta este archivo: python inicio_rapido.py
2. Abre tu navegador en: http://127.0.0.1:5000
3. Prueba los endpoints automáticamente: python test_api_razas_gatos.py

📖 Para más información, consulta: GUIA_RAZAS_GATOS.md
"""

import subprocess
import sys
import time
import requests
import webbrowser
from threading import Thread

def verificar_dependencias():
    """Verificar que Flask esté instalado"""
    try:
        import flask
        print("✅ Flask está instalado")
        return True
    except ImportError:
        print("❌ Flask no está instalado")
        print("💡 Instalar con: pip install flask")
        return False

def probar_api():
    """Hacer una prueba rápida de la API"""
    time.sleep(3)  # Esperar a que la API se inicie
    
    try:
        response = requests.get("http://127.0.0.1:5000/")
        if response.status_code == 200:
            print("\n✅ API funcionando correctamente!")
            print("🌐 Abriendo navegador...")
            webbrowser.open("http://127.0.0.1:5000/")
            
            # Mostrar algunas razas
            razas_response = requests.get("http://127.0.0.1:5000/razas")
            if razas_response.status_code == 200:
                datos = razas_response.json()
                print(f"\n🐱 Razas precargadas: {datos['total_razas']}")
                for raza in datos['razas'][:3]:  # Mostrar primeras 3
                    print(f"   • {raza['nombre']} ({raza['origen']})")
        else:
            print("❌ Error al conectar con la API")
    except requests.exceptions.RequestException:
        print("⚠️  La API aún se está iniciando...")
    except Exception as e:
        print(f"❌ Error: {e}")

def main():
    print("🐱 API de Razas de Gatos - Inicio Rápido")
    print("="*50)
    
    # Verificar dependencias
    if not verificar_dependencias():
        return
    
    try:
        import flask
    except ImportError:
        print("❌ Instala Flask primero: pip install flask")
        return
    
    print("\n🚀 Iniciando API...")
    print("📍 URL: http://127.0.0.1:5000")
    print("🛑 Para detener: Ctrl+C")
    print("\n" + "="*50)
    
    # Iniciar prueba en segundo plano
    Thread(target=probar_api, daemon=True).start()
    
    # Ejecutar la API
    try:
        subprocess.run([sys.executable, "api_razas_gatos.py"])
    except KeyboardInterrupt:
        print("\n\n🛑 API detenida")
        print("👋 ¡Gracias por probar tu API de razas de gatos!")
    except FileNotFoundError:
        print("❌ No se encontró el archivo api_razas_gatos.py")
        print("💡 Asegúrate de estar en el directorio correcto")

if __name__ == "__main__":
    main()
