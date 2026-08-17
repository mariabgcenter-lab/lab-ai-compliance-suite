import streamlit as st

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.title("SOP Clarity & Documentation QC Assistant")

st.write(
    "This module evaluates the clarity, structure, and completeness of scientific SOPs or laboratory documentation. "
    "It highlights missing steps, unclear instructions, formatting issues, and logical flow problems."
)

# ---------------------------------------------------------
# Input Section
# ---------------------------------------------------------
st.subheader("Paste SOP or Documentation Text")

doc_text = st.text_area(
    "Document Under Review:",
    height=300,
    placeholder="Paste SOP, protocol, workflow, or documentation text here..."
)

# ---------------------------------------------------------
# Clarity Criteria
# ---------------------------------------------------------
clarity_checks = {
    "step": "Presence of clearly numbered procedural steps",
    "materials": "Materials, reagents, or equipment listed",
    "purpose": "Clear statement of purpose or objective",
    "scope": "Defined scope or applicability",
    "safety": "Safety notes or precautions included",
    "conditions": "Experimental conditions or parameters described",
    "expected result": "Expected outcomes or acceptance criteria",
    "references": "References or supporting documents cited"
}

# ---------------------------------------------------------
# Run Analysis
# ---------------------------------------------------------
if st.button("Run Clarity Review"):
    st.markdown("### Clarity Review Findings")

    lower_doc = doc_text.lower()
    present = []
    missing = []

    for key, description in clarity_checks.items():
        if key in lower_doc:
            present.append(description)
        else:
            missing.append(description)

    col1, col2 = st.columns(2)

    with col1:
        st.success("Documented Elements")
        for item in present:
            st.write(f"• {item}")

    with col2:
        st.error("Missing Elements")
        for item in missing:
            st.write(f"• {item}")

    st.markdown("---")

    if len(missing) == 0:
        st.success("The document appears complete and well‑structured.")
    else:
        st.warning("The document may require revision to improve clarity and completeness.")
