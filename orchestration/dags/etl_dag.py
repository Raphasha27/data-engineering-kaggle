"""
Airflow DAG for orchestrating ETL pipelines.

Install: pip install apache-airflow
Deploy: Copy to $AIRFLOW_HOME/dags/
"""

from datetime import datetime, timedelta
from pathlib import Path
import os
import sys

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

try:
    from airflow import DAG
    from airflow.operators.python import PythonOperator
    from airflow.operators.bash import BashOperator

    HAS_AIRFLOW = True
except ImportError:
    HAS_AIRFLOW = False

if HAS_AIRFLOW:
    default_args = {
        "owner": "Raphasha27",
        "depends_on_past": False,
        "email_on_failure": True,
        "email_on_retry": False,
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    }

    dag = DAG(
        dag_id="data_engineering_pipeline",
        default_args=default_args,
        description="Enterprise ETL pipeline orchestration",
        schedule="0 6 * * *",
        start_date=datetime(2024, 1, 1),
        catchup=False,
        tags=["etl", "data-engineering"],
    )

    BASE_DIR = Path(__file__).parent.parent.parent
    CONFIG_DIR = BASE_DIR / "configs"

    def run_etl_pipeline(config_name: str):
        from etl_pipeline.etl_pipeline import ETLPipeline
        import json

        config_path = CONFIG_DIR / config_name
        with open(config_path) as f:
            config = json.load(f)
        pipeline = ETLPipeline(config=config)
        return pipeline.run()

    def run_api_pipeline(config_name: str):
        from api_pipeline.api_pipeline import APIDataPipeline
        import json

        config_path = CONFIG_DIR / config_name
        with open(config_path) as f:
            config = json.load(f)
        pipeline = APIDataPipeline(config=config)
        return pipeline.run()

    def run_data_quality_check():
        import pandas as pd
        from src.data_quality import DataQualityChecker

        output_files = list((BASE_DIR / "data").glob("*.parquet"))
        results = []
        for f in output_files:
            df = pd.read_parquet(f)
            dq = DataQualityChecker(df)
            report = dq.run()
            results.append({"file": str(f), "score": report["quality_score"]})
        print(f"Quality checks completed: {results}")
        return results

    extract_task = PythonOperator(
        task_id="extract_api_data",
        python_callable=run_api_pipeline,
        op_kwargs={"config_name": "api_pipeline.json"},
        dag=dag,
    )

    transform_task = PythonOperator(
        task_id="run_etl_pipeline",
        python_callable=run_etl_pipeline,
        op_kwargs={"config_name": "etl_pipeline.json"},
        dag=dag,
    )

    quality_task = PythonOperator(
        task_id="data_quality_check",
        python_callable=run_data_quality_check,
        dag=dag,
    )

    notebook_task = BashOperator(
        task_id="run_titanic_notebook",
        bash_command=f"cd {BASE_DIR} && jupyter nbconvert --to notebook --execute titanic-ml/titanic_kaggle_v7.ipynb --output titanic-ml/titanic_kaggle_v7_executed.ipynb",
        dag=dag,
    )

    extract_task >> transform_task >> quality_task
    quality_task >> notebook_task
