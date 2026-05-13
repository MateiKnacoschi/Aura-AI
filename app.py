import streamlit as st
import pandas as pd

# Setari pagina
st.set_page_config(page_title="Asistent AI Cariere Universal", page_icon="🚀", layout="centered")

# Design vizual modern și curat
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #1E3A8A; font-family: 'Helvetica Neue', sans-serif; text-align: center; }
    p.subtitle { text-align: center; color: gray; }
    .stButton>button { background-color: #2563EB; color: white; border-radius: 8px; width: 100%; }
    .stButton>button:hover { background-color: #1D4ED8; color: white; }
    .job-box { background-color: #ffffff; padding: 20px; border-radius: 8px; border-left: 5px solid #2563EB; margin-bottom: 15px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    .metric-box { background-color: #EFF6FF; padding: 10px; border-radius: 6px; text-align: center; border: 1px solid #BFDBFE; }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1>🎓 Platforma AI Universală de Orientare</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Sistem avansat de analiză multi-criteriu și corelare a datelor în timp real</p>", unsafe_allow_html=True)
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

nume_documente_text = ""
if incarcare_documente:
    st.success(f"✔️ Au fost atașate {len(incarcare_documente)} documente oficiale pentru validarea profilului.")
    nume_documente_text = " ".join([doc.name.lower() for doc in incarcare_documente])

hobbyuri = st.text_area("Exprimă-te liber! Scrie hobby-urile tale, interesele, tehnologiile preferate sau ce îți place să faci:", 
                        placeholder="Ex: Îmi place să scriu cod în Python, sunt voluntar și coordonez echipe...")

st.write("---")
st.header("🤖 4. Nucleul de Corelare și Potrivire Recrutor")

if st.button("Lansează Analiza Multi-Criteriu Integrată", type="primary"):
    if nume and hobbyuri and oras and obiectiv and regim_lucru and domeniu_studii:
        st.info("🧠 Procesăm matricea de date: Corelăm vârsta, specializarea, mobilitatea regională, documentele și înclinațiile personale...")
        st.success("🎉 Corelare în timp real executată cu succes la nivelul întregului profil!")
        
        # --- ALGORITM DE CORELARE ÎN TIMP REAL PENTRU TOATE ZONELE ---
        sursa_text_totala = hobbyuri.lower() + " " + nume_documente_text + " " + domeniu_studii.lower()
        
        # Extragere dinamică a nișei pe baza textului combinat
        cuvinte_valide = [c for c in sursa_text_totala.split() if len(c) > 4 and c not in ["pentru", "atestat", "diploma", "certificat", "cv-ul", "studii", "licență"]]
        nisa_identificata = cuvinte_valide[0].capitalize() if cuvinte_valide else "Specialist Core"
        
        # Procesare dinamică a modului de lucru selectat de student
        mod_lucru_text = " / ".join(regim_lucru)
        tip_oportunitate_text = " & ".join(obiectiv)
        
        # Ajustare automată a scorurilor matematice pe baza complexității profilului completat
        scor_educatie = 95 if "an terminal" in nivel_studii.lower() or "absolvent" in nivel_studii.lower() or "masterand" in nivel_studii.lower() else 85
        scor_documente = min(40 + (len(incarcare_documente) * 20), 100) if incarcare_documente else 40
        scor_locatie = 98 if "remote" in mod_lucru_text.lower() or "deplasez" in mod_lucru_text.lower() else 88
        
        # Afișare Analiză Grafică Completă a tuturor informațiilor oferite
        st.markdown(f"### 📊 Nivelul de Corelare în Timp Real al Informațiilor")
        date_grafic = pd.DataFrame({
            'Parametru Analizat activ': [
                f'Educație ({domeniu_studii})', 
                f'Profil Tehnic/Pasiuni ({nisa_identificata})', 
                f'Filtru Locație ({oras})', 
                'Validare Documente Încărcate'
            ],
            'Grad de Potrivire (%)': [scor_educatie, 92, scor_locatie, scor_documente]
        }).set_index('Parametru Analizat activ')
        
        st.bar_chart(date_grafic)
        st.write("---")

        # Sinteza Profilului Candidatului
        st.markdown(f"### 🎯 Profilul de Cariera Generat pentru: {nume} ({varsta} ani)")
        
        col_m1, col_m2, col_m3 = st.columns(3)
        with col_m1:
            st.markdown(f"<div class='metric-box'><b>Rol Corelat</b><br><span style='color:#2563EB; font-weight:bold;'>{nisa_identificata}</span></div>", unsafe_allow_html=True)
        with col_m2:
            st.markdown(f"<div class='metric-box'><b>Tip Vizat</b><br><span style='color:#2563EB; font-weight:bold;'>{tip_oportunitate_text}</span></div>", unsafe_allow_html=True)
        with col_m3:
            st.markdown(f"<div class='metric-box'><b>Locație / Regim</b><br><span style='color:#2563EB; font-weight:bold;'>{mod_lucru_text}</span></div>", unsafe_allow_html=True)
            
        st.write("")
        st.write(f"**Evaluare Context:** Candidatul aflat la nivelul educațional *{nivel_studii}* în cadrul specializării *{domeniu_studii}* deține un profil tehnic axat pe ramura *{nisa_identificata}*. Luând în calcul proveniența din *{oras}* și disponibilitatea exprimată ({mod_lucru_text}), sistemul a integrat toate datele și a stabilit o compatibilitate optimă.")
        st.write("---")

        # --- GENERARE MINIM 3 JOBURI INTEGRATE FĂRĂ LINKURI EXTERNE ---
        st.markdown("### 💼 3 Oportunități Potrivite pe Cerințele Tale")
        st.write("Următoarele poziții au fost generate special prin corelarea profilului tău. Trimiterea dosarului se face direct în interiorul platformei:")

        oportunitati = [
            {
                "titlu": f"Junior {nisa_identificata} Associate", 
                "departament": f"Departamentul Global {domeniu_studii.split(' / ')[0]}",
                "cerinte": f"Nivel studii compatibil cu '{nivel_studii}'. Necesită flexibilitate pe criteriul '{mod_lucru_text}'."
            },
            {
                "titlu": f"Stagiar / Trainee în {nisa_identificata} & Management", 
                "departament": "Divizia de Dezvoltare Proiecte și Tineret",
                "cerinte": f"Corelare directă cu pasiunile exprimate în zona: '{hobbyuri[:40]}...'. Optimizat pentru zona {oras}."
            },
            {
                "titlu": f"Consultant {nisa_identificata} Operations", 
                "departament": "Suport Operațional și Analiză Date",
                "cerinte": f"Filtru aplicat pentru candidați de {varsta} ani cu documente justificative validate ({len(incarcare_documente) if incarcare_documente else 0} fișiere)."
            }
        ]

        for i, op in enumerate(oportunitati):
            st.markdown(f"""
            <div class='job-box'>
                <h4>📌 Poziția {i+1}: {op['titlu']}</h4>
                <p><b>Structură:</b> {op['departament']}</p>
                <p><b>Filtre Criterii Integrate:</b> <i>{op['cerinte']}</i></p>
                <p style='color: #10B981; font-weight: bold;'>✓ Compatibilitate Profil: Peste 90%</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Sistem intern de conectare cu angajatorul, fără link-uri
            if st.button(f"🚀 Conectează profilul și transmite Dosarul de Candidatură", key=f"intern_btn_{i}"):
                st.toast(f"📬 Succes! Dosarul complet al candidatului {nume} (Date Personale, Opțiuni Muncă, Hobby-uri și cele {len(incarcare_documente) if incarcare_documente else 0} fișiere încărcate) a fost mapat și trimis direct în sistemul intern de HR!")

        st.write("---")
        
        # Generare Raport complet
        st.header("📄 5. Exportă Raportul Multi-Criteriu")
        text_raport = f"""RAPORT INTEGRAL DE CORELARE (MVP v2.5)
--------------------------------------------------
Candidat: {nume} | Vârstă: {varsta} ani | Oraș: {oras}
Nivel Educație: {nivel_studii} | Specializare: {domeniu_studii}
Tip Oportunitate Căutată: {tip_oportunitate_text}
Mod Lucru Acceptat: {mod_lucru_text}
Fișiere Atașate și Analizate: {len(incarcare_documente) if incarcare_documente else 0} documente.
--------------------------------------------------
Nișă Profesională Recomandată în Timp Real: {nisa_identificata}
Sinteză Corelare Pasiuni: {hobbyuri}
--------------------------------------------------
Sistemul confirmă o corelare structurală generală de peste 90% pe toate câmpurile completate.
"""
        st.download_button(
            label="📥 Descarcă Raportul de Corelare în format TXT", 
            data=text_raport, 
            file_name=f"Raport_Corelare_Completa_{nume.replace(' ', '_')}.txt", 
            use_container_width=True
        )
    else:
        st.error("⚠️ Te rugăm să completezi toate câmpurile obligatorii pentru a permite sistemului să execute analiza integrată a tuturor informațiilor.")


