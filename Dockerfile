# Use official Python 3.12 base image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV DEBIAN_FRONTEND=noninteractive

# Set working directory
WORKDIR /app

RUN set -ex \
    && python -m pip install dagster dagit dagster-dg-cli
# Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
RUN set -ex \
    && python -m pip install setuptools \
    && python -m pip install dbt-clickhouse~=1.8.0 dbt-postgres~=1.8.0 dbt-core~=1.8.0 dagster-dbt numpy

# Copy project files
# COPY . .

# Create a non-root user
RUN useradd -m -r appuser && chown -R appuser /app
USER appuser

# Expose port (if your app uses a web server)
EXPOSE 8000

# Default command (can be overridden)
CMD ["python", "--version"]