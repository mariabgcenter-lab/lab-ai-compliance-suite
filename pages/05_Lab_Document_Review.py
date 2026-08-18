import streamlit as st

st.title("📑 Laboratory Document Review Assistant")

st.write(
    "Reviews scientific documents (methods, workflows, technical notes, publications) "
    "for clarity and completeness. Identifies missing conceptual sections and evaluates "
    "overall scientific organization."
)

st.markdown("---")

# ---------------------------------------------------------
# File Upload Section
# ---------------------------------------------------------
st.subheader("📄 Upload Scientific Document")

uploaded_doc = st.file_uploader(
    "Upload document (PDF, TXT, DOCX)",
    type=["pdf", "txt", "docx"]
)

doc_text = ""

# ---------------------------------------------------------
# Extract Text from Uploaded File
# ---------------------------------------------------------
if uploaded_doc:

    # PDF extraction
    if uploaded_doc.type == "application/pdf":
        try:
            import PyPDF2
            reader = PyPDF2.PdfReader(uploaded_doc)
            doc_text = "\n".join(page.extract_text() or "" for page in reader.pages)
        except Exception:
            st.error("Unable to read PDF file.")

    # TXT extraction
    elif uploaded_doc.type == "text/plain":
        try:
            doc_text = uploaded_doc.read().decode("utf-8")
        except Exception:
            st.error("Unable to read TXT file.")

    # DOCX extraction
    elif uploaded_doc.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        try:
            import docx
            doc = docx.Document(uploaded_doc)
            doc_text = "\n".join([para.text for para in doc.paragraphs])
        except Exception:
            st.error("Unable to read DOCX file.")

# ---------------------------------------------------------
# Fallback Manual Paste
# ---------------------------------------------------------
st.subheader("📄 Or Paste Document Text")

manual_text = st.text_area(
    "Paste scientific document text:",
    height=300,
    placeholder="Paste methods, workflow, or scientific text..."
)

# If upload succeeded, use uploaded text; otherwise use manual text
if doc_text.strip() == "":
    doc_text = manual_text

st.markdown("---")

# ---------------------------------------------------------
# Conceptual Sections
# ---------------------------------------------------------
conceptual_sections = [
    "background",
    "introduction",
    "objective",
    "methods",
    "results",
    "discussion",
    "conclusion",
    "limitations",
    "notes"
]

# ---------------------------------------------------------
# Review Button
# ---------------------------------------------------------
if st.button("Run Document Review", type="primary"):
    st.markdown("### 🔍 Document Completeness Review")

    if len(doc_text.strip()) == 0:
        st.warning("Please upload or paste document text before reviewing.")
    else:
        lower_doc = doc_text.lower()
        present = []
        missing = []

        for section in conceptual_sections:
            if section in lower_doc:
                present.append(section)
            else:
                missing.append(section)

        col1, col2 = st.columns(2)

        with col1:
            st.success("✔ Sections Found")
            for p in present:
                st.write(f"• {p.capitalize()}")

        with col2:
            st.error("❌ Sections Missing")
            for m in missing:
                st.write(f"• {m.capitalize()}")

        st.markdown("---")

        if len(missing) == 0:
            st.success("🎉 Document contains all major scientific sections.")
        else
