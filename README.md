# Raphasha27 - Enterprise-Grade Data Engineering & AI Pipeline

[![CI](https://github.com/Raphasha27/data-engineering-kaggle/actions/workflows/ci.yml/badge.svg)](https://github.com/Raphasha27/data-engineering-kaggle/actions)
[![CodeQL](https://github.com/Raphasha27/data-engineering-kaggle/actions/workflows/security-scan.yml/badge.svg)](https://github.com/Raphasha27/data-engineering-kaggle/actions)
[![Dependabot](https://img.shields.io/badge/Dependabot-enabled-blue)](https://github.com/Raphasha27/data-engineering-kaggle)
[![Python 3.12](https://img.shields.io/badge/python-3.12-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

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
pip install -r requirements-dev.txt
```

## Infrastructure
- **CI/CD**: GitHub Actions (lint, test, auto-deploy)
- **Security**: CodeQL, Dependabot, secret scanning
- **Quality**: Ruff linting, pre-commit hooks

## License
MIT
