import streamlit as st

st.title("📑 Laboratory Document Review Assistant")

st.write(
    "Reviews scientific documents (methods, workflows, technical notes, publications) "
    "for clarity and completeness. Identifies missing conceptual sections and evaluates "
    "overall scientific organization."
)

st.markdown("---")

st.subheader("📄 Paste Document Text")

doc_text = st.text_area(
    "Paste scientific document text:",
    height=300,
    placeholder="Paste methods, workflow, or scientific text..."
)

# Conceptual scientific sections
conceptual_sections = [
    "background",
    "introduction",
    "objective",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "limitations",
    "notes"
]

if st.button("Run Document Review", type="primary"):
    st.markdown("### 🔍 Document Completeness Review")

    lower_doc = doc_text.lower()
    present = []
    missing = []

    for section in conceptual_sections:
        if section in lower_doc:
            present.append(section)
        else:
            missing.append(section)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ Sections Found")
        for p in present:
            st.write(f"• {p.capitalize()}")

    with col2:
        st.error("❌ Sections Missing")
        for m in missing:
            st.write(f"• {m.capitalize()}")

    st.markdown("---")

    if len(missing) == 0:
        st.success("🎉 Document contains all major scientific sections.")
    else:
        st.warning("⚠️ Document is missing important scientific components.")
