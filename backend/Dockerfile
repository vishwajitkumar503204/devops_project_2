FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install requirements first (better caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Set Python path
ENV PYTHONPATH=/app

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=40s --retries=3 \
  CMD python -c "import requests; requests.get('http://postgres-service:8080/api/health', timeout=5)" || exit 1

EXPOSE 8080

# ✅ Use single worker to prevent race conditions during development
# For production, use --workers 4 or more with Gunicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]