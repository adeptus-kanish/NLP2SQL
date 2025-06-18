import chromadb
from chromadb.config import Settings
from sentence_transformers import SentenceTransformer


class ChromaVectorStore:
    def __init__(self, persist_path="chroma_store", collection_name="table_docs"):
        self.client = chromadb.Client(Settings(
            persist_directory = persist_path,
            chroma_db_impl = "duckdb+parquet"  # underlying storage
        ))
        self.collection = self.client.get_or_create_collection(collection_name)
        self.embedder = SentenceTransformer("all-MiniLM-L6-v2")  # small and fast

    def add_docs(self, ids, texts, metadata=None):
        embeddings = self.embedder.encode(texts).tolist()
        self.collection.add(documents=texts, metadatas=metadatas, embeddings=embeddings, ids=ids)

    def query(self, text, k=3):
        embedding = self.embedder.encode([text]).tolist()[0]
        results = self.collection.query(query_embeddings=[embedding], n_results=k)
        return results
