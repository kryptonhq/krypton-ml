# 2. Getting started with Docker

This guide explains how to run the Krypton ML examples using Docker. The examples demonstrate various model integrations including LangChain with Ollama LLM.

## Prerequisites

- Docker and Docker Compose installed on your system

## Quick Start

1. Navigate to the examples directory:
```bash
cd examples
```

2. The folder has a `docker-compose.yml` file that defines the services required to run the examples. Run the following command to start the services:
```bash
docker compose up -d
```

This will start two containers:
- An Ollama server for running the LLM
- The Krypton ML server with example models

## Setting up the LLM

Before using the LangChain examples, you'll need to pull the LLM model. Run the following commands:

```bash
# Get the Ollama container ID
container_id=$(docker ps | grep ollama | awk '{print $1}')

# Pull the model
docker exec -it $container_id ollama pull llama3.2:1b
```

This will download and set up the LLaMA model used in the examples. The download might take a few minutes depending on your internet connection.

## Testing the Examples

### Text Completion Example

The completion example generates a paragraph about a given topic. Test it using curl:

```bash
curl -X 'POST' \
  'http://0.0.0.0:5000/models/langchain/llama3.2/completion' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"topic": "Tony stark"}'
```

Expected Response:
```json
{
  "response": "Tony Stark, also known as Iron Man, is a brilliant and reclusive billionaire inventor and businessman. He created a powered suit of armor that allows him to fly and fight crime, using it to become the superhero known as Iron Man. With his wit, intelligence, and advanced technology, he uses his alter ego to protect the world from various threats, often facing off against supervillains like Ultron and Thanos. His personal life is also filled with complex relationships and struggles, including his complicated friendship with his assistant Pepper Potts and his troubled past as a high school student turned genius."
}
```

## Anatomy of Docker setup

The Dockerfile installs the `krypton-ml` pakcage and copies the example code to the container aling with the config file.

```Dockerfile
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
```

The `docker-compose.yml` file defines two services:
```yaml
services:
  ollama:
    image: ollama/ollama:latest
    volumes:
      - ollama_data:/root/.ollama
    ports:
      - "11434:11434"
    networks:
      - krypton-network

    krypton-example:
    build:
      context: .
      dockerfile: Dockerfile
    ports:
      - "5000:5000"
    environment:
      - OLLAMA_HOST=http://ollama:11434
    volumes:
      - ./hf_cache:/root/.cache/huggingface
    depends_on:
      - ollama
    networks:
      - krypton-network
```