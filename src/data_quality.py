import pandas as pd
import numpy as np
from typing import Dict, Any
import logging

logger = logging.getLogger("data_quality")


class DataQualityChecker:
    def __init__(self, df: pd.DataFrame, config: dict = None):
        self.df = df
        self.config = config or {}

    def check_completeness(self) -> Dict[str, float]:
        return {col: round(1 - self.df[col].isnull().mean(), 4) for col in self.df.columns}

    def check_uniqueness(self) -> Dict[str, float]:
        result = {}
        for col in self.df.columns:
            result[col] = round(self.df[col].nunique() / len(self.df), 4) if len(self.df) > 0 else 1.0
        return result

    def check_outliers_iqr(self, factor: float = 1.5) -> Dict[str, int]:
        outliers = {}
        for col in self.df.select_dtypes(include=[np.number]).columns:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            iqr = q3 - q1
            lower = q1 - factor * iqr
            upper = q3 + factor * iqr
            count = int(((self.df[col] < lower) | (self.df[col] > upper)).sum())
            if count > 0:
                outliers[col] = count
        return outliers

    def check_duplicates(self) -> int:
        return int(self.df.duplicated().sum())

    def summary_stats(self) -> Dict[str, dict]:
        stats = {}
        for col in self.df.select_dtypes(include=[np.number]).columns:
            stats[col] = {
                "min": float(self.df[col].min()) if self.df[col].notna().any() else None,
                "max": float(self.df[col].max()) if self.df[col].notna().any() else None,
                "mean": float(self.df[col].mean()) if self.df[col].notna().any() else None,
                "std": float(self.df[col].std()) if self.df[col].notna().any() else None,
                "nulls": int(self.df[col].isnull().sum()),
            }
        return stats

    def run(self) -> Dict[str, Any]:
        if self.df.empty:
            return {"status": "empty", "rows": 0, "columns": 0}

        report = {
            "status": "ok",
            "rows": len(self.df),
            "columns": len(self.df.columns),
            "dtypes": {c: str(d) for c, d in self.df.dtypes.items()},
            "completeness": self.check_completeness(),
            "uniqueness": self.check_uniqueness(),
            "outliers": self.check_outliers_iqr(),
            "duplicate_rows": self.check_duplicates(),
            "memory_mb": round(self.df.memory_usage(deep=True).sum() / 1e6, 2),
            "numeric_stats": self.summary_stats(),
        }
        report["quality_score"] = self._calculate_score(report)
        return report

    def _calculate_score(self, report: dict) -> float:
        completeness = np.mean(list(report["completeness"].values())) * 40
        uniqueness = np.mean(list(report["uniqueness"].values())) * 20
        no_dupes = 20 if report["duplicate_rows"] == 0 else max(0, 20 - report["duplicate_rows"] * 2)
        no_outliers = 20 if not report["outliers"] else max(0, 20 - sum(report["outliers"].values()))
        return round(completeness + uniqueness + no_dupes + no_outliers, 1)
