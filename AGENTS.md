# Krypton ML - Agent Instructions

## Project Overview

Krypton ML is a config-driven FastAPI-based ML model serving framework designed to make deploying machine learning models as API endpoints quick and easy. The framework supports multiple model types and provides a simple configuration-based approach to model deployment.

## Key Architecture Components

### Core Structure
- **Entry Point**: `krypton_ml/main.py` - CLI entry point using Typer
- **Server Runtime**: `krypton_ml/core/webserver/server_runtime.py` - FastAPI server setup with CORS and middleware
- **Model Endpoints**: `krypton_ml/core/webserver/model_endpoints.py` - Dynamic endpoint generation
- **Model Registry**: `krypton_ml/core/registry/model_registry.py` - Model loading and invocation
- **Configuration**: `krypton_ml/core/loader/config.py` - YAML config parsing

### Supported Model Types
1. **LangChain Models** (`type: langchain`)
   - Uses LangChain chains for text completion and chat
   - Requires `module_path` and `callable` configuration
   - Example: `langchain_example.completion.chain`

2. **Custom Models** (`type: custom`)
   - Implements `KryptonCustomModel` interface
   - Requires `predict(input: Dict[str, Any]) -> Dict[str, Any]` method
   - Example: `custom.custom_model.CustomModelExample`

3. **HuggingFace Models** (`type: huggingface`)
   - Direct integration with HuggingFace transformers
   - Supports generation and seq2seq tasks
   - Configuration via `hf_model_name`, `hf_task`, etc.

## Configuration Schema

### Basic Structure
```yaml
krypton:
  models:
    - name: model-name
      type: langchain|custom|huggingface
      endpoint: /api/endpoint
      # ... model-specific config
  server:
    host: 0.0.0.0
    port: 8000
    # ... server config
```

### Model Configuration Parameters
- **Required**: `name`, `type`, `endpoint`
- **LangChain**: `module_path`, `callable`
- **Custom**: `module_path`, `callable` (class implementing KryptonCustomModel)
- **HuggingFace**: `hf_model_name`, `hf_task`, `hf_generation_kwargs`, etc.
- **Optional**: `description`, `tags`, `options.debug`

### Server Configuration
- **Host/Port**: `host` (default: "0.0.0.0"), `port` (default: 8000)
- **CORS**: `allow_origins`, `allow_credentials`, `allow_methods`, `allow_headers`
- **Debug**: `debug` (default: false)

## API Endpoints

### Model Endpoints
- **POST** `/{endpoint}` - Invoke model with JSON input
- **GET** `/registry/models` - List all registered models
- **GET** `/` - Health check
- **GET** `/health` - Health status

### Request/Response Format
```json
// Request
{
  "key": "value",
  "input_data": "..."
}

// Response
{
  "response": "model_output"
}
```

## Development Guidelines

### Adding New Model Types
1. Create loader in `krypton_ml/core/models/registry.py`
2. Add to `ModelRegistry._model_loaders` in `model_registry.py`
3. Implement invocation logic in `invoke_model()` method
4. Update configuration schema in `cli_config.py`

### Creating Custom Models
```python
from krypton_ml.core.models.registry import KryptonCustomModel

class MyCustomModel(KryptonCustomModel):
    def predict(self, input: Dict[str, Any]) -> Dict[str, Any]:
        # Your model logic here
        return {"result": "output"}
```

### LangChain Integration
```python
from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

llm = OllamaLLM(model="llama3.2:1b")
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write about {topic}."
)
chain = prompt | llm
```

## Docker Setup

### Docker Compose Structure
- **Ollama Service**: Runs LLM models
- **Krypton Service**: Runs the ML server
- **Network**: `krypton-network` for service communication

### Environment Variables
- `OLLAMA_HOST`: Ollama service URL (default: http://localhost:11434)

## Testing and Examples

### Example Configurations
- **LangChain Completion**: `examples/langchain_example/completion.py`
- **LangChain Chat**: `examples/langchain_example/chat.py`
- **Custom Model**: `examples/custom/custom_model.py`
- **HuggingFace Models**: GPT-2, T5, Phi-2 examples

### Testing Commands
```bash
# Start server
krypton config.yaml

# Test LangChain completion
curl -X POST http://localhost:5000/models/langchain/llama3.2/completion \
  -H "Content-Type: application/json" \
  -d '{"topic": "artificial intelligence"}'

# Test custom model
curl -X POST http://localhost:5000/models/custom/example \
  -H "Content-Type: application/json" \
  -d '{"x": 5, "y": 3}'
```

## Common Tasks for Agents

### 1. Adding a New Model
1. Create model implementation (LangChain chain, custom class, or HF config)
2. Update `config.yaml` with model configuration
3. Test endpoint with curl or API client

### 2. Debugging Issues
- Check server logs for model loading errors
- Verify `module_path` and `callable` are correct
- Ensure model dependencies are installed
- Use `debug: true` in server config for detailed error traces

### 3. Performance Optimization
- Configure HuggingFace models with appropriate `hf_device` (cuda/cpu)
- Set generation parameters in `hf_generation_kwargs`
- Use model-specific optimizations in custom implementations

### 4. Production Deployment
- Set appropriate CORS settings
- Configure proper host/port binding
- Disable debug mode
- Add health checks and monitoring

### New changes to codebase
- After any changes to codebase, please make sure to summarize the changes and update this AGENTS.md file accordingly.

## File Structure Reference

```
krypton_ml/
├── main.py                    # CLI entry point
├── core/
│   ├── loader/               # Configuration loading
│   ├── models/               # Model definitions and configs
│   ├── registry/             # Model registry and loaders
│   ├── runtime/              # Runtime handlers (HuggingFace)
│   ├── utils/                # Logging utilities
│   └── webserver/            # FastAPI server and endpoints
├── examples/                 # Example implementations
└── tests/                    # Test suites
```

## Dependencies
- **FastAPI**: Web framework
- **LangChain**: ML framework integration
- **HuggingFace Transformers**: Model support
- **Pydantic**: Configuration validation
- **Typer**: CLI interface
- **Uvicorn**: ASGI server

## Notes for AI Agents
- The framework is **experimental** - use with caution in production
- Model endpoints are dynamically generated based on configuration
- All models return responses wrapped in `{"response": "..."}` format
- Error handling includes stack traces when debug mode is enabled
- CORS is configurable for cross-origin requests
