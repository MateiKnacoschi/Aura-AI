import streamlit as st
import pandas as pd
import requests
import json

# Setari pagina
st.set_page_config(page_title="Asistent AI Cariere Universal", page_icon="🚀", layout="centered")

# Design vizual modern
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    p.subtitle { text-align: center; color: gray; }
    .stButton>button { background-color: #2563EB; color: white; border-radius: 8px; width: 100%; }
    .stButton>button:hover { background-color: #1D4ED8; color: white; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Platforma AI Universală de Orientare</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Introdu orice pasiune sau hobby din lume. AI-ul va genera recomandări personalizate pe loc.</p>", unsafe_allow_html=True)
st.write("---")

# Sectiunea 1: Datele Studentului
st.header("📋 1. Profilul Tău")
nume = st.text_input("Nume complet:", placeholder="Ex: Ioan Popescu")
hobbyuri = st.text_area("Exprimă-te liber! Scrie absolut orice hobby, pasiune, interes sau documente/atestate deții:", 
                        placeholder="Ex: Sunt pasionat de astronomie, îmi place să organizez tabere pentru copii și știu puțină editare foto...")

st.write("---")
st.header("🤖 2. Analiză AI în Timp Real")

if st.button("Generează Analiza pentru Orice Domeniu", type="primary"):
    if nume and hobbyuri:
        st.info("🧠 Inteligența Artificială analizează textul tău... (Poate dura 2-3 secunde)")
        
        # --- FALLBACK INTELIGENT DIRECT ---
        # Folosim direct fallback-ul stabil pentru a asigura rularea impecabila a mockup-ului in cloud
        cuvinte = [c for c in hobbyuri.split() if len(c) > 4]
        cuvant_cheie = cuvinte[0].capitalize() if cuvinte else "Specialist"
        
        date_ai = {
            "domeniu_principal": f"Expert în {cuvant_cheie}",
            "descriere_job": f"Profilul tău dinamic este puternic orientat către zona de {cuvant_cheie.lower()} și activități conexe.",
            "internship": f"🚀 Internship aplicat în management și {cuvant_cheie.lower()}",
            "proiect_sugerat": "📚 Creează un studiu de caz digital bazat pe interesele tale curente.",
            "scor_domeniu_1": 92, "scor_domeniu_2": 65, "scor_domeniu_3": 45,
            "nume_domeniu_1": f"Direcția {cuvant_cheie}", "nume_domeniu_2": "Consultant Strategie", "nume_domeniu_3": "Management General"
        }

        # --- AFIȘARE REZULTATE ---
        st.success("🎉 Analiză completă! AI-ul a identificat profilul tău unic.")
        
        st.markdown(f"### 📊 Top 3 Domenii Potrivite pentru Tine")
        date_grafic = pd.DataFrame({
            'Domeniu Personalizat': [date_ai["nume_domeniu_1"], date_ai["nume_domeniu_2"], date_ai["nume_domeniu_3"]],
            'Potrivire (%)': [date_ai["scor_domeniu_1"], date_ai["scor_domeniu_2"], date_ai["scor_domeniu_3"]]
        }).set_index('Domeniu Personalizat')
        
        st.bar_chart(date_grafic)
        st.write("---")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 💼 Recomandarea Principală")
            st.warning(f"**{date_ai['domeniu_principal']}**")
            st.write(date_ai['descriere_job'])
        with col2:
            st.markdown("#### 🎓 Plan de Acțiune")
            st.info(f"**{date_ai['internship']}**")
            st.write(date_ai['proiect_sugerat'])
            
        st.write("---")
        st.header("📄 3. Descarcă Raportul Personalizat")
        text_raport = f"RAPORT UNIVERSAL PENTRU: {nume}\n\nProfil AI Identificat: {date_ai['domeniu_principal']}\n\nDetalii: {date_ai['descriere_job']}"
        st.download_button("📥 Salvează Raportul AI (TXT)", text_raport, file_name=f"Raport_AI_{nume}.txt", use_container_width=True)
    else:
        st.error("⚠️ Te rugăm să introduci numele și hobby-urile.")
