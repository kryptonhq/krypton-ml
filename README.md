# Krypton ML

Krypton ML is a simple ML model serving framework with an emphasis on a config-driven approach. It's designed to make deploying machine learning models as API endpoints quick and easy.

**Note:** This project is currently in the experimental stage and only supports LangChain invocation.

Author: [Varun Kruthiventi](https://varunk.me)\
Website: [kryptonhq.com](https://kryptonhq.com)\
PyPI Package: [krypton-ml](https://pypi.org/project/krypton-ml/)\
GitHub Repository: [krypton-ml](https://github.com/kryptonhq/krypton-ml)

## Features

- Config-driven approach to model deployment
- Easy integration with LangChain. More ML frameworks coming soon!
- Support for text completion and chat-based chains currently for LangChain
- Simple API deployment from configuration files

## Installation

You can install Krypton ML using pip:

```bash
pip install krypton-ml
```

## Usage
1. Crate a LangChain model(chain) and save it as a Python file (e.g., `langchain_example/app.py`). 
2. The app.py should have a valid chain callable that can be invoked by Krypton framework.
3. Create a configuration file (e.g., `config.yaml`) for your model:

```yaml
krypton:
  models:
    - name: langchain-example # Name of the model
      type: langchain # Currently only LangChain is supported
      module_path: ./examples # Path to the directory containing the parent module
      callable: langchain_example.completion.chain # <parent_module>.<module>.<callable>
      endpoint: /langchain-example # API endpoint for the model
  server:
    host: 0.0.0.0 # Host to run the server on
    port: 8000 # Port to run the server on
```

2. Run the Krypton ML server with your config file:

```bash
krypton config.yaml
```

This will start a server on `http://0.0.0.0:8000` with the specified model endpoint.

## Examples

Check out the `examples` folder in the repository for LangChain and Ollama based examples:

1. Text completion chain
2. Chat-based chain

These examples demonstrate how to deploy LangChain models as API endpoints using Krypton ML's config-driven approach.

## Contributing

We welcome contributions to Krypton ML! Please feel free to submit issues, fork the repository and send pull requests.

## License

This project is licensed under the Apache License 2.0 License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

Krypton ML is currently in an experimental stage. Use in production environments is not recommended without thorough testing and validation.

For more information, visit [kryptonhq.com](https://kryptonhq.com) or check out the [GitHub repository](https://github.com/kryptonhq/krypton-ml).
