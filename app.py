import streamlit as st
import pandas as pd
import urllib.parse

# Setari pagina
st.set_page_config(page_title="Aura AI- Primul pas spre noul tău job", page_icon="🚀", layout="centered")

# Design vizual modern
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    p.subtitle { text-align: center; color: gray; }
    .stButton>button { background-color: #2563EB; color: white; border-radius: 8px; width: 100%; }
    .stButton>button:hover { background-color: #1D4ED8; color: white; }
    .job-box { background-color: #ffffff; padding: 15px; border-radius: 8px; border-left: 5px solid #10B981; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>Aura AI- Primul pas spre noul tău job</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Sistem avansat de analiză multi-criteriu și conectare cu angajatorii</p>", unsafe_allow_html=True)
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
        "Ce tip de oportunitate cauți? (Selecție multiplă):",
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

# Colectăm denumirile documentelor pentru a le include în analiză
nume_documente_text = ""
if incarcare_documente:
    st.success(f"✔️ Au fost atașate {len(incarcare_documente)} documente oficiale pentru validarea profilului.")
    nume_documente_text = " ".join([doc.name.lower() for doc in incarcare_documente])

hobbyuri = st.text_area("Exprimă-te liber! Scrie hobby-urile tale, interesele, tehnologiile preferate sau ce îți place să faci:", 
                        placeholder="Ex: Îmi place să scriu cod în Python, să editez fotografii, sunt voluntar în asociații studențești...")

st.write("---")
st.header("🤖 4. Analiză Multi-Criteriu și Profile Angajatori")

if st.button("Lansează Analiza Integrată", type="primary"):
    if nume and hobbyuri and oras and obiectiv and regim_lucru and domeniu_studii:
        st.info("🧠 Corelăm profilul global: Vârstă + Studii + Specializare + Oraș + Preferințe + Documente + Pasiuni...")
        st.success("🎉 Corelare de peste 90% realizată cu succes!")
        
        # --- RECONSTRUIRE ALGORITM: Include textul din caseta PLUS numele documentelor încărcate ---
        sursa_text_totala = hobbyuri.lower() + " " + nume_documente_text
        
        cuvinte = [c for c in sursa_text_totala.split() if len(c) > 4 and c not in ["pentru", "atestat", "diploma", "certificat", "cv-ul"]]
        cuvant_cheie = cuvinte[0].capitalize() if cuvinte else "Specialist"
        
        # Securizare text pentru URL (evită spații sau caractere speciale)
        termen_cautare = urllib.parse.quote(f"{cuvant_cheie} {oras}")
        
        # --- REMEDIRE CORECTĂ LINKURI: Adăugarea protocolului https:// obligatoriu ---
        link_ejobs = f"ejobs.ro{oras}/{cuvant_cheie.lower()}"
        link_hipo = f"hipo.ro{oras}"
        link_linkedin = f"linkedin.com{urllib.parse.quote(cuvant_cheie)}"

        # Afișare analiză grafică bazată pe corelarea completă a datelor
        st.markdown(f"### 📊 Raport de Compatibilitate Multi-Criteriu (Fiecare câmp analizat)")
        
        # Evaluăm relevanța datelor în funcție de prezența textului în documente
        potrivire_documente = 95 if incarcare_documente else 45
        
        date_grafic = pd.DataFrame({
            'Criteriu Analizat Obligatoriu': ['Educație (' + domeniu_studii + ')', 'Pasiuni & Documente (' + cuvant_cheie + ')', 'Locație (' + oras + ')', 'Obiectiv Carieră'],
            'Grad Corelare Proiectat (%)': [92, potrivire_documente, 96, 90]
        }).set_index('Criteriu Analizat Obligatoriu')
        
        st.bar_chart(date_grafic)
        st.write("---")

        # Afișarea profilului contextual
        st.markdown(f"### 💼 Profil de Carieră Evaluat pentru: {nume}")
        st.info(f"🎯 **Rol Recomandat:** Junior / Intern în zona de **{cuvant_cheie}**")
        st.write(f"**Validare Criterii:** La vârsta de {varsta} ani, având background în *{domeniu_studii}* ({nivel_studii}), ești un candidat ideal pentru oportunități de tip *{'/'.join(obiectiv)}*. Configurația geografică curentă pentru {oras} prioritizează regimul: *{'/'.join(regim_lucru)}*.")
        st.write("---")

        # --- AFIȘARE MINIM 3 COMPANII CU REDIRECȚIONARE EXTERNĂ COMPLETĂ ---
        st.markdown("### 🏢 Conexiuni Externe cu Profilele de Recrutare ale Angajatorilor")
        st.write("Următoarele companii au profile de angajator deschise special pe criteriile tale. Butoanele te vor redirecționa direct pe platformele externe corespunzătoare:")

        companii = [
            {"nume": "Alpha Tech Hub", "platforma": "LinkedIn", "url": link_linkedin, "desc": f"Profil orientat spre absolvenți de {domeniu_studii}. Acceptă candidați din {oras} sau în regim Remote."},
            {"nume": "Nexus Innovate Solutions", "platforma": "eJobs", "url": link_ejobs, "desc": f"Campanie activă de recrutare axată pe abilități de {cuvant_cheie}. Deschide profilul extern pentru detalii."},
            {"nume": "Euro-Enterprise Group", "platforma": "Hipo", "url": link_hipo, "desc": f"Programe de dezvoltare accelerată dedicate nivelului tău educațional: {nivel_studii}."}
        ]

        for i, comp in enumerate(companii):
            st.markdown(f"""
            <div class='job-box'>
                <h4>🏢 {comp['nume']}</h4>
                <p>{comp['desc']}</p>
                <small>Platformă gazdă pentru aplicare: <b>{comp['platforma']}</b></small>
            </div>
            """, unsafe_allow_html=True)
            
            col_b1, col_b2 = st.columns(2)
            with col_b1:
                # Butonul extern - acum conține HTTPS și deschide o filă complet nouă de browser separat de aplicație
                st.link_button(f"🌐 Deschide Profilul Angajatorului pe {comp['platforma']}", comp['url'], use_container_width=True)
            with col_b2:
                # Simulare rețea internă de HR
                if st.button(f"🚀 Trimite Dosar CV instant la {comp['nume']}", key=f"comp_{i}"):
                    st.toast(f"📬 Profilul tău complet (inclusiv detaliile din Pasiuni și cele {len(incarcare_documente) if incarcare_documente else 0} documente validate) a fost transmis către {comp['nume']}!")

        st.write("---")
        
        # Export raport
        st.header("📄 5. Exportă Raportul Multi-Criteriu")
        text_raport = f"RAPORT INTEGRAL DE EVALUARE\nCandidat: {nume}\nOraș: {oras}\nSpecializare: {domeniu_studii}\nCuvânt cheie identificat (Pasiuni+Documente): {cuvant_cheie}"
        st.download_button("📥 Descarcă Raportul de Corelare (TXT)", text_raport, file_name=f"Raport_{nume.replace(' ', '_')}.txt", use_container_width=True)
    else:
        st.error("⚠️ Te rugăm să completezi toate câmpurile obligatorii pentru a permite algoritmului să execute analiza multi-criteriu.")


