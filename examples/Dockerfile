FROM python:3.9-slim

# Set working directory
WORKDIR /app

# First create the examples package directory
RUN mkdir -p examples

# Copy all files into examples directory
COPY . examples/

# Install krypton-ml and dependencies
RUN pip install --no-cache-dir krypton-ml langchain-ollama

# Set working directory to where config file is
WORKDIR /app/examples

# Command to start krypton
CMD ["krypton", "config.yaml"]