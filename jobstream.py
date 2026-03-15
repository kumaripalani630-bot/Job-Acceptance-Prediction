import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load cleaned dataset
jobdata = pd.read_csv("C:/Users/admin/Downloads/jobdata_cleaned.csv")

st.title("Job Acceptance Prediction Dashboard")

# ---------------- KPI SECTION ----------------


total_candidates = jobdata.shape[0]

# Placement Rate
placement_rate = jobdata['status'].mean() * 100

# Average Interview Score
avg_interview_score = jobdata['interview_avg'].mean()

# Average Skills Match
avg_skills_match = jobdata['skills_match_percentage'].mean()

# Offer Dropout Rate (Assumption: placed but not joining)
# Since dataset doesn't have joining column we estimate using experience mismatch
offer_dropout_rate = ((jobdata['expected_ctc_lpa'] > jobdata['previous_ctc_lpa'] * 2).mean()) * 100

# High Risk Candidates
high_risk = jobdata[
    (jobdata['skills_match_percentage'] < 50) |
    (jobdata['communication_score'] < 50) |
    (jobdata['technical_score'] < 50)
]

high_risk_percentage = (len(high_risk) / total_candidates) * 100

# ---------------- Display KPIs ----------------

col1, col2, col3 = st.columns(3)

col1.metric("Total Candidates", total_candidates)
col2.metric("Placement Rate (%)", f"{placement_rate:.2f}")
col3.metric("Avg Interview Score", f"{avg_interview_score:.2f}")

col4, col5, col6 = st.columns(3)

col4.metric("Avg Skills Match (%)", f"{avg_skills_match:.2f}")
col5.metric("Offer Dropout Risk (%)", f"{offer_dropout_rate:.2f}")
col6.metric("High Risk Candidates (%)", f"{high_risk_percentage:.2f}")


# Footer / Creator Info
st.markdown("---")
st.markdown("Created by **Palani Kumari** | Data Analyst & ML Enthusiast")
st.markdown("📧 Contact: kumaripalani630@gmail.com")
st.markdown("📍 Location: Madurai, India")