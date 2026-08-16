import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import ndimage as ndi
from skimage import io, filters, morphology, measure, segmentation
from skimage import filters, morphology, segmentation

# Page Configuration
st.set_page_config(
@@ -28,7 +28,7 @@
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Local Privacy Enforcement:** All algorithms run in local execution space to prevent cloud data leakage.")
st.sidebar.info("💡 **Local Privacy Enforcement:** All processing executes locally within session memory to prevent cloud data leakage.")

# ==========================================
# MODULE 1: ISO COMPLIANCE & SOP AUDIT
@@ -40,42 +40,42 @@
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Step 1: Load SOPs & Guidelines")
        st.subheader("Step 1: Active SOP Context")
        sop_text = st.text_area(
            "Active SOP Context (SOP-QC-042):",
            "SOP Reference (SOP-QC-042):",
            value="""SOP-QC-042: Quality Control for Environmental & Clinical Assays
Section 4.1: Calibration Verification
All spectrophotometers and analytical balances must undergo daily calibration verification. Acceptance criteria: Balances must be within +/- 0.0005g.
Section 4.2: Negative Controls
A negative control (blank) must be run every 10 samples. If blank absorbance > 0.005, batch fails.
Section 4.3: Equipment Maintenance Log
The maintenance log ID and expiration dates for all reagents must be explicitly cited in the technical report.""",
            height=200
            height=220
        )

    with col2:
        st.subheader("Step 2: Input Draft Technical Report")
        report_text = st.text_area(
            "Draft Technical Report:",
            "Report Under Audit:",
            value="""TECHNICAL VALIDATION REPORT - BATCH 2026-A8
Author: M. Burgos
Results:
Sample 1-10 analyzed via spectrophotometry. Absorbance values averaged 0.412.
Blank run performed at start of run (Absorbance: 0.002).
Balance check completed. Reagents used: Lot #88219.""",
            height=200
            height=220
        )

    if st.button("Run Compliance Audit Check", type="primary"):
        st.markdown("### 🔍 Audit Findings & Missing Parameters")
        st.markdown("### 🔍 Audit Findings & Regulatory Compliance Status")

        has_expiration = "expiration" in report_text.lower()
        has_balance_tolerance = "+/- 0.0005" in report_text or "0.0005" in report_text

        col_a, col_b = st.columns(2)
        with col_a:
            if has_expiration:
                st.success("✅ Reagent Expiration Citation: Present")
                st.success("✅ Reagent Expiration Citation: Documented")
            else:
                st.error("❌ Reagent Expiration Citation: MISSING (Violates SOP Section 4.3)")

@@ -92,111 +92,199 @@
# ==========================================
elif module == "2. Biofilm Live/Dead Fluorescence Analyzer":
    st.header("🧫 Module 2: Biofilm Live/Dead Fluorescence Analyzer (Computer Vision)")
    st.markdown("Segment dual-channel fluorescence images using H-maxima marker-controlled watershed segmentation to quantify biomass and viability ratios.")
    st.markdown("Segment dual-channel fluorescence micro-images using H-maxima marker-controlled watershed segmentation to quantify cell counts, biomass, and viability ratios.")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Segmentation Parameters")
    col_param, col_input = st.columns([1, 2])
    
    with col_param:
        st.subheader("Segmentation Tuning")
        h_suppression = st.slider("H-Maxima Peak Suppression (h):", 0.5, 5.0, 1.5, 0.1)
        min_size = st.slider("Minimum Cell Pixel Area:", 5, 50, 15, 5)
        min_size = st.slider("Min Cell Pixel Area:", 5, 50, 15, 5)
        bg_sigma = st.slider("Gaussian Blur Sigma:", 0.5, 3.0, 1.0, 0.5)
        
    with col_input:
        st.subheader("Image Input & Analysis Trigger")
        run_analysis = st.button("🔬 Generate & Analyze Dual-Channel Biofilm Image", type="primary")

    with col2:
        st.subheader("Sample Controls")
        if st.button("Generate & Process Synthetic Live/Dead Pair"):
            y, x = np.ogrid[:256, :256]
            mask_live1 = (x - 80)**2 + (y - 80)**2 <= 25**2
            mask_live2 = (x - 100)**2 + (y - 80)**2 <= 20**2
            mock_live = np.zeros((256, 256), dtype=np.uint8)
            mock_live[mask_live1 | mask_live2] = 200

            mask_dead = (x - 180)**2 + (y - 180)**2 <= 15**2
            mock_dead = np.zeros((256, 256), dtype=np.uint8)
            mock_dead[mask_dead] = 180

            live_blurred = filters.gaussian(mock_live, sigma=1.0)
            live_thresh = filters.threshold_otsu(live_blurred)
            live_binary = live_blurred > live_thresh
            live_cleaned = morphology.remove_small_objects(live_binary, min_size=min_size)
            live_dist = ndi.distance_transform_edt(live_cleaned)
            live_h_peaks = morphology.h_maxima(live_dist, h=h_suppression)
            live_markers, _ = ndi.label(live_h_peaks)
            live_labels = segmentation.watershed(-live_dist, live_markers, mask=live_cleaned)

            dead_blurred = filters.gaussian(mock_dead, sigma=1.0)
            dead_thresh = filters.threshold_otsu(dead_blurred)
            dead_binary = dead_blurred > dead_thresh
            dead_cleaned = morphology.remove_small_objects(dead_binary, min_size=min_size)
            dead_dist = ndi.distance_transform_edt(dead_cleaned)
            dead_h_peaks = morphology.h_maxima(dead_dist, h=h_suppression)
            dead_markers, _ = ndi.label(dead_h_peaks)
            dead_labels = segmentation.watershed(-dead_dist, dead_markers, mask=dead_cleaned)

            live_area = int(np.sum(live_cleaned))
            dead_area = int(np.sum(dead_cleaned))
            total_area = live_area + dead_area
            live_pct = round((live_area / total_area * 100), 2) if total_area > 0 else 0
            dead_pct = round((dead_area / total_area * 100), 2) if total_area > 0 else 0

            st.markdown("### 📊 Quantification Results")
            res_df = pd.DataFrame([{
                "Live Biomass (px)": live_area,
                "Dead Biomass (px)": dead_area,
                "Total Biomass (px)": total_area,
                "Viability (% Live)": f"{live_pct}%",
                "Mortality (% Dead)": f"{dead_pct}%",
                "Live Cell Count": len(np.unique(live_labels)) - 1,
                "Dead Cell Count": len(np.unique(dead_labels)) - 1
            }])
            st.dataframe(res_df, use_container_width=True)
    if run_analysis:
        np.random.seed(42)
        y, x = np.ogrid[:256, :256]
        
        # Live Channel (SYTO 9 Green)
        live_mask = ((x - 80)**2 + (y - 80)**2 <= 22**2) | \
                    ((x - 105)**2 + (y - 85)**2 <= 18**2) | \
                    ((x - 60)**2 + (y - 140)**2 <= 25**2) | \
                    ((x - 180)**2 + (y - 70)**2 <= 20**2)
        mock_live = np.zeros((256, 256), dtype=np.float64)
        mock_live[live_mask] = 180
        mock_live += np.random.normal(0, 15, (256, 256))
        mock_live = np.clip(mock_live, 0, 255).astype(np.uint8)

        # Dead Channel (Propidium Iodide Red)
        dead_mask = ((x - 180)**2 + (y - 180)**2 <= 16**2) | \
                    ((x - 130)**2 + (y - 190)**2 <= 14**2)
        mock_dead = np.zeros((256, 256), dtype=np.float64)
        mock_dead[dead_mask] = 160
        mock_dead += np.random.normal(0, 12, (256, 256))
        mock_dead = np.clip(mock_dead, 0, 255).astype(np.uint8)

        # Watershed Segmentation - Live
        live_blurred = filters.gaussian(mock_live, sigma=bg_sigma)
        live_thresh = filters.threshold_otsu(live_blurred)
        live_binary = live_blurred > live_thresh
        live_cleaned = morphology.remove_small_objects(live_binary, min_size=min_size)
        live_dist = ndi.distance_transform_edt(live_cleaned)
        live_h_peaks = morphology.h_maxima(live_dist, h=h_suppression)
        live_markers, _ = ndi.label(live_h_peaks)
        live_labels = segmentation.watershed(-live_dist, live_markers, mask=live_cleaned)
        live_count = len(np.unique(live_labels)) - 1

        # Watershed Segmentation - Dead
        dead_blurred = filters.gaussian(mock_dead, sigma=bg_sigma)
        dead_thresh = filters.threshold_otsu(dead_blurred)
        dead_binary = dead_blurred > dead_thresh
        dead_cleaned = morphology.remove_small_objects(dead_binary, min_size=min_size)
        dead_dist = ndi.distance_transform_edt(dead_cleaned)
        dead_h_peaks = morphology.h_maxima(dead_dist, h=h_suppression)
        dead_markers, _ = ndi.label(dead_h_peaks)
        dead_labels = segmentation.watershed(-dead_dist, dead_markers, mask=dead_cleaned)
        dead_count = len(np.unique(dead_labels)) - 1

        live_area = int(np.sum(live_cleaned))
        dead_area = int(np.sum(dead_cleaned))
        total_area = live_area + dead_area
        viability_pct = round((live_area / total_area * 100), 2) if total_area > 0 else 0
        mortality_pct = round((dead_area / total_area * 100), 2) if total_area > 0 else 0

        st.markdown("### 🖼️ Channel Visualization & Segmentation Mask")
        fig, axes = plt.subplots(1, 3, figsize=(12, 4))
        
        rgb_overlay = np.zeros((256, 256, 3), dtype=np.uint8)
        rgb_overlay[..., 0] = dead_cleaned * 255
        rgb_overlay[..., 1] = live_cleaned * 255
        
        axes[0].imshow(mock_live, cmap="Greens")
        axes[0].set_title("SYTO 9 (Live Channel)")
        axes[0].axis("off")

        axes[1].imshow(mock_dead, cmap="Reds")
        axes[1].set_title("Propidium Iodide (Dead Channel)")
        axes[1].axis("off")

        axes[2].imshow(rgb_overlay)
        axes[2].set_title("Segmentation Mask Overlay")
        axes[2].axis("off")

        st.pyplot(fig)

        st.markdown("### 📈 Viability & Population Metrics")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Live Cell Count", f"{live_count} cells")
        m2.metric("Dead Cell Count", f"{dead_count} cells")
        m3.metric("Viability Ratio", f"{viability_pct}%")
        m4.metric("Mortality Ratio", f"{mortality_pct}%")

        res_df = pd.DataFrame([{
            "Live Biomass (px)": live_area,
            "Dead Biomass (px)": dead_area,
            "Total Biomass (px)": total_area,
            "Live Cell Count": live_count,
            "Dead Cell Count": dead_count,
            "Viability (% Live)": f"{viability_pct}%",
            "Mortality (% Dead)": f"{mortality_pct}%"
        }])
        st.dataframe(res_df, use_container_width=True)

# ==========================================
# MODULE 3: DIAGNOSTIC BATCH QC VALIDATOR
# ==========================================
elif module == "3. Diagnostic Batch QC Validator":
    st.header("🧪 Module 3: Diagnostic Batch QC Validator (Data Pipelines)")
    st.markdown("Parse batch run data, enforce system suitability controls (NC, PC, IC), and issue QA release decisions.")
    st.markdown("Parse diagnostic assay batch runs, evaluate multi-parameter system suitability controls (NC, PC, IC), and issue downloadable QA certificates.")

    st.subheader("Active Batch Run Preview")
    sample_batch_data = {
        "batch_id": ["BATCH-2026-DX-001"] * 6,
        "well": ["A01", "A02", "B01", "B02", "B03", "B04"],
        "sample_id": ["NC_01", "PC_01", "PATIENT_101", "PATIENT_102", "PATIENT_103", "PATIENT_104"],
        "sample_type": ["NC", "PC", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN"],
        "ct_value": [np.nan, 20.4, 24.1, np.nan, 36.2, 22.8],
        "ic_ct_value": [28.1, 27.9, 28.5, 39.1, 28.2, 28.0]
        "well": ["A01", "A02", "A03", "A04", "B01", "B02", "B03", "B04", "C01", "C02", "C03", "C04"],
        "sample_id": ["NC_01", "PC_01", "PATIENT_101", "PATIENT_102", "PATIENT_103", "PATIENT_104", "PATIENT_105", "PATIENT_106", "PATIENT_107", "PATIENT_108", "PATIENT_109", "PATIENT_110"],
        "sample_type": ["NC", "PC", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN", "UNKNOWN"],
        "target_ct": [np.nan, 20.4, 24.1, np.nan, 36.2, 22.8, np.nan, 28.4, np.nan, 21.5, 34.8, np.nan],
        "ic_ct": [28.1, 27.9, 28.5, 39.1, 28.2, 28.0, 27.8, 28.3, 28.1, 28.6, 28.0, 41.2]
    }
    df = pd.DataFrame(sample_batch_data)

    st.subheader("1. Active Batch Data Stream")
    st.dataframe(df, use_container_width=True)

    if st.button("Evaluate System Suitability & Run QA Check", type="primary"):
        st.markdown("### 📝 Batch Quality Control Evaluation")
        
        failed_ic = df[df['ic_ct_value'] > 32.0]
        
        st.success("✅ Negative Control (NC_01): Clean (No Signal)")
        st.success("✅ Positive Control (PC_01): In Spec (Ct 20.4 within [18.0 - 24.0])")
        
        if not failed_ic.empty:
            for _, row in failed_ic.iterrows():
                st.error(f"❌ Well {row['well']} ({row['sample_id']}): Extraction Inhibition Flagged (IC Ct = {row['ic_ct_value']} > 32.0 threshold)")
    c1, c2 = st.columns(2)
    with c1:
        ic_cutoff = st.slider("Internal Control (IC) Threshold (Ct):", 30.0, 36.0, 32.0, 0.5)
    with c2:
        pc_max_ct = st.slider("Positive Control Max Target Ct:", 20.0, 26.0, 24.0, 0.5)

        st.markdown("---")
        st.markdown("#### 📜 QA Release Certificate")
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
Timestamp:          {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
Timestamp:          {timestamp_str}
Batch Identifier:   BATCH-2026-DX-001
OVERALL QC STATUS:  [PARTIAL RELEASE - 1 REPEAT REQUIRED]
Assay Target:       Multiplex Pathogen Surveillance Panel
OVERALL QC DECISION: {"PASS - APPROVED FOR RELEASE" if (nc_status and pc_status and inhabited_wells.empty) else "CONDITIONAL RELEASE - RE-RUN FLAGGED SAMPLES"}
------------------------------------------------------------
SYSTEM SUITABILITY AUDIT LOG:
  - All batch system controls (NC, PC) met specifications.
  - Well B02 (PATIENT_102) flagged for IC failure.
SYSTEM SUITABILITY AUDIT TRAIL:
  - Negative Control (NC_01): {"PASS" if nc_status else "FAIL"}
  - Positive Control (PC_01): {"PASS" if pc_status else "FAIL"} (Observed Ct: {pc_val})
  - Internal Control (IC) Threshold Cutoff: Ct {ic_cutoff}
------------------------------------------------------------
SAMPLE RESULTS SUMMARY:
  - POSITIVE: 2
  - NEGATIVE: 1
  - INCONCLUSIVE/RE-RUN: 1 (PATIENT_103)
  - INVALID (EXTRACTION FAIL): 1 (PATIENT_102)
============================================================"""
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
