# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /usr/src/app

# Copy only the requirements file first for layer caching
COPY requirements.txt /usr/src/app/

# Install system dependencies and Redis server
RUN apt update && \
    apt install -y redis-server && \
    apt clean

# # Create a virtual environment inside the container
# RUN python -m venv /usr/src/app/env

# # Set the virtual environment as default
# ENV PATH="/usr/src/app/env/bin:$PATH"

# Install Python dependencies inside the virtual environment
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Copy the rest of the application code
COPY . /usr/src/app/

# Expose the default Django port
EXPOSE 8000

# Start Redis and the Django development server
CMD service redis-server start && python manage.py runserver 0.0.0.0:8000
