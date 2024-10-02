from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate

# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.2:1b")

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}.",
)

# Create an LLMChain
chain = prompt | llm