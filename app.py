# app.py
import streamlit as st
import io
import re
from collections import Counter
import pandas as pd

# Optional imports used in pages; if not installed the page will show a friendly message
try:
    from PyPDF2 import PdfReader
    _has_pypdf2 = True
except Exception:
    _has_pypdf2 = False

try:
    from skimage import io as skio
    _has_skimage = True
except Exception:
    _has_skimage = False

st.set_page_config(page_title="Laboratory AI & QC Suite", layout="wide")
st.title("Laboratory AI & Quality Control Suite")

st.markdown("**Live demo:** https://lab-ai-compliance-suite-icr9e9zehffzgw8qj4fdb2.streamlit.app/")

# Sidebar navigation
page = st.sidebar.selectbox("Choose module", [
    "Home",
    "01 ISO Compliance Audit",
    "02 Biofilm Live/Dead Analyzer",
    "03 Diagnostic QC Validator",
    "04 Document Review",
    "05 Lab Risk Assessment"
])

# --- Home ---
if page == "Home":
    st.header("Welcome")
    st.write(
        "This multi‑module app includes simple, safe placeholders for:\n\n"
        "- ISO Compliance & SOP Audit Assistant\n"
        "- Biofilm Live/Dead Analyzer\n"
        "- Diagnostic Batch QC Validator\n"
        "- Document Review\n"
        "- Lab Risk Assessment\n\n"
        "Use the sidebar to open a module. These pages are intentionally lightweight and rule‑based; replace with validated institutional code for production."
    )

# --- ISO Compliance Audit ---
elif page == "01 ISO Compliance Audit":
    st.header("01 — ISO Compliance & SOP Audit Assistant")
    st.write("Upload a TXT or PDF (text layer). This assistant scans for common SOP parameters and flags missing items.")
    uploaded = st.file_uploader("Upload SOP or report (TXT or PDF)", type=["txt", "pdf"])
    def simple_checks(text):
        checks = []
        if not re.search(r"\b(sample collection|sample handling|storage temperature)\b", text, re.I):
            checks.append("Missing sample collection/handling/storage details.")
        if not re.search(r"\b(acceptance criteria|specification|limit)\b", text, re.I):
            checks.append("No acceptance criteria or specification found.")
        if not re.search(r"\b(controls|positive control|negative control)\b", text, re.I):
            checks.append("No controls described.")
        if not re.search(r"\b(verification|validation|qualification)\b", text, re.I):
            checks.append("No validation/verification steps found.")
        return checks

    if uploaded:
        raw = uploaded.read()
        text = ""
        if uploaded.name.lower().endswith(".txt"):
            try:
                text = raw.decode("utf-8", errors="ignore")
            except Exception:
                text = str(raw)
        else:
            if _has_pypdf2:
                try:
                    reader = PdfReader(io.BytesIO(raw))
                    pages = [p.extract_text() or "" for p in reader.pages]
                    text = "\n".join(pages)
                except Exception:
                    text = ""
            else:
                text = ""
        if not text:
            st.warning("No text extracted. For scanned PDFs OCR is required or install PyPDF2.")
        else:
            st.subheader("Extracted text preview")
            st.text_area("Text", value=text[:2000], height=220)
            flags = simple_checks(text)
            st.subheader("Audit flags")
            if flags:
                for f in flags:
                    st.error(f)
            else:
                st.success("Basic checks passed.")
    else:
        st.info("Upload a file to run a quick SOP audit.")

# --- Biofilm Analyzer ---
elif page == "02 Biofilm Live/Dead Analyzer":
    st.header("02 — Biofilm Live/Dead Analyzer")
    st.write("Upload a fluorescence image. This placeholder shows image upload and preview. Replace with your validated analysis pipeline when ready.")
    uploaded = st.file_uploader("Upload image (PNG/JPG/TIFF)", type=["png", "jpg", "jpeg", "tif", "tiff"])
    if uploaded:
        if not _has_skimage:
            st.error("scikit-image is not installed. Add scikit-image to requirements.txt to enable image preview and analysis.")
        else:
            try:
                img = skio.imread(uploaded)
                st.image(img, caption="Uploaded image", use_column_width=True)
                st.write("Placeholder analysis: add your watershed segmentation and live/dead ratio code here.")
            except Exception as e:
                st.error(f"Image load error: {e}")
    else:
        st.info("Upload an image to preview.")

