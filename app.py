import streamlit as st

st.set_page_config(
    page_title="Laboratory AI & Quality Control Suite",
    page_icon="🔬",
    layout="wide"
)

# ---------------------------------------------------------
# Branding Block — Lab AI Suite Banner
# ---------------------------------------------------------
st.markdown("""
<div style="padding: 20px; border-radius: 12px; background-color:#f0f2f6; border: 1px solid #d9d9d9;">
    <h2 style="text-align:center; color:#2c3e50; margin-bottom:0;">
        🔬 Laboratory AI & Quality Control Suite
    </h2>
    <p style="text-align:center; font-size:16px; color:#4a4a4a;">
        ISO/CLIA‑aligned automation for diagnostics, QC, microscopy, and regulatory documentation.
    </p>
</div>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Home Page Intro
# ---------------------------------------------------------
st.title("Unified Laboratory AI & Quality Control Suite")
st.markdown("*ISO 17025 / CLIA Compliant Analytical & Regulatory Workflows*")

st.write("Use the sidebar to navigate to SOP audit, QC validation, biofilm analysis, QA certificate generation, and document review modules.")

# ---------------------------------------------------------
# Coming Soon Section
# ---------------------------------------------------------
st.markdown("## 🚧 Coming Soon")

st.markdown("""
- 🧬 **BiofilmAI Gene Expression Predictor**  
  ML-based modeling of biofilm formation using differential gene expression signatures — built from the research in **AI Biofilm Multimodal Predictor Project** of my portfolio.

- 🧫 **Microscopy QC Module**  
  Automated assessment of blur, illumination uniformity, and imaging artifacts for routine microscopy quality checks.

- 📊 **PCR Curve Analyzer**  
  Cq extraction, amplification curve evaluation, and melt-curve anomaly detection for molecular assay QC.

- 🧾 **SOP Auto-Formatter**  
  Transforms raw procedural text into structured SOP format with sections, numbering, and compliance-aligned metadata.

- 🗂️ **Plate Map Designer**  
  Interactive builder for 96-well and 384-well plate layouts used in assays, QC runs, and experimental planning.

- 🔍 **AI-Powered Document Summaries**  
  Automated summaries of SOPs, QC reports, validation documents, and technical files to support rapid review.

*Additional modules are under development as I continue building tools that bridge microbiology, diagnostics, and modern AI workflows.*
""")

