# Bird Academy

## Sommaire
- [Description du projet](#description-du-projet)
- [Pré-requis](#pré-requis)
- [Installation](#installation)
- [Base de données](#base-de-données)
- [Utilisation](#utilisation)
- [English Version](#english-version)

## Description du projet

Bird Academy est une application Django conçue pour aider les utilisateurs à apprendre à reconnaître les chants d'oiseaux par la répétition. L'utilisateur sélectionne les oiseaux qu'il souhaite apprendre à reconnaître, puis l'application lui proposera aléatoirement des chants d'oiseaux. Les chants sont récupérés via l'API de [xeno-canto](https://www.xeno-canto.org/).

## Pré-requis

- Python 3.x
- pip (gestionnaire de paquets pour Python)

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://gitlab.com/Naukogha/BirdAcademy.git
    cd Bird_Academy
    ```

2. Créez et activez un environnement virtuel :
    ```bash
    python -m venv env
    ```

    Pour Windows :
    ```bash
    .\env\Scripts\activate
    ```

    Pour Linux et MacOS :
    ```bash
    source env/bin/activate
    ```

3. Installez les dépendances :
    ```bash
    pip install -r requirements.txt
    ```

4. Naviguez vers le répertoire du projet :
    ```bash
    cd .\Bird_Academy\
    ```

## Base de données

La liste des noms d'oiseaux a été générée grâce à la base de données TAXREF.

1. Appliquez les migrations :
    ```bash
    python manage.py makemigrations 
    python manage.py migrate
    ```

2. Importez la liste des oiseaux :
    ```bash
    python import_bird.py 
    ```

## Utilisation

1. Lancez le serveur de développement Django :
    ```bash
    python manage.py runserver
    ```

2. Ouvrez votre navigateur et allez à `http://127.0.0.1:8000` pour accéder à l'application.

## English Version

### Table of Contents
- [Project Description](#project-description)
- [Prerequisites](#prerequisites)
- [Installation](#installation-1)
- [Database](#database)
- [Usage](#usage)

### Project Description

Bird Academy is a Django application designed to help users learn to recognize bird songs through repetition. Users select the birds they want to learn to recognize, and the application will randomly propose bird songs. The songs are retrieved via the [xeno-canto](https://www.xeno-canto.org/) API.

### Prerequisites

- Python 3.x
- pip (Python package manager)

### Installation

1. Clone the repository:
    ```bash
    git clone https://gitlab.com/Naukogha/BirdAcademy.git
    cd Bird_Academy
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv env
    ```

    For Windows:
    ```bash
    .\env\Scripts\activate
    ```

    For Linux and MacOS:
    ```bash
    source env/bin/activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Navigate to the project directory:
    ```bash
    cd .\Bird_Academy\
    ```

### Database

The list of bird names was generated using the TAXREF database.

1. Apply the migrations:
    ```bash
    python manage.py makemigrations 
    python manage.py migrate
    ```

2. Import the bird list:
    ```bash
    python import_bird.py 
    ```

### Usage

1. Start the Django development server:
    ```bash
    python manage.py runserver
    ```

2. Open your browser and go to `http://127.0.0.1:8000` to access the application.
