# 🚀 Guide de Démarrage Rapide - OliveDash

Guide pour lancer votre dashboard en moins de 30 minutes !

## ⚡ Installation Express

### 1. Cloner et installer (5 minutes)

```bash
# Cloner le projet
git clone https://github.com/votre-repo/olivedash.git
cd olivedash

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement
# Windows :
venv\Scripts\activate
# Mac/Linux :
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

### 2. Configuration Google Sheets (10 minutes)

#### A. Créer le projet Google Cloud

1. Aller sur https://console.cloud.google.com/
2. Créer un nouveau projet "OliveDash"
3. Activer les APIs :
   - Rechercher "Google Sheets API" → Activer
   - Rechercher "Google Drive API" → Activer

#### B. Créer le compte de service

1. Menu → IAM & Admin → Service Accounts
2. "Create Service Account"
   - Nom : `olivedash-service`
   - Rôle : Éditeur
3. Actions → Manage Keys → Add Key → Create new key → JSON
4. Télécharger le fichier JSON
5. Le renommer en `google_credentials.json`
6. Le placer dans un dossier `config/` à la racine du projet

#### C. Créer le Google Sheet

1. Aller sur https://docs.google.com/spreadsheets/
2. Créer un nouveau sheet
3. Le nommer "OliveDash Database"
4. Copier l'ID depuis l'URL :
   ```
   https://docs.google.com/spreadsheets/d/[COPIEZ_CET_ID]/edit
   ```
5. Cliquer sur "Partager"
6. Coller l'email du compte de service (dans le fichier JSON, champ `client_email`)
7. Donner les droits "Éditeur"

### 3. Configuration Email Gmail (5 minutes)

1. Aller sur https://myaccount.google.com/security
2. Activer la "Validation en deux étapes"
3. Aller dans "Mots de passe des applications"
4. Créer un mot de passe pour "Mail"
5. Copier le mot de passe généré (16 caractères)

### 4. Configuration OpenWeatherMap (3 minutes)

1. Créer un compte sur https://openweathermap.org/api
2. Choisir le plan gratuit (1000 appels/jour)
3. Copier votre API Key

### 5. Créer le fichier .env (2 minutes)

Créer un fichier `.env` à la racine du projet :

```env
# Google Sheets - Coller l'ID copié à l'étape 2C
GOOGLE_SHEET_ID=1abc...xyz

# Email Gmail
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_EMAIL=votre.email@gmail.com
SMTP_PASSWORD=abcd efgh ijkl mnop  # Mot de passe d'application

# OpenWeatherMap
OPENWEATHER_API_KEY=votre_api_key

# Sécurité - Générer une clé aléatoire de 32 caractères
SECRET_KEY=abcdefghijklmnopqrstuvwxyz123456

# Configuration
APP_NAME=OliveDash
APP_TIMEZONE=Africa/Casablanca
SESSION_TIMEOUT_MINUTES=30
```

### 6. Créer le premier utilisateur (2 minutes)

```bash
python scripts/create_first_user.py
```

Suivre les instructions pour créer votre compte administrateur.

### 7. Lancer l'application (1 minute)

```bash
streamlit run app.py
```

🎉 **C'est prêt !** L'application s'ouvre automatiquement dans votre navigateur sur http://localhost:8501

## 📱 Première Connexion

1. Entrer votre email et mot de passe
2. Choisir l'authentification par email
3. Cliquer sur "Envoyer le code"
4. Vérifier votre email et entrer le code reçu
5. Vous êtes connecté ! 🎊

## ✅ Checklist de démarrage

- [ ] Projet cloné et dépendances installées
- [ ] Projet Google Cloud créé
- [ ] APIs Google Sheets et Drive activées
- [ ] Compte de service créé et fichier JSON téléchargé
- [ ] Google Sheet créé et partagé avec le compte de service
- [ ] Compte Gmail configuré avec mot de passe d'application
- [ ] Compte OpenWeatherMap créé
- [ ] Fichier .env créé et rempli
- [ ] Premier utilisateur admin créé
- [ ] Application lancée avec succès

## 🆘 Problèmes courants

### "Erreur de connexion à Google Sheets"
→ Vérifier que le sheet est bien partagé avec l'email du compte de service

### "Module not found"
→ Réactiver l'environnement virtuel : `source venv/bin/activate`

### "Erreur envoi email"
→ Vérifier le mot de passe d'application Gmail (pas votre mot de passe normal)

### "Sheet not found"
→ Vérifier le GOOGLE_SHEET_ID dans le fichier .env

## 📚 Prochaines étapes

1. **Ajouter des parcelles**
   - Menu → Parcelles → Nouvelle parcelle
   - Remplir avec vos coordonnées GPS réelles

2. **Ajouter les 8 utilisateurs**
   - Lors de la création du premier admin, répondre "oui" pour créer les utilisateurs d'exemple
   - Ou les ajouter manuellement dans Google Sheets

3. **Configurer Google Authenticator** (optionnel)
   - Paramètres → Sécurité
   - Scanner le QR code avec l'app Google Authenticator

4. **Explorer les modules**
   - Dashboard : vue d'ensemble
   - Parcelles : gestion et carte
   - Logs : historique des actions

## 🚀 Déploiement en ligne (GRATUIT)

Une fois que tout fonctionne en local :

1. Pusher sur GitHub
2. Aller sur https://share.streamlit.io
3. Connecter votre repo
4. Configurer les secrets (copier/coller depuis .env)
5. Déployer !

Votre dashboard sera accessible publiquement avec une URL type :
`https://votre-app.streamlit.app`

## 💡 Conseils

- **Sauvegardez régulièrement** votre Google Sheet
- **Ne partagez JAMAIS** votre fichier .env ou google_credentials.json
- **Testez avec des données fictives** avant d'entrer vos vraies données
- **Configurez des alertes** pour être notifié des modifications

## 📞 Besoin d'aide ?

- Documentation complète : voir README.md
- Issues GitHub : [votre-repo/issues](https://github.com)
- Email : support@olivedash.com

---

**Temps total d'installation : ~30 minutes**

Bonne gestion de votre production oléicole ! 🫒
