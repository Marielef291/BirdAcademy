#!/bin/bash

# Activer l'environnement virtuel
source ./env/Scripts/activate

# Vérifier si l'environnement virtuel est activé
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "L'environnement virtuel est activé : $VIRTUAL_ENV"
else
    echo "Erreur : Impossible d'activer l'environnement virtuel."
    exit 1
fi

# Changer le répertoire vers celui du projet Django
cd ./Bird_Academy/

# Lancer le serveur de développement Django
python manage.py runserver 0.0.0.0:8000

# Message de confirmation
echo "Le serveur Django est en cours d'exécution à l'adresse http://0.0.0.0:8000"
