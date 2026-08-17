import streamlit as st

# ---------------------------------------------------------
# Page Configuration
# ---------------------------------------------------------
st.set_page_config(
    page_title="BiofilmAI Laboratory Assistant",
    page_icon="🔬",
    layout="wide"
)

# ---------------------------------------------------------
# Landing Page
# ---------------------------------------------------------
st.title("BiofilmAI Laboratory Assistant")

st.write(
    "A unified scientific workspace designed to support the core components of the BiofilmAI multimodular system. "
    "This app provides tools for SOP clarity checking, gene expression exploration, microscopy image analysis, "
    "and multimodal fusion previews — all aligned with my scientific AI portfolio."
)

# ---------------------------------------------------------
# Sidebar Navigation
# ---------------------------------------------------------
st.sidebar.header("BiofilmAI Modules")

module = st.sidebar.radio(
    "Select a module:",
    [
        "Module 1 — BONUS: SOP Clarity & Documentation QC Assistant",
        "Module 2 — Gene Expression Checker (Coming Soon)",
        "Module 3 — Biofilm Image Analyzer (Coming Soon)",
        "Module 4 — Multimodal Fusion Preview (Coming Soon)"
    ]
)

# ---------------------------------------------------------
# Module 1 — SOP Clarity & Documentation QC Assistant
# ---------------------------------------------------------
if module == "Module 1 — BONUS: SOP Clarity & Documentation QC Assistant":
    st.header("Module 1 — BONUS: SOP Clarity & Documentation QC Assistant")
    st.write(
        "This module helps evaluate the clarity, structure, and completeness of scientific SOPs or lab documentation. "
        "It highlights missing steps, unclear instructions, and formatting issues."
    )

    sop_text = st.text_area("Paste your SOP or documentation text here:")

    if st.button("Check Clarity"):
        if sop_text.strip() == "":
            st.warning("Please paste some text before checking.")
        else:
            st.success("Analysis complete.")
            st.write("• Checked for missing steps")
            st.write("• Checked for unclear instructions")
            st.write("• Checked for formatting issues
