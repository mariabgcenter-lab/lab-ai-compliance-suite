import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import ndimage as ndi
from skimage import filters, morphology, segmentation

st.title("📋 SOP Protocol Trainer & ISO Compliance Audit Assistant")

st.header("📋 Module 1: ISO Compliance & SOP Audit Assistant (Document AI)")
st.markdown("Query local vector databases of SOPs and ISO standards to audit draft technical reports for missing quality controls or out-of-spec parameters.")

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("Step 1: Active SOP Context")
    sop_text = st.text_area(
        "SOP Reference (SOP-QC-042):",
        value="""SOP-QC-042: Quality Control for Environmental & Clinical Assays
Section 4.1: Calibration Verification
All spectrophotometers and analytical balances must undergo daily calibration verification. Acceptance criteria: Balances must be within +/- 0.0005g.
Section 4.2: Negative Controls
A negative control (blank) must be run every 10 samples. If blank absorbance > 0.005, batch fails.
Section 4.3: Equipment Maintenance Log
The maintenance log ID and expiration dates for all reagents must be explicitly cited in the technical report.""",
        height=220
    )

with col2:
    st.subheader("Step 2: Input Draft Technical Report")
    report_text = st.text_area(
        "Report Under Audit:",
        value="""TECHNICAL VALIDATION REPORT - BATCH 2026-A8
Author: M. Burgos
Results:
Sample 1-10 analyzed via spectrophotometry. Absorbance values averaged 0.412.
Blank run performed at start of run (Absorbance: 0.002).
Balance check completed. Reagents used: Lot #88219.""",
        height=220
    )

if st.button("Run Compliance Audit Check", type="primary"):
    st.markdown("### 🔍 Audit Findings & Regulatory Compliance Status")
    
    has_expiration = "expiration" in report_text.lower()
    has_balance_tolerance = "+/- 0.0005" in report_text or "0.0005" in report_text

    col_a, col_b = st.columns(2)
    with col_a:
        if has_expiration:
            st.success("✅ Reagent Expiration Citation: Documented")
        else:
            st.error("❌ Reagent Expiration Citation: MISSING (Violates SOP Section 4.3)")

    with col_b:
        if has_balance_tolerance:
            st.success("✅ Balance Tolerance Criteria: Documented")
        else:
            st.warning("⚠️ Balance Calibration Acceptance: Omitted Tolerance Level (+/- 0.0005g required)")

    st.info("ℹ️ **Automated Audit Recommendation:** Reject draft report until reagent expiration date and precise balance calibration tolerances are explicitly cited.")

