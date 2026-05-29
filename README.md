# Data Engineering & Kaggle Portfolio

[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)]
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)]
[![PySpark](https://img.shields.io/badge/PySpark-E25A1C?style=for-the-badge&logo=apache-spark&logoColor=white)]
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)]
[![Kaggle](https://img.shields.io/badge/Kaggle-Competition-20BEFF?style=for-the-badge&logo=kaggle)](https://www.kaggle.com/Raphasha27)

Portfolio of data engineering projects and Kaggle competition solutions by [Raphasha27](https://kaggle.com/Raphasha27).

## Projects

| Project | Description | Tech Stack | Status |
|---------|-------------|------------|--------|
| `etl-pipeline/` | Production ETL: CSV → PostgreSQL with validation, dedup, null imputation, audit logging | pandas, SQLAlchemy, psycopg2 | ✅ Complete |
| `spark-etl/` | Distributed PySpark ETL with multi-format support (CSV/Parquet/JSON/Avro), schema validation, partition pruning, broadcast joins | PySpark, HDFS, Parquet | ✅ Complete |
| `titanic-ml/` | End-to-end ML solution for Kaggle Titanic competition. EDA, 17 features, 5 models, weighted ensemble | pandas, scikit-learn, XGBoost | ✅ v2 (83.2% acc) |

## Titanic Competition Results

| Version | CV Accuracy | Val Accuracy | Models | Features |
|---------|:-----------:|:------------:|--------|:--------:|
| v1 | 82.6% | 81.0% | RF, GB, LR (soft vote) | 14 |
| v2 | 83.1% | 83.2% | Weighted ensemble (RF, GB, XGB, LR, SVC) | 17 |

> **Next up:** Tabular Playground Series, hyperparameter optimization for 85%+

## Skills Demonstrated

- **Data Processing**: pandas, PySpark, SQL, data cleaning, validation
- **ML Pipeline**: scikit-learn, XGBoost, feature engineering, ensemble methods
- **Production ETL**: PostgreSQL, audit logging, error handling, pipeline reporting
- **Big Data**: PySpark, distributed processing, partition pruning, broadcast joins

## Author

**Koketso Raphasha** — [Kaggle](https://kaggle.com/Raphasha27) | [GitHub](https://github.com/Raphasha27) | [Portfolio](https://github.com/Raphasha27)
