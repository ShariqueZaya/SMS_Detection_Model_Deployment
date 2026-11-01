# Use Python as the base image
FROM python:3.11-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install required libraries
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files
COPY . .

# Expose Flask API port
EXPOSE 5000

# Run the Flask API
CMD ["python", "src/api.py"]