# --- Diagnostic QC Validator ---
elif page == "03 Diagnostic QC Validator":
    st.header("03 — Diagnostic Batch QC Validator")
    st.write("Upload a CSV with QC metrics. This page runs simple checks and produces a copyable summary.")
    uploaded = st.file_uploader("Upload QC CSV (columns: sample, metric, value)", type=["csv"])
    if uploaded:
        try:
            df = pd.read_csv(uploaded)
            st.dataframe(df.head())
            issues = []
            if df.isnull().any().any():
                issues.append("Missing values found.")
            if "value" in df.columns:
                out_of_range = df[(df["value"] < 0) | (df["value"] > 100)]
                if not out_of_range.empty:
                    issues.append(f"{len(out_of_range)} values out of expected range (0-100).")
            if issues:
                for i in issues:
                    st.error(i)
            else:
                st.success("Basic QC checks passed.")
            summary = f"QC summary: {len(df)} rows; issues: {', '.join(issues) if issues else 'none'}"
            st.subheader("QC summary (copyable)")
            st.text_area("Summary", value=summary, height=120)
        except Exception as e:
            st.error(f"CSV read error: {e}")
    else:
        st.info("Upload a QC CSV to validate.")

# --- Document Review ---
elif page == "04 Document Review":
    st.header("04 — Lab Document Review")
    st.write("Upload a PDF or TXT file. This page extracts plain text (TXT or PDF text layer), shows top keywords, and applies simple rule-based flags.")
    uploaded = st.file_uploader("Upload a document (PDF or TXT)", type=["pdf", "txt"])
    def extract_text_from_pdf_bytes(pdf_bytes):
        if not _has_pypdf2:
            return ""
        try:
            reader = PdfReader(io.BytesIO(pdf_bytes))
            pages = [p.extract_text() or "" for p in reader.pages]
            return "\n".join(pages)
        except Exception:
            return ""
    def simple_tokenize(text):
        tokens = re.findall(r"[A-Za-z]{3,}", text.lower())
        return tokens
    def flag_rules(text):
        flags = []
        if not re.search(r"\b(glove|gloves|goggles|eye protection|mask|respirator|PPE|lab coat)\b", text, re.I):
            flags.append("No explicit PPE mention found.")
        if not re.search(r"\b(biosafety cabinet|BSC|containment|BSL-2|BSL-3|hood|isolator)\b", text, re.I):
            flags.append("No containment or biosafety cabinet mention found.")
        if not re.search(r"\b(waste|autoclave|decontaminat|dispose|sharps)\b", text, re.I):
            flags.append("No waste handling or decontamination instructions found.")
        if not re.search(r"\b(training|competent|certified|qualified)\b", text, re.I):
            flags.append("No training or competency statement found.")
        return flags

    if uploaded:
        file_bytes = uploaded.read()
        text = ""
        if uploaded.name.lower().endswith(".txt"):
            try:
                text = file_bytes.decode("utf-8", errors="ignore")
            except Exception:
                text = str(file_bytes)
        else:
            text = extract_text_from_pdf_bytes(file_bytes)
            if not text:
                st.warning("PDF text extraction failed or PDF has no text layer. Install PyPDF2 or use a TXT file.")
        if text:
            st.subheader("Extracted text (first 2000 characters)")
            st.text_area("Document text", value=text[:2000], height=220)
            tokens = simple_tokenize(text)
            counts = Counter(tokens)
            common = counts.most_common(20)
            st.subheader("Top keywords")
            st.table({"Keyword": [k for k, _ in common], "Count": [v for _, v in common]})
            st.subheader("Rule-based flags")
            flags = flag_rules(text)
            if flags:
                for f in flags:
                    st.error(f)
            else:
                st.success("No obvious missing items found by simple rules.")
            summary = (
                f"Document review summary\n\n"
                f"File: {uploaded.name}\n"
                f"Top keywords: {', '.join([k for k, _ in common[:10]])}\n\n"
                f"Flags:\n" + ("\n".join(f"- {f}" for f in flags) if flags else "- None")
            )
            st.subheader("Review summary (copy to clipboard)")
            st.text_area("Summary", value=summary, height=180)
        else:
            st.info("No text could be extracted from the uploaded file.")
    else:
        st.info("Upload a PDF or TXT file to start document review.")

