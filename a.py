import yaml
import os
from xml.etree.ElementTree import Element, SubElement, tostring
from datetime import datetime

def str_convert(value):
    """Tüm değerleri string'e çevir"""
    return str(value) if not isinstance(value, str) else value

# YAML dosyasını oku
with open('index.yml', 'r', encoding='utf-8') as f:
    data = yaml.safe_load(f)

# XML yapısını oluştur
root = Element('fdroid')

# Repo bilgileri
repo = SubElement(root, 'repo', {
    'name': str_convert(data['repo']['name']),
    'description': str_convert(data['repo']['description']),
    'timestamp': str_convert(data['repo']['timestamp']),
    'icon': 'fdroid-icon.png'  # Varsayılan ikon
})

# Uygulama bilgileri
for app in data['apps']:
    application = SubElement(root, 'application', {
        'id': str_convert(app['id'])
    })
    SubElement(application, 'name').text = str_convert(app['name'])
    SubElement(application, 'summary').text = str_convert(app.get('desc', ''))
    
    # APK boyutunu al (opsiyonel)
    apk_path = app['apk']
    apk_size = os.path.getsize(apk_path) if os.path.exists(apk_path) else 0
    
    version = SubElement(application, 'version', {
        'versioncode': '1',  # Varsayılan version code
        'version': str_convert(app['version']),
        'apkname': str_convert(apk_path),
        'size': str(apk_size)  # Boyutu ekle
    })

# XML'i dosyaya yaz
with open('index.xml', 'wb') as f:
    # XML declaration ve doctype ekle
    f.write(b'<?xml version="1.0" encoding="utf-8"?>\n')
    f.write(b'<!DOCTYPE fdroid [\n')
    f.write(b'<!ENTITY % fdroid "fdroid">\n')
    f.write(b']>\n')
    f.write(tostring(root, encoding='utf-8', method='xml'))

print("index.xml başarıyla oluşturuldu!")