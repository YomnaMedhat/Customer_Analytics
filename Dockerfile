FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        gfortran \
        libblas-dev \
        libatlas3-base \
        liblapack-dev && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pandas numpy matplotlib seaborn scikit-learn scipy requests

# Create working directory and Copy project into it
RUN mkdir -p /app/pipeline
COPY . /app/pipeline/

# Set working directory
WORKDIR /app/pipeline/

# Start Interactive Bash shell
CMD ["bash"]