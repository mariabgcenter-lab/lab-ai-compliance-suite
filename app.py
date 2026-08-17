import streamlit as st

st.set_page_config(
    page_title="BiofilmAI Lab Suite",
    page_icon="🧫",
    layout="wide"
)

# ---------------------------------------------------------
# Home Page — BiofilmAI Lab Suite
# ---------------------------------------------------------

st.title("BiofilmAI Lab Suite")
st.write(
    "Welcome to the BiofilmAI Lab Suite — a unified scientific environment designed to support "
    "multimodal prediction of biofilm formation using gene expression data, microscopy features, "
    "and structured scientific documentation."
)

st.markdown("---")

# ---------------------------------------------------------
# About BiofilmAI
# ---------------------------------------------------------
st.subheader("📘 About BiofilmAI")
st.write(
    "BiofilmAI is a scientific machine learning project focused on predicting biofilm formation "
    "by integrating transcriptomic features (Project A), microscopy-derived features (Project B), "
    "and multimodal fusion strategies (Project C)."
)

st.markdown("---")

# ---------------------------------------------------------
# Available Modules
# ---------------------------------------------------------
st.subheader("🧪 Available Modules")

st.markdown("""
### **BiofilmAI Core Modules**
- **Gene Expression Checker** — Analyze transcriptomic features used in Project A  
- **Biofilm Image Analyzer** — Process microscopy images used in Project B  
- **Multimodal Fusion Hub** — Preview how gene and image features combine in Project C  

### **BiofilmAI Support Modules**
- **SOP & Protocol Clarity Assistant** — Clarify scientific workflows relevant to biofilm and AMR research  
- **Universal Scientific Summarizer** — Summarize scientific articles, SOPs, protocols, and methods  
""")

st.markdown("---")

# ---------------------------------------------------------
# Navigation Note
# ---------------------------------------------------------
st.write(
    "Use the navigation menu on the left to explore each module."
)
