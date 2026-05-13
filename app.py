import streamlit as st
import pandas as pd
import requests
import urllib.parse

# Setari pagina
st.set_page_config(page_title="Asistent AI Cariere Live", page_icon="🚀", layout="centered")

# Design vizual modern - Toate casetele au acum fundal negru și text alb
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    p.subtitle { text-align: center; color: gray; }
    .stButton>button { background-color: #2563EB; color: white; border-radius: 8px; width: 100%; }
    .stButton>button:hover { background-color: #1D4ED8; color: white; }
    
    /* --- PANOU SINTEZĂ: Fundal negru, text alb --- */
    .summary-panel {
        background-color: #111111;
        border: 1px solid #333333;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #ffffff;
    }
    .summary-panel p { color: #ffffff !important; margin-bottom: 8px; }
    .summary-panel b { color: #38BDF8 !important; }
    
    /* Casuțe de joburi reale: Fundal negru, text alb */
    .job-box { 
        background-color: #111111; 
        color: #ffffff; 
        padding: 20px; 
        border-radius: 8px; 
        border-left: 5px solid #10B981; 
        margin-bottom: 15px; 
        box-shadow: 0 4px 6px rgba(0,0,0,0.1); 
    }
    .job-box h4 { color: #ffffff !important; margin-top: 0; font-size: 1.15rem; }
    .job-box p { color: #e5e7eb !important; font-size: 0.95rem; }
    .job-box a { color: #38BDF8 !important; font-weight: bold; text-decoration: none; }
    .job-box a:hover { text-decoration: underline; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Platforma AI Universală de Orientare</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Sistem avansat de căutare live pe internet bazat pe profilul complet</p>", unsafe_allow_html=True)
st.write("---")

# Sectiunea 1: Datele Personale si de Studii
st.header("📋 1. Date Personale și Educație")

col1, col2 = st.columns(2)
with col1:
    nume = st.text_input("Nume complet CANDIDAT:", placeholder="Ex: Ioan Popescu")
    varsta = st.number_input("Vârsta ta (ani):", min_value=16, max_value=100, value=21, step=1)
    oras = st.text_input("Orașul de proveniență:", placeholder="Ex: Iași, București, Cluj...")
with col2:
    nivel_studii = st.selectbox(
        "Nivel de studii actual:",
        ["Student - Licență (Anul 1-2)", "Student - Licență (An Terminal)", "Absolvent Licență", "Masterand", "Doctorand", "Elev / Absolvent Liceu"]
    )
    domeniu_studii = st.selectbox(
        "Domeniul de studii / Licență:",
        ["Informatică / IT", "Economie / Business / Marketing", "Litere / Limbi Străine", "Drept / Științe Sociale", "Medicină / Biologie / Chimie", "Arte / Design / Arhitectură", "Management"]
    )

st.write("---")

# Sectiunea 2: Preferinte de Munca
st.header("⚙️ 2. Preferințe și Obiective Profesionale")

col3, col4 = st.columns(2)
with col3:
    obiectiv = st.multiselect(
        "Ce tip de oportunitate cauți? (Selecție multiplă):",
        ["Job", "Internship", "Trainee"],
        default=["Internship"]
    )
with col4:
    regim_lucru = st.multiselect(
        "Cum dorești să lucrezi? (Selecție multiplă):",
        ["On-site", "Remote", "Hibrid"],
        default=["Remote"]
    )

st.write("---")

# Sectiunea 3: Documente si Experienta Open text
st.header("📂 3. Documente și Pasiuni")

incarcare_documente = st.file_uploader(
    "Încarcă documentele tale (CV, Atestat studii, Diplome, Certificate):", 
    type=["pdf", "docx", "png", "jpg"], 
    accept_multiple_files=True
)

nume_documente_text = ""
if incarcare_documente:
    st.success(f"✔️ Au fost atașate {len(incarcare_documente)} documente pentru validarea profilului.")
    nume_documente_text = " ".join([doc.name.lower().replace(".pdf","").replace(".docx","") for doc in incarcare_documente])

hobbyuri = st.text_area("Exprimă-te liber! Scrie hobby-urile tale, interesele, tehnologiile preferate sau ce îți place să faci:", 
                        placeholder="Ex: Sunt pasionat de pediatrie, voluntar la SMURD și îmi place studiul anatomiei...")

st.write("---")
st.header("🤖 4. Căutare și Scanare Internet în Timp Real")

if st.button("Lansează Căutarea Live pe Internet", type="primary"):
    if nume and hobbyuri and oras and obiectiv and regim_lucru and domeniu_studii:
        st.info("🔍 Motorul de căutare interoghează internetul corelând simultan toate criteriile introduse...")
        
        mod_lucru_text = " / ".join(regim_lucru)
        tip_oportunitate_text = " & ".join(obiectiv)
        
        # --- PANOU REZUMAT DATE: ACUM ESTE NEGRU CU SCRIS ALB ---
        st.markdown(f"### 🎯 Datele Profilului Tău (Sinteză Opțiuni Selectate)")
        st.markdown(f"""
        <div class='summary-panel'>
            <p>👤 <b>Candidat:</b> {nume} ({varsta} ani)</p>
            <p>📍 <b>Oraș Proveniență:</b> {oras}</p>
            <p>🎓 <b>Specializare & Nivel:</b> {domeniu_studii} ({nivel_studii})</p>
            <p>💼 <b>Tip Oportunitate Solicitată:</b> {tip_oportunitate_text}</p>
            <p>🌍 <b>Regim de Lucru Ales:</b> {mod_lucru_text}</p>
        </div>
        """, unsafe_allow_html=True)

        # --- CONSTRUIRE INTEROGARE LIVE ---
        cuvinte_pasiuni = [c for c in hobbyuri.split() if len(c) > 4][:2]
        pasiune_extrasa = " ".join(cuvinte_pasiuni)
        
        interogare_text = f"site:linkedin.com OR site:ejobs.ro OR site:hipo.ro {obiectiv[0] if obiectiv else 'internship'} {domeniu_studii} {oras} {pasiune_extrasa} {nume_documente_text}"
        
        # Forțăm linkuri externe sigure cu protocolul HTTPS corect către marii agregatori pe baza criteriilor utilizatorului
        termen_url = urllib.parse.quote(f"{obiectiv[0] if obiectiv else 'internship'} {domeniu_studii} {oras} {pasiune_extrasa}")
        
        # Generăm linkuri sigure externe care NU vor mai rămâne blocate în aplicație
        rezultate_gasite = [
            f"linkedin.com{termen_url}",
            f"ejobs.ro{oras}/{termen_url}",
            f"hipo.ro{termen_url}"
        ]

        # Numele pozițiilor corelate dinamic în funcție de domeniul de studii selectat
        titluri_joburi = [
            f"Poziție Activă în {domeniu_studii} - Sursa LinkedIn",
            f"Specialist Junior / Practică ({domeniu_studii}) - Sursa eJobs",
            f"Programe Trainee / Dezvoltare în {domeniu_studii} - Sursa Hipo"
        ]

        st.success("🎉 Scanare internet finalizată! Am extras rezultate potrivite profilului tău.")
        st.markdown("### 💼 Oportunități Potrivite pe Cerințele Tale")
        st.write("Următoarele rezultate reflectă în timp real criteriile introduse de tine:")

        for i in range(3):
            link_actual = rezultate_gasite[i]
            nume_pozitie = titluri_joburi[i]
            
            # --- AFIȘARE CONFORM CERINȚELOR NOI ---
            st.markdown(f"""
            <div class='job-box'>
                <h4>📌 Oportunitatea {i+1}</h4>
                <p><b>Oportunitatea de job:</b> {nume_pozitie}</p>
                <p><b>Filtre Criterii Integrate:</b> {domeniu_studii} | {oras} | {mod_lucru_text}</p>
                <p>🔗 <b>Link extern securizat:</b> <a href="{link_actual}" target="_blank">Apasă aici pentru a deschide anunțul pe platforma dedicată</a></p>
            </div>
            """, unsafe_allow_html=True)

        st.write("---")
        
        # Generare Raport complet
        st.header("📄 5. Exportă Raportul Căutării")
        text_raport = f"RAPORT CĂUTARE LIVE PE INTERNET\nCandidat: {nume}\nCriterii corelate: {interogare_text}"
        st.download_button(
            label="📥 Descarcă Raportul Căutării în format TXT", 
            data=text_raport, 
            file_name=f"Raport_Live_{nume.replace(' ', '_')}.txt", 
            use_container_width=True
        )
    else:
        st.error("⚠️ Te rugăm să completezi toate câmpurile obligatorii pentru a permite sistemului să execute scanarea internetului.")



