import streamlit as st

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.title("BiofilmAI Lab Suite — SOP & Protocol Clarity Assistant")

st.write(
    "This module supports the BiofilmAI multimodal prediction system by helping clarify and interpret "
    "scientific SOPs, protocols, and workflows used in biofilm, AMR, and molecular biology research."
)

st.markdown("---")

# ---------------------------------------------------------
# SOP Input
# ---------------------------------------------------------
st.subheader("📄 Paste SOP or Protocol Text")

sop_text = st.text_area(
    "Paste your SOP or protocol here:",
    height=300,
    placeholder="Paste scientific workflow text here..."
)

# ---------------------------------------------------------
# Clarity Checks
# ---------------------------------------------------------
clarity_items = [
    "purpose",
    "materials",
    "equipment",
    "procedure",
    "conditions",
    "notes",
    "safety",
    "expected results"
]

if st.button("Run Clarity Check", type="primary"):
    st.markdown("### 🔍 Clarity Review Results")

    missing = []
    present = []

    lower_sop = sop_text.lower()

    for item in clarity_items:
        if item in lower_sop:
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
        st.success("🎉 This SOP/protocol contains all major clarity components.")
    else:
        st.warning("⚠️ Some clarity components are missing. Consider revising the document.")
