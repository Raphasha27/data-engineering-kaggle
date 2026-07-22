import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import os

import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from etl_pipeline.etl_pipeline import ETLPipeline


@pytest.fixture
def sample_csv():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("id,name,amount,date\n")
        f.write("1,Alice,100.50,2024-01-01\n")
        f.write("2,Bob,200.75,2024-01-02\n")
        f.write("3,Charlie,,2024-01-03\n")
        f.write("1,Alice,100.50,2024-01-01\n")
        fname = f.name
    yield fname
    os.unlink(fname)


@pytest.fixture
def pipeline():
    return ETLPipeline(config={"batch_size": 100})


class TestETLPipeline:
    def test_extract_csv(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        assert len(df) == 4
        assert list(df.columns) == ["id", "name", "amount", "date"]

    def test_extract_missing_file(self, pipeline):
        with pytest.raises(FileNotFoundError):
            pipeline.extract("nonexistent.csv")

    def test_profile(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        profile = pipeline.profile(df)
        assert profile["rows"] == 4
        assert profile["columns"] == 4
        assert "id" in profile["dtypes"]

    def test_deduplicate(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        before = len(df)
        df = pipeline.clean(df)
        assert len(df) < before
        assert pipeline.stats["duplicates"] == 1

    def test_clean_fills_nulls(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        df = pipeline.clean(df)
        assert df["amount"].isnull().sum() == 0
        assert pipeline.stats["null_filled"] == 1

    def test_transform_adds_etl_columns(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        df = pipeline.clean(df)
        df = pipeline.transform(df)
        assert "_etl_loaded_at" in df.columns
        assert "_etl_batch_id" in df.columns
        assert "_etl_hash" in df.columns

    def test_validate_schema_strict_mode(self, pipeline, sample_csv):
        df = pipeline.extract(sample_csv)
        pipeline.strict_mode = True
        schema = {"missing_col": {"nullable": False}}
        with pytest.raises(ValueError, match="Missing column"):
            pipeline.validate_schema(df, schema)

    def test_report_output(self, pipeline, sample_csv, capsys):
        df = pipeline.extract(sample_csv)
        df = pipeline.clean(df)
        pipeline.stats["start_time"] = 0
        pipeline.stats["end_time"] = 1
        pipeline.report()
        captured = capsys.readouterr()
        assert "ROWS IN" in captured.out or "Rows in" in captured.out
