from typing import List, Dict

# --- Mock Libraries for Demonstration ---
class Document:
    def __init__(self, content: str, doc_id: str):
        self.content = content
        self.doc_id = doc_id
    
    def __repr__(self):
        return f"Doc(id={self.doc_id}, len={len(self.content)})"

class TextSplitter:
    def split_text(self, text: str, chunk_size: int = 200) -> List[str]:
        # Simple split logic for demonstration
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])
        return chunks
# ----------------------------------------

def preprocess_document_for_rag(doc: Document) -> List[Dict]:
    """
    Loads a Document, splits it into chunks, and prepares metadata.
    This simulates the initial RAG ingestion pipeline.
    """
    splitter = TextSplitter()
    text_chunks = splitter.split_text(doc.content, chunk_size=300)
    
    chunks_with_metadata = []
    for i, chunk in enumerate(text_chunks):
        chunks_with_metadata.append({
            "chunk_id": f"{doc.doc_id}-{i}",
            "source_doc": doc.doc_id,
            "text": chunk,
            # In a real platform, this chunk would be converted to a vector embedding here
            "status": "ready_for_embedding" 
        })
        
    return chunks_with_metadata

# Example Usage
long_doc_text = "The private AI platform ensures that all enterprise data remains within a secure boundary..." * 10
my_document = Document(content=long_doc_text, doc_id="POLICY_001")

processed_chunks = preprocess_document_for_rag(my_document)

print(f"Total Chunks: {len(processed_chunks)}")
print("First Chunk Data:")
print(processed_chunks[0])
