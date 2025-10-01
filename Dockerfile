FROM python:3.11-slim as builder

RUN apt-get update && apt-get install -y --no-install-recommends build-essential curl \
 && rm -rf /var/lib/apt/lists/*

RUN curl -LsSf https://astral.sh/uv/install.sh | sh
ENV PATH="/root/.cargo/bin:${PATH}"

WORKDIR /app
COPY pyproject.toml ./
RUN uv sync --frozen --no-dev

FROM python:3.11-slim
WORKDIR /app

COPY --from=builder /app/.venv /app/.venv
COPY opengov_earlyukrainian /app/opengov_earlyukrainian

ENV PATH="/app/.venv/bin:${PATH}"
ENV PYTHONUNBUFFERED=1
EXPOSE 8000
HEALTHCHECK CMD curl -f http://localhost:8000/health || exit 1
CMD ["uvicorn", "opengov_earlyukrainian.api.main:app", "--host", "0.0.0.0", "--port", "8000"]

