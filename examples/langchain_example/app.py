from langchain_ollama.llms import OllamaLLM
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Initialize the Ollama LLM
llm = OllamaLLM(model="llama3.1")

# Create a prompt template
prompt = PromptTemplate(
    input_variables=["topic"],
    template="Write a short paragraph about {topic}.",
)

# Create an LLMChain
chain = LLMChain(llm=llm, prompt=prompt)