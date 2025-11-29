# HR Predictive Retention & Performance Insights

This project develops an advanced HR Analytics solution, transforming raw employee data into a comprehensive Star Schema to power an interactive dashboard and a Machine Learning model for predicting employee attrition risk. The goal is to provide HR leadership with actionable, forward-looking insights to improve employee retention, optimize performance management, and guide strategic organizational planning.

Understanding workforce behavior is essential for reducing turnover, improving employee experience, and enabling strategic HR planning.

This project analyzes HR data to uncover actionable insights related to:

* Employee demographics
* Performance trends
* Job satisfaction
* Training utilization
* Attrition (retention risk)


## Project Outcomes & Key Insights
This project delivers both historical analytical capabilities and future-facing predictions:
- Interactive HR Dashboard (Power BI): A multi-page visualization that tracks performance, satisfaction, operational efficiency, and highlights risk areas.
- Predictive Model: A highly accurate Random Forest Classifier trained to calculate an Attrition Risk Score for every active employee.
- Written Report: Final document detailing methodology, key findings (e.g., high-risk tenure groups), and strategic recommendations.
---

## Dataset Overview
The project uses 5 CSV tables:

| File | Description | Rows |
|------|-------------|------|
| Employee.csv | Employee demographics & job info | 1470 |
| EducationLevel.csv | Education category mapping | 5 |
| PerformanceRating.csv | Historical performance reviews | 6709 |
| RatingLevel.csv | Performance level descriptions | 5 |
| SatisfiedLevel.csv | Satisfaction scale mapping | 5 |

---

## Project Architecture

```bash
HR_Data_Analysis_Project/
│
├── data/
│   ├── raw/           # Original untouched datasets
│   └── clean/         # Cleaned, Modeled & Final Export files for Power BI
│       ├── employee_master.csv        
│       ├── performance_fact.csv       
│       ├── ml_data_for_prediction.csv 
│       └── employee_predictions.csv   
│
├── scripts/
│   ├── data_cleaning_functions.py
│   ├── data_modeling.py               # (New Script for Star Schema Creation)
│   └── model_training.py              # (New Script for ML Workflow)
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_KPI_Analysis.ipynb
│
├── models/            # Saved Machine Learning Model
│   └── random_forest_model.pkl
│
├── report/            # Saved Machine Learning Model
│   └── HR Analytics: Workforce Performance, Risk Assessment, and Strategic Recommendations.docx
│
├── README.md
└── requirements.txt
```
## Project Phases & Key Accomplishments

### Phase 1: Data Cleaning & Star Schema Modeling

* **ETL:** Loaded, cleaned, standardized, and merged raw data.
* **Modeling:** Created the **Star Schema** architecture:
    - **Dimension Table:** `employee_master.csv` (One row per employee).
    - **Fact Table:** `performance_fact.csv` (Multiple time-series rows per employee).
* **Feature Engineering (Advanced):** Added crucial time-series features to the Fact Table:
    - `previous_manager_rating:` Lagging feature to track performance trend.
    - `days_since_last_review:` Operational metric measuring management review cadence.


* Handled missing values
* Converted datatypes (hiredate, reviewdate → datetime)
* Removed duplicates
* Created a master merged dataset (bigDF.csv)
* Exported cleaned files into data/clean/

## Phase 2: KPI Development

### Employee Demographics KPIs:
|KPI|Dataset Used|
|---|------------|
|Gender Distribution | employeeDF|
|Age Distribution | employeeDF|
|Education Level Distribution | bigDF|
|Department Distribution | employeeDF|
|Tenure Statistics | employeeDF|


### Performance & Satisfaction KPIs:
|KPI|Dataset Used|
|---|------------|
|Average Performance Rating (Self + Manager) | bigDF|
|Self vs Manager Rating Alignment (Latest Review Only)|bigDF (using reviewdate)|
|Satisfaction & Engagement (Environment, Job, Relationship) |	bigDF|
|Training Utilization Rate | bigDF|
|Work-Life Balance Score|bigDF|


### Attrition KPIs:
|KPI|Dataset Used|
|---|------------|
|Attrition Rate | employeeDF|
|Attrition by Department | employeeDF|


## Project Phases:
- [x] Phase 1	Data Cleaning & Merging
- [x] Phase 2	KPI Development & Analysis
- [ ] Phase 3	Data Visualization & Dashboard
- [ ] Phase 4	Machine Learning Model (Attrition Prediction)
- [ ] Phase 5	Final Report & Presentation



### Tools & Libraries Used:

- Python (Pandas, NumPy)
- Machine Learning: Scikit-learn, Joblib
- Development: VS Code, Virtual Environment (.venv)
- Visualization: Power BI


## How to Run the Project
```bash
# Create a virtual environment
python -m venv .venv

# Activate environment
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Launch Jupyter
jupyter notebook
```