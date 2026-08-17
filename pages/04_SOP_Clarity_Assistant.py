import streamlit as st

st.title("🧪 SOP & Protocol Summary Assistant")

st.write(
    "Summarizes SOPs, protocols, and step-by-step workflows to provide a clear overview of "
    "what the document contains and what the experiment is about."
)

st.markdown("---")

st.subheader("📄 Paste SOP or Protocol Text")

sop_text = st.text_area(
    "Paste SOP or protocol here:",
    height=300,
    placeholder="Paste your SOP/protocol text..."
)

if st.button("Generate SOP Summary", type="primary"):
    st.markdown("### 📝 SOP Summary")

    if len(sop_text.strip()) == 0:
        st.warning("Please paste SOP text before summarizing.")
    else:
        # Simple section extraction
        sections = {
            "Purpose": ["purpose", "objective", "goal"],
            "Materials": ["materials", "reagents", "supplies"],
            "Equipment": ["equipment", "instruments", "tools"],
            "Procedure": ["procedure", "steps", "protocol"],
            "Conditions": ["conditions", "temperature", "incubation", "timing"],
            "Safety": ["safety", "hazards", "ppe"],
            "Expected Results": ["results", "outcome", "observation"]
        }

        lower_sop = sop_text.lower()

        for title, keywords in sections.items():
            st.markdown(f"#### {title}")
            extracted = []

            for kw in keywords:
                if kw in lower_sop:
                    extracted.append(kw)

            if extracted:
                st.write(f"Section detected based on keywords: {', '.join(extracted)}")
                st.write("Summary:")
                st.write(f"- This SOP contains information related to **{title.lower()}**.")
            else:
                st.write("No explicit section detected.")
            st.markdown("---")

        st.success("SOP summary generated.")
