import streamlit as st

st.title("📑 Laboratory Document Review Assistant")
st.markdown("Automated ISO/CLIA‑aligned document review for SOPs, technical reports, QC summaries, and validation documents.")

st.subheader("Upload or Paste Document Text")

doc_text = st.text_area(
    "Paste SOP, Technical Report, or QC Summary:",
    height=300,
    placeholder="Paste your document text here..."
)

required_items = [
    "expiration date",
    "lot number",
    "calibration",
    "negative control",
    "positive control",
    "internal control",
    "maintenance log",
    "acceptance criteria",
    "tolerance",
    "instrument ID"
]

if st.button("Run Document Review", type="primary"):
    st.markdown("### 🔍 Document Review Findings")

    missing = []
    present = []

    lower_doc = doc_text.lower()

    for item in required_items:
        if item in lower_doc:
            present.append(item)
        else:
            missing.append(item)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ Documented Items")
        for p in present:
            st.write(f"• {p}")

    with col2:
        st.error("❌ Missing Required Items")
        for m in missing:
            st.write(f"• {m}")

    st.markdown("---")
    if len(missing) == 0:
        st.success("🎉 Document meets ISO/CLIA documentation requirements.")
    else:
        st.warning("⚠️ Document requires revision before approval.")

