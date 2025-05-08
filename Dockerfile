# Use official Python image
FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Copy app files
COPY server.py .
COPY weather.py .
COPY requirements.txt .
COPY templates/ templates/
COPY static/ static/

# Install dependencies
RUN pip install -r requirements.txt

# Expose the port
EXPOSE 8000

# Command to run the app
CMD ["python", "server.py"]
