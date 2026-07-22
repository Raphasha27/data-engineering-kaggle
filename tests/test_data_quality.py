import pytest
import pandas as pd
import numpy as np

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.data_quality import DataQualityChecker


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4, 5],
            "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
            "age": [25, 30, None, 35, 40],
            "salary": [50000, 60000, 70000, None, 90000],
            "department": ["ENG", "ENG", "FIN", "FIN", "ENG"],
            "email": ["a@x.com", "b@x.com", "c@x.com", "d@x.com", None],
        }
    )


class TestDataQualityChecker:
    def test_completeness(self, sample_df):
        dq = DataQualityChecker(sample_df)
        report = dq.run()
        assert report["completeness"]["age"] < 1.0
        assert report["completeness"]["id"] == 1.0

    def test_uniqueness(self, sample_df):
        dq = DataQualityChecker(sample_df)
        report = dq.run()
        assert report["uniqueness"]["id"] == 1.0

    def test_detect_duplicates(self, sample_df):
        df_dup = pd.concat([sample_df, sample_df.iloc[[0]]], ignore_index=True)
        dq = DataQualityChecker(df_dup)
        report = dq.run()
        assert report["duplicate_rows"] == 1

    def test_outliers_iqr(self, sample_df):
        df = sample_df.copy()
        df.loc[0, "salary"] = 9999999
        dq = DataQualityChecker(df)
        report = dq.run()
        assert report["outliers"]["salary"] > 0

    def test_empty_dataframe(self):
        dq = DataQualityChecker(pd.DataFrame())
        report = dq.run()
        assert report["status"] == "empty"

    def test_dtypes_detected(self, sample_df):
        dq = DataQualityChecker(sample_df)
        report = dq.run()
        assert "id" in report["dtypes"]
        assert "name" in report["dtypes"]
