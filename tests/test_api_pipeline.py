import pytest
import pandas as pd
import numpy as np
from pathlib import Path
import tempfile
import os
import json

import sys

sys.path.insert(0, str(Path(__file__).parent.parent))

from api_pipeline.api_pipeline import APIDataPipeline


@pytest.fixture
def sample_json():
    data = [
        {"id": 1, "name": "Alice", "score": 95.5},
        {"id": 2, "name": "Bob", "score": 87.0},
        {"id": 3, "name": "Charlie", "score": None},
        {"id": 1, "name": "Alice", "score": 95.5},
    ]
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(data, f)
        fname = f.name
    yield fname
    os.unlink(fname)


@pytest.fixture
def pipeline():
    return APIDataPipeline(config={"rate_limit": 0})


class TestAPIDataPipeline:
    def test_extract_from_file_json(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        assert len(df) == 4
        assert list(df.columns) == ["id", "name", "score"]

    def test_clean_deduplicates(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        df = pipeline.clean(df)
        assert len(df) == 3
        assert pipeline.stats["duplicates_removed"] == 1

    def test_clean_fills_nulls(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        df = pipeline.clean(df)
        assert df["score"].isnull().sum() == 0

    def test_transform_adds_metadata(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        df = pipeline.transform(df)
        assert "_pipeline_loaded_at" in df.columns
        assert "_pipeline_batch" in df.columns

    def test_load_csv(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        df = pipeline.clean(df)
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as f:
            out = f.name
        try:
            pipeline.load(df, out)
            loaded = pd.read_csv(out)
            assert len(loaded) == 3
        finally:
            os.unlink(out)

    def test_validate_schema(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        schema = {"id": {"dtype": "int64", "required": True}, "score": {"dtype": "float64"}}
        result = pipeline.validate_schema(df, schema)
        assert result is not None

    def test_stats_tracking(self, pipeline, sample_json):
        df = pipeline.extract_from_file(sample_json)
        df = pipeline.clean(df)
        assert pipeline.stats["rows_extracted"] == 4
        assert pipeline.stats["duplicates_removed"] == 1
