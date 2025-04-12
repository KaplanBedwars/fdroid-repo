#!/bin/python3
import os
import json
import yaml  # pip install pyyaml
from zipfile import ZipFile

# 1. index.yml'yi oku
with open("index.yml", "r") as f:
    data = yaml.safe_load(f)

# 2. index-v1.json oluştur
with open("index-v1.json", "w") as f:
    json.dump(data, f)

# 3. index-v1.jar oluştur (içinde index-v1.json olacak)
with ZipFile("index-v1.jar", "w") as jar:
    jar.write("index-v1.json")

print("✅ index-v1.json ve index-v1.jar oluşturuldu!")