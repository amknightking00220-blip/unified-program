import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.title("Employee Engagement & Burnout Dashboard")

file = st.file_uploader("Upload CSV", type=["csv"])

if file:
    df = pd.read_csv(file)

    # Clean column names
    df.columns = df.columns.str.strip().str.replace(" ", "")

    # ---- CREATE ENGAGEMENT ----
    df["Engagement"] = (
        df["JobSatisfaction"] +
        df["EnvironmentSatisfaction"] +
        df["WorkLifeBalance"] +
        df["JobInvolvement"]
    ) / 4

    # ---- SIDEBAR ----
    st.sidebar.header("Filters")

    dept = st.sidebar.selectbox("Department", df["Department"].unique())
    threshold = st.sidebar.slider("Engagement Threshold", 1.0, 5.0, 3.0)
    overtime_filter = st.sidebar.checkbox("Only Overtime Employees")

    filtered_df = df[df["Department"] == dept].copy()

    if overtime_filter:
        filtered_df = filtered_df[filtered_df["OverTime"] == "Yes"]

    # ---- KPI ----
    st.subheader("Engagement Overview")
    st.metric("Average Engagement", round(filtered_df["Engagement"].mean(), 2))

    # ---- DISTRIBUTION ----
    st.subheader("Engagement Distribution")
    st.bar_chart(filtered_df["Engagement"].value_counts())

    # ---- BURNOUT LOGIC ----
    filtered_df["Burnout_Risk"] = (
        (filtered_df["Engagement"] < threshold) &
        (filtered_df["OverTime"] == "Yes")
    )

    st.subheader("Burnout Risk")
    st.bar_chart(filtered_df["Burnout_Risk"].value_counts())

    # ---- ROLE ANALYSIS ----
    st.subheader("Engagement by Job Role")
    st.bar_chart(filtered_df.groupby("JobRole")["Engagement"].mean())

    # ---- TENURE ----
    st.subheader("Tenure vs Engagement")
    st.line_chart(filtered_df.groupby("YearsAtCompany")["Engagement"].mean())

    # ---- ACTION PANEL ----
    st.subheader("High Risk Employees")
    st.dataframe(filtered_df[filtered_df["Engagement"] < threshold])

else:
    st.warning("Upload your dataset to begin")