import os
from dotenv import load_dotenv
from pathlib import Path

# Charger les variables d'environnement
load_dotenv()

# Chemins
BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_DIR = BASE_DIR / "config"
ASSETS_DIR = BASE_DIR / "assets"

# Google Sheets
GOOGLE_SHEET_ID = os.getenv("GOOGLE_SHEET_ID")
GOOGLE_CREDENTIALS_FILE = CONFIG_DIR / "google_credentials.json"

# Email
SMTP_CONFIG = {
    "server": os.getenv("SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.getenv("SMTP_PORT", "587")),
    "email": os.getenv("SMTP_EMAIL"),
    "password": os.getenv("SMTP_PASSWORD")
}

# OpenWeatherMap
OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
OPENWEATHER_BASE_URL = "https://api.openweathermap.org/data/2.5"

# Security
SECRET_KEY = os.getenv("SECRET_KEY", "default_secret_key_change_in_production")
SESSION_TIMEOUT_MINUTES = int(os.getenv("SESSION_TIMEOUT_MINUTES", "30"))

# App
APP_NAME = os.getenv("APP_NAME", "OliveDash")
APP_TIMEZONE = os.getenv("APP_TIMEZONE", "Africa/Casablanca")

# Noms des feuilles Google Sheets
SHEET_NAMES = {
    "parcelles": "Parcelles",
    "utilisateurs": "Utilisateurs",
    "couts": "Couts",
    "production_olives": "Production_Olives",
    "production_huile": "Production_Huile",
    "prix_marche": "Prix_Marche",
    "meteo": "Meteo",
    "logs": "Logs"
}

# Coefficients de répartition
REPARTITION_COEFFICIENTS = {
    "H": 1.0,  # Homme
    "F": 0.5   # Femme
}

# Unités de mesure
UNITES = {
    "surface": "hectares",
    "olives": "quintaux",
    "huile": "litres",
    "distance": "kilomètres",
    "monnaie": "MAD"
}

# Qualités olives
QUALITES_OLIVES = ["A", "B", "C"]

# Types de coûts
TYPES_COUTS = [
    "Entretien",
    "Main d'œuvre",
    "Transport",
    "Engrais",
    "Produits phytosanitaires",
    "Irrigation",
    "Autre"
]

# Rôles utilisateurs
ROLES = {
    "admin": "Administrateur",
    "responsable": "Responsable parcelle",
    "consultation": "Consultation"
}

# Configuration Streamlit
STREAMLIT_CONFIG = {
    "page_title": APP_NAME,
    "page_icon": "🫒",
    "layout": "wide",
    "initial_sidebar_state": "expanded"
}

# Theme Configuration
THEME_CONFIG = {
    "primaryColor": "#2E7D32",
    "backgroundColor": "#FFFFFF",
    "secondaryBackgroundColor": "#F1F8E9",
    "textColor": "#212121",
    "font": "sans serif"
}
