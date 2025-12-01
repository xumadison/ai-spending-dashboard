FROM python:3.10-slim

WORKDIR /app

# System deps for pandas/numpy/scikit-learn wheels (keep small)
RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY assets/ ./assets

ENV PYTHONUNBUFFERED=1
EXPOSE 8080

# Use gunicorn in container
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "src.app:app"]
