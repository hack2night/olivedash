# 🫒 OliveDash

> Dashboard Streamlit pour la gestion de production oléicole avec Google Drive & Google Sheets

![Status](https://img.shields.io/badge/status-MVP%20Phase%201-green)
![License](https://img.shields.io/badge/license-MIT-blue)
![Python](https://img.shields.io/badge/python-3.8+-blue)

## 📊 Fonctionnalités

### Phase 1 (MVP) - ✅ Complétée

- 🔐 **Authentification 2FA** - Email + Google Authenticator
- 📍 **Gestion des parcelles** - Carte interactive avec Folium
- 📁 **Système de logs** - Historique complet avec export
- 📊 **Dashboard temps réel** - Métriques et statistiques
- ☁️ **Stockage cloud** - Google Drive (2TB) + Google Sheets
- 👥 **Multi-utilisateurs** - Support pour 8 utilisateurs

### Prochaines phases

- **Phase 2** : Modules Utilisateurs, Coûts, Production
- **Phase 3** : Prix du marché, Répartition automatique
- **Phase 4** : Météo, Notifications, Optimisations

## 🚀 Installation

### Prérequis

- Python 3.8+
- Compte Google Cloud (gratuit)
- Compte Gmail pour les notifications

### Installation rapide

```bash
# Cloner le dépôt
git clone https://github.com/hack2night/olivedash.git
cd olivedash

# Créer l'environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows: venv\\Scripts\\activate

# Installer les dépendances
pip install -r requirements.txt

# Configurer les variables d'environnement
cp .env.example .env
# Puis éditez .env avec vos credentials

# Lancer l'application
streamlit run app.py
```

## 📚 Documentation

- **[SETUP.md](SETUP.md)** - Guide complet de mise en service
- **[CHECKLIST.md](CHECKLIST.md)** - Liste des étapes d'installation (disponible dans les artéfacts Claude)
- **[QUICKSTART.md](QUICKSTART.md)** - Guide de démarrage rapide (disponible dans les artéfacts Claude)

## ⚙️ Configuration

### 1. Google Cloud

1. Créez un projet sur [Google Cloud Console](https://console.cloud.google.com)
2. Activez les APIs :
   - Google Sheets API
   - Google Drive API
3. Créez un Service Account
4. Téléchargez les credentials dans `config/google_credentials.json`

### 2. Google Sheets

1. Créez un Google Spreadsheet "OliveDash_Data"
2. Créez 8 feuilles : Parcelles, Utilisateurs, Couts, Production_Olives, Production_Huile, Prix_Marche, Meteo, Logs
3. Partagez avec l'email du Service Account

### 3. Variables d'environnement

Créez un fichier `.env` :

```env
SPREADSHEET_ID=votre_id_spreadsheet
GOOGLE_CREDENTIALS_PATH=config/google_credentials.json
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=votre.email@gmail.com
SMTP_PASSWORD=votre_app_password
OPENWEATHER_API_KEY=votre_api_key
APP_NAME=OliveDash
APP_TIMEZONE=Africa/Casablanca
SECRET_KEY=generer_une_cle_aleatoire
```

## 💻 Stack Technique

- **Frontend** : Streamlit, Plotly, Folium, Altair
- **Backend** : Python, Google Sheets API, Google Drive API
- **Authentification** : bcrypt, pyotp, streamlit-authenticator
- **Data** : Pandas, NumPy
- **Météo** : OpenWeatherMap API
- **Web Scraping** : BeautifulSoup4, lxml

## 💰 Coûts

- **Infrastructure** : 0€/mois (100% gratuit)
- **Hébergement** : Streamlit Community Cloud (gratuit)
- **Stockage** : Google Drive 2TB (déjà payé)
- **APIs** : Plans gratuits suffisants

## 📝 Structure du projet

```
olivedash/
├── app.py                    # Application principale
├── requirements.txt          # Dépendances Python
├── .env                      # Variables d'environnement
├── config/
│   ├── settings.py          # Configuration globale
│   └── google_credentials.json
├── modules/
│   ├── auth.py              # Authentification 2FA
│   ├── parcelles.py         # Gestion parcelles
│   ├── logs.py              # Système de logs
│   └── ...
└── utils/
    ├── database.py          # Connexion Google Sheets
    └── ...
```

## 🤝 Contribution

Les contributions sont les bienvenues ! N'hésitez pas à :

1. Fork le projet
2. Créer une branche (`git checkout -b feature/AmazingFeature`)
3. Commit vos changements (`git commit -m 'Add some AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 👨‍💻 Auteur

**hack2night**

- GitHub: [@hack2night](https://github.com/hack2night)

## 📝 License

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🆘 Support

Pour obtenir de l'aide :

1. Consultez la documentation dans `SETUP.md`
2. Ouvrez une [issue](https://github.com/hack2night/olivedash/issues)
3. Contactez [@hack2night](https://github.com/hack2night)

---

**Made with ❤️ for olive grove management**
