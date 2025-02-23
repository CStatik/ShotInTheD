# Base image
FROM nvidia/cuda:11.8.0-runtime-ubuntu20.04

# Set working directory
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y \
    python3 python3-pip git \
    && rm -rf /var/lib/apt/lists/*

# Copy files into the container
COPY requirements.txt requirements.txt
COPY . .

# Install Python dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Set entrypoint
CMD ["python3", "main.py"]
