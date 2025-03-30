import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# Configuration de la page
st.set_page_config(
    page_title="Analyse des Forages Miniers",
    layout="wide",  # Utilise toute la largeur de la page
    initial_sidebar_state="expanded",
)

# Titre principal de l'application
st.title("💎 Analyse des Données de Forages Miniers")
st.write("Bienvenue dans cette application interactive pour analyser et visualiser vos données de forages miniers !")

# Ajout des onglets
tab1, tab2, tab3, tab4 = st.tabs(["📂 Importer les données", "👁️ Aperçu", "📊 Statistiques", "🌐 Visualisation 3D"])

# Initialisation des variables pour stocker les données
collars, survey, lithology, assays = None, None, None, None

# --- Onglet 1 : Importer les données ---
with tab1:
    st.header("📂 Importer vos fichiers CSV")
    st.write("Téléchargez vos fichiers contenant les informations des forages.")

    # Chargement des fichiers
    collars = st.file_uploader("Fichier des Collars (positions des forages)", type=["csv"])
    survey = st.file_uploader("Fichier du Survey (orientations des forages)", type=["csv"])
    lithology = st.file_uploader("Fichier de Lithologie (stratigraphie)", type=["csv"])
    assays = st.file_uploader("Fichier des Assays (analyses géochimiques)", type=["csv"])

    # Feedback utilisateur
    if collars or survey or lithology or assays:
        st.success("✅ Fichiers chargés avec succès ! Passez aux onglets suivants pour explorer vos données.")
    else:
        st.warning("⚠️ Veuillez importer tous les fichiers nécessaires pour continuer.")

# --- Onglet 2 : Aperçu des données ---
with tab2:
    st.header("👁️ Aperçu des Données")

    if collars:
        st.subheader("📍 Données des Collars")
        df_collars = pd.read_csv(collars)
        st.dataframe(df_collars)
    else:
        st.info("ℹ️ Importez un fichier des collars pour afficher les données.")

    if survey:
        st.subheader("🧭 Données du Survey")
        df_survey = pd.read_csv(survey)
        st.dataframe(df_survey)
    else:
        st.info("ℹ️ Importez un fichier du survey pour afficher les données.")

    if lithology:
        st.subheader("🪨 Données de Lithologie")
        df_lithology = pd.read_csv(lithology)
        st.dataframe(df_lithology)
    else:
        st.info("ℹ️ Importez un fichier de lithologie pour afficher les données.")

    if assays:
        st.subheader("🔬 Données des Assays")
        df_assays = pd.read_csv(assays)
        st.dataframe(df_assays)
    else:
        st.info("ℹ️ Importez un fichier des assays pour afficher les données.")

# --- Onglet 3 : Statistiques ---
with tab3:
    st.header("📊 Statistiques")

    col1, col2 = st.columns(2)

    with col1:
        if collars:
            st.subheader("📍 Statistiques des Collars")
            st.write(df_collars.describe())
        else:
            st.info("ℹ️ Importez un fichier des collars pour afficher les statistiques.")

        if survey:
            st.subheader("🧭 Statistiques du Survey")
            st.write(df_survey.describe())
        else:
            st.info("ℹ️ Importez un fichier du survey pour afficher les statistiques.")

    with col2:
        if lithology:
            st.subheader("🪨 Statistiques de Lithologie")
            st.write(df_lithology.describe())
        else:
            st.info("ℹ️ Importez un fichier de lithologie pour afficher les statistiques.")

        if assays:
            st.subheader("🔬 Statistiques des Assays")
            st.write(df_assays.describe())
        else:
            st.info("ℹ️ Importez un fichier des assays pour afficher les statistiques.")

# --- Onglet 4 : Visualisation 3D ---
with tab4:
    st.header("🌐 Visualisation 3D des Forages")

    if collars and survey:
        st.write("Voici une visualisation interactive en 3D des positions des forages.")
        
        # Exemple de visualisation 3D avec Plotly
        df_collars = pd.read_csv(collars)  # Chargement des données des collars
        fig = px.scatter_3d(
            df_collars,
            x="X",  # Colonne X
            y="Y",  # Colonne Y
            z="Z",  # Colonne Z
            color="Elevation",  # Couleur basée sur l'élévation
            title="Carte 3D des Forages",
        )
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info(
            "ℹ️ Veuillez importer les fichiers des collars et du survey pour visualiser la carte 3D des forages."
        )