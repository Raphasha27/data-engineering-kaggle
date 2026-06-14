import pytest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

try:
    from spark_etl.spark_etl_pipeline import SparkETLPipeline, HAS_SPARK
except ImportError:
    HAS_SPARK = False


pytestmark = pytest.mark.skipif(not HAS_SPARK, reason="PySpark not installed")


class TestSparkETLPipeline:
    def test_pipeline_class_imports(self):
        assert HAS_SPARK is True

    def test_detect_format_parquet(self):
        p = SparkETLPipeline.__new__(SparkETLPipeline)
        ext = p.detect_format("/data/file.parquet")
        assert ext == ".parquet"

    def test_detect_format_csv(self):
        p = SparkETLPipeline.__new__(SparkETLPipeline)
        ext = p.detect_format("/data/file.csv")
        assert ext == ".csv"

    def test_detect_format_default(self):
        p = SparkETLPipeline.__new__(SparkETLPipeline)
        ext = p.detect_format("s3://bucket/path/data")
        assert ext == ".parquet"