# --- Lab Risk Assessment ---
elif page == "05 Lab Risk Assessment":
    st.header("05 — Lab Risk Assessment")
    st.write("Enter scenario details and click Compute risk.")
    activity = st.text_area("Describe the activity or experiment", height=100)
    st.subheader("Hazard and procedure")
    organism_risk = st.slider("Organism risk class (1 low — 5 high)", 1, 5, 2)
    procedure_risk = st.slider("Procedure risk (1 low — 5 high)", 1, 5, 2)
    exposure_likelihood = st.slider("Exposure likelihood (1 unlikely — 5 likely)", 1, 5, 2)
    st.subheader("Existing mitigations")
    ppe_level = st.slider("PPE level (1 minimal — 5 full PPE)", 1, 5, 3)
    engineering_controls = st.slider("Engineering controls (1 none — 5 full containment)", 1, 5, 3)
    training_level = st.slider("Training level (1 none — 5 certified and recent)", 1, 5, 3)
    num_people = st.number_input("Number of personnel involved", min_value=1, max_value=50, value=1, step=1)
    location = st.text_input("Location or lab area", value="")

    def compute_risk_score_simple(inputs):
        pos = inputs["organism_risk"] + inputs["procedure_risk"] + inputs["exposure_likelihood"]
        mitig = inputs["ppe_level"] + inputs["engineering_controls"] + inputs["training_level"]
        raw = pos - mitig
        raw_clamped = max(-3, min(15, raw))
        score = int(round((raw_clamped + 3) / 18 * 100))
        breakdown = {
            "Organism risk": inputs["organism_risk"],
            "Procedure risk": inputs["procedure_risk"],
            "Exposure likelihood": inputs["exposure_likelihood"],
            "PPE mitigation": -inputs["ppe_level"],
            "Engineering mitigation": -inputs["engineering_controls"],
            "Training mitigation": -inputs["training_level"],
        }
        return {"score": score, "breakdown": breakdown}

    def risk_level_from_score(score):
        if score < 25:
            return "Low", "#2ECC71"
        if score < 50:
            return "Moderate", "#F1C40F"
        if score < 75:
            return "High", "#E67E22"
        return "Critical", "#E74C3C"

    if st.button("Compute risk"):
        inputs = {
            "organism_risk": organism_risk,
            "procedure_risk": procedure_risk,
            "exposure_likelihood": exposure_likelihood,
            "ppe_level": ppe_level,
            "engineering_controls": engineering_controls,
            "training_level": training_level,
        }
        result = compute_risk_score_simple(inputs)
        score = result["score"]
        level, color = risk_level_from_score(score)
        st.markdown(f"### **Risk score: {score} / 100**")
        st.markdown(f"### **Risk level: <span style='color:{color}'>{level}</span>**", unsafe_allow_html=True)
        df = pd.DataFrame({
            "Component": list(result["breakdown"].keys()),
            "Contribution": [round(v, 2) for v in result["breakdown"].values()]
        })
        try:
            import altair as alt
            chart = alt.Chart(df).mark_bar().encode(
                x=alt.X("Contribution:Q", title="Contribution (positive increases risk; negative decreases)"),
                y=alt.Y("Component:N", sort='-x'),
                color=alt.condition(alt.datum.Contribution > 0, alt.value("#d9534f"), alt.value("#5cb85c")),
                tooltip=["Component", "Contribution"]
            ).properties(height=300)
            st.altair_chart(chart, use_container_width=True)
        except Exception:
            st.table(df)
        st.subheader("Recommendations")
        if level == "Low":
            st.write("- Routine controls adequate; continue standard procedures.")
        elif level == "Moderate":
            st.write("- Increase PPE and confirm training; consider extra engineering controls.")
        elif level == "High":
            st.write("- Restrict to trained personnel; use containment and notify biosafety officer.")
        else:
            st.write("- Suspend non-essential work; engage biosafety committee and senior leadership.")
        st.subheader("Detailed assessment")
        st.write("**Activity**:", activity or "—")
        st.write("**Location**:", location or "—")
        st.write("**Personnel involved**:", int(num_people))
        st.write("**Inputs**:", inputs)
        summary_text = (
            f"Risk assessment summary\n\nScore: {score}/100\nLevel: {level}\n\n"
            f"Activity: {activity}\nLocation: {location}\nPersonnel: {num_people}\n\n"
        )
        st.text_area("Assessment summary (copy to clipboard)", value=summary_text, height=180)
