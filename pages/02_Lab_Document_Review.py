# pages/02_Lab_Document_Review.py
import streamlit as st
import io
import re
from collections import Counter

st.set_page_config(page_title="Document Review", layout="wide")
st.title("02 — Lab Document Review")

st.write("Upload a PDF or TXT file. This page extracts plain text (TXT or PDF text layer), shows top keywords, and applies simple rule-based flags for common compliance items.")

uploaded = st.file_uploader("Upload a document (PDF or TXT)", type=["pdf", "txt"])

def extract_text_from_pdf_bytes(pdf_bytes):
    try:
        # lightweight PDF text extraction using PyPDF2 if available
        from PyPDF2 import PdfReader
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
    # rule: mention of PPE
    if not re.search(r"\b(glove|gloves|goggles|eye protection|mask|respirator|PPE|lab coat)\b", text, re.I):
        flags.append("No explicit PPE mention found.")
    # rule: containment
    if not re.search(r"\b(biosafety cabinet|BSC|containment|BSL-2|BSL-3|hood|isolator)\b", text, re.I):
        flags.append("No containment or biosafety cabinet mention found.")
    # rule: waste/disposal
    if not re.search(r"\b(waste|autoclave|decontaminat|dispose|sharps)\b", text, re.I):
        flags.append("No waste handling or decontamination instructions found.")
    # rule: training
    if not re.search(r"\b(training|competent|certified|qualified)\b", text, re.I):
        flags.append("No training or competency statement found.")
    return flags

if uploaded is not None:
    file_bytes = uploaded.read()
    text = ""
    if uploaded.type == "text/plain" or uploaded.name.lower().endswith(".txt"):
        try:
            text = file_bytes.decode("utf-8", errors="ignore")
        except Exception:
            text = str(file_bytes)
    elif uploaded.type == "application/pdf" or uploaded.name.lower().endswith(".pdf"):
        text = extract_text_from_pdf_bytes(file_bytes)
        if not text:
            st.warning("PDF text extraction failed or PDF has no text layer. For scanned images, OCR is required (not included).")
    else:
        st.warning("Unsupported file type.")

    if text:
        st.subheader("Extracted text (first 2000 characters)")
        st.text_area("Document text", value=text[:2000], height=220)

        # Keywords
        tokens = simple_tokenize(text)
        counts = Counter(tokens)
        common = counts.most_common(20)
        st.subheader("Top keywords")
        st.table({"Keyword": [k for k, _ in common], "Count": [v for _, v in common]})

        # Flags
        st.subheader("Rule-based flags")
        flags = flag_rules(text)
        if flags:
            for f in flags:
                st.error(f)
        else:
            st.success("No obvious missing items found by simple rules.")

        # Copyable summary
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
