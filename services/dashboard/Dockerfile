FROM python:3.10-slim

WORKDIR /app

# Install system dependencies needed to compile certain Python packages
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the dashboard application code
COPY . /app/

# Expose the default network port Streamlit communicates over
EXPOSE 8501

# Run Streamlit with absolute configuration for Docker environments
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]