from sentence_transformers import SentenceTransformer
import chromadb
from dotenv import load_dotenv

class DocumentProcessor:
  def __init__(self):
    # initializing the embedding model
    self.embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

    # initializing the chromadb client
    self.chroma_client = chromadb.Client()

    # creating/getting collection
    self.collection = self.chroma_client.create_collection(
        name="nutrition_docs",
        get_or_create=True
    )

    # default number of search results
    self.n_results = 3

  # method to add documents to the vector database
  def add_document(self, text, doc_id):
    # create embedding of text
    embedding = self.embedding_model.encode(text)

    # adding to chromadb
    self.collection.add(
        embeddings=[embedding.tolist()],
        documents=[text],
        ids=[doc_id]
    )
    print(f"Document ID: {doc_id} added to database.")


  # method to search through stored documents
  def search_documents(self, query):
    results = self.collection.query(
        query_texts=[query],
        n_results=self.n_results
    )
    return results

# if __name__ == "__main__":
#   # Create processor instance
#   processor = DocumentProcessor()
#
#   # Add some test nutrition documents
#   processor.add_document("Protein helps build muscle mass", "doc1")
#   processor.add_document("Creatine improves strength and power", "doc2")
#   processor.add_document("Vitamin D supports bone health", "doc3")
#
#   # Test search
#   query = "muscle building"
#   results = processor.search_documents(query)
#
#   print(f"\nSearch results for: '{query}'")
#   print(results)