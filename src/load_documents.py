import os
from document_processor import DocumentProcessor

def load_nutrition_docs():
  processor = DocumentProcessor()

  # showing where docs are
  docs_folder = "data/raw/sample_docs"

  # getting all txt files in folder
  for filename in os.listdir(docs_folder):
    if filename.endswith(".txt"):
      file_path = os.path.join(docs_folder, filename)
      with open(file_path, 'r') as file:
        content = file.read()

      doc_id = filename.replace('.txt', '')

      processor.add_document(content, doc_id)
  return processor

# if __name__ == "__main__":
#   # Load all documents
#   processor = load_nutrition_docs()
#
#   # Test search
#   query = "How much protein do athletes need?"
#   results = processor.search_documents(query)
#
#   print(f"\nSearch results for: '{query}'")
#   for i, doc in enumerate(results['documents'][0]):
#     print(f"{i+1}. {doc[:100]}...")  # First 100 characters