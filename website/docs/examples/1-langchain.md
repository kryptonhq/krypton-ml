# Langchain

This guide will walk you through the process of implementing a Langchain model with Krypton ML. We'll create a simple text generation model using Langchain and deploy it using Krypton ML.

## Step 1: Create the Langchain Model

First, let's create a simple Langchain model. Create a new file called `langchain_model.py` in folder `app`:

```python
from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2:1b")

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}.",
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)
```

## Step 2: Configure Krypton ML

Create a configuration file for Krypton ML. Name it `krypton_config.yaml`:

```yaml
krypton:
  server:
    host: "0.0.0.0"
    port: 8000
  models:
    - name: langchain-example
      type: langchain
      module_path: ./app
      callable: langchain_model.chain
      endpoint: langchain-example
      description: "A simple Langchain text generation model"
      tags:
        - langchain
        - text-generation
```

Make sure to replace `./app` with the actual folder path of your `langchain_model.py` file.

## Step 3: Run Krypton ML Server

Now, start the Krypton ML server with your configuration:

```bash
krypton krypton_config.yaml
```

## Step 4: Test the Model

You can now test your Langchain model using a simple curl command or any API client:

```bash
curl -X POST http://localhost:8000/langchain-example \
     -H "Content-Type: application/json" \
     -d '{"topic": "artificial intelligence"}'
```

This should return a JSON response with a short paragraph about artificial intelligence.

## Conclusion

You've successfully implemented and deployed a Langchain model using Krypton ML. This example demonstrates how easy it is to integrate Langchain models into your Krypton ML workflow. You can extend this example by adding more complex Langchain models or chains as needed.