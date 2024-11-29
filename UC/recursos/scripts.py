import requests
from bs4 import BeautifulSoup
import re
from pathlib import Path
import time
import os

class SimpleScriptCleaner:
    def __init__(self, output_dir="scripts_limpios", headers=None):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(exist_ok=True)
        self.headers = headers or {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def clean_script(self, text):
        """
        Limpia el texto del guión, eliminando elementos no deseados
        """
        # Eliminar etiquetas HTML
        text = re.sub(r'<[^>]+>', '', text)
        
        # Eliminar caracteres especiales preservando puntuación básica
        text = re.sub(r'[^\w\s\n.!?:()"\-\']', ' ', text)
        
        # Normalizar espacios y líneas en blanco
        text = re.sub(r'\s+', ' ', text)
        text = re.sub(r'\n\s*\n', '\n\n', text)
        
        return text.strip()

    def process_url(self, url):
        """
        Descarga y procesa un guión desde una URL
        """
        try:
            # Esperar 2 segundos entre descargas
            time.sleep(2)
            
            # Obtener el título del guión de la URL
            title = url.split('/')[-1].replace('.html', '').replace('-', ' ')
            print(f"Procesando: {title}")
            
            # Descargar el contenido
            response = requests.get(url, headers=self.headers)
            response.raise_for_status()
            
            # Extraer el contenido del guión
            soup = BeautifulSoup(response.text, 'html.parser')
            script_content = soup.find('pre')
            
            if script_content:
                # Limpiar el texto
                clean_text = self.clean_script(script_content.get_text())
                
                # Guardar el archivo
                output_file = self.output_dir / f"{title}.txt"
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(clean_text)
                    
                print(f"✓ Guardado: {title}")
                return True
            else:
                print(f"✗ No se encontró contenido en: {title}")
                return False
                
        except Exception as e:
            print(f"✗ Error procesando {title}: {str(e)}")
            return False

def main():
    # URLs de los guiones
    urls = [
        "https://imsdb.com/scripts/Whistleblower,-The.html",
        "https://imsdb.com/scripts/White-Christmas.html",
        "https://imsdb.com/scripts/White-Jazz.html",
        "https://imsdb.com/scripts/White-Ribbon,-The.html",
        "https://imsdb.com/scripts/White-Squall.html",
        "https://imsdb.com/scripts/Whiteout.html",
        "https://imsdb.com/scripts/Who-Framed-Roger-Rabbit?.html",
        "https://imsdb.com/scripts/Who's-Your-Daddy.html",
        "https://imsdb.com/scripts/Wild-At-Heart.html",
        "https://imsdb.com/scripts/Wild-Bunch,-The.html",
        "https://imsdb.com/scripts/Wild-Hogs.html"
    ]
    
    cleaner = SimpleScriptCleaner()
    for url in urls:
        cleaner.process_url(url)

if __name__ == "__main__":
    main()