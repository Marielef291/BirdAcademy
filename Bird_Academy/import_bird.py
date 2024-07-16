import json
import os
import django

# Configure Django settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "Bird_Academy.settings")
django.setup()

from Application.models import Bird

# Charger le fichier JSON
with open('birds_data.json', 'r') as json_file:
    birds_data = json.load(json_file)

# Créer des instances du modèle Bird et les sauvegarder dans la base de données
for bird_data in birds_data:
    bird = Bird(
        Latin_name=bird_data['Latin_name'],
        Fr_name=bird_data['Fr_name'],
        Eng_name=bird_data['Eng_name']
    )
    bird.save()

print("Importation terminée avec succès.")
