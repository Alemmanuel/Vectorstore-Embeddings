# Retrieval Project with LangChain, FAISS, and HuggingFace Embeddings

This project demonstrates how to perform semantic search over a set of documents using the LangChain framework, FAISS vector store, and HuggingFace sentence embeddings.

## Features
- Loads a FAISS vector store containing document embeddings.
- Uses HuggingFace's `all-MiniLM-L6-v2` model for embedding queries and documents.
- Performs similarity search to retrieve the most relevant documents for a given query.

## Project Structure
```
main.py                # Main script to perform the search
mi_vectorstore/        # Directory containing FAISS index and metadata
    index.faiss        # FAISS index file
    index.pkl          # Pickle file with document metadata
```

## Requirements
- Python 3.8+
- `langchain_community`
- `faiss-cpu` or `faiss-gpu`
- `sentence-transformers`

Install dependencies with:
```bash
pip install langchain_community faiss-cpu sentence-transformers
```

## Usage
1. Ensure you have a FAISS vector store created in the `mi_vectorstore` directory.
2. Run the main script:
```bash
python main.py
```
3. The script will output the most relevant documents for the hardcoded query:
```
¿Qué dice el documento sobre la privacidad?
```

## How It Works
- The script loads the FAISS vector store and the HuggingFace embedding model.
- It embeds the query and retrieves the most similar documents from the vector store.
- The results are printed to the console.

## Customization
- To change the query, modify the `query` variable in `main.py`.
- To use a different embedding model, change the `model_name` parameter in the `HuggingFaceEmbeddings` initialization.

## License
This project is for educational purposes.
