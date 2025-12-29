import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import json
from pathlib import Path
import os

# Configuration de la page
st.set_page_config(
    page_title="OliveDash - Tableau de bord",
    page_icon="🫒",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Import des modules
from modules.auth import check_authentication
from modules.data_manager import DataManager
from modules.production import ProductionDashboard
from modules.quality import QualityDashboard
from modules.inventory import InventoryDashboard
from modules.financial import FinancialDashboard
from modules.settings import SettingsDashboard
from config.settings import THEME_CONFIG

# Initialisation
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False

if 'data_manager' not in st.session_state:
    st.session_state.data_manager = DataManager()

def apply_custom_css():
    """Applique le CSS personnalisé"""
    st.markdown(f"""
    <style>
        .main {{
            background-color: {THEME_CONFIG['backgroundColor']};
        }}
        .stMetric {{
            background-color: {THEME_CONFIG['secondaryBackgroundColor']};
            padding: 15px;
            border-radius: 5px;
        }}
        .metric-card {{
            background: {THEME_CONFIG['secondaryBackgroundColor']};
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
    </style>
    """, unsafe_allow_html=True)

def main():
    """Fonction principale de l'application"""
    
    # Vérification de l'authentification
    if not st.session_state.authenticated:
        check_authentication()
        return
    
    # Application du CSS personnalisé
    apply_custom_css()
    
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/150x50?text=OliveDash", use_column_width=True)
        st.title("🫒 OliveDash")
        
        # Menu de navigation
        page = st.radio(
            "Navigation",
            ["📊 Vue d'ensemble", "🌿 Production", "⭐ Qualité", 
             "📦 Inventaire", "💰 Finances", "⚙️ Paramètres"]
        )
        
        st.divider()
        
        # Informations utilisateur
        st.write(f"👤 {st.session_state.get('user_name', 'Utilisateur')}")
        if st.button("🚪 Déconnexion"):
            st.session_state.authenticated = False
            st.rerun()
    
    # Contenu principal
    if page == "📊 Vue d'ensemble":
        show_overview()
    elif page == "🌿 Production":
        ProductionDashboard(st.session_state.data_manager).render()
    elif page == "⭐ Qualité":
        QualityDashboard(st.session_state.data_manager).render()
    elif page == "📦 Inventaire":
        InventoryDashboard(st.session_state.data_manager).render()
    elif page == "💰 Finances":
        FinancialDashboard(st.session_state.data_manager).render()
    elif page == "⚙️ Paramètres":
        SettingsDashboard(st.session_state.data_manager).render()

def show_overview():
    """Affiche la vue d'ensemble du dashboard"""
    st.title("📊 Vue d'ensemble")
    
    # Métriques principales
    col1, col2, col3, col4 = st.columns(4)
    
    data_manager = st.session_state.data_manager
    
    with col1:
        production_total = data_manager.get_total_production()
        st.metric(
            "Production totale",
            f"{production_total:,.0f} L",
            delta="+12% vs année dernière"
        )
    
    with col2:
        qualite_moyenne = data_manager.get_average_quality()
        st.metric(
            "Qualité moyenne",
            f"{qualite_moyenne:.1f}/10",
            delta="+0.5"
        )
    
    with col3:
        stock_actuel = data_manager.get_current_stock()
        st.metric(
            "Stock actuel",
            f"{stock_actuel:,.0f} L",
            delta="-8%"
        )
    
    with col4:
        chiffre_affaires = data_manager.get_revenue()
        st.metric(
            "Chiffre d'affaires",
            f"{chiffre_affaires:,.0f} €",
            delta="+15%"
        )
    
    st.divider()
    
    # Graphiques
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📈 Évolution de la production")
        production_data = data_manager.get_production_trend()
        if not production_data.empty:
            fig = px.line(
                production_data,
                x='date',
                y='production',
                title='Production mensuelle (L)'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Aucune donnée de production disponible")
    
    with col2:
        st.subheader("🎯 Répartition des ventes")
        sales_data = data_manager.get_sales_distribution()
        if not sales_data.empty:
            fig = px.pie(
                sales_data,
                values='montant',
                names='categorie',
                title='Ventes par catégorie'
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Aucune donnée de vente disponible")
    
    # Alertes et notifications
    st.divider()
    st.subheader("🔔 Alertes et notifications")
    
    alerts = data_manager.get_alerts()
    if alerts:
        for alert in alerts:
            alert_type = alert.get('type', 'info')
            if alert_type == 'warning':
                st.warning(alert['message'])
            elif alert_type == 'error':
                st.error(alert['message'])
            else:
                st.info(alert['message'])
    else:
        st.success("✅ Aucune alerte pour le moment")

if __name__ == "__main__":
    main()
