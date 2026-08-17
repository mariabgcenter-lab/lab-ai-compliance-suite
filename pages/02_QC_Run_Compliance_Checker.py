import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime

st.title("🧪 Diagnostic Batch QC Validator")
st.markdown("Parse diagnostic assay batch runs, evaluate multi-parameter system suitability controls (NC, PC, IC), and issue downloadable QA certificates.")

sample_batch_data = {
    "well": ["A01", "A02", "A03", "A04", "B01", "B02", "B03", "B04", "C01", "C02", "C03", "C04"],
    "sample_id": ["NC_01", "PC_01", "PATIENT_101", "PATIENT_102", "PATIENT_103", "PATIENT_104", "PATIENT_105", "PATIENT_106", "PATIENT_107", "PATIENT_108", "PATIENT_109", "PATIENT_110"],
    "sample_type": ["NC", "PC", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN"],
    "target_ct": [np.nan, 20.4, 24.1, np.nan, 36.2, 22.8, np.nan, 28.4, np.nan, 21.5, 34.8, np.nan],
    "ic_ct": [28.1, 27.9, 28.5, 39.1, 28.2, 28.0, 27.8, 28.3, 28.1, 28.6, 28.0, 41.2]
}
df = pd.DataFrame(sample_batch_data)

st.subheader("1. Active Batch Data Stream")
st.dataframe(df, use_container_width=True)

c1, c2 = st.columns(2)
with c1:
    ic_cutoff = st.slider("Internal Control (IC) Threshold (Ct):", 30.0, 36.0, 32.0, 0.5)
with c2:
    pc_max_ct = st.slider("Positive Control Max Target Ct:", 20.0, 26.0, 24.0, 0.5)

if st.button("Evaluate System Suitability & Issue Release Decision", type="primary"):
    st.markdown("### 📝 System Suitability & Control Evaluation")

    nc_status = df[df['sample_type'] == 'NC']['target_ct'].isna().all()
    pc_val = df[df['sample_type'] == 'PC']['target_ct'].values[0]
    pc_status = (pc_val >= 18.0) and (pc_val <= pc_max_ct)
    inhabited_wells = df[df['ic_ct'] > ic_cutoff]

    col_nc, col_pc, col_ic = st.columns(3)
    with col_nc:
        if nc_status:
            st.success("✅ Negative Control: PASS")
        else:
            st.error("❌ Negative Control: FAIL")

    with col_pc:
        if pc_status:
            st.success(f"✅ Positive Control: PASS (Ct {pc_val})")
        else:
            st.error(f"❌ Positive Control: FAIL (Ct {pc_val})")

    with col_ic:
        if inhabited_wells.empty:
            st.success("✅ Internal Controls: ALL PASS")
        else:
            st.error(f"❌ Internal Controls: {len(inhabited_wells)} Flagged")

    df['status'] = 'PASS'
    df.loc[df['ic_ct'] > ic_cutoff, 'status'] = 'EXTRACTION_FAIL'
    df.loc[df['sample_type'] == 'NC', 'status'] = 'CONTROL_NC'
    df.loc[df['sample_type'] == 'PC', 'status'] = 'CONTROL_PC'

    st.markdown("### 📊 Annotated Batch Output")
    st.dataframe(df[['well', 'sample_id', 'sample_type', 'target_ct', 'ic_ct', 'status']], use_container_width=True)

    timestamp_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cert_text = f"""============================================================
 DIAGNOSTIC BATCH QUALITY ASSURANCE RELEASE REPORT     
============================================================
Timestamp:          {timestamp_str}
Batch Identifier:   BATCH-2026-DX-001
Assay Target:       Multiplex Pathogen Surveillance Panel
OVERALL QC DECISION: {"PASS - APPROVED FOR RELEASE" if (nc_status and pc_status and inhabited_wells.empty) else "CONDITIONAL RELEASE - RE-RUN FLAGGED SAMPLES"}
------------------------------------------------------------
SYSTEM SUITABILITY AUDIT TRAIL:
  - Negative Control (NC_01): {"PASS" if nc_status else "FAIL"}
  - Positive Control (PC_01): {"PASS" if pc_status else "FAIL"} (Observed Ct: {pc_val})
  - Internal Control (IC) Threshold Cutoff: Ct {ic_cutoff}
------------------------------------------------------------
FLAGGED SAMPLES REQUIRING RE-EXTRACTION / RE-TEST:
"""
    if inhabited_wells.empty:
        cert_text += "  - None. All sample internal controls met system suitability.\n"
    else:
        for _, row in inhabited_wells.iterrows():
            cert_text += f"  - Well {row['well']} ({row['sample_id']}): IC Ct = {row['ic_ct']} (Exceeds {ic_cutoff} threshold)\n"

    cert_text += "============================================================"

    st.markdown("#### 📜 QA Release Certificate")
    st.code(cert_text)

    st.download_button(
        label="💾 Download QA Release Certificate (.txt)",
        data=cert_text,
        file_name="QA_Release_Certificate_BATCH-2026-DX-001.txt",
        mime="text/plain"
    )

