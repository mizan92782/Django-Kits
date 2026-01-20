# ==============================
# Base image
# ==============================
FROM python:3.11-slim

# ==============================
# Environment variables
# ==============================
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ==============================
# Set working directory
# ==============================
WORKDIR /app

# ==============================
# System dependencies
# ==============================
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    curl \
    && rm -rf /var/lib/apt/lists/*

# ==============================
# Install Python dependencies
# ==============================
COPY requirements.txt .

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# ==============================
# Copy project files
# ==============================
COPY . .

# ==============================
# Collect static files (optional)
# ==============================
RUN python manage.py collectstatic --noinput || true
RUN pip install gunicorn

# ==============================
# Expose port
# ==============================
EXPOSE 8000

# ==============================
# Run server
# ==============================
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
