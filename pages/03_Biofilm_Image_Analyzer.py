import streamlit as st

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.title("Biofilm Image Analyzer (Coming Soon)")

st.write(
    "This module will support the microscopy component of the BiofilmAI multimodal system. "
    "It will allow users to upload fluorescence or brightfield biofilm images and preview segmentation, "
    "biomass estimation, live/dead ratios, and feature extraction for downstream machine learning."
)

# ---------------------------------------------------------
# Module Preview
# ---------------------------------------------------------
st.subheader("Module Preview")

st.write(
    "The Biofilm Image Analyzer will include the following capabilities once implemented:"
)

st.markdown("""
- Upload fluorescence or brightfield microscopy images  
- Automatic preprocessing (denoising, normalization, channel separation)  
- Watershed or deep-learning segmentation preview  
- Biomass and cell-count estimation  
- Live/dead ratio estimation for dual-channel images  
- Exportable feature tables for multimodal fusion with gene expression data  
""")

st.info(
    "This module is currently under development as part of the BiofilmAI multimodal prediction system."
)

# ---------------------------------------------------------
# Coming Soon Notice
# ---------------------------------------------------------
st.markdown("---")
st.write(
    "Additional functionality will be added once the image preprocessing and segmentation pipelines "
    "from the BiofilmAI project are integrated."
)
