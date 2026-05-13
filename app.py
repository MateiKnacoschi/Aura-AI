import streamlit as st
import pandas as pd

# Setări pagină
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
st.markdown("<p class='subtitle'>Prototip avansat de potrivire profesională pentru studenți și absolvenți</p>", unsafe_allow_html=True)
st.write("---")

# Secțiunea 1: Datele Personale și de Studii
st.header("📋 1. Date Personale și Educație")

col1, col2 = st.columns(2)
with col1:
    nume = st.text_input("Nume complet:", placeholder="Ex: Ioan Popescu")
    varsta = st.number_input("Vârsta ta:", min_value=16, max_value=100, value=20, step=1)
with col2:
    nivel_studii = st.selectbox(
        "Nivel de studii actual:",
        ["Student - Licență (Anul 1-2)", "Student - Licență (An Terminal)", "Absolvent Licență", "Masterand", "Doctorand", "Elev / Absolvent Liceu"]
    )
    oras = st.text_input("Orașul de proveniență:", placeholder="Ex: Iași, București, Cluj...")

st.write("---")

# Secțiunea 2: Preferințe de Muncă
st.header("⚙️ 2. Preferințe și Obiective Profesionale")

col3, col4 = st.columns(2)
with col3:
    obiectiv = st.multiselect(
        "Ce tip de oportunitate cauți? (Poți alege ambele):",
        ["Loc de muncă (Job)", "Internship / Stagiu de practică"],
        default=["Loc de muncă (Job)"]
    )
with col4:
    regim_lucru = st.multiselect(
        "Cum dorești să lucrezi? (Selecție multiplă):",
        ["În orașul de proveniență (On-site)", "Sunt dispus să mă deplasez / relochez", "Remote (De acasă)"],
        default=["Remote (De acasă)"]
    )

st.write("---")

# Secțiunea 3: Documente și Experiență Open text
st.header("📂 3. Documente și Pasiuni")

# Încarcă documente multiple
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
st.header("🤖 4. Analiză AI și Rezultate")

if st.button("Generează Analiza Profilului Complet", type="primary"):
    if nume and hobbyuri and oras and obiectiv and regim_lucru:
        st.info("🧠 Inteligența Artificială corelează studiile, locația, documentele și pasiunile tale...")
        st.success("🎉 Analiză structurală finalizată!")
        
        # Algoritm dinamic simplu pentru mockup pe baza textului introdus
        text_analizat = hobbyuri.lower()
        cuvinte = [c for c in hobbyuri.split() if len(c) > 4]
        cuvant_cheie = cuvinte.capitalize() if cuvinte else "Specialist"
        
        # Generăm date adaptate dinamic bazate pe input-ul utilizatorului
        date_ai = {
            "domeniu_principal": f"Expert / Junior în {cuvant_cheie}",
            "descriere_job": f"Având în vedere nivelul tău de studii ({nivel_studii}) și locația din {oras}, profilul tău bazat pe pasiunea '{hobbyuri}' indică un potențial ridicat.",
            "locatie_recomandata": " / ".join(regim_lucru),
            "tip_oportunitate": " și ".join(obiectiv),
            "scor_domeniu_1": 95, "scor_domeniu_2": 68, "scor_domeniu_3": 45,
            "nume_domeniu_1": f"Direcția {cuvant_cheie}", "nume_domeniu_2": "Management & Coordonare", "nume_domeniu_3": "Consultant Tehnic"
        }

        # Graficul vizual bazat pe preferințele reale ale studentului
        st.markdown(f"### 📊 Compatibilitatea pe Domenii de Activitate")
        date_grafic = pd.DataFrame({
            'Domeniu profesional personalizat': [date_ai["nume_domeniu_1"], date_ai["nume_domeniu_2"], date_ai["nume_domeniu_3"]],
            'Potrivire (%)': [date_ai["scor_domeniu_1"], date_ai["scor_domeniu_2"], date_ai["scor_domeniu_3"]]
        }).set_index('Domeniu profesional personalizat')
        
        st.bar_chart(date_grafic)
        st.write("---")

        # Afișarea rezultatelor corelate
        col_st, col_dr = st.columns(2)
        with col_st:
            st.markdown("#### 💼 Poziția Potrivită Identificată")
            st.warning(f"**{date_ai['domeniu_principal']}**")
            st.write(date_ai['descriere_job'])
            st.write(f"📍 **Mod de lucru recomandat:** {date_ai['locatie_recomandata']}")
        with col_dr:
            st.markdown("#### 🎓 Oportunitatea de Pregătire Sugerată")
            st.info(f"**{date_ai['tip_oportunitate']} adaptat profilului**")
            st.write(f"Se recomandă aplicarea la un program accelerat în regim {date_ai['locatie_recomandata']} special conceput pentru nivelul: {nivel_studii}.")
            
        st.write("---")
        
        # Generare Raport complex cu noile câmpuri introduse
        st.header("📄 5. Exportă Datele Proiectului")
        text_raport = f"""RAPORT AI EVALUARE CARIERĂ STUDENT
----------------------------------------
Candidat: {nume} | Vârstă: {varsta} ani
Origine: {oras} | Nivel Studii: {nivel_studii}
Tip Oportunitate Căutată: {date_ai['tip_oportunitate']}
Regim Lucru Preferat: {date_ai['locatie_recomandata']}
----------------------------------------
Profil AI Recomandat: {date_ai['domeniu_principal']}
Evaluare Context: {date_ai['descriere_job']}
Documente atașate procesate: {len(incarcare_documente) if incarcare_documente else 0} fișiere.
----------------------------------------
Generat cu succes în versiunea MVP v1.5
"""
        st.download_button(
            label="📥 Descarcă Raportul Complet în format TXT", 
            data=text_raport, 
            file_name=f"Raport_Complex_{nume.replace(' ', '_')}.txt", 
            use_container_width=True
        )
    else:
        st.error("⚠️ Te rugăm să completezi câmpurile obligatorii (Nume, Oraș, Hobby-uri) și să selectezi preferințele de muncă pentru analiză.")

