FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install build deps and dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure python output is not buffered (helpful for logs)
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

# Use gunicorn as the production WSGI server
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:5000", "--workers", "4"]
