# Use the official Python image as a base
FROM python:3.12-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app

# Install the required packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libportaudio2 \
    portaudio19-dev \
    gcc \
    libc-dev \
    make \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

# Expose the port the app runs on
EXPOSE 7860

# Command to run the application
CMD ["sh", "-c", "python -m gradio_app.py"]
