# Mushroom Yield Predictor
### Zelbytes Agritech Internship — AI Data Analyst (Beginner)
**Intern:** Niranjan P  
**Reference:** ZEL-AGR-00077-2026  
**Duration:** 02 June 2026 – 30 June 2026  
**Phase 1:** Foundation & Data (Days 1–6)

---

## Problem Statement
Predict daily mushroom yield (kg) in a climate-controlled
polyhouse using three sensor readings:
- Temperature (°C)
- Relative Humidity (%)
- CO2 Concentration (ppm)

---

## Project Structure

mushroom-yield-predictor/
├── src/
│   ├── smoke_test.py        # Day 1: Environment verification
│   ├── generate_data.py     # Day 3: Synthetic dataset generator
│   ├── ingest.py            # Day 3: CSV ingestion pipeline
│   ├── clean.py             # Day 4: Data cleaning pipeline
│   ├── stats.py             # Day 5: Descriptive statistics
│   └── eda.py               # Day 6: EDA plots
├── data/
│   ├── raw/
│   │   └── polyhouse_sensors.csv   # 365 days of sensor data
│   ├── interim/
│   │   ├── 01_loaded.parquet       # After ingestion
│   │   └── 02_cleaned.parquet      # After cleaning
│   └── processed/                  # Reserved for modeling
├── notebooks/                      # Jupyter notebooks (Phase 2)
├── reports/
│   ├── figures/
│   │   ├── corr_heatmap.png        # Correlation heatmap
│   │   └── scatter_yield.png       # Scatter plots
│   ├── data_quality.md             # Day 5: Quality report
│   └── eda_notes.md                # Day 6: EDA takeaways
├── docs/
│   └── cleaning_log.md             # Day 4: Cleaning decisions
├── .gitignore
├── requirements.txt
└── README.md

---

## Environment Setup

### Requirements
- Python 3.10+
- Git

### Step 1 — Clone the repo
git clone https://github.com/niranjanprem7777/mushroom-yield-predictor.git
cd mushroom-yield-predictor

### Step 2 — Create virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

### Step 3 — Install dependencies
pip install -r requirements.txt

### Step 4 — Verify setup
python src/smoke_test.py

---

## Dependencies

pandas>=2.0
numpy>=1.24
matplotlib>=3.7
scikit-learn>=1.3
jupyter>=1.0
streamlit>=1.28
joblib>=1.3
pyarrow>=12.0
tabulate>=0.9

---

## Phase 1 — Day by Day Summary

### Day 1 — Python & Virtual Environments
- Verified Python 3.10+ on Windows
- Created project folder and virtual environment
- Installed all core libraries
- Ran smoke_test.py to verify baseline setup
- Documented setup in README

**Script:** src/smoke_test.py

---

### Day 2 — Git, GitHub & Project Structure
- Initialized local Git repository
- Created full folder skeleton with placeholders
- Wrote .gitignore (excludes venv, CSV, pycache)
- Set up requirements.txt with minimum versions
- Created remote repo on GitHub
- Made 3 meaningful commits and pushed to main

**Commits:**
1. chore: initialize mushroom yield forecast project skeleton
2. docs: update README with agritech problem statement
3. chore: verify project structure and folder layout

---

### Day 3 — Agritech Dataset Introduction & CSV Ingestion
- Generated 365-day synthetic polyhouse sensor dataset
- Yield formula: yield_kg = 8 + 0.3×temp + 0.05×humidity
  − 0.002×CO2 + noise
- Built ingest.py to load CSV with correct dtypes
- Parsed timestamp as datetime64
- Saved interim snapshot as 01_loaded.parquet

**Dataset shape:** 365 rows × 5 columns  
**Scripts:** src/generate_data.py, src/ingest.py

| Column        | Type       | Description                  |
|---------------|------------|------------------------------|
| timestamp     | datetime64 | Daily reading date           |
| temperature_c | float64    | Temperature in Celsius       |
| humidity_pct  | float64    | Relative humidity %          |
| co2_ppm       | float64    | CO2 in parts per million     |
| yield_kg      | float64    | Mushroom yield in kilograms  |

---

### Day 4 — Data Cleaning: Missing Values & Duplicates
- Reported missing values per column before any fixes
- Applied validity rules:
  - humidity_pct: 50–100%
  - temperature_c: 10–35°C
  - co2_ppm: 400–2000 ppm
  - yield_kg: not null
- Forward-filled sensor columns for short gaps (max 2)
- Dropped rows with null target (yield_kg never imputed)
- Removed duplicate timestamps (kept last)
- Saved cleaned file as 02_cleaned.parquet
- Documented all decisions in docs/cleaning_log.md

**Final row count:** 365 (dataset was clean — no drops needed)  
**Script:** src/clean.py

---

### Day 5 — Descriptive Statistics & Data Quality Reports
- Computed describe() for all 4 numeric columns
- Added coefficient of variation (cv = std/mean)
- Reported date range and total observation count
- Compared mean vs median to check for skew
- Validated % of rows passing each validity rule
- Exported readable report to reports/data_quality.md

**Key findings:**
- yield_kg mean ≈ median → approximately normal distribution
- humidity clusters tightly in 75–98% (good polyhouse control)
- All columns pass 100% validity rules after cleaning

**Script:** src/stats.py

---

### Day 6 — EDA: Correlation Heatmaps & Scatter Plots
- Plotted correlation heatmap for all 4 features
- Created 3 scatter plots:
  - Humidity (%) vs Yield (kg)
  - Temperature (°C) vs Yield (kg)
  - CO2 (ppm) vs Yield (kg)
- Saved both figures as PNG at 150 DPI
- Wrote 5 biological insight takeaways

**Key findings:**
- temperature_c has strongest positive correlation with yield
- humidity_pct has moderate positive correlation with yield
- co2_ppm has slight negative correlation with yield
- No multicollinearity risk between features
- Linear model should capture temperature effect well

**Script:** src/eda.py

---

## Data Pipeline

Raw CSV → ingest.py → 01_loaded.parquet
                    → clean.py → 02_cleaned.parquet
                               → stats.py → data_quality.md
                               → eda.py   → figures/

---

## Git History Summary

Phase 1 produced the following commits:
1. chore: initialize mushroom yield forecast project skeleton
2. docs: update README with agritech problem statement
3. chore: verify project structure and folder layout
4. feat: add synthetic data generator and CSV ingestion script
5. feat: add data cleaning pipeline with validity rules
6. feat: add descriptive statistics and data quality report
7. feat: add EDA correlation heatmap and scatter plots

---

## Next Phase

Phase 2 — Core Modeling (Days 7–15):
- Day 7:  Train/Test Split & Baseline Model
- Day 8:  Linear Regression
- Day 9:  Ridge & Lasso Regularization
- Day 10: Decision Tree Regressor
- Day 11: Random Forest Regressor
- Day 12: Feature Engineering
- Day 13: Cross Validation
- Day 14: Hyperparameter Tuning
- Day 15: Model Evaluation & Selection

---

## Contact

**Intern:** Niranjan P  
**Email:** niranjanprem2005@gmail.com  
**Company:** Zelbytes Private Limited  
**Portal:** zelbytes.com/portal  
**GitHub:** github.com/niranjanprem7777/mushroom-yield-predictor
