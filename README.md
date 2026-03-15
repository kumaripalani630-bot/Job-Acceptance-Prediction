# Job-Acceptance-Prediction
Machine Learning project that predicts whether candidates will accept or reject job offers using recruitment data analysis, EDA, and Streamlit dashboards.
Job Acceptance Prediction System
Project Overview

Recruitment and placement teams handle large volumes of candidate data such as academic performance, technical skills, certifications, work experience, interview outcomes, and job market conditions. However, not every candidate who receives a job offer ends up accepting it.

The Job Acceptance Prediction System is designed to analyze candidate placement data and build a machine learning model that predicts whether a candidate will accept or reject a job offer. The project also provides analytical insights that help recruiters understand the key factors influencing job acceptance decisions.

This system helps HR teams reduce offer dropouts, improve hiring strategies, and support data-driven recruitment decisions.

Project Objectives

Predict whether a candidate will accept or reject a job offer

Identify key factors influencing job acceptance

Handle real-world data challenges such as missing values and inconsistent data

Provide actionable insights for recruitment and placement teams

Develop an interactive dashboard for recruitment analytics

Business Use Cases

Help recruitment teams predict offer acceptance probability

Reduce offer dropout rates

Improve hiring cycle efficiency

Identify factors affecting placement success

Support data-driven HR decision-making

Dataset Description

The dataset contains approximately 50,000 candidate records and simulates real-world recruitment scenarios.

The dataset includes features such as:

Candidate Profile

Age

Gender

Education Level

Academic Performance

Secondary School Percentage

Higher Secondary Percentage

Graduation Score

Employability Test Score

Skills and Certifications

Skills Match Percentage

Number of Certifications

Technical Skill Score

Work Experience

Years of Experience

Internship Experience

Interview Performance

Technical Interview Score

HR Interview Score

Average Interview Score

Job Market Conditions

Company Tier

Competition Level

Salary Offered

Target Variable

Status

1 → Job Accepted

0 → Job Rejected

The dataset also contains real-world data challenges such as:

Missing values

Duplicate-like records

Inconsistent categorical values

Project Pipeline
1 Data Collection

The dataset containing candidate recruitment data was collected and loaded into Python for analysis.

2 Data Understanding

Initial dataset exploration included:

Dataset shape

Data types verification

Sample records inspection

Null value analysis

Tools used:

Pandas

NumPy

3 Data Cleaning & Preprocessing

Key preprocessing steps:

Handling Missing Values

Missing values were handled using:

Mean

Median

Mode

Handling Inconsistent Data

Categorical values were standardized to maintain consistency.

Example:

Male, male, M → Male
Female, female, F → Female
Encoding Categorical Variables

Categorical columns were encoded using:

Label Encoding

One-Hot Encoding

Feature Scaling

Numerical features were scaled to improve model performance.

Exploratory Data Analysis (EDA)

EDA was performed to understand relationships between variables and job acceptance.

Key analyses performed:

Academic Performance vs Placement

Understanding how academic scores influence job acceptance.

Skills Match vs Job Acceptance

Analyzing how well candidate skills align with job requirements.

Experience vs Placement Success

Evaluating the impact of work experience on placement outcomes.

Interview Score vs Placement

Analyzing how interview performance affects job acceptance.

Company Tier vs Acceptance Rate

Studying acceptance rates across different company tiers.

Correlation Analysis

Heatmap used to identify relationships between numerical features.

Libraries used:

Pandas

Matplotlib

Seaborn

Feature Engineering

New analytical features were created to improve model performance.

Examples include:

Experience Category

Fresher

Junior

Senior

Skills Match Level

Low

Medium

High

Interview Performance Category

Poor

Average

Excellent

These derived features help improve model interpretability and prediction accuracy.

Machine Learning Modeling

The goal of the machine learning model is to predict job acceptance probability.

Target Variable

Status

1 → Candidate Accepted Job Offer
0 → Candidate Rejected Job Offer
Machine Learning Models Used

Logistic Regression

Decision Tree

Random Forest

Gradient Boosting

Model Evaluation Metrics

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

The best-performing model was selected based on evaluation metrics.

Data Storage (SQL) (optional)

The cleaned dataset can be stored in MySQL for scalable querying and reporting.

Benefits:

Efficient data management

Integration with analytics dashboards

Faster data retrieval

Streamlit Dashboard

An interactive dashboard was developed using Streamlit to visualize insights and key recruitment metrics.

The dashboard allows HR teams to explore recruitment data and monitor hiring performance.

Dashboard KPIs

The dashboard includes the following key performance indicators:

Total Candidates

Placement Rate (%)

Job Acceptance Rate (%)

Average Interview Score

Average Skills Match Percentage

Offer Dropout Rate

High-Risk Candidate Percentage

These KPIs provide a quick overview of recruitment effectiveness.

Project Results

The project successfully produced:

A cleaned and structured recruitment dataset

Data-driven insights about placement trends

Machine learning models predicting job acceptance

An interactive Streamlit dashboard for HR analytics

Key insights discovered:

Higher interview scores increase job acceptance probability

Strong skills match significantly improves placement chances

Work experience increases hiring success

Company tier influences candidate acceptance decisions

Technology Stack
Programming Language

Python

Libraries Used

Pandas

NumPy

Matplotlib

Seaborn

Scikit-learn

Dashboard

Streamlit

Database

Version Control

GitHub

Project Structure
job-acceptance-prediction
│
├── data
│   └── jobdata_cleaned.csv
│
├── notebooks
│   └── eda_analysis.ipynb
│
├── src
│   ├── data_preprocessing.py
│   ├── feature_engineering.py
│   └── model_training.py
│
├── dashboard
│   └── jobstream.py
│
├── requirements.txt
├── README.md
└── .gitignore
How to Run the Project
Clone the Repository
git clone https://github.com/your-username/job-acceptance-prediction.git
Install Required Libraries
pip install -r requirements.txt
Run Streamlit Dashboard
streamlit run jobstream.py
