# Laboratory AI & Quality Control Suite

🚀 **Live Interactive App:** https://lab-ai-compliance-suite-icr9e9zehffzgw8qj4fdb2.streamlit.app/

A unified Streamlit application designed for **clinical diagnostics**, **industrial QA/QC**, and **ISO‑compliant laboratory workflows**.  
This suite centralizes document auditing, QC validation, microscopy analysis, and certificate generation into a single interactive platform.

---

## 📦 Included Modules

### 1. **ISO Compliance & Document Audit Assistant**
Automatically reviews SOPs, technical reports, validation documents, and QC summaries for missing ISO/CLIA‑required elements such as:
- calibration tolerances  
- reagent expiration dates  
- lot numbers  
- negative/positive/internal control documentation  
- maintenance logs  
- acceptance criteria  
- instrument IDs  

Provides instant compliance flags aligned with **ISO 17025** and **CLIA** expectations.

---

### 2. **Biofilm Live/Dead Fluorescence Analyzer**
Computer‑vision module for dual‑channel fluorescence microscopy:
- H‑maxima watershed segmentation  
- live/dead cell counts  
- biomass quantification  
- viability & mortality ratios  
- RGB overlay visualization  

Ideal for microbial ecology, biofilm research, and microscopy QC.

---

### 3. **Diagnostic Batch QC Validator**
Evaluates diagnostic assay batch runs using:
- Negative Control (NC) checks  
- Positive Control (PC) Ct thresholds  
- Internal Control (IC) suitability  
- Sample‑level extraction failures  

Generates annotated batch tables and automated **QA release decisions**.

---

### 4. **QA Certificate Generator**
Creates downloadable, ISO‑aligned QA release certificates:
- batch metadata  
- assay target  
- instrument & analyst  
- NC/PC/IC status  
- flagged samples  
- timestamped audit trail  

Exports a clean `.txt` certificate for regulatory documentation.

---

### 5. **Laboratory Document Review Assistant**
Automated document reviewer for:
- SOPs  
- QC summaries  
- technical validation reports  
- assay documentation  

Flags missing required elements such as:
- lot numbers  
- expiration dates  
- tolerances  
- acceptance criteria  
- instrument IDs  

Provides a general‑purpose document completeness check complementary to the ISO compliance module.

---

## ⚙️ Quick Features
- Interactive sliders and parameter tuning  
- Real‑time microscopy segmentation  
- Automated QC decision logic  
- Downloadable QA certificates  
- Document compliance auditing  
- ISO/CLIA‑aligned rule‑based checks  
- Fully modular multipage Streamlit architecture  

---

## 📁 Requirements

Ensure your `requirements.txt` contains:

