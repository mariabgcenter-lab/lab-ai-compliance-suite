import streamlit as st

st.title("📋 ISO Compliance & Document Audit Assistant")
st.markdown("Automatically reviews SOPs, technical reports, and validation documents for missing ISO/CLIA‑required elements.")

st.subheader("Paste Document Text for Compliance Review")

doc_text = st.text_area(
    "Document Under Audit:",
    height=300,
    placeholder="Paste SOP, technical report, validation summary, or QC documentation here..."
)

required_items = {
    "calibration": "Calibration verification or tolerance documentation",
    "tolerance": "Instrument tolerance or acceptance limits",
    "expiration": "Reagent expiration dates",
    "lot": "Reagent or consumable lot numbers",
    "negative control": "Negative control documentation",
    "positive control": "Positive control documentation",
    "internal control": "Internal control (IC) documentation",
    "maintenance": "Maintenance logs or instrument service records",
    "acceptance criteria": "Defined acceptance criteria for run validity",
    "instrument": "Instrument ID or serial number"
}

if st.button("Run ISO/CLIA Compliance Audit", type="primary"):
    st.markdown("### 🔍 Compliance Audit Findings")

    lower_doc = doc_text.lower()
    present = []
    missing = []

    for key, description in required_items.items():
        if key in lower_doc:
            present.append(description)
        else:
            missing.append(description)

    col1, col2 = st.columns(2)

    with col1:
        st.success("✔ Documented Elements")
        for item in present:
            st.write(f"• {item}")

    with col2:
        st.error("❌ Missing Required Elements")
        for item in missing:
            st.write(f"• {item}")

    st.markdown("---")

    if len(missing) == 0:
        st.success("🎉 Document meets ISO/CLIA documentation requirements.")
    else:
        st.warning("⚠️ Document requires revision before approval.")
