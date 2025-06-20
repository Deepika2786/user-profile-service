# Use a lightweight official Python image as a base
FROM python:3.9-slim-buster

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirement.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the application code into the container
COPY app.py .

# Expose the port the Flask app runs on
EXPOSE 5000

# Command to run the Flask application when the container starts
CMD ["python", "app.py"]