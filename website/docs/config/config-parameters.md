# Configuration Guide

This guide describes the structure and supported parameters for the `config.yaml` file used by Krypton ML.

## Configuration Structure

The configuration file follows this basic structure:

```yaml
krypton:
  models:
    - # Model 1 configuration
    - # Model 2 configuration
  server:
    # Server configuration
```

## Supported Parameters

### Root Configuration

| Parameter | Type | Description |
|-----------|------|-------------|
| krypton   | Object | The root object containing all configuration |

### Krypton Configuration

| Parameter | Type | Description |
|-----------|------|-------------|
| models    | List[Model] | List of model configurations |
| server    | ServerConfig | (Optional) Server configuration |

### Model Configuration

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| name | String | Yes | Name of the model |
| type | String | Yes | Type of the model (e.g., "langchain", "custom") |
| module_path | String | No | Python path to the module containing the model |
| callable | String | No | Name of the function or class to call within the module |
| endpoint | String | Yes | API endpoint for the model |
| options | ModelOptions | No | Additional options for the model |
| tags | List[String] | No | Tags associated with the model (defaults to empty list) |
| description | String | No | Description of the model (defaults to empty string) |
| hf_model_name | String | No | Hugging Face model name (for HuggingFace models only) |
| hf_task | String | No | Hugging Face task type (defaults to "generation") |
| hf_model_kwargs | Object | No | Additional keyword arguments for HuggingFace model initialization |
| hf_generation_kwargs | Object | No | Additional keyword arguments for HuggingFace model generation |
| hf_device | String | No | Device to run the HuggingFace model on (defaults to "cpu") |

### ModelOptions

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| debug | Boolean | False | Enable debug mode for this model |

### ServerConfig

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| host | String | "0.0.0.0" | Host to bind the server to |
| port | Integer | 8000 | Port to run the server on |
| allow_origins | List[String] | [] | List of allowed origins for CORS |
| allow_credentials | Boolean | False | Allow credentials for CORS |
| allow_methods | List[String] | [] | Allowed HTTP methods for CORS |
| allow_headers | List[String] | [] | Allowed headers for CORS |
| debug | Boolean | False | Enable debug mode for the server |

## Example Configuration

Here's an example of a complete `config.yaml` file:

```yaml
krypton:
  models:
    # LangChain model example
    - name: text-completion
      type: langchain
      module_path: examples.text_completion
      callable: create_chain
      endpoint: /complete
      options:
        debug: true
      tags:
        - nlp
        - completion
      description: "A text completion model using LangChain"
    
    # HuggingFace model example
    - name: text-generation
      type: huggingface
      endpoint: /generate
      hf_model_name: gpt2
      hf_task: text-generation
      hf_device: cuda
      hf_model_kwargs:
        torch_dtype: float16
      hf_generation_kwargs:
        max_length: 100
        do_sample: true
      tags:
        - nlp
        - generation
      description: "GPT-2 text generation model"

  server:
    host: "0.0.0.0"
    port: 8080
    allow_origins:
      - "https://example.com"
    allow_credentials: true
    allow_methods:
      - "GET"
      - "POST"
    allow_headers:
      - "Content-Type"
    debug: true
```

The example above demonstrates:
1. A LangChain-based model configuration
2. A HuggingFace model configuration with specific model parameters
3. Server configuration with CORS settings

Remember to adjust the paths and parameters according to your specific setup and requirements.
