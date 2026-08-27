BiofilmAI Lab Suite — Interactive Deployment & Computational Sandbox
--Image of: --Streamlit App --Image of: --Python --Image of: --Microbiology --Image of: --Regulatory Compliance

The BiofilmAI Lab Suite (deployed as lab-ai-compliance-suite) is a unified, interactive scientific environment designed to support multimodal prediction of biofilm formation and streamline laboratory compliance workflows.

This repository serves as a unified computational ecosystem—housing both your live, user-facing Streamlit analytics dashboard and the underlying, developmental Jupyter Notebooks used to build, validate, and audit your machine learning models. It translates raw transcriptomic pipelines, computer vision segmentation tasks, and data engineering into ready-to-use, web-based tools for bench scientists, microbiologists, and laboratory operations directors.

🔗 Live Interactive App: Launch the BiofilmAI Lab Suite

🗂️ Unified Directory Structure
lab-ai-compliance-suite/
├── pages/                             # Multi-page Streamlit Frontend
│   ├── 01_Gene_Expression_Checker.py  # Transcriptomic feature explorer
│   ├── 02_Biofilm_Image_Analyzer.py    # Bioimage segmentation interface
│   ├── 03_Multimodal_Fusion.py         # Cross-modal feature alignment hub
│   ├── 04_SOP_Summary_Assistant.py     # Procedural workflow summarizer
│   └── 05_Scientific_Document_Summary.py # Key scientific term extractor
├── notebooks/                         # Core ML Development Sandbox (Project A)
│   ├── 01_preprocessing.ipynb          # Raw DE transcript cleanup & alignment
│   ├── 02_feature_engineering.ipynb    # Biological interaction & ratio metrics
│   ├── 03_model_training.ipynb         # Classifier training (RF, Logistic Regression)
│   ├── 04_feature_importance.ipynb    # Model parameter & pathway relevance mapping
│   └── 05_gene_level_predictions.ipynb # Scaled single-gene pipeline inference
├── app.py                             # Streamlit main entrance page
├── requirements.txt                   # Application dependencies
└── README.md                          # Repository documentation
🧪 Included Modules & Core Features
1. Gene Expression Checker
Supports Project A (Genomic Profiling) of BiofilmAI by allowing users to upload and explore raw differential expression tables:

Required column validation (gene, logFC, p‑value, adj p‑value)
Summary statistics for expression distributions
Identification of significantly up/down‑regulated genes ($|logFC| > 1.5$, $p < 0.05$)
Volcano plot previews to audit statistical thresholds
Exportable feature tables directly prepared for downstream ML modeling
2. Biofilm Image Analyzer
Supports Project B (BiofilmNN) by processing fluorescence and brightfield microscopy images:

Interactive image preprocessing (denoising and normalization)
Multi-channel fluorophore separation
Watershed segmentation previews to segment cellular biomass
Automated biomass and cell‑count estimation
Live/dead ratio estimation for dual-channel assays
Exportable image‑derived morphological feature tables
3. Multimodal Fusion Hub
Supports Project C (Multimodal Fusion) by previewing how gene expression and microscopy features combine:

Multi-source file ingestion (upload gene-derived and image-derived tables)
Dynamic feature alignment and cross-modal normalization
Visual previews of combined, high-dimensional feature vectors
Early-stage multimodal machine learning model predictions
Exportable unified multimodal datasets for training advanced classifiers
4. SOP & Protocol Summary Assistant
Summarizes procedural scientific documents such as SOPs, JoVE protocols, and step‑by‑step experimental workflows:

Parses uploaded files (PDF, TXT, DOCX) or raw text pastes
Automatically extracts the core components of a procedure: Purpose, Materials, Equipment, Steps, Conditions, Safety, and Expected Results
Helps researchers and quality auditors quickly understand what a protocol contains and how a workflow is organized, without manual review
5. Scientific Document Summarization Module
Summarizes scientific literature, methods, workflows, and technical notes to accelerate literature review and laboratory onboarding:

Provides a rapid, concise 5-sentence overview of the document's main purpose and context
Features automatic term frequency analysis to extract and display key scientific terms (e.g., specific microbial strains, assays, or parameters)
🛡️ Clinical Alignment & Quality Standards
The BiofilmAI Lab Suite bridges the gap between machine learning and clinical microbiology compliance frameworks (GLP / CLIA-aligned):

Reproducible ML Pipelines: Keeping your developmental notebooks and deployment scripts in a single repository ensures that every model feature and preprocessing step is auditable from raw data to the final dashboard.
Narrative-Driven Design ("Vibe Coding"): Code architecture and data structures are explicitly named after their biological or statistical realities (e.g., biofilm_significant, logFC_interaction) to ensure transparency for peer reviewers and lab inspectors.
Operational Readiness: Procedural summaries and keyword parsers support workforce development, CAPA tracking, and laboratory quality management systems (QMS).
🛠️ Local Installation & Launch
To run the Streamlit app locally in your Conda or virtual environment:

1. Clone the Repository
git clone https://github.com/mariabgcenter-lab/lab-ai-compliance-suite.git
cd lab-ai-compliance-suite
2. Install Dependencies
pip install -r requirements.txt
3. Launch Streamlit
streamlit run app.py
📋 Requirements
The BiofilmAI Lab Suite uses a simplified, unpinned environment for maximum cross-platform compatibility and reproducibility. Your requirements.txt should contain:

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

Good content
Bad content
