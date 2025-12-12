import json
import os
import glob
import re

JSON_FILE = 'themes.json'
DEFAULT_VERSION = "1.0"
DEFAULT_IMAGE_DIR = "screenshots"

def load_themes():
    if not os.path.exists(JSON_FILE):
        return []
    try:
        with open(JSON_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Warnung: {JSON_FILE} war leer oder ungültig. Starte neu.")
        return []

def save_themes(themes):
    with open(JSON_FILE, 'w', encoding='utf-8') as f:
        json.dump(themes, f, indent=2, ensure_ascii=False)
    print(f"✅ {JSON_FILE} erfolgreich aktualisiert.")

def generate_name(filename):
    # Entfernt .css, ersetzt Unterstriche durch Leerzeichen und macht den ersten Buchstaben groß
    name = os.path.splitext(filename)[0]
    return name.replace('_', ' ').title()

def extract_css_metadata(filepath):
    metadata = {
        'name': None,
        'description': None,
        'version': None,
        'author': None
    }
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
            # Suche nach NAME
            name_match = re.search(r'/\*\s*NAME:\s*(.*?)\s*\*/', content)
            if name_match:
                metadata['name'] = name_match.group(1).strip()

            # Suche nach DESCRIPTION
            desc_match = re.search(r'/\*\s*DESCRIPTION:\s*(.*?)\s*\*/', content)
            if desc_match:
                metadata['description'] = desc_match.group(1).strip()

            # Suche nach VERSION
            version_match = re.search(r'/\*\s*VERSION:\s*(.*?)\s*\*/', content)
            if version_match:
                metadata['version'] = version_match.group(1).strip()
                
            # Suche nach AUTHOR
            author_match = re.search(r'/\*\s*AUTHOR:\s*(.*?)\s*\*/', content)
            if author_match:
                metadata['author'] = author_match.group(1).strip()
    except Exception as e:
        print(f"Fehler beim Lesen von {filepath}: {e}")
        
    return metadata

def update_themes():
    existing_themes = load_themes()
    
    # Erstelle ein Dictionary für schnellen Zugriff auf existierende Daten: 'filename' -> theme_obj
    theme_map = {item['file']: item for item in existing_themes if 'file' in item}
    
    # Finde alle CSS-Dateien im aktuellen Verzeichnis
    css_files = glob.glob('*.css')
    css_files.sort()
    
    new_themes_list = []
    
    print(f"Gefundene CSS-Dateien: {len(css_files)}")
    
    for css_file in css_files:
        metadata = extract_css_metadata(css_file)
        
        if css_file in theme_map:
            # Existierendes Theme nehmen
            print(f"  Verarbeite: {css_file}")
            theme_entry = theme_map[css_file]
        else:
            # Neues Theme hinzufügen
            base_name = os.path.splitext(css_file)[0]
            # Fallback Name, falls nicht in Metadata
            new_name = metadata['name'] if metadata['name'] else generate_name(css_file)
            default_image_path = os.path.join(DEFAULT_IMAGE_DIR, f"{base_name}.png").replace("\\", "/") 
            
            print(f"  Neu: {css_file}")
            theme_entry = {
                "name": new_name,
                "description": "", # Wird unten aktualisiert, falls vorhanden
                "file": css_file,
                "version": DEFAULT_VERSION,
                "image": default_image_path
            }
        
        # Metadata aktualisieren, falls gefunden
        if metadata['name']:
            theme_entry['name'] = metadata['name']
        if metadata['description']:
            theme_entry['description'] = metadata['description']
        if metadata['version']:
            theme_entry['version'] = metadata['version']
        if metadata['author']:
            theme_entry['author'] = metadata['author']
            
        new_themes_list.append(theme_entry)
            
    # Änderungen speichern
    save_themes(new_themes_list)

if __name__ == "__main__":
    update_themes()
