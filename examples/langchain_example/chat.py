from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

# Initialize the Ollama LLM
llm = ChatOllama(
    model="llama3.2:1b",
    temperature=0
)

# Create a prompt template
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful assistant that translates {input_language} to {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

# Create an LLMChain
chain = prompt | llm