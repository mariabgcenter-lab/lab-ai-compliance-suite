# BiofilmAI Lab Suite

🚀 **Live Interactive App:**  
https://lab-ai-compliance-suite-icr9e9zehffzgw8qj4fdb2.streamlit.app/

The **BiofilmAI Lab Suite** is a unified Streamlit application designed to support multimodal prediction of biofilm formation using gene expression data, microscopy features, and structured scientific documentation.  
This suite provides an integrated scientific environment for exploring transcriptomic patterns, analyzing biofilm images, previewing multimodal fusion, and working with research‑related documents.

---

## 📦 Included Modules

### 1. **Gene Expression Checker**
Supports **Project A** of BiofilmAI by allowing users to upload gene expression tables and preview:
- required columns (gene, logFC, p‑value, adj p‑value)  
- summary statistics  
- significantly up/down‑regulated genes  
- volcano plot previews  
- exportable feature tables for ML modeling  

---

### 2. **Biofilm Image Analyzer**
Supports **Project B** by processing fluorescence and brightfield microscopy images:
- denoising and normalization  
- channel separation  
- watershed segmentation previews  
- biomass and cell‑count estimation  
- live/dead ratio estimation  
- exportable image‑derived feature tables  

---

### 3. **Multimodal Fusion Hub**
Supports **Project C** by previewing how gene expression and microscopy features combine:
- upload gene‑derived feature tables  
- upload image‑derived feature tables  
- feature alignment and normalization  
- combined feature vector visualization  
- early‑stage multimodal model previews  
- export unified multimodal datasets  

---

### 4. **SOP & Protocol Summary Assistant**
Summarizes procedural scientific documents such as SOPs, JoVE protocols, and step‑by‑step experimental workflows.  
This module extracts the core components of a procedure — including purpose, materials, equipment, steps, conditions, safety, and expected results — and presents them as a structured overview.  
It helps researchers quickly understand **what the SOP contains**, **what the experiment is about**, and **how the workflow is organized**, without performing any completeness or compliance checks.

---

### 5. **Laboratory Document Review Assistant**
Evaluates scientific documents for conceptual clarity and completeness.  
Designed for publications, methods sections, research workflows, technical notes, and other non‑procedural scientific text, this module identifies missing scientific sections such as background, objectives, methods, results, discussion, and limitations.  
It helps researchers assess **whether a document is well‑structured**, **scientifically coherent**, and **contains all major conceptual components**, without summarizing procedural content.

---

