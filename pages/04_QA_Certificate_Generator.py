import streamlit as st
from datetime import datetime
import pandas as pd

st.title("📜 QA Certificate Generator")
st.markdown("Generate ISO/CLIA‑aligned QA release certificates for diagnostic or research assay batches.")

st.subheader("Batch Metadata")
col1, col2 = st.columns(2)

with col1:
    batch_id = st.text_input("Batch Identifier:", "BATCH-2026-DX-001")
    assay_name = st.text_input("Assay Target / Panel:", "Multiplex Pathogen Surveillance Panel")

with col2:
    analyst = st.text_input("Analyst Name:", "M. Burgos")
    instrument = st.text_input("Instrument / Platform:", "QuantStudio 7 Pro")

st.subheader("Control Summary")
col_nc, col_pc, col_ic = st.columns(3)

with col_nc:
    nc_status = st.selectbox("Negative Control Status:", ["PASS", "FAIL"])

with col_pc:
    pc_ct = st.number_input("Positive Control Ct:", 18.0, 40.0, 22.4, 0.1)
    pc_status = st.selectbox("Positive Control Status:", ["PASS", "FAIL"])

with col_ic:
    ic_cutoff = st.number_input("IC Ct Cutoff:", 25.0, 45.0, 32.0, 0.5)
    ic_status = st.selectbox("Internal Control Status:", ["ALL PASS", "FLAGGED SAMPLES"])

st.subheader("Flagged Samples (Optional)")
flagged = st.text_area(
    "List flagged wells or sample IDs:",
    value="",
    height=120
)

if st.button("Generate QA Certificate", type="primary"):
    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    cert = f"""
============================================================
        QUALITY ASSURANCE RELEASE CERTIFICATE
============================================================
Timestamp:          {timestamp_str}
Batch Identifier:   {batch_id}
Assay Target:       {assay_name}
Analyst:            {analyst}
Instrument:         {instrument}

------------------ SYSTEM SUITABILITY ----------------------
Negative Control:   {nc_status}
Positive Control:   {pc_status} (Ct = {pc_ct})
IC Cutoff:          Ct {ic_cutoff}
IC Status:          {ic_status}

------------------ FLAGGED SAMPLES -------------------------
"""

    if flagged.strip() == "":
        cert += "None. All samples met system suitability.\n"
    else:
        cert += flagged + "\n"

    cert += "============================================================"

    st.markdown("### 📄 Generated Certificate")
    st.code(cert)

    st.download_button(
        "💾 Download Certificate (.txt)",
        cert,
        file_name=f"QA_Certificate_{batch_id}.txt",
        mime="text/plain"
    )

