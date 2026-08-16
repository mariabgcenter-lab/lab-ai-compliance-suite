# app.py
import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Lab AI Compliance Suite", layout="wide")
st.title("Lab AI Compliance Suite")

st.header("Lab Risk Assessment")
st.write("Enter the scenario details below and click Compute risk.")

# Scenario inputs
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

# Simple scoring function
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

# Compute button
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

    chart = alt.Chart(df).mark_bar().encode(
        x=alt.X("Contribution:Q", title="Contribution (positive increases risk; negative decreases)"),
        y=alt.Y("Component:N", sort='-x'),
        color=alt.condition(alt.datum.Contribution > 0, alt.value("#d9534f"), alt.value("#5cb85c")),
        tooltip=["Component", "Contribution"]
    ).properties(height=300)

    st.altair_chart(chart, use_container_width=True)

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
