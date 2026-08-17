import streamlit as st

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.title("BiofilmAI Lab Suite — Laboratory Document Review Assistant")

st.write(
    "This module provides general scientific clarity review for SOPs, protocols, methods, and "
    "research workflows used in biofilm, AMR, and molecular biology research. It identifies missing "
    "sections and helps improve document organization."
)

st.markdown("---")

# ---------------------------------------------------------
# Document Input
# ---------------------------------------------------------
st.subheader("📄 Paste Document Text")

doc_text = st.text_area(
    "Paste SOP, protocol, or scientific workflow:",
    height=300,
    placeholder="Paste your document text here..."
)

# ---------------------------------------------------------
# Clarity Components
# ---------------------------------------------------------
clarity_items = [
    "purpose",
    "materials",
    "equipment",
    "procedure",
    "conditions",
    "safety",
    "notes",
    "expected results"
]

if st.button("Run Clarity Review", type="primary"):
    st.markdown("### 🔍 Clarity Review Findings")

    missing = []
    present = []

    lower_doc = doc_text.lower()

    for item in clarity_items:
        if item in lower_doc:
            present.append(item)
        else:
            missing.append(item)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ Sections Detected")
        for p in present:
            st.write(f"• {p.capitalize()}")

    with col2:
        st.error("❌ Sections Not Found")
        for m in missing:
            st.write(f"• {m.capitalize()}")

    st.markdown("---")

    if len(missing) == 0:
        st.success("🎉 This document contains all major clarity components.")
    else:
        st.warning("⚠️ Some clarity components are missing. Consider revising the document.")
