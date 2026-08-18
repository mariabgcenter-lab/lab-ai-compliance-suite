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

### 5. **Scientific Document Summarization Module**
Summarizes scientific documents — including methods, workflows, technical notes, and publications — to extract the main purpose, experimental context, and key scientific content.  
This module provides a concise overview of **what the document contains** and **what the study or experiment is about**, supporting rapid scientific interpretation without performing structural or completeness analysis.

---

## ⚙️ Quick Features
- Modular multipage Streamlit architecture  
- Real‑time microscopy segmentation previews  
- Transcriptomic feature exploration  
- Multimodal dataset construction  
- SOP/protocol summarization  
- Scientific document summarization  

---

## 📁 Requirements
The BiofilmAI Lab Suite uses a simplified, unpinned environment for compatibility and reproducibility.  
Your `requirements.txt` should contain:

