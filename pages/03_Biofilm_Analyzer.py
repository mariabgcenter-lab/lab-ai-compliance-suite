import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
from scipy import ndimage as ndi
from skimage import filters, morphology, segmentation

st.title("🧫 Biofilm Live/Dead Fluorescence Analyzer")

st.markdown("Segment dual-channel fluorescence micro-images using H-maxima marker-controlled watershed segmentation to quantify cell counts, biomass, and viability ratios.")

col_param, col_input = st.columns([1, 2])

with col_param:
    st.subheader("Segmentation Tuning")
    h_suppression = st.slider("H-Maxima Peak Suppression (h):", 0.5, 5.0, 1.5, 0.1)
    min_size = st.slider("Min Cell Pixel Area:", 5, 50, 15, 5)
    bg_sigma = st.slider("Gaussian Blur Sigma:", 0.5, 3.0, 1.0, 0.5)

with col_input:
    st.subheader("Image Input & Analysis Trigger")
    run_analysis = st.button("🔬 Generate & Analyze Dual-Channel Biofilm Image", type="primary")

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

