# ✅ OliveDash - Checklist d'Installation

## 📦 Phase 1 : Préparation des fichiers

### Structure des dossiers
- [ ] Créer le dossier principal `olivedash/`
- [ ] Créer le sous-dossier `config/`
- [ ] Créer le sous-dossier `modules/`
- [ ] Créer le sous-dossier `utils/`
- [ ] Créer le sous-dossier `scripts/`
- [ ] Créer le sous-dossier `assets/`
- [ ] Créer le sous-dossier `.streamlit/`

### Fichiers racine
- [ ] Copier `app.py`
- [ ] Copier `requirements.txt`
- [ ] Copier `.gitignore`
- [ ] Copier `README.md`
- [ ] Copier `QUICKSTART.md`
- [ ] Copier `STRUCTURE.md`
- [ ] Copier `INSTALLATION_COMPLETE.md`
- [ ] Copier `RESUME_PROJET.md`
- [ ] Créer le fichier `.env` (vide pour l'instant)

### Dossier config/
- [ ] Créer `config/__init__.py` (fichier vide)
- [ ] Copier `config/settings.py`

### Dossier modules/
- [ ] Créer `modules/__init__.py` (fichier vide)
- [ ] Copier `modules/auth.py`
- [ ] Copier `modules/parcelles.py`
- [ ] Copier `modules/logs.py`

### Dossier utils/
- [ ] Créer `utils/__init__.py` (fichier vide)
- [ ] Copier `utils/database.py`

### Dossier scripts/
- [ ] Copier `scripts/create_first_user.py`

### Dossier .streamlit/
- [ ] Copier `.streamlit/config.toml`

---

## 🔧 Phase 2 : Configuration Google Cloud

### Création du projet Google Cloud
- [ ] Aller sur https://console.cloud.google.com/
- [ ] Se connecter avec votre compte Google
- [ ] Cliquer sur "Select a project" → "New Project"
- [ ] Nommer le projet : `OliveDash`
- [ ] Cliquer sur "Create"
- [ ] Attendre la création du projet (30 secondes)

### Activation des APIs
- [ ] Menu → "APIs & Services" → "Library"
- [ ] Rechercher "Google Sheets API"
- [ ] Cliquer sur "Google Sheets API"
- [ ] Cliquer sur "ENABLE"
- [ ] Attendre l'activation
- [ ] Revenir à "Library"
- [ ] Rechercher "Google Drive API"
- [ ] Cliquer sur "Google Drive API"
- [ ] Cliquer sur "ENABLE"

### Création du compte de service
- [ ] Menu → "IAM & Admin" → "Service Accounts"
- [ ] Cliquer sur "CREATE SERVICE ACCOUNT"
- [ ] Service account name : `olivedash-service`
- [ ] Cliquer sur "CREATE AND CONTINUE"
- [ ] Select a role : "Editor"
- [ ] Cliquer sur "CONTINUE"
- [ ] Cliquer sur "DONE"

### Téléchargement de la clé JSON
- [ ] Cliquer sur le compte de service `olivedash-service`
- [ ] Onglet "KEYS"
- [ ] "ADD KEY" → "Create new key"
- [ ] Type : JSON
- [ ] Cliquer sur "CREATE"
- [ ] Le fichier JSON se télécharge automatiquement
- [ ] Renommer le fichier en `google_credentials.json`
- [ ] Déplacer le fichier dans le dossier `config/`

### Copier l'email du compte de service
- [ ] Ouvrir le fichier `config/google_credentials.json`
- [ ] Chercher la ligne `"client_email": "..."`
- [ ] Copier l'adresse email complète (ex: `olivedash-service@project-id.iam.gserviceaccount.com`)
- [ ] **GARDER CETTE EMAIL SOUS LA MAIN**

---

## 📊 Phase 3 : Configuration Google Sheets

### Création du Google Sheet
- [ ] Aller sur https://docs.google.com/spreadsheets/
- [ ] Cliquer sur "+" (Blank spreadsheet)
- [ ] Nommer le document : `OliveDash Database`

### Récupération de l'ID du Sheet
- [ ] Regarder l'URL dans la barre d'adresse
- [ ] L'URL ressemble à : `https://docs.google.com/spreadsheets/d/[COPIEZ_CETTE_PARTIE]/edit`
- [ ] Copier la partie entre `/d/` et `/edit`
- [ ] C'est votre `GOOGLE_SHEET_ID`
- [ ] **GARDER CET ID SOUS LA MAIN**

### Partage avec le compte de service
- [ ] Dans Google Sheets, cliquer sur "Share" (en haut à droite)
- [ ] Coller l'email du compte de service copié précédemment
- [ ] Sélectionner "Editor" dans le menu déroulant
- [ ] **IMPORTANT** : Décocher "Notify people"
- [ ] Cliquer sur "Share"
- [ ] Confirmer "Share anyway" si demandé

---

## 📧 Phase 4 : Configuration Email (Gmail)

### Activation de la validation en deux étapes
- [ ] Aller sur https://myaccount.google.com/security
- [ ] Chercher "2-Step Verification"
- [ ] Cliquer sur "2-Step Verification"
- [ ] Suivre les instructions pour activer
- [ ] Valider avec votre téléphone

### Création d'un mot de passe d'application
- [ ] Sur la page de sécurité, chercher "App passwords"
- [ ] Cliquer sur "App passwords"
- [ ] Dans "Select app", choisir "Mail"
- [ ] Dans "Select device", choisir "Other"
- [ ] Taper : `OliveDash`
- [ ] Cliquer sur "Generate"
- [ ] Copier le mot de passe de 16 caractères (avec espaces)
- [ ] **GARDER CE MOT DE PASSE SOUS LA MAIN**

---

## 🌤️ Phase 5 : Configuration OpenWeatherMap

### Création du compte
- [ ] Aller sur https://openweathermap.org/api
- [ ] Cliquer sur "Sign Up"
- [ ] Remplir le formulaire
- [ ] Confirmer l'email reçu

### Récupération de l'API Key
- [ ] Se connecter sur OpenWeatherMap
- [ ] Aller dans "API keys" (menu utilisateur)
- [ ] Copier la clé "Default"
- [ ] **GARDER CETTE CLÉ SOUS LA MAIN**

---

## 🔐 Phase 6 : Configuration du fichier .env

### Créer et remplir le fichier .env
- [ ] Ouvrir le fichier `.env` avec un éditeur de texte
- [ ] Copier le template ci-dessous et le coller dans le fichier
- [ ] Remplacer les valeurs entre crochets par VOS valeurs

```env
# Google Sheets
GOOGLE_SHEET_ID=[Coller votre GOOGLE_SHEET_ID ici]
GOOGLE_CREDENTIALS_FILE=config/google_credentials.json

# Email Gmail
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=[Votre email Gmail]
SMTP_PASSWORD=[Mot de passe d'application 16 caractères]

# OpenWeatherMap
OPENWEATHER_API_KEY=[Votre API key OpenWeatherMap]

# Security - Générer une clé aléatoire de 32 caractères
SECRET_KEY=[Générer une clé comme: abcdefghijklmnopqrstuvwxyz123456]

# App Configuration
APP_NAME=OliveDash
APP_TIMEZONE=Africa/Casablanca
SESSION_TIMEOUT_MINUTES=30
```

### Vérifications
- [ ] Toutes les valeurs entre [] ont été remplacées
- [ ] Pas d'espaces avant ou après les valeurs
- [ ] Le fichier est sauvegardé

---

## 🐍 Phase 7 : Installation Python

### Vérification de Python
- [ ] Ouvrir un terminal/invite de commande
- [ ] Taper : `python --version`
- [ ] Vérifier que la version est 3.9 ou supérieure
- [ ] Si non installé, télécharger depuis https://python.org

### Navigation vers le dossier du projet
```bash
cd chemin/vers/olivedash
```
- [ ] Se placer dans le dossier `olivedash/`

### Création de l'environnement virtuel

**Sur Windows :**
```bash
python -m venv venv
venv\Scripts\activate
```
- [ ] Créer l'environnement virtuel
- [ ] Activer l'environnement (vous devriez voir `(venv)` devant votre prompt)

**Sur Mac/Linux :**
```bash
python3 -m venv venv
source venv/bin/activate
```
- [ ] Créer l'environnement virtuel
- [ ] Activer l'environnement (vous devriez voir `(venv)` devant votre prompt)

### Installation des dépendances
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
- [ ] Mettre à jour pip
- [ ] Installer toutes les dépendances
- [ ] Attendre la fin de l'installation (2-3 minutes)
- [ ] Vérifier qu'il n'y a pas d'erreurs

---

## 👤 Phase 8 : Création du premier utilisateur

### Exécution du script
```bash
python scripts/create_first_user.py
```
- [ ] Lancer le script d'initialisation

### Remplir les informations
- [ ] Entrer votre **Nom**
- [ ] Entrer votre **Prénom**
- [ ] Entrer votre **Email** (le même que pour Gmail)
- [ ] Entrer votre **Téléphone** (ex: +212600000000)
- [ ] Entrer un **Mot de passe** (minimum 8 caractères)
- [ ] Confirmer le mot de passe
- [ ] Attendre la création

### Créer les utilisateurs d'exemple (optionnel)
- [ ] Répondre `o` quand demandé
- [ ] Les 8 utilisateurs seront créés avec le mot de passe : `Olive2025!`

### Vérification
- [ ] Ouvrir votre Google Sheet "OliveDash Database"
- [ ] Vérifier que la feuille "Utilisateurs" contient votre admin
- [ ] Vérifier que les 8 feuilles ont été créées

---

## 🚀 Phase 9 : Lancement de l'application

### Démarrage local
```bash
streamlit run app.py
```
- [ ] Lancer l'application
- [ ] Attendre que le navigateur s'ouvre automatiquement
- [ ] L'URL devrait être : http://localhost:8501

### Premier login
- [ ] Entrer votre email
- [ ] Entrer votre mot de passe
- [ ] Cliquer sur "Se connecter"
- [ ] Choisir "Code Email"
- [ ] Cliquer sur "Envoyer le code"
- [ ] Vérifier votre boîte email
- [ ] Entrer le code à 6 chiffres
- [ ] Cliquer sur "Vérifier"
- [ ] **Vous êtes connecté !** 🎉

---

## ✅ Phase 10 : Tests et vérifications

### Test du Dashboard
- [ ] Vérifier que les métriques s'affichent
- [ ] Vérifier que le tableau de bord est accessible

### Test du module Parcelles
- [ ] Cliquer sur "Parcelles" dans le menu
- [ ] Cliquer sur "➕ Nouvelle parcelle"
- [ ] Remplir le formulaire avec des données de test :
  - Nom : `Parcelle Test`
  - Latitude : `32.5`
  - Longitude : `-6.5`
  - Surface : `5`
  - Oliviers : `200`
  - Variétés : `Picholine, Menara`
- [ ] Cliquer sur "Enregistrer"
- [ ] Vérifier que la parcelle apparaît dans la liste
- [ ] Vérifier que la parcelle apparaît sur la carte

### Test des logs
- [ ] Cliquer sur "Historique" dans le menu
- [ ] Vérifier que les actions sont enregistrées
- [ ] Tester les filtres

### Test de déconnexion/reconnexion
- [ ] Cliquer sur "Déconnexion"
- [ ] Se reconnecter avec le même compte
- [ ] Vérifier la réception d'un nouveau code par email

---

## 🌐 Phase 11 : Déploiement en ligne (Optionnel)

### Préparation Git
```bash
git init
git add .
git commit -m "Initial commit - OliveDash v1.0.0"
```
- [ ] Initialiser Git
- [ ] Ajouter tous les fichiers
- [ ] Faire le premier commit

### Création du repository GitHub
- [ ] Aller sur https://github.com
- [ ] Cliquer sur "New repository"
- [ ] Nom : `olivedash`
- [ ] Visibilité : Private (recommandé)
- [ ] Ne pas initialiser avec README (déjà fait)
- [ ] Cliquer sur "Create repository"

### Push vers GitHub
```bash
git remote add origin https://github.com/votre-username/olivedash.git
git branch -M main
git push -u origin main
```
- [ ] Copier les commandes depuis GitHub
- [ ] Exécuter les commandes
- [ ] Vérifier que les fichiers sont sur GitHub

### Déploiement Streamlit Cloud
- [ ] Aller sur https://share.streamlit.io
- [ ] Se connecter avec GitHub
- [ ] Cliquer sur "New app"
- [ ] Repository : `votre-username/olivedash`
- [ ] Branch : `main`
- [ ] Main file : `app.py`
- [ ] Cliquer sur "Advanced settings"

### Configuration des secrets
- [ ] Copier TOUT le contenu du fichier `.env`
- [ ] Copier AUSSI tout le contenu de `google_credentials.json` au format TOML
- [ ] Coller dans la zone "Secrets"
- [ ] Format :

```toml
GOOGLE_SHEET_ID = "votre_sheet_id"
SMTP_SERVER = "smtp.gmail.com"
# ... etc (tout le .env)

[google_credentials]
type = "service_account"
project_id = "votre-project"
# ... etc (tout le JSON)
```

### Lancement du déploiement
- [ ] Cliquer sur "Deploy!"
- [ ] Attendre 2-3 minutes
- [ ] L'application est en ligne !
- [ ] Tester la connexion avec votre URL : `https://olivedash-xxx.streamlit.app`

---

## 🎯 Checklist finale

### Fonctionnalités vérifiées
- [ ] ✅ Authentification fonctionne
- [ ] ✅ Double authentification (email) fonctionne
- [ ] ✅ Dashboard s'affiche correctement
- [ ] ✅ Parcelles : création fonctionne
- [ ] ✅ Parcelles : carte s'affiche
- [ ] ✅ Logs : enregistrement fonctionne
- [ ] ✅ Déconnexion/reconnexion fonctionne

### Données vérifiées
- [ ] ✅ Google Sheet contient 8 feuilles
- [ ] ✅ Utilisateurs créés dans le sheet
- [ ] ✅ Logs s'enregistrent dans le sheet
- [ ] ✅ Parcelles s'enregistrent dans le sheet

### Documentation consultée
- [ ] 📖 README.md lu
- [ ] 📖 QUICKSTART.md lu
- [ ] 📖 STRUCTURE.md consulté
- [ ] 📖 RESUME_PROJET.md lu

---

## 🆘 En cas de problème

### Erreur lors de l'installation
- [ ] Vérifier que Python 3.9+ est installé
- [ ] Vérifier que l'environnement virtuel est activé
- [ ] Réinstaller : `pip install -r requirements.txt --force-reinstall`

### Erreur de connexion Google Sheets
- [ ] Vérifier que les APIs sont activées
- [ ] Vérifier que le sheet est partagé avec `client_email`
- [ ] Vérifier le `GOOGLE_SHEET_ID` dans `.env`
- [ ] Vérifier que `google_credentials.json` est dans `config/`

### Erreur d'envoi d'email
- [ ] Vérifier que la validation 2 étapes est activée
- [ ] Utiliser un mot de passe d'application (16 caractères)
- [ ] Vérifier `SMTP_EMAIL` et `SMTP_PASSWORD` dans `.env`

### L'application ne démarre pas
- [ ] Vérifier que toutes les dépendances sont installées
- [ ] Vérifier que le fichier `.env` existe et est correctement rempli
- [ ] Vérifier les logs dans le terminal pour identifier l'erreur

### Besoin d'aide
- [ ] Relire la documentation
- [ ] Vérifier les fichiers de logs
- [ ] Contacter le support : support@olivedash.com

---

## 🎉 Félicitations !

Si toutes les cases sont cochées, votre application **OliveDash** est :
- ✅ Installée
- ✅ Configurée
- ✅ Fonctionnelle
- ✅ Prête à l'emploi !

**Temps total d'installation : 1-2 heures**

**Prochaines étapes :**
1. Ajouter vos vraies parcelles
2. Former les 8 utilisateurs
3. Commencer à saisir les données de production

---

**Version** : 1.0.0 (MVP)
**Date** : Décembre 2025
**Statut** : Production Ready ✅
