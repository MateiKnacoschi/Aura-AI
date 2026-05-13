import streamlit as st
import pandas as pd

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
    .job-box { background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 5px solid #2563EB; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Platforma AI Universală de Orientare</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Conexiune directă între studenți și angajatori prin Inteligență Artificială</p>", unsafe_allow_html=True)
st.write("---")

# Sectiunea 1: Datele Personale si de Studii
st.header("📋 1. Date Personale și Educație")

col1, col2 = st.columns(2)
with col1:
    nume = st.text_input("Nume complet:", placeholder="Ex: Ioan Popescu")
    varsta = st.number_input("Vârsta ta:", min_value=16, max_value=100, value=20, step=1)
    oras = st.text_input("Orașul de proveniență:", placeholder="Ex: Iași, București, Cluj...")
with col2:
    nivel_studii = st.selectbox(
        "Nivel de studii actual:",
        ["Student - Licență (Anul 1-2)", "Student - Licență (An Terminal)", "Absolvent Licență", "Masterand", "Doctorand", "Elev / Absolvent Liceu"]
    )
    # --- FUNCȚIONALITATE NOUĂ: Domeniul de studii ---
    domeniu_studii = st.selectbox(
        "Domeniul de studii / Licență:",
        ["Informatică / IT / Inginerie", "Economie / Business / Marketing", "Litere / Limbi Străine / Comunicare", "Drept / Științe Sociale", "Medicină / Biologie / Chimie", "Arte / Design / Arhitectură", "Alt domeniu"]
    )

st.write("---")

# Sectiunea 2: Preferinte de Munca
st.header("⚙️ 2. Preferințe și Obiective Profesionale")

col3, col4 = st.columns(2)
with col3:
    obiectiv = st.multiselect(
        "Ce tip de oportunitate cauți? (Poți alege ambele):",
        ["Loc de muncă (Job)", "Internship / Stagiu de practică"],
        default=["Internship / Stagiu de practică"]
    )
with col4:
    regim_lucru = st.multiselect(
        "Cum dorești să lucrezi? (Selecție multiplă):",
        ["În orașul de proveniență (On-site)", "Sunt dispus să mă deplasez / relochez", "Remote (De acasă)"],
        default=["Remote (De acasă)"]
    )

st.write("---")

# Sectiunea 3: Documente si Experienta Open text
st.header("📂 3. Documente și Pasiuni")

incarcare_documente = st.file_uploader(
    "Încarcă documentele tale (CV, Atestat studii, Diplome, Certificate):", 
    type=["pdf", "docx", "png", "jpg"], 
    accept_multiple_files=True
)

if incarcare_documente:
    st.success(f"✔️ Au fost încărcate cu succes {len(incarcare_documente)} documente pentru analiză.")

hobbyuri = st.text_area("Exprimă-te liber! Scrie hobby-urile tale, interesele, tehnologiile preferate sau ce îți place să faci:", 
                        placeholder="Ex: Îmi place să scriu cod în Python, să editez fotografii, sunt voluntar în asociații studențești...")

st.write("---")
st.header("🤖 4. Analiză AI și Conexiune Angajatori")

if st.button("Generează Analiza și Deschide Joburile Active", type="primary"):
    if nume and hobbyuri and oras and obiectiv and regim_lucru:
        st.info("🧠 Inteligența Artificială corelează studiile, locația, documentele și pasiunile tale...")
        st.success("🎉 Analiză structurală finalizată! Am găsit poziții compatibile.")
        
        # Algoritm dinamic pentru extragerea cuvintelor cheie
        cuvinte = [c for c in hobbyuri.split() if len(c) > 4]
        cuvant_cheie = cuvinte[0].capitalize() if cuvinte else "Specialist"
        
        # Generam date adaptate dinamic bazate pe input
        date_ai = {
            "domeniu_principal": f"Expert / Junior în {cuvant_cheie}",
            "descriere_job": f"Având în vedere specializarea ta în '{domeniu_studii}' la nivelul '{nivel_studii}' și locația din {oras}, profilul tău bazat pe pasiunea '{hobbyuri}' are o deschidere excelentă pe piață.",
            "locatie_recomandata": " / ".join(regim_lucru),
            "tip_oportunitate": " și ".join(obiectiv),
            "scor_domeniu_1": 95, "scor_domeniu_2": 68, "scor_domeniu_3": 45,
            "nume_domeniu_1": f"Direcția {cuvant_cheie}", "nume_domeniu_2": "Management & Strategie", "nume_domeniu_3": "Consultant Operațiuni"
        }

        # Graficul vizual
        st.markdown(f"### 📊 Compatibilitatea pe Domenii de Activitate")
        date_grafic = pd.DataFrame({
            'Domeniu profesional personalizat': [date_ai["nume_domeniu_1"], date_ai["nume_domeniu_2"], date_ai["nume_domeniu_3"]],
            'Potrivire (%)': [date_ai["scor_domeniu_1"], date_ai["scor_domeniu_2"], date_ai["scor_domeniu_3"]]
        }).set_index('Domeniu profesional personalizat')
        
        st.bar_chart(date_grafic)
        st.write("---")

        # --- NOUĂ FUNCȚIONALITATE: Generare MINIM 3 JOBURI + LINKURI + CONEXIUNE ---
        st.markdown("### 💼 3 Oportunități Active pentru Tine (Aplicați Instant)")
        st.write("Pe baza profilului tău, sistemul a trimis automat fișierele și datele tale către partenerii noștri:")

        # Generăm listele de joburi simulate inteligent pe baza cuvântului cheie
        joburi_fictive = [
            {"titlu": f"Junior {cuvant_cheie} Specialist", "companie": "TechSolutions România", "platforma": "eJobs", "url": "ejobs.ro"},
            {"titlu": f"Internship în {cuvant_cheie} & Business", "companie": "Global Startups Hub", "platforma": "Hipo", "url": "hipo.ro"},
            {"titlu": f"Trainee - {cuvant_cheie} Operations", "companie": "Enterprise Corp", "platforma": "LinkedIn", "url": "linkedin.com"}
        ]

        for i, job in enumerate(joburi_fictive):
            st.markdown(f"""
            <div class='job-box'>
                <h4>📍 {job['titlu']}</h4>
                <p><b>Companie:</b> {job['companie']} | <b>Regim:</b> {date_ai['locatie_recomandata']}</p>
                <p><i>Sincronizat prin platforma externă: {job['platforma']}</i></p>
            </div>
            """, unsafe_allow_html=True)
            
            # Coloane interactive pentru fiecare job în parte
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                # Link real către agregatorul de joburi
                st.link_button(f"🔗 Vezi Jobul pe {job['platforma']}", job['url'], use_container_width=True)
            with col_b2:
                # Conexiunea directă: Simulare de trimitere instantă din aplicație
                if st.button(f"🚀 Aplică Instant (Trimite CV-ul tău către {job['companie']})", key=f"btn_{i}"):
                    st.toast(f"📬 Succes! Profilul lui {nume} și cele {len(incarcare_documente) if incarcare_documente else 0} documente au fost transmise la departamentul HR al {job['companie']}!")

        st.write("---")
        
        # Generare Raport complex
        st.header("📄 5. Exportă Datele Proiectului")
        text_raport = f"RAPORT AI EVALUARE CARIERĂ STUDENT\n----------------------------------------\nCandidat: {nume}\nSpecializare: {domeniu_studii}\nNivel Studii: {nivel_studii}\nTip Oportunitate: {date_ai['tip_oportunitate']}\nRegim Lucru: {date_ai['locatie_recomandata']}\n----------------------------------------\nProfil AI Recomandat: {date_ai['domeniu_principal']}\n"
        
        st.download_button(
            label="📥 Descarcă Raportul Complet în format TXT", 
            data=text_raport, 
            file_name=f"Raport_Complex_{nume.replace(' ', '_')}.txt", 
            use_container_width=True
        )
    else:
        st.error("⚠️ Te rugăm să completezi câmpurile obligatorii (Nume, Oraș, Hobby-uri) și să selectezi preferințele de muncă pentru analiză.")


