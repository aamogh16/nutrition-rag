import google.generativeai as genai
from dotenv import load_dotenv
import os
from document_processor import DocumentProcessor
from load_documents import load_nutrition_docs

class RAGSystem:
  def __init__(self):
    load_dotenv()
    # configuring gemini api
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    self.model = genai.GenerativeModel("gemini-2.0-flash-lite")

    # getting the processor and loading documents
    self.processor = load_nutrition_docs()


  def ask_question(self, question: str):
    # searching for relevant documents for this prompt
    search_results = self.processor.search_documents(question)
    relevant_docs = search_results['documents'][0]

    # creating prompt for gemini with context
    context = "\n\n".join(relevant_docs)
    print(f"Context: {context}")
    prompt = f"""
    Based on this nutritional information:
    {context}
    Answer this question: {question}
    
    Please provide a detailed answer based on only the provided context and nothing else. 
    """
    response = self.model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
  # Test the system
  rag = RAGSystem()

  question = "How much protein do athletes need daily?"
  answer = rag.ask_question(question)

  print(f"Question: {question}")
  print(f"Answer: {answer}")