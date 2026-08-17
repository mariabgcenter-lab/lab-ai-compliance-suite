import streamlit as st

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.title("BiofilmAI Lab Suite — Gene Expression Checker")

st.write(
    "This module supports the BiofilmAI multimodal prediction system by allowing you to upload "
    "gene expression tables and explore transcriptomic features used in Project A. "
    "It provides basic previews of differential expression patterns, summary statistics, and "
    "feature distributions relevant to biofilm formation research."
)

st.markdown("---")

# ---------------------------------------------------------
# Module Preview
# ---------------------------------------------------------
st.subheader("📘 Module Preview")

st.write(
    "The Gene Expression Checker will include the following capabilities once implemented:"
)

st.markdown("""
- Upload CSV or TSV gene expression tables  
- Automatic detection of required columns (gene, log
