# multiple_dashboard_fixed.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# -------------------------
# Load Data
# -------------------------
DATA_PATH = r"C:\Users\vijay\OneDrive\Desktop\lally\BMI\merged_patient_data_normalized.csv"
df = pd.read_csv(DATA_PATH)

# Clean data
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Utility function to safely access columns
def get_column(df, possible_names, default=None):
    for name in possible_names:
        if name in df.columns:
            return df[name]
    return pd.Series([default]*len(df))

# -------------------------
# Sidebar - Navigation
# -------------------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", [
    "Home",
    "Medication Adherence and Prescription Trends Dashboard",
    "Prescription Insights: Adherence, Cost, and Safety",
    "Drug Utilization and Patient Adherence Overview",
    "Pharmacy Performance & Patient Compliance Report",
    "Prescription Analytics: Cost, Adherence & Outcomes"
])

# Safe column mapping
prescription_col = get_column(df, ["Prescription_ID", "Prescription Id", "Rx_ID"])
patient_col = get_column(df, ["Patient_ID", "Patient Id", "PatientID"])
adherence_col = get_column(df, ["Adherence_Percent", "Adherence %"], default=0)
drug_col = get_column(df, ["Drug_Name", "Drug Name"], default="Unknown Drug")
drug_cat_col = get_column(df, ["Drug_Category", "Category"], default="Unknown Category")
cost_col = get_column(df, ["Cost_USD", "Cost"], default=0)
doctor_col = get_column(df, ["Prescribing_Doctor", "Doctor_Name", "Doctor"], default="Unknown Doctor")
adverse_col = get_column(df, ["Adverse_Event_Reported", "Adverse Event"], default="No")

# -------------------------
# Home Page
# -------------------------
if page == "Home":
    st.title("🏥 Healthcare Dashboard Project")
    st.markdown("""
    **Project Overview:**  
    Multi-page dashboard to analyze patient prescription trends, adherence, cost, and pharmacy performance.  

    **Presenter:** Sriya Prathi  
    **Roll Number:** [Enter Your Roll Number]  
    **Date:** [Enter Date]  
    **Course:** [Enter Course Name]  
    """)
    st.markdown("### Dataset Overview")
    st.write(df.head())
    st.markdown("### Key Metrics")
    st.metric("Total Patients", patient_col.nunique())
    st.metric("Total Prescriptions", prescription_col.nunique())
    st.metric("Average Adherence (%)", round(adherence_col.mean(),2))
    st.metric("Total Cost (USD)", round(cost_col.sum(),2))

# -------------------------
# Page 1 - Medication Adherence
# -------------------------
elif page == "Medication Adherence and Prescription Trends Dashboard":
    st.title("💊 Medication Adherence & Prescription Trends")
    col1, col2, col3 = st.columns(3)
    col1.metric("Average Adherence (%)", round(adherence_col.mean(),2))
    col2.metric("Max Adherence (%)", round(adherence_col.max(),2))
    col3.metric("Min Adherence (%)", round(adherence_col.min(),2))

    st.subheader("Top 10 Drugs by Adherence")
    top_drugs = df.groupby(drug_col)[adherence_col.name].mean().sort_values(ascending=False).head(10)
    fig = px.bar(top_drugs, x=top_drugs.index, y=top_drugs.values, color=top_drugs.values)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Adherence Distribution")
    fig2 = px.histogram(adherence_col, nbins=20, color_discrete_sequence=['#EF553B'])
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Page 2 - Prescription Insights
# -------------------------
elif page == "Prescription Insights: Adherence, Cost, and Safety":
    st.title("📈 Prescription Insights: Adherence, Cost & Safety")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total Prescriptions", prescription_col.nunique())
    col2.metric("Total Cost USD", round(cost_col.sum(),2))
    col3.metric("Average Adherence", round(adherence_col.mean(),2))

    st.subheader("Cost vs Adherence")
    fig = px.scatter(df, x=cost_col, y=adherence_col, color=drug_cat_col, hover_data=[drug_col, patient_col])
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Adverse Events Reported")
    adverse_count = adverse_col.value_counts()
    fig2 = px.pie(values=adverse_count.values, names=adverse_count.index,
                  color_discrete_sequence=px.colors.sequential.RdBu)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Page 3 - Drug Utilization & Patient Adherence
# -------------------------
elif page == "Drug Utilization and Patient Adherence Overview":
    st.title("💊 Drug Utilization & Patient Adherence Overview")

    st.subheader("Top 10 Prescribed Drugs")
    drug_counts = df[drug_col.name].value_counts().head(10)
    fig = px.bar(drug_counts, x=drug_counts.index, y=drug_counts.values, color=drug_counts.values)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Average Adherence by Drug Category")
    adherence_cat = df.groupby(drug_cat_col)[adherence_col.name].mean()
    fig2 = px.bar(adherence_cat, x=adherence_cat.index, y=adherence_cat.values, color=adherence_cat.values)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Page 4 - Pharmacy Performance
# -------------------------
elif page == "Pharmacy Performance & Patient Compliance Report":
    st.title("🏥 Pharmacy Performance & Patient Compliance Report")
    col1, col2, col3 = st.columns(3)
    col1.metric("Avg Adherence", round(adherence_col.mean(),2))
    col2.metric("Total Prescriptions", prescription_col.nunique())
    col3.metric("Total Patients", patient_col.nunique())

    # Removed "Prescriptions per Doctor"

    st.subheader("Patient Compliance Distribution")
    compliance = pd.cut(adherence_col, bins=[0,50,80,100], labels=["Low","Medium","High"])
    fig2 = px.pie(compliance.value_counts(),
                  values=compliance.value_counts().values,
                  names=compliance.value_counts().index)
    st.plotly_chart(fig2, use_container_width=True)

# -------------------------
# Page 5 - Prescription Analytics
# -------------------------
elif page == "Prescription Analytics: Cost, Adherence & Outcomes":
    st.title("📊 Prescription Analytics: Cost, Adherence & Outcomes")

    st.subheader("Cost by Drug Category")
    cost_cat = df.groupby(drug_cat_col)[cost_col.name].sum()
    fig = px.bar(cost_cat, x=cost_cat.index, y=cost_cat.values, color=cost_cat.values)
    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Adherence vs Cost per Patient")
    patient_summary = df.groupby(patient_col).agg({adherence_col.name:'mean', cost_col.name:'sum'}).reset_index()
    fig2 = px.scatter(patient_summary, x=cost_col.name, y=adherence_col.name, hover_data=[patient_col])
    st.plotly_chart(fig2, use_container_width=True)

    st.subheader("Patient Summary Table")
    st.dataframe(patient_summary.head(20))
