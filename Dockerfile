FROM python:3.12-slim AS base

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml README.md Makefile ./
COPY src/ ./src/

RUN pip install --no-cache-dir -e ".[dev]"

COPY . .

FROM base AS test
CMD ["pytest", "tests/", "-v", "--tb=short"]

FROM base AS etl
CMD ["python", "-m", "src.etl_runner"]

FROM base AS jupyter
EXPOSE 8888
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
