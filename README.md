# Raphasha27 - Enterprise-Grade Data Engineering & AI Pipeline

[![CI](https://github.com/Raphasha27/data-engineering-kaggle/actions/workflows/ci.yml/badge.svg)](https://github.com/Raphasha27/data-engineering-kaggle/actions)
[![CodeQL](https://github.com/Raphasha27/data-engineering-kaggle/actions/workflows/security-scan.yml/badge.svg)](https://github.com/Raphasha27/data-engineering-kaggle/actions)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue)](https://github.com/Raphasha27/data-engineering-kaggle)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Gumroad](https://img.shields.io/badge/ETL_Pipeline_Suite-$45-FF90E8?logo=gumroad&style=flat)](https://raphashakoketso.gumroad.com/l/etl-pipeline-suite)
[![Gumroad](https://img.shields.io/badge/AI_Agent_Framework-FREE-FF90E8?logo=gumroad&style=flat)](https://raphashakoketso.gumroad.com/l/ai-agent-blueprint)

Comprehensive data engineering projects, production ETL pipelines, and Kaggle competition solutions. Part of the Kirov Dynamics sovereign infrastructure ecosystem.

## Projects

### ETL Pipelines
| Project | Tech | Description |
|---------|------|-------------|
| [etl-pipeline](etl-pipeline) | Python, PostgreSQL | CSV to PostgreSQL ETL with validation |
| [spark-etl](spark-etl) | PySpark | Distributed big data processing pipeline |
| [api-pipeline](api-pipeline) | Python, REST | Public API data extraction with pagination |

### Kaggle Competitions
| Project | Score | Model |
|---------|-------|-------|
| [titanic-ml](titanic-ml) | 78.5% | Ensemble (RF, GB, XGB) |
| [house-prices](house-prices) | - | Ridge/Lasso/GB |
| [spaceship-titanic](spaceship-titanic) | - | KNN + Ensemble |
| [f1-pit-stops](f1-pit-stops) | - | ROC AUC Ensemble |

## Getting Started
```bash
git clone https://github.com/Raphasha27/data-engineering-kaggle.git
cd data-engineering-kaggle
pip install -e ".[dev]"
```

### Docker
```bash
docker compose up
```
Starts PostgreSQL + runs the ETL pipeline. Jupyter available at `http://localhost:8888`.

### Tests
```bash
pytest tests/ -v --cov=src
```

## Project Structure
```
├── etl-pipeline/          # CSV → PostgreSQL ETL
├── spark-etl/             # Distributed PySpark pipeline
├── api-pipeline/          # REST API extraction pipeline
├── titanic-ml/            # Kaggle Titanic (v2-v7, 78.5%)
├── data-quality/          # Data quality monitoring
├── house-prices/          # House Prices competition
├── spaceship-titanic/     # Spaceship Titanic competition
├── f1-pit-stops/          # F1 Pit Stops analysis
├── orchestration/         # Airflow DAGs
├── configs/               # Pipeline config examples
├── tests/                 # Unit tests
├── Dockerfile / docker-compose.yml
└── pyproject.toml
```

## Infrastructure
- **CI/CD**: GitHub Actions (lint, test, notebook validation, Docker build)
- **Security**: CodeQL, Dependabot, secret scanning, safety check
- **Quality**: Ruff linting, pytest, pre-commit hooks

## License
MIT
