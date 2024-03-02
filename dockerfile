# Use an official Python runtime as a parent image
FROM python:3.8

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Define environment variable for Flask
ENV FLASK_APP=main.py

# Command to run the Flask application
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000"]
