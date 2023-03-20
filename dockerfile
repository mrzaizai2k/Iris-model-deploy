# Use an official Python runtime as a parent image
FROM python:3.8-slim-buster

# Set the working directory to /app
WORKDIR D:\Project\mlmodel_deploy

# Copy the current directory contents into the container at /app
COPY . .

# Install the required packages
RUN pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org install -r setup.txt

# Expose port 5000 for the Flask app
EXPOSE 5000

# Start the Flask app when the container launches
CMD ["python", "app.py"]
