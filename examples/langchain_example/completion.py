import os

from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate

# Initialize the Ollama LLM with configurable host
llm = OllamaLLM(
    model="llama3.2:1b",
    base_url=os.getenv('OLLAMA_HOST', 'http://localhost:11434')
)

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}.",
)

# Create an LLMChain
chain = prompt | llm
