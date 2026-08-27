BiofilmAI Lab Suite
Live Interactive App:
https://lab-ai-compliance-suite-icr9e9zehffzgw8qj4fdb2.streamlit.app/

The BiofilmAI Lab Suite is a unified Streamlit application designed to support multimodal prediction of biofilm formation using gene expression data, microscopy features, and structured scientific documentation.
This suite provides an integrated scientific environment for exploring transcriptomic patterns, analyzing biofilm images, previewing multimodal fusion, and working with research‑related documents.

🗂️ Repository Directory Structure
This repository acts as a unified environment containing both your interactive Streamlit application files and your developmental research notebooks:

lab-ai-compliance-suite/
├── pages/                             # Multi-page Streamlit App Pages
│   ├── 01_Gene_Expression_Checker.py  # Transcriptomic feature explorer
│   ├── 02_Biofilm_Image_Analyzer.py    # Bioimage segmentation frontend
│   ├── 03_Multimodal_Fusion.py         # Cross-modal feature alignment hub
│   ├── 04_SOP_Summary_Assistant.py     # Procedural workflow summarizer
│   └── 05_Scientific_Document_Summary.py # Key scientific term extractor
├── notebooks/                         # Core ML Development Sandbox
│   ├── 01_preprocessing.ipynb          # Raw DE transcript cleanup & alignment
│   ├── 02_feature_engineering.ipynb    # Biological interaction & ratio metrics
│   ├── 03_model_training.ipynb         # Classifier training (RF, Logistic Regression)
│   ├── 04_feature_importance.ipynb    # Model parameter & pathway relevance mapping
│   └── 05_gene_level_predictions.ipynb # Scaled single-gene pipeline inference
├── app.py                             # Main Streamlit entrance script
├── requirements.txt                   # Application dependencies
└── README.md                          # Repository documentation
Included Modules
1. Gene Expression Checker
Supports Project A of BiofilmAI by allowing users to upload gene expression tables and preview:
required columns (gene, logFC, p‑value, adj p‑value)
summary statistics
significantly up/down‑regulated genes
volcano plot previews
exportable feature tables for ML modeling

2. Biofilm Image Analyzer
Supports Project B by processing fluorescence and brightfield microscopy images:
denoising and normalization
channel separation
watershed segmentation previews
biomass and cell‑count estimation
live/dead ratio estimation
exportable image‑derived feature tables

3. Multimodal Fusion Hub
Supports Project C by previewing how gene expression and microscopy features combine:
upload gene‑derived feature tables
upload image‑derived feature tables
feature alignment and normalization
combined feature vector visualization
early‑stage multimodal model previews
export unified multimodal datasets

4. SOP & Protocol Summary Assistant
Summarizes procedural scientific documents such as SOPs, JoVE protocols, and step‑by‑step experimental workflows.
This module extracts the core components of a procedure — including purpose, materials, equipment, steps, conditions, safety, and expected results — and presents them as a structured overview.
It helps researchers quickly understand what the SOP contains, what the experiment is about, and how the workflow is organized, without performing any completeness or compliance checks.

5. Scientific Document Summarization Module
Summarizes scientific documents — including methods, workflows, technical notes, and publications — to extract the main purpose, experimental context, and key scientific content.
This module provides a concise overview of what the document contains and what the study or experiment is about, supporting rapid scientific interpretation without performing structural or completeness analysis.
Quick Features
Modular multipage Streamlit architecture
Real‑time microscopy segmentation previews
Transcriptomic feature exploration
Multimodal dataset construction
SOP/protocol summarization
Scientific document summarization

Requirements
The BiofilmAI Lab Suite uses a simplified, unpinned environment for compatibility and reproducibility.
Your requirements.txt should contain:
streamlit
pandas
numpy
matplotlib
seaborn
scikit-learn
joblib
PyPDF2
python-docx
📬 Academic & Professional Profiles

Explore my peer-reviewed publications, open-source code repositories, and professional networks:
Portfolio Showcase: Maria BG Scientific Portfolio
ORCID: 0000-0002-7525-4262
Google Scholar: Maria BG Profile
LinkedIn: maria-burgos-garay
GitHub: mariabgcenter-lab

© 2026 Maria BG Scientific. Developed under an agile, open-science model at the intersection of advanced microbiology, clinical data standards, and AI-driven biological discovery.
