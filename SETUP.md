# 🫒 OliveDash - Guide de Mise en Service

## 📋 Vue d'ensemble

OliveDash est un dashboard Streamlit pour la gestion de production oléicole avec:
- 🔐 Authentification 2FA (Email + Google Authenticator)
- 📍 Gestion des parcelles avec carte interactive
- 💰 Suivi des coûts et production
- 📊 Graphiques et analytics en temps réel
- ☁️ Stockage gratuit sur Google Drive (2TB)
- 👥 Support pour 8 utilisateurs

## 🚀 Installation Rapide

### 1. Cloner le dépôt
```bash
git clone https://github.com/hack2night/olivedash.git
cd olivedash
```

### 2. Créer l'environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\\Scripts\\activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

### 1. Google Cloud Setup (15 min)

1. Allez sur [Google Cloud Console](https://console.cloud.google.com)
2. Créez un nouveau projet "OliveDash"
3. Activez les APIs:
   - Google Sheets API
   - Google Drive API
4. Créez des credentials (Service Account)
5. Téléchargez le fichier JSON dans `config/google_credentials.json`

### 2. Google Sheets Setup (5 min)

1. Créez un nouveau Google Spreadsheet nommé "OliveDash_Data"
2. Créez 8 feuilles:
   - Parcelles
   - Utilisateurs
   - Couts
   - Production_Olives
   - Production_Huile
   - Prix_Marche
   - Meteo
   - Logs

3. Partagez le sheet avec l'email du service account

### 3. Variables d'environnement

Créez un fichier `.env` à la racine:

```env
# Google Sheets
SPREADSHEET_ID=votre_spreadsheet_id
GOOGLE_CREDENTIALS_PATH=config/google_credentials.json

# Email Configuration (Gmail)
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre.email@gmail.com
SMTP_PASSWORD=votre_mot_de_passe_app

# OpenWeather API
OPENWEATHER_API_KEY=votre_api_key

# App Configuration
APP_NAME=OliveDash
APP_TIMEZONE=Africa/Casablanca
SECRET_KEY=generer_une_cle_secrete_aleatoire
```

### 4. Gmail App Password

1. Activez la 2FA sur votre compte Gmail
2. Générez un "App Password"
3. Utilisez ce password dans `SMTP_PASSWORD`

## 📁 Structure du Projet

```
olivedash/
├── app.py                 # Application principale
├── requirements.txt       # Dépendances
├── .env                   # Variables d'environnement
├── config/
│   ├── settings.py       # Configuration
│   └── google_credentials.json
├── modules/
│   ├── auth.py           # Authentification
│   ├── parcelles.py      # Gestion parcelles
│   ├── logs.py           # Système de logs
│   └── ...
└── utils/
    ├── database.py       # Connexion Google Sheets
    └── ...
```

## 🎯 Prochaines étapes

1. **Téléchargez tous les fichiers depuis Claude**
   - Ouvrez la conversation Claude
   - Cliquez sur "Artéfacts" pour voir tous les fichiers générés
   - Copiez chaque fichier dans la structure appropriée

2. **Fichiers essentiels à ajouter:**
   - `app.py` - Application principale
   - `config/settings.py` - Configuration globale
   - `modules/auth.py` - Système d'authentification
   - `modules/parcelles.py` - Gestion des parcelles
   - `modules/logs.py` - Système de logs
   - `utils/database.py` - Connexion Google Sheets
   - `.streamlit/config.toml` - Configuration Streamlit

3. **Lancer l'application:**
```bash
streamlit run app.py
```

## 📚 Documentation

Pour plus de détails, consultez les fichiers générés par Claude:
- `CHECKLIST.md` - Liste complète des étapes
- `QUICKSTART.md` - Guide de démarrage rapide  
- `INSTALLATION_COMPLETE.md` - Guide détaillé
- `STRUCTURE.md` - Architecture du projet

## 💰 Coûts

- Infrastructure: **0€/mois** (100% gratuit)
- Hébergement: Streamlit Community Cloud (gratuit)
- Stockage: Google Drive 2TB (déjà payé)
- APIs: Plans gratuits

## 🆘 Support

Pour obtenir de l'aide:
1. Consultez les fichiers de documentation
2. Ouvrez une issue sur GitHub
3. Contactez @hack2night

---

**Status:** Phase 1 (MVP) complétée ✅

**Prochaines phases:**
- Phase 2: Modules Utilisateurs, Coûts, Production
- Phase 3: Prix du marché, Répartition automatique  
- Phase 4: Météo, Notifications, Optimisations
