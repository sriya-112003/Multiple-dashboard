I've updated the `README.md` to include a clear project structure section, while keeping the entire content on a single page.

````markdown
# 💊 Healthcare Prescription and Patient Analytics Dashboard

A multi-page interactive dashboard built with **Streamlit** and **Plotly** for analyzing patient prescription data, medication adherence, cost trends, and drug safety in the healthcare sector.

**Presenter:** Sriya Prathi
**Roll Number:** [Enter Your Roll Number]
**Date:** [Enter Date]
**Course:** [Enter Course Name]

## 🎯 Project Goal

The primary objective is to provide healthcare administrators and pharmacovigilance teams with a unified analytical tool to monitor key performance indicators (KPIs) related to drug utilization and patient compliance. This dashboard facilitates:
* Identifying drugs with low adherence for targeted patient interventions.
* Analyzing the relationship between prescription cost and adherence rates.
* Monitoring the distribution of adverse event reports for safety signals.

---

## 🚀 Getting Started

### Prerequisites
Requires **Python 3.7+**.

### Installation
1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/your-username/your-repository-name.git](https://github.com/your-username/your-repository-name.git)
    cd your-repository-name
    ```
2.  **Install Dependencies:**
    ```bash
    pip install streamlit pandas numpy plotly
    ```

### Data Setup & Execution
1.  **Data File:** Ensure your data file (`merged_patient_data_normalized.csv`) is accessible and the `DATA_PATH` variable in `multiple_dashboard.py` is updated to the correct location.
2.  **Run the App:**
    ```bash
    streamlit run multiple_dashboard.py
    ```
    The application will automatically launch in your web browser.

---

## 📁 Project Structure

The repository is organized simply, focusing on the core application and data file.

````

.
├── multiple\_dashboard.py  \# The main Streamlit application file
├── merged\_patient\_data\_normalized.csv \# Placeholder for the dataset
├── README.md              \# This file
└── requirements.txt       \# (Optional) List of dependencies

```

---

## 📊 Dashboard Pages & Key Analytics

The application features a sidebar for navigation across several key reports:

| Dashboard Name | Key Metrics & Focus | Primary Visualizations |
| :--- | :--- | :--- |
| **Home** | Overview of dataset size and overall health metrics. | Total Patients, Total Prescriptions, Average Adherence (%). |
| **Medication Adherence and Prescription Trends Dashboard** | Focus on patient compliance and drug-specific performance. | Bar Chart: Top 10 Drugs by Adherence. Histogram: Adherence Distribution. |
| **Prescription Insights: Adherence, Cost, and Safety** | Core analysis of cost, adherence, and adverse events (ADR). | Scatter Plot: Cost vs. Adherence (colored by Drug Category). Pie Chart: Adverse Events Reported. |
| **Drug Utilization and Patient Adherence Overview** | Analysis of the most frequently prescribed medications. | Bar Chart: Top 10 Prescribed Drugs (Count). Bar Chart: Average Adherence by Drug Category. |
| **Prescription Analytics: Cost, Adherence & Outcomes** | Patient-level and categorical cost-outcome analysis. | Bar Chart: Total Cost by Drug Category. Scatter Plot: Adherence vs. Cost per Patient. |

---

## ⚙️ Technology Stack & Data Mapping

### Technology Used
* **App Framework:** Streamlit
* **Visualization:** Plotly Express
* **Data Science:** Pandas, NumPy

### Key Data Fields (Safe Column Mapping)
The code is designed to safely map common variations of column names:

| Internal Variable | Example Column Names | Data Focus |
| :--- | :--- | :--- |
| `patient_col` | `Patient_ID`, `Patient Id` | Patient Identifier |
| `adherence_col` | `Adherence_Percent`, `Adherence %` | Compliance Rate (0-100) |
| `drug_col` | `Drug_Name`, `Drug Name` | Medication Identity |
| `cost_col` | `Cost_USD`, `Cost` | Financial Metric |
| `adverse_col` | `Adverse_Event_Reported`, `Adverse Event` | Safety Outcome (Yes/No) |
```
