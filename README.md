# HR Analytics & Employee Retention Insights

This project focuses on analyzing key Human Resources metrics to better understand employee demographics, performance, satisfaction, and attrition behavior. By uncovering workforce patterns and risk areas, the analysis supports data-driven decision-making that improves employee retention, increases engagement, and strengthens organizational effectiveness.
Understanding workforce behavior is essential for reducing turnover, improving employee experience, and enabling strategic HR planning.

This project analyzes HR data to uncover actionable insights related to:

* Employee demographics
* Performance trends
* Job satisfaction
* Training utilization
* Attrition (retention risk)

The final outcome includes:
* Interactive HR Dashboard (Power BI)  
* Predictive Modeling (Attrition Prediction)  
* Written Report with Insights & Recommendations  

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
│   └── clean/         # Cleaned and merged datasets
│
├── scripts/
│   ├── data_cleaning_functions.py
│   └── kpi_functions.py
│
├── notebooks/
│   ├── 01_Data_Cleaning.ipynb
│   └── 02_KPI_Analysis.ipynb
│
├── README.md
└── requirements.txt
```
## Phase 1 Complete: Data Cleaning & Preprocessing

* Loaded raw CSV files using pandas
* Cleaned column names (standardized lowercase, underscores)
* Handled missing values
* Converted datatypes (hiredate, reviewdate → datetime)
* Removed duplicates
* Created a master merged dataset (bigDF.csv)
* Exported cleaned files into data/clean/

### Tools Used:

- Python (Pandas, NumPy)
- VS Code + Jupyter Notebook
- Virtual Environment (.venv)

## Phase 2 In Progress: KPI Development

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