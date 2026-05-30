# Data Engineering & Kaggle

[![Python](https://img.shields.io/badge/Python-3.10+-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)]
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169e1?style=for-the-badge&logo=postgresql&logoColor=white)]
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)]
[![Kaggle](https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=kaggle)](https://kaggle.com/Raphasha27)

Collection of data engineering projects (ETL pipelines, API extraction, Spark processing) and Kaggle competition notebooks.

## Data Engineering Pipelines

| Project | Description | Tech Stack |
|---------|-------------|------------|
| [`etl-pipeline/`](etl-pipeline/) | CSV to PostgreSQL ETL with dialect detection, batch processing, data profiling, schema evolution | pandas, SQLAlchemy, psycopg2, config |
| [`spark-etl/`](spark-etl/) | Distributed PySpark ETL with AQE optimization, Delta Lake/ORC/Avro, streaming, checkpointing | PySpark, Delta Lake, Parquet, ORC |
| [`api-pipeline/`](api-pipeline/) | REST API data extraction with pagination, rate limiting, auth, transform, load | requests, pandas, SQLAlchemy |

## Kaggle Competition Notebooks

All notebooks are published as Kaggle kernels ready to run with data on the Kaggle platform.

| Notebook | Competition | Metric | Approach |
|----------|-------------|--------|----------|
| [`titanic-ml/titanic_kaggle.ipynb`](titanic-ml/titanic_kaggle.ipynb) | [Titanic](https://www.kaggle.com/c/titanic) | Accuracy | KNN impute + family survival LOO + GB/XGB ensemble → **78.5%** |
| [`house-prices/house_prices_kaggle.ipynb`](house-prices/house_prices_kaggle.ipynb) | [House Prices](https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques) | RMSLE | Ridge/Lasso/ElasticNet/GB/XGB, log transform, 70+ features |
| [`spaceship-titanic/spaceship_titanic_kaggle.ipynb`](spaceship-titanic/spaceship_titanic_kaggle.ipynb) | [Spaceship Titanic](https://www.kaggle.com/competitions/spaceship-titanic) | Accuracy | Cabin parsing, KNN impute, RF/GB/XGB voting ensemble |
| [`f1-pit-stops/f1_pit_stops_kaggle.ipynb`](f1-pit-stops/f1_pit_stops_kaggle.ipynb) | [F1 Pit Stops](https://www.kaggle.com/competitions/playground-series-s6e5) | ROC AUC | Label encoding, GB/RF/XGB ensemble (Playground S6E5) |

## Getting Started

To run locally:
```bash
pip install -r titanic-ml/requirements.txt
python titanic-ml/titanic_kaggle_v6.py   # Best Titanic submission (78.5%)
```

Each pipeline has its own README with setup and usage instructions.

## Author

**Koketso Raphasha** — [Kaggle](https://kaggle.com/Raphasha27) | [GitHub](https://github.com/Raphasha27) | [Portfolio](https://portfolio-iota-eight-90.vercel.app/)
