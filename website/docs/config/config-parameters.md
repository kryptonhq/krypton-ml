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

| Parameter | Type | Description |
|-----------|------|-------------|
| name | String | Name of the model |
| type | String | Type of the model (e.g., "langchain") |
| module_path | String | Python path to the module containing the model |
| callable | String | Name of the function or class to call within the module |
| endpoint | String | API endpoint for the model |
| options | ModelOptions | (Optional) Additional options for the model |
| tags | List[String] | (Optional) Tags associated with the model |
| description | String | (Optional) Description of the model |

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
    
    - name: chat-model
      type: langchain
      module_path: examples.chat_model
      callable: create_chat_chain
      endpoint: /chat
      tags:
        - nlp
        - chat

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

This configuration sets up two models (a text completion model and a chat model) and configures the server with custom settings.

Remember to adjust the `module_path` and `callable` parameters to match your actual module structure and function names.