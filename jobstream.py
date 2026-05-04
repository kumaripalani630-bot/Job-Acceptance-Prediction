import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
jobdata = pd.read_csv('C:/Users/LENOVO/Desktop/Job Acceptance/jobdata_cleaned.csv')

st.set_page_config(layout="wide")
st.title("📊 Job Acceptance Prediction Dashboard")


# ==================================
# STATUS IS ALREADY ENCODED (0/1)
# ==================================
# NO .str.lower()

jobdata["placed"] = jobdata["status"].astype(int)


# Interview average
jobdata["interview_avg"] = jobdata[
    [
        "technical_score",
        "aptitude_score",
        "communication_score"
    ]
].mean(axis=1)


# Accepted
jobdata["accepted"] = jobdata["placed"]


# High risk
jobdata["high_risk"] = (
    (jobdata["skills_match_percentage"] < 50)
    |
    (jobdata["technical_score"] < 50)
    |
    (jobdata["communication_score"] < 50)
).astype(int)


# ==================================
# KPI
# ==================================
total_candidates = len(jobdata)

placement_rate = (
    jobdata["placed"].mean() * 100
)

job_acceptance_rate = (
    jobdata["accepted"].mean() * 100
)

avg_interview_score = (
    jobdata["interview_avg"].mean()
)

avg_skills_match = (
    jobdata["skills_match_percentage"].mean()
)

offer_dropout_rate = (
    (1 - jobdata["accepted"].mean()) * 100
)

high_risk_percentage = (
    jobdata["high_risk"].mean() * 100
)


# ==================================
# KPI DISPLAY
# ==================================
st.header("📌 Key KPIs")

c1, c2, c3 = st.columns(3)

c1.metric("Total Candidates", total_candidates)
c2.metric("Placement Rate (%)", f"{placement_rate:.2f}")
c3.metric("Job Acceptance Rate (%)", f"{job_acceptance_rate:.2f}")


c4, c5, c6, c7 = st.columns(4)

c4.metric("Average Interview Score", f"{avg_interview_score:.2f}")
c5.metric("Average Skills Match %", f"{avg_skills_match:.2f}")
c6.metric("Offer Dropout Rate %", f"{offer_dropout_rate:.2f}")
c7.metric("High-Risk Candidate %", f"{high_risk_percentage:.2f}")


# ==================================
st.markdown("---")
st.header("📈 Analyst Tasks (EDA & ML Analytics)")
st.subheader("1️⃣ Academic Scores vs Placement Outcome")

academic = jobdata.groupby("placed")[
    [
        "ssc_percentage",
        "hsc_percentage",
        "degree_percentage"
    ]
].mean()

st.bar_chart(academic)
st.subheader("2️⃣ Skills Match vs Interview Performance")

fig, ax = plt.subplots()

ax.scatter(
    jobdata["skills_match_percentage"],
    jobdata["interview_avg"]
)

ax.set_xlabel("Skills Match %")
ax.set_ylabel("Interview Score")

st.pyplot(fig)

st.subheader("3️⃣ Certification Impact on Job Acceptance")

certification = jobdata.groupby(
    "certifications_count"
)["accepted"].mean()

st.line_chart(certification)

st.subheader("5️⃣ Experience vs Placement Success")

experience = jobdata.groupby(
    "years_of_experience"
)["placed"].mean()

st.line_chart(experience)
st.subheader("6️⃣ Interview Score vs Placement Probability")

jobdata["score_bins"] = pd.cut(
    jobdata["interview_avg"],
    bins=10
).astype(str)

probability = jobdata.groupby(
    "score_bins"
)["placed"].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,4))

ax.plot(
    probability["score_bins"],
    probability["placed"],
    marker="o"
)

plt.xticks(rotation=45)
plt.xlabel("Interview Score Range")
plt.ylabel("Placement Probability")

st.pyplot(fig)
st.subheader("7️⃣ Employability Test Score Analysis")

scores = pd.Series({
    "Technical":
        jobdata["technical_score"].mean(),

    "Aptitude":
        jobdata["aptitude_score"].mean(),

    "Communication":
        jobdata["communication_score"].mean()
})

st.bar_chart(scores)
# ==================================
# FOOTER
# ==================================
st.markdown("---")
st.markdown(
    """
    **Created by Palani Kumari**  
    📧 kumaripalani630@gmail.com  
    📍 Madurai, India
    """
    )