# Use the official Python image as a parent image
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt /app/

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Run migration and collect static files (you can modify this step as needed)
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "collectstatic", "--no-input"]

# Set the entry point for the container
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]