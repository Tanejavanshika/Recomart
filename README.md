# Recomart

## Project Structure

```
Recomart/
│
├── data/
│   ├── raw/              # Raw ingested data
│   ├── validated/        # Validated data
│   ├── processed/        # Cleaned and processed data
│   └── features/         # Engineered features
│
├── ingestion/
│   └── ingest_data.py    # Data ingestion module
│
├── validation/
│   └── validate_data.py  # Data validation module
│
├── preparation/
│   └── clean_eda.ipynb   # Data cleaning and EDA notebook
│
├── transformation/
│   └── feature_engineering.py  # Feature engineering module
│
├── feature_store/
│   └── feature_registry.py  # Feature store registry
│
├── model/
│   ├── train_model.py     # Model training
│   └── evaluate_model.py  # Model evaluation
│
├── orchestration/
│   └── pipeline_dag.py    # Pipeline orchestration DAG
│
├── versioning/
│   └── dvc.yaml           # DVC pipeline configuration
│
├── logs/                  # Log files
│
├── report.pdf             # Project report
│
└── README.md              # Project documentation
```

## Overview

Recomart is a machine learning project with a structured pipeline for data processing, feature engineering, and model training.

## Getting Started

1. Install dependencies
2. Run data ingestion: `python ingestion/ingest_data.py`
3. Validate data: `python validation/validate_data.py`
4. Execute pipeline: `dvc repro` (if using DVC)