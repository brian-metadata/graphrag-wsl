"""Quick test of Ollama integration with LangChain."""
from langchain_ollama import OllamaLLM

# Initialize the model
llm = OllamaLLM(model="llama3.2")

# Test a simple query
print("Testing Ollama with LangChain...\n")
response = llm.invoke("What is a knowledge graph? Answer in 2 sentences.")
print(f"Response: {response}\n")

print("✅ Ollama is working with LangChain!")
